<template lang="pug">
  div
    v-container(fluid grid-list-md)
      img.elfo(src="/img/elfo.png")
      h1.title Weihnachten fällt AUS!

      br
      p.
        Vielen Dank das Sie uns buchen möchten!
        #[br]#[br]
        Bitte wählen Sie einen Veranstaltungstag, füllen das untenstehnde Formular aus
        und drücken dann auf "BUCHEN". Das Eintrittsgeld beträgt für Kinder und Erwachsene
        jeweils 3,- €, wobei pro 10 Kinder ein Erwachsener frei ist. #[br]
        Sie erhalten nach der Buchung eine Bestätigungs-E-Mail mit den Kontodaten.
        Bitte überweisen Sie den Betrag innerhalb von 5 Tagen. Eine Stornierung ist nicht möglich.
        Sobald das Geld auf unserem Konto eingegangens ist, erhalten Sie eine weitere E-Mail
        mit Ihrer Buchungsbestätigung. #[br]
        Bringen Sie diese bitte am Veranstaltungstag mit.
        #[br]#[br]
        Mit freundlichen Grüßen #[br]
        Ihr Musical AG Team

      div.spacer

      h4(v-if="!selectedEvent") Wählen Sie einen Veranstaltungstag:

      v-layout(row wrap)
        v-flex.event(v-for="event in events" xs12 sm6 md4 lg2 :key="event.id"  @click="selectedEvent = event")
          v-card(:class="{active: selectedEvent == event}")
            v-card-title
              div
                h3.headline.mb-0 {{ event.start | moment("D.M.Y") }}
                div {{ event.available_places}} freie Plätze
                div {{ event.start | moment("HH:mm") }} Uhr, Jugendfreizeiteinrichtung FAIR
                div Marzahner Promenade 51, 12679 Berlin

      br

      v-form(v-model="valid" ref="form" v-if="selectedEvent")
        v-layout(row wrap)
          v-flex(xs12 sm6)
            v-text-field(
              label="Vorname*" v-model="form.first_name" required :counter="25"
              :error-messages="form.errors.get('first_name')"
              @focus="form.errors.clear('first_name')")
          v-flex(xs12 sm6)
            v-text-field(
              label="Nachname*" v-model="form.last_name" required :counter="25"
              :error-messages="form.errors.get('last_name')"
              @focus="form.errors.clear('last_name')")
          v-flex(xs12 sm6)
            v-text-field(
              label="E-Mail*" v-model="form.email" required
              :error-messages="form.errors.get('email')"
              @focus="form.errors.clear('email')")
          v-flex(xs12 sm6)
            v-text-field(
              label="Telefonnummer*" v-model="form.phone" required
              :error-messages="form.errors.get('phone')"
              @focus="form.errors.clear('phone')")
          v-flex(xs12 sm6)
            v-text-field(
              label="Anzahl Kinder*" v-model="form.kids" required
              :error-messages="form.errors.get('kids')"
              @focus="form.errors.clear('kids')")
          v-flex(xs12 sm6)
            v-text-field(
              label="Anzahl Erwachsene*" v-model="form.adults" required
              :error-messages="form.errors.get('adults')"
              @focus="form.errors.clear('adults')")
          v-flex(xs12 sm6)
            v-text-field(
              label="Schule / Klasse" v-model="form.class_name" required
              :error-messages="form.errors.get('class_name')"
              @focus="form.errors.clear('class_name')")

        v-alert(:value="form.errors.isDanger('non_field_errors')"
                type="error" icon="new_releases")
          span(v-text="form.errors.get('non_field_errors')")

        p Gesamtbetrag:
          |
          |
          strong {{ total }}
        v-btn.primary.mx-0(:disabled="!valid" @click="submit") Buchen

        br
        br
        span.grey--text * Pflichtfelder

</template>

<script>
import Form from '@/core/Form'

export default {
  data: function () {
    return {
      events: [],
      selectedEvent: null,
      valid: true,
      form: new Form({
        first_name: '',
        last_name: '',
        email: '',
        phone: '',
        class_name: '',
        kids: '',
        adults: '',
        event: null
      })
    }
  },
  created: function () {
    this.axios.get('events').then(response => {
      this.events = response.data
    })
  },
  methods: {
    submit () {
      // if (this.$refs.form.validate()) {

      if (!this.selectedEvent.for_schools) {
        this.form.class_name = 'privat'
      }

      this.form.event = this.selectedEvent.id
      this.form.submit('post', 'inquiries').then((response) => {
        this.$router.push('/done')
      }).catch(error => {
        console.log(error)
      })
    }
    // }
  },
  computed: {
    total: function () {
      if (this.form.kids || this.form.adults) {
        let sum = 0
        let kids = parseInt(this.form.kids)
        let adults = parseInt(this.form.adults)

        if (kids && kids > 0) {
          sum += kids
        }
        if (adults && adults > 0) {
          if (kids && kids > 0) {
            let discount = parseInt(kids / 10)
            sum += Math.max(0, adults - discount)
          } else {
            sum += adults
          }
        }
        return sum * 3 + ',- €'
      }
      return '-'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="sass">
.title
  color: #d3353d

@media screen and (min-width: 800px)
  .elfo
    height: 350px
    float: right
@media screen and (max-width: 799px)
  .elfo
    height: 200px
    margin: 0 auto
    display: block
    margin-bottom: 30px


.spacer
  clear: both

.event
  cursor: pointer
  .active
    background: rgba(245, 221, 93, 1)
</style>
