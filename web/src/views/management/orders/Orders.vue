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
        <MobileNavigation v-if="isMobile" />

        <!-- 页面标题 -->
        <div class="page-header">
          <h1>订单管理</h1>
          <button class="btn btn-primary" @click="showCreateModal = true">创建订单</button>
        </div>

        <!-- 订单统计卡片 -->
        <div class="stats-cards">
          <div class="stat-card">
            <div class="stat-value">12</div>
            <div class="stat-label">待处理订单</div>
          </div>
          <div class="stat-card">
            <div class="stat-value">36</div>
            <div class="stat-label">处理中订单</div>
          </div>
          <div class="stat-card">
            <div class="stat-value">84</div>
            <div class="stat-label">已完成订单</div>
          </div>
          <div class="stat-card">
            <div class="stat-value">2</div>
            <div class="stat-label">已取消订单</div>
          </div>
        </div>

        <!-- 订单列表 -->
        <div class="orders-section">
          <h2>订单列表</h2>
          <div class="orders-table-container">
            <table class="orders-table">
              <thead>
              <tr>
                <th>订单编号</th>
                <th>客户名称</th>
                <th>下单时间</th>
                <th>总金额</th>
                <th>状态</th>
                <th>操作</th>
              </tr>
              </thead>
              <tbody>
              <tr v-for="order in orders" :key="order.id">
                <td>{{ order.id }}</td>
                <td>{{ order.customer }}</td>
                <td>{{ order.date }}</td>
                <td>¥{{ order.amount }}</td>
                <td>
                    <span :class="['status-badge', order.statusClass]">
                      {{ order.status }}
                    </span>
                </td>
                <td>
                  <button class="btn btn-sm btn-outline-primary" @click="viewOrder(order)">查看</button>
                  <button class="btn btn-sm btn-outline-secondary" @click="editOrder(order)">编辑</button>
                </td>
              </tr>
              </tbody>
            </table>
          </div>
        </div>

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
import { ref, onMounted, onBeforeUnmount } from 'vue'
import AppHeader from "@/components/layout/AppHeader.vue"
import AppFooter from "@/components/layout/AppFooter.vue"
import SidebarNavigation from "@/components/layout/SidebarNavigation.vue"
import MobileNavigation from "@/components/layout/MobileNavigation.vue";

