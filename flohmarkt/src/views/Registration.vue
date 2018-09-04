<template lang="pug">
  .home
    h1(v-if="registrationOver || nextEvent") Nachtflohmarkt
    h1(v-if="registrationOver") {{ currentEvent.start | moment('D.MM.Y [um] HH:mm') }} Uhr

    p(v-if="registrationOver")
      | Die Anmeldung hierfür ist bereits abgeschlossen. Wir freuen uns über deinen Besuch.
      br
      br

    template(v-if="nextEvent")

      h1(v-if="registrationOver") Standanmeldung
      h1 {{ nextEvent.start | moment('D.MM.Y [um] HH:mm') }} Uhr

      p
        | Hier kannst Du dich bis zum
        span.marker  {{ nextEvent.cancel_date | moment('D.MM.Y') }}
        |  bewerben. #[br]
        | Da wir meist mehr Anmeldungen als Tische haben, entscheidet das Los. Wir werden Dich spätestens
        |  eine Woche vor dem Termin per Mail informieren ob Du zu den glücklichen Gewinnern gehörst.

      RegistrationForm(:nextEvent="nextEvent")

    template(v-if="!nextEvent")
      h2 Im Moment ist kein weiterer Nachtflohmarkt geplant.
      p Sobald der nächste Flohmarkt feststeht, findest Du alle Infos hier.
        br
        br
        | Bis bald
        br
        | Dein SO36 Team

    .faq

      br
      br
      h1 FAQ

      question
        span(slot="question") Was kostet mich das?
        span(slot="answer").
          Der Platz inkl. Biertisch und Bierbank kostet 10,- € und diese sind vor Ort am Eingang zu bezahlen.
          #[br]
          Der Eintritt ist natürlich frei.

      question
        span(slot="question") Muss ich einen Tisch mitbringen?
        span(slot="answer").
          Nein! Ein Biertisch und eine Bierbank sind in den 10,- € enthalten und werden von uns gestellt.
          Eigene Tische oder Kleiderständer sind nicht gestattet, der Platz ist begrenzt! Und wir behalten
          uns vor, Dich damit wieder nach Hause zu schicken.

      question
        span(slot="question") Wann muss ich da sein?
        span(slot="answer").
          Am Besten kommst Du kurz vor 19:00 Uhr. Denn es gilt: „first come - first serve“.
          Nur wer früh kommt, bekommt den besten Platz. Wir reservieren keine speziellen Plätze!

      question
        span(slot="question") Was wenn ich doch nicht kommen kann?
        span(slot="answer").
          In Deiner Bestätigungsmail ist ein Link zur Absage enthalten. Den kannst Du bis 7 Tage vor dem
          Flohmarkt nutzen.

      question
        span(slot="question") Darf ich meine eigenen Getränke mitbringen?
        span(slot="answer").
          Nein, es ist nicht gestattet eigene Getränke mitzubringen, dafür haben wir ja unsere Bar geöffnet. Wir bitten
          Dich das zu respektieren.

      question
        span(slot="question") Ich brauche unbedingt noch einen Platz, gibt es nicht doch noch eine Möglichkeit?
        span(slot="answer").
          Nein, wenn Du keine Mail bis eine Woche vorab erhalten hast sind alle Tische belegt.
          #[br]
          Versuch es einfach beim nächsten Termin nochmal oder komm als Gast für ein
          Bierchen vorbei und schau was die Anderen zu bieten haben. Darüber freuen wir uns sehr!

      question
        span(slot="question") Meine Frage wurde nicht beantwortet. Kann ich euch eine Mail schicken?
        span(slot="answer").
          Bestimmt kannst Du das, aber bitte hab Verständnis dafür, dass wir nicht die Zeit haben alle
          Mails zu beantworten. Darum komm doch einfach mal zum Flohmarkt und frag uns direkt. Dort
          beantworten wir Dir gerne Deine Fragen!

</template>

<script>
// @ is an alias to /src
import RegistrationForm from '@/components/RegistrationForm.vue'
import Question from '@/components/Question.vue'

export default {
  name: 'home',
  components: {
    RegistrationForm,
    Question
  },
  data () {
    return {
      nextEvent: null,
      currentEvent: null
    }
  },
  created () {
    window.axios.get('/next-market-event').then((response) => {
      if (response.data.start) {
        this.nextEvent = response.data
      }
    })
    window.axios.get('/current-market-event').then((response) => {
      if (response.data.start) {
        this.currentEvent = response.data
      }
    })
  },
  computed: {
    registrationOver: function () {
      return this.nextEvent && this.currentEvent && this.currentEvent.id !== this.nextEvent.id
    }
  }
}
</script>

<style lang="sass">
.marker
  color: #e09900
  font-weight: bold

h1, h2, h3
  font-family: 'Special Elite', cursive
  font-size: 30px
  line-height: 1em
  margin-bottom: 0.5em

h3
  font-size: 20px

body
  .application.theme--dark
    font-family: 'Raleway', serif
    font-size: 14px
    line-height: 1.8em
    color: #f2f2f2
    background: #080705

    .input-group--text-field input, .input-group--text-field textarea, label
      font-size: 14px

</style>
