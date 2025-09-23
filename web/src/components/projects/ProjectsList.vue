<template>
  <!-- 项目列表 -->
  <div class="projects-section">
    <h2>项目列表</h2>
    <div class="projects-table-container">
      <table class="projects-table">
        <thead>
        <tr>
          <th>项目名称</th>
          <th>负责人</th>
          <th>开始日期</th>
          <th>截止日期</th>
          <th>状态</th>
          <th>进度</th>
          <th>操作</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="project in projects" :key="project.id">
          <td>{{ project.name }}</td>
          <td>{{ project.manager }}</td>
          <td>{{ project.startDate }}</td>
          <td>{{ project.endDate }}</td>
          <td>
              <span :class="['status-badge', project.statusClass]">
                {{ project.status }}
              </span>
          </td>
          <td>
            <div class="progress-bar">
              <div class="progress-fill" :style="{ width: project.progress + '%' }"></div>
            </div>
            <span class="progress-text">{{ project.progress }}%</span>
          </td>
          <td>
            <button class="btn btn-sm btn-outline-primary" @click="$emit('viewProject', project)">查看</button>
            <button class="btn btn-sm btn-outline-secondary" @click="$emit('editProject', project)">编辑</button>
          </td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProjectsList',
  props: {
    // 接收来自父组件的项目数据
    projects: {
      type: Array,
      required: true
    }
  }
}
</script>

<style scoped>
/* 项目列表 */
.projects-section h2 {
  font-size: 1.4rem;
  font-weight: 600;
  margin-bottom: 20px;
  color: #212529;
}

.projects-table-container {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.projects-table {
  width: 100%;
  border-collapse: collapse;
}

.projects-table th,
.projects-table td {
  padding: 12px 15px;
  text-align: left;
  border-bottom: 1px solid #dee2e6;
}

.projects-table th {
  background-color: #f8f9fa;
  font-weight: 600;
  color: #495057;
}

.projects-table tbody tr:hover {
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

/* 进度条 */
.progress-bar {
  width: 100%;
  height: 8px;
  background-color: #e9ecef;
  border-radius: 4px;
  overflow: hidden;
  margin-bottom: 5px;
}

.progress-fill {
  height: 100%;
  background-color: #0d6efd;
  border-radius: 4px;
  transition: width 0.3s ease;
}

.progress-text {
  font-size: 0.8rem;
  color: #6c757d;
}
</style>