<template lang="pug">
  .cancellation

    v-progress-circular(:width="3", color="primary", indeterminate, v-if="cancellationPending")
    h1 Absage

    template(v-if="!cancellationPending")
      span Hallo {{ user }},
      br
      br

      span(v-if="cancellationWorked")
        span.
          wir haben deine Absage im System eingetragen, danke für deine rechtzeitige Absage.
          Du musst nichts weiter tun.
        br
        br
        span Hoffentlich bis zum nächsten Mal!

      span(v-if="!cancellationWorked")
        span leider kann das System deine Absage nicht mehr aufnehmen.
        br
        span
          b Bitte melde dich Mo.-Fr. zwischen 12 -15 Uhr telefonisch unter:
          br
          b.phone 030 - 61 40 13 08
          br
          br
          span Vielen Dank!

      br
      span Dein SO36 Team

</template>

<script>
export default {
  name: 'ValidateEmail',
  data () {
    return {
      user: undefined,
      cancellationWorked: false,
      cancellationPending: true
    }
  },
  created () {
    if (!this.$route.params.token) {
      this.cancellationPending = false
    }

    window.axios.post(`/cancel-market-inquiry/${this.$route.params.token}`).then((response) => {
      this.cancellationWorked = true
      this.user = response.data.user
    }).catch((error) => {
      this.user = error.response.data.user
    })

    this.cancellationPending = false
  }
}
</script>

<style lang="sass">
.phone
  font-size: 18px
</style>
