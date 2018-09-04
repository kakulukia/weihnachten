<template lang="pug">
  v-app#app(dark)
    v-content
      .nav
        v-container.header
          a.logo(href="https://so36.com/")
            img(src="https://so36.com/wp-content/uploads/2018/02/SO36_VektorLogo-03.png",
                alt="SO36", height="66")
          v-spacer
          .desktop
            a(href="https://so36.com/events/") Events
            a.active(href="https://flohmarkt.so36.com/") Flohmarkt
            a(href="https://tickets.so36.de/browse/tickets/de,0,4757,0,0.html") Tickets / Shop
            ul.sub-menu
              li
                a(href="https://tickets.so36.de/browse/tickets/de,0,4757,0,0.html") Tickets
              li
                a(href="https://shop.so36.de/browse/buecher/de,0,5732,0,0.html") Das SO36 Buch
              li
                a(href="https://shop.so36.de/browse/merchandise/de,0,7530,0,0.html") Merchandise
            a(href="https://so36.com/about/") About
            a(href="https://so36.com/contact/") Contact

          .mobile
            span.mobile-button(@click="menuActive = !menuActive")
              v-icon mdi-menu

      ul.mobile-menu(:class="{menuActive}")
        li
          a(href="https://so36.com/events/") Events
        li
          a(href="https://tickets.so36.de/browse/tickets/de,0,4757,0,0.html") Tickets / Shop
        li.sub
          a(href="https://tickets.so36.de/browse/tickets/de,0,4757,0,0.html") Tickets
        li.sub
          a(href="https://shop.so36.de/browse/buecher/de,0,5732,0,0.html") Das SO36 Buch
        li.sub
          a(href="https://shop.so36.de/browse/merchandise/de,0,7530,0,0.html") Merchandise
        li
          a(href="https://so36.com/gallery/") Gallery
        li
          a(href="https://so36.com/about/") About
        li
          a(href="https://so36.com/contact/") Contact

      div.main
        v-container.view-area
          router-view

        footer
          v-container
            v-layout(row, wrap)
              v-flex.message(sm12, md6)
                h3.so
                  em SO36
                p
                  em.
                    stands up against any form of deeds or expressions of racism, sexism or homophobia.
                    We reserve our right to cancel events or performances and to banish any person from
                    our venue which offend against this policy!
                    #[a.more(href="https://so36.com/about/") read more]

                .media-links
                  a.fb(href="https://www.facebook.com/Esso36/", title="Facebook", target="_blank")
                   v-icon mdi-facebook
                  a.ig(href="https://www.instagram.com/so36_club/", title="Instagram", target="_blank")
                    v-icon mdi-instagram
                  a.yt(href="https://www.youtube.com/results?search_query=so36+berlin", title="Youtube", target="_blank")
                    v-icon mdi-youtube
                  a.tw(href="https://twitter.com/so36berlin", title="Twitter", target="_blank")
                    v-icon mdi-twitter

              v-flex.about(xs12, sm6, md3)
                h3 About
                ul
                  li
                    a(href="https://so36.com/about/") The Club
                  li
                    a(href="https://so36.com/technics/") Technics
                  li
                    a(href="https://so36.com/history/") History
                  li
                    a(href="https://so36.com/60m2/") 60m² Kunst im Klub

              v-flex.imprint(xs12, sm6, md3)
                h3 Info/Imprint
                ul
                  li
                    a(href="https://so36.com/impressum/") Imprint
                  li
                    a(href="https://so36.com/datenschutz/") Datenschutz/Disclaimer
                  li
                    a(href="https://so36.com/kontakt/") Contact
                  li
                    a(href="https://so36.com/press/") Press

</template>

<script>

export default {
  data: function () {
    return {
      menuActive: false
    }
  }
}
</script>

<style lang="sass">
body

  .main
    position: relative
    display: flex
    flex-direction: column
    min-height: 100vh

    .view-area
      flex-grow: 4

  footer
    background: #191919
    padding-top: 60px
    font-family: 'Raleway', serif
    font-size: 14px
    line-height: 1.8em
    font-weight: 500

    h3.so
      font-size: 22px

    h3
      font-weight: 500

    a
      color: #dd9933
      text-decoration: none

    .message, .about, .imprint
      padding-bottom: 30px

    .media-links
      a
        display: inline-flex
        align-items: center
        justify-content: center
        height: 32px
        width: 32px
        border-radius: 4px
        margin-right: 8px

        .icon
          font-size: 20px

        &.fb
          background-color: #3b5998
        &.ig
          background-color: #ea2c59
        &.yt
          background-color: #a82400
        &.tw
          background-color: #00aced

  .mobile-menu
    top: -400px
    transition: all 0.5s
    visibility: visible
    position: absolute
    right: 16px
    z-index: 2
    width: 250px
    padding: 5%
    border-top: 3px solid #e09900
    opacity: 1
    background: #fff
    -webkit-box-shadow: 0 2px 5px rgba(0,0,0,.1)
    -moz-box-shadow: 0 2px 5px rgba(0,0,0,.1)
    box-shadow: 0 2px 5px rgba(0,0,0,.1)

    &.menuActive
      top: 60px

    li
      list-style: none

      &.sub
        margin-left: 30px

      a
        text-decoration: none
        font-weight: bold
        display: block
        padding: 10px 20px
        font-size: 14px
        border-bottom: 1px solid rgba(0,0,0,.03)
        color: #666

        &:hover
          opacity: .7
          background-color: rgba(0,0,0,.03)

  .desktop, .logo img
    transition: all 0.5s

  .logo img
    position: relative
    top: 4px

  @media only screen and (max-width: 810px)
    .mobile-button .icon
      display: inline-flex
      color: #e09900
      cursor: pointer

    .main
      padding-top: 70px

    .header
      height: 60px
      .desktop
        display: none

    .logo img
      height: 42px

  @media only screen and (min-width: 811px)
    .mobile-button .icon, .mobile-menu
      display: none

    .main
      padding-top: 120px

    .desktop
      display: block

.nav
  z-index: 7
  background: url('./assets/header-bg.png')
  position: fixed
  width: 100%
  top: 0
.header
  transition: all 0.5s
  height: 94px

  font-family: 'Special Elite', cursive
  font-size: 20px
  flex-direction: row
  display: flex
  align-items: center

  .desktop
    flex-direction: row
    display: flex
    align-items: center
    a
      display: block
      color: rgba(0, 0, 0, .6)
      padding-left: 22px
      font-weight: bold
      text-transform: uppercase
      &.logo
        margin-left: -40px
      &.active
        color: #e09900
      &:hover
        color: rgba(0, 0, 0, 0.7)

@media only screen and (min-width: 1264px)
  body .container
    max-width: 1080px

ul.sub-menu
  width: 240px
  border-top: 3px solid #2ea3f2
  opacity: 0
  visibility: hidden
  background-image: initial
  background-position-x: initial
  background-position-y: initial
  background-size: initial
  background-attachment: initial
  background-origin: initial
  background-clip: initial
  background-color: rgb(255, 255, 255)
  box-shadow: 0 2px 5px rgba(0,0,0,.1)
  position: absolute
  padding: 20px 0
  color: rgba(0,0,0,0.7)
  list-style: none

  li
    padding: 0 20px
    a
      padding: 6px 20px
    a:hover
      background-color: rgba(0, 0, 0, .03)
</style>
