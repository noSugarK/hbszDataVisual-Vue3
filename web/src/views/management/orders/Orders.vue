<template>
  <div class="orders-management-container">
    <!-- 头部导航 -->
    <AppHeader />

    <!-- 主要内容区域 -->
    <main class="main-content">
      <!-- 侧边栏 -->
      <SidebarNavigation />

      <!-- 内容区 -->
      <div class="content-area">
        <!-- 移动端二级导航 -->
        <MobileNavigation />

        <!-- 页面标题 -->
        <div class="page-header d-flex justify-content-between align-items-center mb-4">
          <h1 class="h3 mb-0">订单管理</h1>
          <button class="btn btn-primary" @click="showCreateForm">
            <i class="bi bi-plus-circle me-1"></i>添加订单
          </button>
        </div>

        <!-- 使用 StatsCards 组件展示统计信息 -->
        <StatsCards :stats="orderStats" />

        <!-- 使用 OrdersList 组件展示订单列表 -->
        <OrdersList
            :orders="orders"
            @viewOrder="viewOrder"
            @editOrder="editOrder"
        />

        <!-- 创建订单模态框 -->
        <div v-if="showCreateModal" class="modal-overlay" @click="showCreateModal = false">
          <div class="modal-content" @click.stop>
            <div class="modal-header">
              <h3>创建新订单</h3>
              <button class="close-btn" @click="showCreateModal = false">&times;</button>
            </div>
            <div class="modal-body">
              <form @submit.prevent="createOrder">
                <div class="form-group">
                  <label for="customerId">客户ID</label>
                  <input type="text" id="customerId" v-model="newOrder.customerId" required>
                </div>
                <div class="form-group">
                  <label for="customerName">客户名称</label>
                  <input type="text" id="customerName" v-model="newOrder.customerName" required>
                </div>
                <div class="form-group">
                  <label for="orderAmount">订单金额</label>
                  <input type="number" id="orderAmount" v-model="newOrder.amount" required>
                </div>
                <div class="form-group">
                  <label for="orderDescription">订单描述</label>
                  <textarea id="orderDescription" v-model="newOrder.description" rows="3"></textarea>
                </div>
                <div class="form-actions">
                  <button type="button" class="btn btn-secondary" @click="showCreateModal = false">取消</button>
                  <button type="submit" class="btn btn-primary">创建订单</button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </main>

    <!-- 页脚 -->
    <AppFooter />
  </div>
</template>

<script>
import { ref } from 'vue'
import AppHeader from "@/components/layout/AppHeader.vue"
import AppFooter from "@/components/layout/AppFooter.vue"
import SidebarNavigation from "@/components/layout/SidebarNavigation.vue"
import MobileNavigation from "@/components/layout/MobileNavigation.vue"
import OrdersList from "@/components/orders/OrdersList.vue"
import StatsCards from "@/components/common/StatsCards.vue"

export default {
  name: 'OrdersManagement',
  components: {
    AppHeader,
    AppFooter,
    SidebarNavigation,
    MobileNavigation,
    OrdersList,
    StatsCards
  },
  setup() {
    const showCreateModal = ref(false)

    const newOrder = ref({
      customerId: '',
      customerName: '',
      amount: '',
      description: ''
    })

    const orders = ref([
      {
        id: 'ORD-2025-001',
        customer: '湖北建设集团',
        date: '2025-09-10',
        amount: '125,000',
        status: '待处理',
        statusClass: 'status-pending'
      },
      {
        id: 'ORD-2025-002',
        customer: '武汉市政公司',
        date: '2025-09-09',
        amount: '86,500',
        status: '处理中',
        statusClass: 'status-in-progress'
      },
      {
        id: 'ORD-2025-003',
        customer: '宜昌工程公司',
        date: '2025-09-08',
        amount: '210,000',
        status: '已完成',
        statusClass: 'status-completed'
      },
      // ... 其他重复的 ORD-2025-003 订单数据
      {
        id: 'ORD-2025-004',
        customer: '荆州建筑公司',
        date: '2025-09-07',
        amount: '75,200',
        status: '已取消',
        statusClass: 'status-canceled'
      }
    ])

    // 订单统计信息，作为独立的数据对象
    const orderStats = ref([
      { value: 12, label: '待处理订单', color: '#ffc107' },
      { value: 36, label: '处理中订单', color: '#0d6efd' },
      { value: 84, label: '已完成订单', color: '#198754' },
      { value: 2,  label: '已取消订单', color: '#dc3545' }
    ])

    const viewOrder = (order) => {
      console.log('查看订单:', order)
    }

    const editOrder = (order) => {
      console.log('编辑订单:', order)
    }

    const createOrder = () => {
      console.log('创建订单:', newOrder.value)
      showCreateModal.value = false
      newOrder.value = {
        customerId: '',
        customerName: '',
        amount: '',
        description: ''
      }
    }

    return {
      showCreateModal,
      newOrder,
      orders,
      orderStats,
      viewOrder,
      editOrder,
      createOrder
    }
  }
}
</script>

<style scoped>
.main-content {
  max-width: 1500px;
  margin: 0 auto;
  padding: 20px;
  display: flex;
  flex: 1;
  gap: 20px;
}

.content-area {
  flex: 1;
  transition: filter 0.3s ease;
  position: relative;
}

@media (max-width: 1024px) {
  .main-content { flex-direction: row; }
  .content-area { width: 100%; }
}

@media (max-width: 768px) {
  .main-content { padding: 15px; gap: 15px; }
  .page-header { flex-direction: column; align-items: flex-start; gap: 15px; }
}
</style>