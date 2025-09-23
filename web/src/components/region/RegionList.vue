<template>
  <!-- 区域列表 -->
  <div class="region-list-section">
    <h2>区域列表</h2>
    <div class="region-table-container">
      <table class="region-table">
        <thead>
        <tr>
          <th>区域名称</th>
          <th>负责人</th>
          <th>项目数量</th>
          <th>合作单位</th>
          <th>状态</th>
          <th>操作</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="region in regions" :key="region.id">
          <td>{{ region.name }}</td>
          <td>{{ region.manager }}</td>
          <td>{{ region.projectCount }}</td>
          <td>{{ region.partners }}</td>
          <td>
              <span :class="['status-badge', region.statusClass]">
                {{ region.status }}
              </span>
          </td>
          <td>
            <button class="btn btn-sm btn-outline-primary" @click="$emit('viewRegion', region)">
              查看
            </button>
            <button class="btn btn-sm btn-outline-secondary" @click="$emit('editRegion', region)">
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
  name: 'RegionList',
  props: {
    // 接收来自父组件的区域数据
    regions: {
      type: Array,
      required: true
    }
  },
  emits: ['viewRegion', 'editRegion']
}
</script>

<style scoped>
/* 区域列表 */
.region-list-section h2 {
  font-size: 1.4rem;
  font-weight: 600;
  margin-bottom: 20px;
  color: #212529;
}

.region-table-container {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.region-table {
  width: 100%;
  border-collapse: collapse;
}

.region-table th,
.region-table td {
  padding: 12px 15px;
  text-align: left;
  border-bottom: 1px solid #dee2e6;
}

.region-table th {
  background-color: #f8f9fa;
  font-weight: 600;
  color: #495057;
}

.region-table tbody tr:hover {
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
  margin-right: 5px;
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
  .region-table {
    font-size: 0.8rem;
  }

  .region-table th,
  .region-table td {
    padding: 8px 10px;
  }
}

@media (max-width: 480px) {
  .region-table {
    display: block;
    overflow-x: auto;
  }
}
</style>
