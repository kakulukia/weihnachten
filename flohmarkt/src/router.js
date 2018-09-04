import Vue from 'vue'
import Router from 'vue-router'
import Registration from './views/Registration.vue'
import Done from './views/Done.vue'
import ValidateEmail from './views/ValidateEmail.vue'
import CancelMarketInquiry from './views/CancelMarketInquiry.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Registration
    },
    {
      path: '/done',
      name: 'done',
      component: Done
    },
    {
      path: '/validate-email/:token',
      name: 'done',
      component: ValidateEmail
    },
    {
      path: '/cancel-market-inquiry/:token',
      name: 'done',
      component: CancelMarketInquiry
    }
  ]
})
