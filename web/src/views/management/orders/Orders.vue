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
        <div class="page-header">
          <h1>订单管理</h1>
          <button class="btn btn-primary" @click="showCreateModal = true">创建订单</button>
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
/* 基础样式重置 */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  line-height: 1.6;
  color: #333;
  background-color: #f8f9fa;
}

/* 全局容器 */
.orders-management-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

/* 主要内容区域 */
.main-content {
  max-width: 1500px;
  margin: 0 auto;
  padding: 20px;
  display: flex;
  flex: 1;
  gap: 20px;
  align-items: flex-start;
}

/* 内容区 */
.content-area {
  flex: 1;
}

/* 页面标题 */
.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
}

.page-header h1 {
  font-size: 1.8rem;
  font-weight: 600;
  color: #212529;
}

/* 按钮样式 */
.btn {
  display: inline-block;
  font-weight: 400;
  text-align: center;
  white-space: nowrap;
  vertical-align: middle;
  user-select: none;
  border: 1px solid transparent;
  padding: 0.375rem 0.75rem;
  font-size: 0.875rem;
  line-height: 1.5;
  border-radius: 0.25rem;
  transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
  cursor: pointer;
}

.btn-primary {
  color: #fff;
  background-color: #0d6efd;
  border-color: #0d6efd;
}

.btn-primary:hover {
  background-color: #0b5ed7;
  border-color: #0a58ca;
}

.btn-secondary {
  color: #fff;
  background-color: #6c757d;
  border-color: #6c757d;
}

.btn-secondary:hover {
  background-color: #5c636a;
  border-color: #565e64;
}

.btn-outline-primary {
  color: #0d6efd;
  background-color: transparent;
  border-color: #0d6efd;
}

.btn-outline-primary:hover {
  color: #fff;
  background-color: #0d6efd;
  border-color: #0d6efd;
}

.btn-outline-secondary {
  color: #6c757d;
  background-color: transparent;
  border-color: #6c757d;
}

.btn-outline-secondary:hover {
  color: #fff;
  background-color: #6c757d;
  border-color: #6c757d;
}

.btn-sm {
  padding: 0.25rem 0.5rem;
  font-size: 0.75rem;
  border-radius: 0.2rem;
}

/* 模态框 */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 500px;
  max-height: 90vh;
  overflow-y: auto;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  border-bottom: 1px solid #dee2e6;
}

.modal-header h3 {
  margin: 0;
  font-size: 1.25rem;
  font-weight: 600;
}

.close-btn {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: #6c757d;
}

.close-btn:hover {
  color: #000;
}

.modal-body {
  padding: 20px;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: 500;
  color: #495057;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 8px 12px;
  border: 1px solid #ced4da;
  border-radius: 4px;
  font-size: 0.875rem;
}

.form-group input:focus,
.form-group textarea:focus {
  outline: none;
  border-color: #86b7fe;
  box-shadow: 0 0 0 0.25rem rgba(13, 110, 253, 0.25);
}

.form-actions {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-top: 20px;
}

/* 响应式设计 */
@media (max-width: 1024px) {
  .main-content {
    flex-direction: row;
  }

  .content-area {
    width: calc(100% - 270px);
    min-width: 0;
  }
}

@media (max-width: 768px) {
  .page-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 15px;
  }

  .modal-content {
    margin: 10px;
  }
}
</style>