// 主要页面路由
const mainRoutes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue'),
    meta: { requiresAuth: true, title: '首页' },
  },
  // 可以在这里添加更多主要页面路由
]

export default mainRoutes