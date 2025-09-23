<template>
  <div class="region-management-container">
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
          <h1>区域管理</h1>
          <button class="btn btn-primary" @click="showCreateModal = true">添加区域</button>
        </div>

        <!-- 区域统计卡片 -->
        <StatsCards :stats="statsData" />

        <!-- 区域列表 -->
        <RegionList :regions="regions" @view-region="viewRegion" @edit-region="editRegion" />

        <!-- 添加区域模态框 -->
        <div v-if="showCreateModal" class="modal-overlay" @click="showCreateModal = false">
          <div class="modal-content" @click.stop>
            <div class="modal-header">
              <h3>添加新区域</h3>
              <button class="close-btn" @click="showCreateModal = false">&times;</button>
            </div>
            <div class="modal-body">
              <form @submit.prevent="createRegion">
                <div class="form-group">
                  <label for="regionName">区域名称</label>
                  <input type="text" id="regionName" v-model="newRegion.name" required>
                </div>
                <div class="form-group">
                  <label for="regionManager">负责人</label>
                  <input type="text" id="regionManager" v-model="newRegion.manager" required>
                </div>
                <div class="form-group">
                  <label for="partners">合作单位</label>
                  <input type="text" id="partners" v-model="newRegion.partners">
                </div>
                <div class="form-group">
                  <label for="regionDescription">区域描述</label>
                  <textarea id="regionDescription" v-model="newRegion.description" rows="3"></textarea>
                </div>
                <div class="form-actions">
                  <button type="button" class="btn btn-secondary" @click="showCreateModal = false">取消</button>
                  <button type="submit" class="btn btn-primary">添加区域</button>
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
import StatsCards from "@/components/common/StatsCards.vue"
import RegionList from "@/components/region/RegionList.vue"

export default {
  name: 'RegionManagement',
  components: {
    AppHeader,
    AppFooter,
    SidebarNavigation,
    MobileNavigation,
    StatsCards,
    RegionList
  },
  setup() {
    // 模态框状态
    const showCreateModal = ref(false)

    // 新区域数据
    const newRegion = ref({
      name: '',
      manager: '',
      partners: '',
      description: ''
    })

    // 区域统计数据
    const statsData = ref([
      { value: 8, label: '运营区域', color: '#0d6efd' },
      { value: 15, label: '项目区域', color: '#0d6efd' },
      { value: 3, label: '待开发区域', color: '#0d6efd' },
      { value: 26, label: '合作单位', color: '#0d6efd' }
    ])

    // 区域数据
    const regions = ref([
      {
        id: 1,
        name: '武汉市',
        manager: '张三',
        projectCount: 12,
        partners: '3家',
        status: '运营中',
        statusClass: 'status-in-progress'
      },
      {
        id: 2,
        name: '宜昌市',
        manager: '李四',
        projectCount: 8,
        partners: '2家',
        status: '运营中',
        statusClass: 'status-in-progress'
      },
      {
        id: 3,
        name: '襄阳市',
        manager: '王五',
        projectCount: 5,
        partners: '1家',
        status: '待开发',
        statusClass: 'status-pending'
      },
      {
        id: 4,
        name: '黄石市',
        manager: '赵六',
        projectCount: 7,
        partners: '2家',
        status: '运营中',
        statusClass: 'status-in-progress'
      },
      {
        id: 5,
        name: '十堰市',
        manager: '孙七',
        projectCount: 3,
        partners: '1家',
        status: '项目中',
        statusClass: 'status-completed'
      }
    ])

    // 查看区域详情
    const viewRegion = (region) => {
      console.log('查看区域:', region)
      // 这里可以跳转到区域详情页面
    }

    // 编辑区域
    const editRegion = (region) => {
      console.log('编辑区域:', region)
      // 这里可以打开编辑模态框
    }

    // 创建区域
    const createRegion = () => {
      console.log('创建区域:', newRegion.value)
      // 这里可以调用API创建区域
      showCreateModal.value = false
      // 重置表单
      newRegion.value = {
        name: '',
        manager: '',
        partners: '',
        description: ''
      }
    }

    return {
      showCreateModal,
      newRegion,
      statsData,
      regions,
      viewRegion,
      editRegion,
      createRegion
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
.region-management-container {
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
