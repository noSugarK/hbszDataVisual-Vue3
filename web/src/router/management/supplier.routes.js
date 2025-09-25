const supplierRoutes = [
    {
        path: '/supplier',
        name: 'supplier',
        component: () => import('@/views/management/supplier/Supplier.vue'),
        meta: { requiresAuth: true, title: '地区列表' },
    },
    // 可以在这里添加更多页面路由
]

export default supplierRoutes