import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  scrollBehavior() {
    return { top: 0 }
  },
  routes: [
    {
      path: '/',
      name: 'portfolio',
      meta: { title: "Sadellie's cool website" },
      component: () => import('@/views/HomeView.vue'),
    },
    {
      path: '/unitto',
      component: () => import('@/views/UnittoView.vue'),
      meta: { title: 'Unitto' },
      children: [
        {
          path: '',
          name: 'home',
          meta: { title: 'Unitto' },
          component: () => import('@/components/UnittoHomePage.vue'),
        },
        {
          path: 'privacy',
          name: 'privacy',
          meta: { title: 'Unitto Privacy Policy' },
          component: () => import('@/components/UnittoPrivacyPolicyPage.vue')
        },
        {
          path: 'terms',
          name: 'terms',
          meta: { title: 'Unitto Terms and Conditions' },
          component: () => import('@/components/UnittoTermsAndConditionsPage.vue')
        },
        {
          path: 'press',
          name: 'press',
          meta: { title: 'Unitto Press Kit' },
          component: () => import('@/components/UnittoPressKitPage.vue')
        },
      ]
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'not-found',
      meta: { title: 'Not Found' },
      component: () => import('@/views/NotFoundView.vue')
    }
  ]
})

router.beforeEach((to, from, next) => {
  let pageTitle = to.meta?.title as string | null
  if (pageTitle != null) {
    document.title = pageTitle
  }

  next()
})

export default router