export default {
  name: 'OrdersManagement',
  components: {
    AppHeader,
    AppFooter,
    SidebarNavigation,
    MobileNavigation,
  },
  setup() {
    // 移动端状态
    const isMobile = ref(false)

    // 模态框状态
    const showCreateModal = ref(false)

    // 新订单数据
    const newOrder = ref({
      customerId: '',
      customerName: '',
      amount: '',
      description: ''
    })

    // 订单数据
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
      {
        id: 'ORD-2025-003',
        customer: '宜昌工程公司',
        date: '2025-09-08',
        amount: '210,000',
        status: '已完成',
        statusClass: 'status-completed'
      },
      {
        id: 'ORD-2025-003',
        customer: '宜昌工程公司',
        date: '2025-09-08',
        amount: '210,000',
        status: '已完成',
        statusClass: 'status-completed'
      },
      {
        id: 'ORD-2025-003',
        customer: '宜昌工程公司',
        date: '2025-09-08',
        amount: '210,000',
        status: '已完成',
        statusClass: 'status-completed'
      },
      {
        id: 'ORD-2025-003',
        customer: '宜昌工程公司',
        date: '2025-09-08',
        amount: '210,000',
        status: '已完成',
        statusClass: 'status-completed'
      },
      {
        id: 'ORD-2025-003',
        customer: '宜昌工程公司',
        date: '2025-09-08',
        amount: '210,000',
        status: '已完成',
        statusClass: 'status-completed'
      },
      {
        id: 'ORD-2025-003',
        customer: '宜昌工程公司',
        date: '2025-09-08',
        amount: '210,000',
        status: '已完成',
        statusClass: 'status-completed'
      },
      {
        id: 'ORD-2025-003',
        customer: '宜昌工程公司',
        date: '2025-09-08',
        amount: '210,000',
        status: '已完成',
        statusClass: 'status-completed'
      },
      {
        id: 'ORD-2025-003',
        customer: '宜昌工程公司',
        date: '2025-09-08',
        amount: '210,000',
        status: '已完成',
        statusClass: 'status-completed'
      },
      {
        id: 'ORD-2025-003',
        customer: '宜昌工程公司',
        date: '2025-09-08',
        amount: '210,000',
        status: '已完成',
        statusClass: 'status-completed'
      },
      {
        id: 'ORD-2025-003',
        customer: '宜昌工程公司',
        date: '2025-09-08',
        amount: '210,000',
        status: '已完成',
        statusClass: 'status-completed'
      },
      {
        id: 'ORD-2025-003',
        customer: '宜昌工程公司',
        date: '2025-09-08',
        amount: '210,000',
        status: '已完成',
        statusClass: 'status-completed'
      },
      {
        id: 'ORD-2025-003',
        customer: '宜昌工程公司',
        date: '2025-09-08',
        amount: '210,000',
        status: '已完成',
        statusClass: 'status-completed'
      },
      {
        id: 'ORD-2025-003',
        customer: '宜昌工程公司',
        date: '2025-09-08',
        amount: '210,000',
        status: '已完成',
        statusClass: 'status-completed'
      },
      {
        id: 'ORD-2025-003',
        customer: '宜昌工程公司',
        date: '2025-09-08',
        amount: '210,000',
        status: '已完成',
        statusClass: 'status-completed'
      },
      {
        id: 'ORD-2025-003',
        customer: '宜昌工程公司',
        date: '2025-09-08',
        amount: '210,000',
        status: '已完成',
        statusClass: 'status-completed'
      },
      {
        id: 'ORD-2025-003',
        customer: '宜昌工程公司',
        date: '2025-09-08',
        amount: '210,000',
        status: '已完成',
        statusClass: 'status-completed'
      },
      {
        id: 'ORD-2025-003',
        customer: '宜昌工程公司',
        date: '2025-09-08',
        amount: '210,000',
        status: '已完成',
        statusClass: 'status-completed'
      },
      {
        id: 'ORD-2025-003',
        customer: '宜昌工程公司',
        date: '2025-09-08',
        amount: '210,000',
        status: '已完成',
        statusClass: 'status-completed'
      },
      {
        id: 'ORD-2025-003',
        customer: '宜昌工程公司',
        date: '2025-09-08',
        amount: '210,000',
        status: '已完成',
        statusClass: 'status-completed'
      },
      {
        id: 'ORD-2025-003',
        customer: '宜昌工程公司',
        date: '2025-09-08',
        amount: '210,000',
        status: '已完成',
        statusClass: 'status-completed'
      },
      {
        id: 'ORD-2025-003',
        customer: '宜昌工程公司',
        date: '2025-09-08',
        amount: '210,000',
        status: '已完成',
        statusClass: 'status-completed'
      },
      {
        id: 'ORD-2025-003',
        customer: '宜昌工程公司',
        date: '2025-09-08',
        amount: '210,000',
        status: '已完成',
        statusClass: 'status-completed'
      },
      {
        id: 'ORD-2025-003',
        customer: '宜昌工程公司',
        date: '2025-09-08',
        amount: '210,000',
        status: '已完成',
        statusClass: 'status-completed'
      },
      {
        id: 'ORD-2025-003',
        customer: '宜昌工程公司',
        date: '2025-09-08',
        amount: '210,000',
        status: '已完成',
        statusClass: 'status-completed'
      },
      {
        id: 'ORD-2025-003',
        customer: '宜昌工程公司',
        date: '2025-09-08',
        amount: '210,000',
        status: '已完成',
        statusClass: 'status-completed'
      },
      {
        id: 'ORD-2025-003',
        customer: '宜昌工程公司',
        date: '2025-09-08',
        amount: '210,000',
        status: '已完成',
        statusClass: 'status-completed'
      },
      {
        id: 'ORD-2025-003',
        customer: '宜昌工程公司',
        date: '2025-09-08',
        amount: '210,000',
        status: '已完成',
        statusClass: 'status-completed'
      },
      {
        id: 'ORD-2025-004',
        customer: '荆州建筑公司',
        date: '2025-09-07',
        amount: '75,200',
        status: '已取消',
        statusClass: 'status-delayed'
      }
    ])

    // 响应式处理
    const checkScreenSize = () => {
      isMobile.value = window.innerWidth < 768
    }

    // 查看订单详情
    const viewOrder = (order) => {
      console.log('查看订单:', order)
      // 这里可以跳转到订单详情页面
    }

    // 编辑订单
    const editOrder = (order) => {
      console.log('编辑订单:', order)
      // 这里可以打开编辑模态框
    }

    // 创建订单
    const createOrder = () => {
      console.log('创建订单:', newOrder.value)
      // 这里可以调用API创建订单
      showCreateModal.value = false
      // 重置表单
      newOrder.value = {
        customerId: '',
        customerName: '',
        amount: '',
        description: ''
      }
    }

    onMounted(() => {
      checkScreenSize()
      window.addEventListener('resize', checkScreenSize)
    })

    onBeforeUnmount(() => {
      window.removeEventListener('resize', checkScreenSize)
    })

    return {
      isMobile,
      showCreateModal,
      newOrder,
      orders,
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

/* 统计卡片 */
.stats-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.stat-card {
  background-color: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.stat-value {
  font-size: 2rem;
  font-weight: 600;
  color: #0d6efd;
  margin-bottom: 5px;
}

.stat-label {
  font-size: 0.9rem;
  color: #6c757d;
}

/* 订单列表 */
.orders-section h2 {
  font-size: 1.4rem;
  font-weight: 600;
  margin-bottom: 20px;
  color: #212529;
}

.orders-table-container {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.orders-table {
  width: 100%;
  border-collapse: collapse;
}

.orders-table th,
.orders-table td {
  padding: 12px 15px;
  text-align: left;
  border-bottom: 1px solid #dee2e6;
}

.orders-table th {
  background-color: #f8f9fa;
  font-weight: 600;
  color: #495057;
}

.orders-table tbody tr:hover {
  background-color: #f8f9fa;
}

/* 状态标签 */
.status-badge {
  display: inline-block;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 0.75rem;
  font-weight: 500;
}

.status-in-progress {
  background-color: #d1ecf1;
  color: #0c5460;
}

.status-completed {
  background-color: #d4edda;
  color: #155724;
}

.status-pending {
  background-color: #fff3cd;
  color: #856404;
}

.status-delayed {
  background-color: #f8d7da;
  color: #721c24;
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

/* 移动端二级导航 */
.mobile-filters {
  display: none;
  background-color: white;
  border-radius: 8px;
  padding: 15px 20px;
  margin-bottom: 20px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  margin: 0 -20px 20px -20px;
}

.mobile-filters {
  flex-direction: row;
  flex-wrap: auto;
  overflow-x: auto;
  padding-bottom: 5px;
  white-space: nowrap;
}

.mobile-filters {
  flex-shrink: 0;
  background-color: transparent;
  color: #5f6368;
  border: none;
  padding: 6px 10px;
  border-radius: 4px;
  font-size: 0.85rem;
  cursor: pointer;
  text-align: left;
  transition: all 0.2s ease;
  text-decoration: none;
  display: inline-block;
  margin-right: 5px;
}

.mobile-filters :hover {
  background-color: #f0f2f5;
  color: #1a73e8;
}

.mobile-filters  {
  background-color: #f0f2f5;
  color: #1a73e8;
  font-weight: 500;
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
  /* 显示移动端二级导航 */
  .page-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 15px;
  }

  .stats-cards {
    grid-template-columns: 1fr 1fr;
  }

  .orders-table {
    font-size: 0.8rem;
  }

  .orders-table th,
  .orders-table td {
    padding: 8px 10px;
  }

  .modal-content {
    margin: 10px;
  }
}

@media (max-width: 480px) {
  .stats-cards {
    grid-template-columns: 1fr;
  }

  .orders-table {
    display: block;
    overflow-x: auto;
  }
}
</style>
