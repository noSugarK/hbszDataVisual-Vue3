const categoryRoutes = [
    {
        path: '/category',
        name: 'category',
        component: () => import('@/views/management/category/Category.vue'),
        meta: { requiresAuth: true, title: '物资列表' },
    },
    // 可以在这里添加更多页面路由
]

export default categoryRoutes