const guidePriceRoutes = [
    {
        path: '/guide-price',
        name: 'guide-price',
        component: () => import('@/views/management/guidePrice/GuidePrice.vue'),
        meta: { requiresAuth: true, title: '指导价管理' },
    },
    // 可以在这里添加更多页面路由
]

export default guidePriceRoutes