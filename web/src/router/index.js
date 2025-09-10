import { createRouter, createWebHistory } from 'vue-router'
import { useAccountStore } from '../stores/account.js'

const routes = [
    {
        path: '/login',
        name: 'Login',
        component: () => import('@/views/account/Login.vue'),
        meta: { requiresGuest: true , title: '登录' },
    },
    {
        path: '/',
        name: 'Home',
        component: () => import('../views/Home.vue'),
        meta: { requiresAuth: true , title: '首页' },
    },
    {
        path: '/forgot-password',
        name: 'ForgotPassword',
        component: () => import('@/views/account/ForgotPassword.vue'),
        meta: { title: '忘记密码' },
    },
    {
        path: '/reset-password/:uid/:token',
        name: 'ResetPassword',
        component: () => import('@/views/account/ResetPassword.vue'),
        meta: { title: '重置密码' },
    },
    {
        path: '/profile',
        name: 'UserProfile',
        component: () => import('../views/user/UserProfile.vue'),
        meta: { requiresAuth: true , title: '用户信息' },
    },
    {
        path: '/user/:id',
        name: 'UserDetail',
        component: () => import('../views/user/UserDetail.vue'),
        meta: { requiresAuth: true , title: '用户详情' },
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

// 全局路由守卫
router.beforeEach((to, from, next) => {
    const authStore = useAccountStore()

    if (to.meta.requiresAuth && !authStore.isAuthenticated) {
        next('/login')
    } else if (to.meta.requiresGuest && authStore.isAuthenticated) {
        next('/')
    } else {
        next()
    }
})

// 全局后置钩子，用于设置页面标题
router.afterEach((to, from) => {
    // 设置页面标题
    const appName = '材料成本可视化平台'
    const title = to.meta.title || '默认页面'
    document.title = `${appName} - ${title}`
})

export default router