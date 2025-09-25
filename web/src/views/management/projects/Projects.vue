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
        <div class="page-header d-flex justify-content-between align-items-center mb-4">
          <h1 class="h3 mb-0">项目管理</h1>
          <button class="btn btn-primary" @click="showCreateForm">
            <i class="bi bi-plus-circle me-1"></i>项目信息
          </button>
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