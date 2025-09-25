const brandRoutes = [
    {
        path: '/brand',
        name: 'brand',
        component: () => import('@/views/management/brand/Brand.vue'),
        meta: { requiresAuth: true, title: '品牌列表' },
    },
    // 可以在这里添加更多页面路由
]

export default brandRoutes