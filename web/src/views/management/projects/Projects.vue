<template>
  <div class="project-management-container">
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
          <h1>项目管理</h1>
          <button class="btn btn-primary" @click="showCreateModal = true">创建项目</button>
        </div>

        <!-- 项目统计卡片 -->
        <div class="stats-cards">
          <div class="stat-card">
            <div class="stat-value">24</div>
            <div class="stat-label">进行中项目</div>
          </div>
          <div class="stat-card">
            <div class="stat-value">18</div>
            <div class="stat-label">已完成项目</div>
          </div>
          <div class="stat-card">
            <div class="stat-value">6</div>
            <div class="stat-label">待启动项目</div>
          </div>
          <div class="stat-card">
            <div class="stat-value">3</div>
            <div class="stat-label">延期项目</div>
          </div>
        </div>

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
                  <button class="btn btn-sm btn-outline-primary" @click="viewProject(project)">查看</button>
                  <button class="btn btn-sm btn-outline-secondary" @click="editProject(project)">编辑</button>
                </td>
              </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- 创建项目模态框 -->
        <div v-if="showCreateModal" class="modal-overlay" @click="showCreateModal = false">
          <div class="modal-content" @click.stop>
            <div class="modal-header">
              <h3>创建新项目</h3>
              <button class="close-btn" @click="showCreateModal = false">&times;</button>
            </div>
            <div class="modal-body">
              <form @submit.prevent="createProject">
                <div class="form-group">
                  <label for="projectName">项目名称</label>
                  <input type="text" id="projectName" v-model="newProject.name" required>
                </div>
                <div class="form-group">
                  <label for="projectManager">负责人</label>
                  <input type="text" id="projectManager" v-model="newProject.manager" required>
                </div>
                <div class="form-group">
                  <label for="startDate">开始日期</label>
                  <input type="date" id="startDate" v-model="newProject.startDate" required>
                </div>
                <div class="form-group">
                  <label for="endDate">截止日期</label>
                  <input type="date" id="endDate" v-model="newProject.endDate" required>
                </div>
                <div class="form-group">
                  <label for="projectDescription">项目描述</label>
                  <textarea id="projectDescription" v-model="newProject.description" rows="3"></textarea>
                </div>
                <div class="form-actions">
                  <button type="button" class="btn btn-secondary" @click="showCreateModal = false">取消</button>
                  <button type="submit" class="btn btn-primary">创建项目</button>
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
import MobileNavigation from "@/components/layout/MobileNavigation.vue"

