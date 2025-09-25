前端主目录结构

```
src/
├── assets/                 # 静态资源
│   ├── base.css
│   └── main.css
├── components/             # 公共组件
│   ├── layout/             # 布局组件
│   │   ├── AppFooter.vue
│   │   ├── AppHeader.vue
│   │   └── MainLayout.vue
│   └── common/             # 通用业务组件
├── router/                 # 路由配置
│   └── index.js
├── services/               # API服务
│   ├── api.js
│   ├── auth.service.js
│   ├── project.service.js
│   ├── user.api.js
│   └── visualization.service.js
├── stores/                 # 状态管理
│   ├── account.js
│   ├── project.js
│   └── visualization.js
├── utils/                  # 工具函数
│   └── account.js
├── views/                  # 页面视图
│   ├── auth/               # 认证模块
│   │   ├── Login.vue
│   │   ├── Register.vue
│   │   ├── ForgotPassword.vue
│   │   └── ResetPassword.vue
│   ├── dashboard/          # 主控面板
│   │   └── Dashboard.vue
│   ├── profile/            # 个人中心模块
│   │   ├── ProfileView.vue
│   │   ├── EditProfile.vue
│   │   └── ChangePassword.vue
│   ├── users/              # 用户管理模块
│   │   ├── UserList.vue
│   │   └── UserForm.vue
│   ├── projects/           # 项目管理模块
│   │   ├── ProjectList.vue
│   │   ├── ProjectForm.vue
│   │   └── ProjectDetail.vue
│   ├── regions/            # 地区管理模块
│   │   ├── RegionList.vue
│   │   └── RegionForm.vue
│   ├── materials/          # 物资管理模块
│   │   ├── CategoryList.vue
│   │   ├── SpecificationList.vue
│   │   ├── BrandList.vue
│   │   └── SupplierList.vue
│   ├── orders/             # 采购订单模块
│   │   ├── OrderList.vue
│   │   ├── OrderForm.vue
│   │   └── OrderDetail.vue
│   ├── prices/             # 价格管理模块
│   │   ├── PriceList.vue
│   │   ├── PriceForm.vue
│   │   └── PriceImport.vue
│   ├── permissions/        # 权限管理模块
│   │   ├── ProjectPermission.vue
│   │   ├── RegionPermission.vue
│   │   └── PermissionList.vue
│   ├── visualizations/     # 数据可视化模块
│   │   ├── VisualizationList.vue
│   │   ├── VisualizationForm.vue
│   │   ├── PriceTrend.vue
│   │   ├── PurchaseAnalysis.vue
│   │   └── OrderAnalysis.vue
│   ├── reports/            # 报表模块
│   │   ├── ReportList.vue
│   │   └── CustomReport.vue
│   ├── system/             # 系统管理模块
│   │   ├── Logs.vue
│   │   ├── Settings.vue
│   │   └── DataSubmission.vue
│   └── Home.vue
├── App.vue
└── main.js
```