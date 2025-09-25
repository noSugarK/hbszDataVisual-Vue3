<template>
  <!-- 订单列表 -->
  <div class="orders-list-section">
    <h2>订单列表</h2>
    <div class="orders-table-container">
      <table class="orders-table">
        <thead>
        <tr>
          <th>订单编号</th>
          <th>客户名称</th>
          <th>下单日期</th>
          <th>订单金额</th>
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
            <button class="btn btn-sm btn-outline-primary" @click="$emit('viewOrder', order)">
              查看
            </button>
            <button class="btn btn-sm btn-outline-secondary" @click="$emit('editOrder', order)">
              编辑
            </button>
          </td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'OrdersList',
  props: {
    // 接收来自父组件的订单数据
    orders: {
      type: Array,
      required: true
    }
  }
}
</script>

<style scoped>
/* 订单列表 */
.orders-list-section h2 {
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

.status-pending {
  background-color: #fff3cd;
  color: #856404;
}

.status-in-progress {
  background-color: #d1ecf1;
  color: #0c5460;
}

.status-completed {
  background-color: #d4edda;
  color: #155724;
}

.status-canceled {
  background-color: #f8d7da;
  color: #721c24;
}

/* 按钮样式（复用主样式） */
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

.btn-sm {
  padding: 0.25rem 0.5rem;
  font-size: 0.75rem;
  border-radius: 0.2rem;
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

/* 响应式设计 */
@media (max-width: 768px) {
  .orders-table {
    font-size: 0.8rem;
  }

  .orders-table th,
  .orders-table td {
    padding: 8px 10px;
  }
}

@media (max-width: 480px) {
  .orders-table {
    display: block;
    overflow-x: auto;
  }
}
</style>