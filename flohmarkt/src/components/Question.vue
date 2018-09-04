<template lang="pug">

  .question

    b.question(@click="visible=!visible")
      v-icon(:class="{visible}") mdi-chevron-right
      slot(name="question") Frage

    p.answer(:class="{visible}")
      slot(name="answer") Antwort

</template>

<script>
export default {
  name: 'Question',
  data: () => ({
    visible: false
  })
}
</script>

<style scoped lang="sass">
b
  cursor: pointer
i
  margin-left: -4px
.answer
  line-height: 0.01em
  opacity: 0
  transition: all 0.25s ease-in-out
.answer.visible
  line-height: 1.8em
  opacity: 1
.icon.visible
  transform: rotate(90deg)

b.question
  color: #e09900
</style>
