<template lang="pug">
  v-app
    v-content.app
      div.header
      router-view
    v-footer.px-3
      span
        | Copyright ©2018
        |
        a(href="http://peter-pan-grundschule.de/" target="_blank") Peter-Pan-Grundschule
        |  |
        a(href="http://peter-pan-grundschule.de/index.php/datenschutzerklaerung/"
          target="_blank")  Datenschutzerklärung
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
    }
  }
}
</script>

<style lang="sass">
.header
  background: url('/img/header.png')
  height: 20vw
  background-size: contain
  background-repeat: no-repeat
  background-position: center top

footer
  a
    color: #777
    text-decoration: none
    &:hover
      color: #05A9C5
</style>
