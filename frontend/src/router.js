import { createRouter, createWebHistory } from 'vue-router'
import { session } from './data/session'
import { userResource } from '@/data/user'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/pages/Home.vue'),
    children: [
      { path: '/welcome', component: () => import('@/components/Welcomehome.vue') },
      { path: '/companydetails', component: () => import('@/components/Companydetails.vue') },
      { path: '/Categorybusiness', component: () => import('@/components/Categorybusiness.vue') },
      { path: '/contactdetails', component: () => import('@/components/Contactdetails.vue') },
      { path: '/accountdetails', component: () => import('@/components/Accountdetails.vue') },
      { path: '/documentdetails', component: () => import('@/components/Documentdetails.vue') },
      
    ]
  },
  {
    name: 'Login',
    path: '/account/login',
    component: () => import('@/pages/Login.vue'),
  }
]

let router = createRouter({
  history: createWebHistory('/frontend'),
  routes,
})

router.beforeEach(async (to, from, next) => {
  let isLoggedIn = session.isLoggedIn
  try {
    await userResource.promise
  } catch (error) {
    isLoggedIn = false
  }

  if (to.name === 'Login' && isLoggedIn) {
    next({ name: 'Home' })
  } else if (to.name !== 'Login' && !isLoggedIn) {
    next({ name: 'Login' })
  } else {
    next()
  }
})

export default router
