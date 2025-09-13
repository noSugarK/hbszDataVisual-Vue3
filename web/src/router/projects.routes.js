const projectsRoutes = [
  {
    path: '/projects',
    name: 'Projects',
    component: () => import('@/views/management/projects/Projects.vue'),
    meta: { requiresAuth: true, title: '项目列表' },
  },
  // 可以在这里添加更多页面路由
]

export default projectsRoutes