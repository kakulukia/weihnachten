<template lang="pug">
  v-app
    v-content
      div.header
      router-view
    // v-footer(:fixed="true")
      span &copy; 2018
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
</style>
