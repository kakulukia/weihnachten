import '@mdi/font/css/materialdesignicons.css'
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import moment from 'moment'

import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'

Vue.use(Vuetify, {
  theme: {
    primary: '#e09900'
  },
  iconfont: 'mdi' // 'md' || 'mdi' || 'fa' || 'fa4'
})

Vue.config.productionTip = false

let host = window.location.hostname
let port = ':8000'
if (host === 'flohmarkt.pepperz.de') {
  host = 'salatverkostung.pepperz.de'
  port = ''
}
if (host === 'flohmarkt.so36.com') {
  host = 'salat.pepperz.de'
  port = ''
}

let apiUrl = window.location.protocol + '//' + host + port
// let apiHost = apiUrl
apiUrl += '/api'
axios.defaults.baseURL = apiUrl
window.axios = axios

moment.locale('de')
Vue.filter('moment', function (date, format) {
  return moment(date).format(format)
})

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
