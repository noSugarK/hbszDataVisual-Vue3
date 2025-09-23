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
        <MobileNavigation />

        <!-- 页面标题 -->
        <div class="page-header">
          <h1>项目管理</h1>
          <button class="btn btn-primary" @click="showCreateModal = true">创建项目</button>
        </div>

        <!-- 使用 StatsCards 组件展示统计信息 -->
        <StatsCards :stats="projectStats" />

        <!-- 使用 ProjectsList 组件展示项目列表 -->
        <ProjectsList
            :projects="projects"
            @viewProject="viewProject"
            @editProject="editProject"
        />

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
import { ref } from 'vue'
import AppHeader from "@/components/layout/AppHeader.vue"
import AppFooter from "@/components/layout/AppFooter.vue"
import SidebarNavigation from "@/components/layout/SidebarNavigation.vue"
import MobileNavigation from "@/components/layout/MobileNavigation.vue"
import ProjectsList from "@/components/projects/ProjectsList.vue"
import StatsCards from "@/components/common/StatsCards.vue" // 引入新的统计卡片组件

export default {
  name: 'Projects',
  components: {
    AppHeader,
    AppFooter,
    SidebarNavigation,
    MobileNavigation,
    ProjectsList,
    StatsCards
  },
  setup() {
    const showCreateModal = ref(false)

    const newProject = ref({
      name: '',
      manager: '',
      startDate: '',
      endDate: '',
      description: ''
    })

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

    // 项目统计信息，现在作为独立的数据对象
    const projectStats = ref([
      { value: 24, label: '进行中项目', color: '#0d6efd' },
      { value: 18, label: '已完成项目', color: '#198754' },
      { value: 6,  label: '待启动项目', color: '#ffc107' },
      { value: 3,  label: '延期项目',   color: '#dc3545' }
    ])

    const viewProject = (project) => {
      console.log('查看项目:', project)
    }

    const editProject = (project) => {
      console.log('编辑项目:', project)
    }

    const createProject = () => {
      console.log('创建项目:', newProject.value)
      showCreateModal.value = false
      newProject.value = {
        name: '',
        manager: '',
        startDate: '',
        endDate: '',
        description: ''
      }
    }

    return {
      showCreateModal,
      newProject,
      projects,
      projectStats,
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