// 账户相关路由
const accountRoutes = [
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/account/Login.vue'),
    meta: { requiresGuest: true, title: '登录' },
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
]

export default accountRoutes