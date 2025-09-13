const ordersRoutes = [
    {
        path: '/orders',
        name: 'orders',
        component: () => import('@/views/management/orders/Orders.vue'),
        meta: { requiresAuth: true, title: '地区列表' },
    },
    // 可以在这里添加更多页面路由
]

export default ordersRoutes