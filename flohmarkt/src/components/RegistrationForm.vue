<template lang="pug">

  .form
    v-alert(:value="error", color="error", icon="warning", outline) {{ error }}
    v-form(v-model="valid", ref="form")
      v-text-field(v-model="first_name", label="Vorname", required,
          :rules="[v => !!v || 'Vorname wird benötigt.']")
      v-text-field(v-model="last_name", label="Nachname", required,
          :rules="[v => !!v || 'Nachname wird benötigt.']")
      v-text-field(v-model="email", label="E-Mail", required, :rules="emailRules")
      v-text-field(v-model="phone", label="Telefonnummer", required, :rules="phoneRules")
      v-btn.mx-0.primary(@click="submit") Bewerbung absenden
</template>

<script>
export default {
  name: 'RegistrationForm',
  props: ['nextEvent'],
  data: () => ({
    valid: true,
    first_name: '',
    last_name: '',
    email: '',
    phone: '',
    emailRules: [
      v => !!v || 'Die E-Mail-Adresse wird benötigt.',
      v => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'Die E-Mail-Adresse ist ungültig.'
    ],
    phoneRules: [
      v => !!v || 'Die Telefonnummer wird benötigt.',
      v => /^0[\d ]+$/.test(v) || 'Bitte die Telefonnummer inkl. Vorwahl und ohne Sonderzeichen eingeben.'
    ],
    error: ''
  }),
  methods: {
    submit () {
      if (this.$refs.form.validate()) {
        window.axios.post('/submit-market-inquiry/', {
          first_name: this.first_name,
          last_name: this.last_name,
          email: this.email,
          phone: this.phone,
          event: this.nextEvent.id
        }).then((response) => {
          this.error = ''
          this.$refs.form.reset()
          this.$router.push('/done')
        }).catch((error) => {
          this.error = error.response.data.non_field_errors[0]
        })
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="sass">
h3
  margin: 40px 0 0
ul
  list-style-type: none
  padding: 0
li
  display: inline-block
  margin: 0 10px
a
  color: #42b983
</style>
