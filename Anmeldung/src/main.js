import '@babel/polyfill'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import store from './store'
import './registerServiceWorker'
import axios from 'axios'
import VueAxios from 'vue-axios'
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

// configure the api connection
let host = window.location.hostname
if (host === 'pepperz.de') {
  host = 'admin.pepperz.de'
}
let apiUrl = window.location.protocol + '//' + host
if (window.location.hostname !== 'pepperz.de') {
  apiUrl += ':8000'
}
apiUrl += '/api'
let api = axios.create({
  baseURL: apiUrl,
  timeout: 15000,
  addTrailingSlash: true
})
api.interceptors.request.use((config) => {
  if (config.addTrailingSlash && config.url[config.url.length - 1] !== '/') {
    config.url += '/'
  }
  return config
})

window.axios = api
Vue.use(VueAxios, api)
moment.locale('de')
Vue.filter('moment', function (date, format) {
  return moment(date).format(format)
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
