<template lang="pug">
  .validation
    h1 E-Mail-Verifizierung

    v-progress-circular(:width="3", color="primary", indeterminate, v-if="verificationPending")

    template(v-if="!verificationPending")
      p(v-if="verificationWorked").
        Vielen Dank für die Bestätigung Deiner E-Mail-Adresse. #[br]
        Deine Flohmarktanfrage wird jetzt bei der Auslosung der Tische mit berücksichtigt.
        #[br] Wir werden dich spätestens eine Woche vor dem Termin per Mail informieren ob
        du zu den glücklichen Gewinnern gehörst.
      p(v-if="!verificationWorked").
        Die Bestätigung dieser E-Mail-Adresse ist nicht möglich. #[br]

</template>

<script>
export default {
  name: 'ValidateEmail',
  data () {
    return {
      verificationWorked: false,
      verificationPending: true
    }
  },
  created () {
    if (!this.$route.params.token) {
      this.verificationPending = false
    }

    window.axios.post(`/validate-email/${this.$route.params.token}`).then((response) => {
      this.verificationWorked = true
    })
    this.verificationPending = false
  }
}
</script>

<style lang="sass">
</style>