export default {
  name: 'ProjectManagement',
  components: {
    AppHeader,
    AppFooter,
    SidebarNavigation,
    MobileNavigation
  },
  setup() {
    // 移动端状态
    const isMobile = ref(false)

    // 模态框状态
    const showCreateModal = ref(false)

    // 新项目数据
    const newProject = ref({
      name: '',
      manager: '',
      startDate: '',
      endDate: '',
      description: ''
    })

    // 项目数据
    const projects = ref([
      {
        id: 1,
        name: '市政道路改造项目',
        manager: '张三',
        startDate: '2025-01-15',
        endDate: '2025-06-30',
        status: '进行中',
        statusClass: 'status-in-progress',
        progress: 65
      },
      {
        id: 2,
        name: '桥梁建设工程',
        manager: '李四',
        startDate: '2025-03-01',
        endDate: '2025-09-15',
        status: '待启动',
        statusClass: 'status-pending',
        progress: 0
      },
      {
        id: 3,
        name: '地下管网升级',
        manager: '王五',
        startDate: '2024-11-20',
        endDate: '2025-04-30',
        status: '已完成',
        statusClass: 'status-completed',
        progress: 100
      },
      {
        id: 3,
        name: '地下管网升级',
        manager: '王五',
        startDate: '2024-11-20',
        endDate: '2025-04-30',
        status: '已完成',
        statusClass: 'status-completed',
        progress: 100
      },
      {
        id: 3,
        name: '地下管网升级',
        manager: '王五',
        startDate: '2024-11-20',
        endDate: '2025-04-30',
        status: '已完成',
        statusClass: 'status-completed',
        progress: 100
      },
      {
        id: 3,
        name: '地下管网升级',
        manager: '王五',
        startDate: '2024-11-20',
        endDate: '2025-04-30',
        status: '已完成',
        statusClass: 'status-completed',
        progress: 100
      },
      {
        id: 3,
        name: '地下管网升级',
        manager: '王五',
        startDate: '2024-11-20',
        endDate: '2025-04-30',
        status: '已完成',
        statusClass: 'status-completed',
        progress: 100
      },
      {
        id: 3,
        name: '地下管网升级',
        manager: '王五',
        startDate: '2024-11-20',
        endDate: '2025-04-30',
        status: '已完成',
        statusClass: 'status-completed',
        progress: 100
      },
      {
        id: 3,
        name: '地下管网升级',
        manager: '王五',
        startDate: '2024-11-20',
        endDate: '2025-04-30',
        status: '已完成',
        statusClass: 'status-completed',
        progress: 100
      },
      {
        id: 3,
        name: '地下管网升级',
        manager: '王五',
        startDate: '2024-11-20',
        endDate: '2025-04-30',
        status: '已完成',
        statusClass: 'status-completed',
        progress: 100
      },
      {
        id: 4,
        name: '公园绿化工程',
        manager: '赵六',
        startDate: '2025-02-10',
        endDate: '2025-05-20',
        status: '延期',
        statusClass: 'status-delayed',
        progress: 40
      },
      {
        id: 4,
        name: '公园绿化工程',
        manager: '赵六',
        startDate: '2025-02-10',
        endDate: '2025-05-20',
        status: '延期',
        statusClass: 'status-delayed',
        progress: 40
      },
      {
        id: 4,
        name: '公园绿化工程',
        manager: '赵六',
        startDate: '2025-02-10',
        endDate: '2025-05-20',
        status: '延期',
        statusClass: 'status-delayed',
        progress: 40
      },
      {
        id: 4,
        name: '公园绿化工程',
        manager: '赵六',
        startDate: '2025-02-10',
        endDate: '2025-05-20',
        status: '延期',
        statusClass: 'status-delayed',
        progress: 40
      },
      {
        id: 4,
        name: '公园绿化工程',
        manager: '赵六',
        startDate: '2025-02-10',
        endDate: '2025-05-20',
        status: '延期',
        statusClass: 'status-delayed',
        progress: 40
      },
      {
        id: 4,
        name: '公园绿化工程',
        manager: '赵六',
        startDate: '2025-02-10',
        endDate: '2025-05-20',
        status: '延期',
        statusClass: 'status-delayed',
        progress: 40
      },
      {
        id: 4,
        name: '公园绿化工程',
        manager: '赵六',
        startDate: '2025-02-10',
        endDate: '2025-05-20',
        status: '延期',
        statusClass: 'status-delayed',
        progress: 40
      },
      {
        id: 4,
        name: '公园绿化工程',
        manager: '赵六',
        startDate: '2025-02-10',
        endDate: '2025-05-20',
        status: '延期',
        statusClass: 'status-delayed',
        progress: 40
      },
      {
        id: 4,
        name: '公园绿化工程',
        manager: '赵六',
        startDate: '2025-02-10',
        endDate: '2025-05-20',
        status: '延期',
        statusClass: 'status-delayed',
        progress: 40
      },
      {
        id: 5,
        name: '城市照明系统',
        manager: '孙七',
        startDate: '2025-04-01',
        endDate: '2025-08-30',
        status: '进行中',
        statusClass: 'status-in-progress',
        progress: 25
      }
    ])

    // 响应式处理
    const checkScreenSize = () => {
      isMobile.value = window.innerWidth < 768
    }

    // 查看项目详情
    const viewProject = (project) => {
      console.log('查看项目:', project)
      // 这里可以跳转到项目详情页面
    }

    // 编辑项目
    const editProject = (project) => {
      console.log('编辑项目:', project)
      // 这里可以打开编辑模态框
    }

    // 创建项目
    const createProject = () => {
      console.log('创建项目:', newProject.value)
      // 这里可以调用API创建项目
      showCreateModal.value = false
      // 重置表单
      newProject.value = {
        name: '',
        manager: '',
        startDate: '',
        endDate: '',
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
      newProject,
      projects,
      viewProject,
      editProject,
      createProject
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
.project-management-container {
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

  .stats-cards {
    grid-template-columns: 1fr 1fr;
  }

  .projects-table {
    font-size: 0.8rem;
  }

  .projects-table th,
  .projects-table td {
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

  .projects-table {
    display: block;
    overflow-x: auto;
  }
}
</style>
