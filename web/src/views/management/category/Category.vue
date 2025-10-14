<template>
  <div class="category-management-container">
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
          <h1 class="h3 mb-0">物资类别管理</h1>
          <div class="btn-group">
            <button type="button" class="btn btn-primary" @click="showAddModal">
              <i class="bi bi-plus-circle me-1"></i>添加类别
            </button>
            <button type="button" class="btn btn-outline-secondary" @click="exportData">
              <i class="bi bi-download me-1"></i>导出数据
            </button>
          </div>
        </div>

        <!-- 使用 StatsCards 组件展示统计信息 -->
        <StatsCards :stats="categoryStats" />
        
        <!-- 搜索和筛选 -->
        <div class="search-section mb-4">
          <div class="input-group">
            <span class="input-group-text"><i class="bi bi-search"></i></span>
            <input type="text" class="form-control" placeholder="搜索类别名称..." v-model="searchQuery" @keyup.enter="searchCategories">
            <button class="btn btn-outline-secondary" type="button" @click="searchCategories">搜索</button>
          </div>
        </div>

        <!-- 列表 -->
        <CategoryList :refresh-trigger="refreshTrigger" />
      </div>
    </main>
    
    <!-- 添加/编辑模态框 -->
    <div class="modal fade" id="categoryModal" tabindex="-1" ref="categoryModal">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">{{ isEditing ? '编辑类别' : '添加类别' }}</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="saveCategory">
              <div class="form-group">
                <label for="categoryName" class="form-label">类别名称</label>
                <input type="text" class="form-control" id="categoryName" v-model="formData.category_name" required>
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">取消</button>
            <button type="button" class="btn btn-primary" @click="saveCategory">保存</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, reactive } from 'vue'
import AppHeader from '@/components/layout/AppHeader.vue'
import SidebarNavigation from '@/components/layout/SidebarNavigation.vue'
import MobileNavigation from '@/components/layout/MobileNavigation.vue'
import CategoryList from '@/components/category/CategoryList.vue'
import StatsCards from '@/components/common/StatsCards.vue'
import CategoryApi from '@/api/category.api.js'
import { Modal } from 'bootstrap'

export default {
  name: 'Category',
  components: {
    AppHeader,
    SidebarNavigation,
    MobileNavigation,
    CategoryList,
    StatsCards
  },
  setup() {
    const categoryStats = ref([
      { value: 25, label: '总类别数', color: '#0d6efd' },
      { value: 3, label: '本月新增', color: '#198754' },
      { value: 20, label: '活跃类别', color: '#ffc107' },
      { value: 15, label: '最近更新天数', color: '#6c757d' }
    ])
    
    const searchQuery = ref('')
    const refreshTrigger = ref(0)
    const categoryModal = ref(null)
    let modalInstance = null
    
    const isEditing = ref(false)
    const currentCategoryId = ref(null)
    const formData = ref({
      category_name: ''
    })
    
    // 加载统计数据
    const loadStats = async () => {
      try {
        // 模拟统计数据，实际应该从API获取
        categoryStats.value = [
          { value: 25, label: '总类别数', color: '#0d6efd' },
          { value: 3, label: '本月新增', color: '#198754' },
          { value: 20, label: '活跃类别', color: '#ffc107' },
          { value: 15, label: '最近更新天数', color: '#6c757d' }
        ]
      } catch (error) {
        console.error('加载统计数据失败:', error)
      }
    }
    
    // 搜索类别
    const searchCategories = () => {
      refreshTrigger.value++
    }
    
    // 显示添加模态框
    const showAddModal = () => {
      isEditing.value = false
      currentCategoryId.value = null
      formData.value = {
        category_name: ''
      }
      if (!modalInstance) {
        const modalElement = document.getElementById('categoryModal')
        if (modalElement) {
          modalInstance = new Modal(modalElement)
        }
      }
      modalInstance.show()
    }
    
    // 保存类别
    const saveCategory = async () => {
      try {
        if (isEditing.value) {
          await CategoryApi.updateCategory(currentCategoryId.value, formData.value)
        } else {
          await CategoryApi.createCategory(formData.value)
        }
        
        modalInstance.hide()
        refreshTrigger.value++
        loadStats()
      } catch (error) {
        console.error('保存类别失败:', error)
      }
    }
    
    // 导出数据
    const exportData = async () => {
      try {
        // 模拟导出功能
        console.log('导出类别数据')
      } catch (error) {
        console.error('导出数据失败:', error)
      }
    }
    
    onMounted(() => {
      loadStats()
      // 延迟初始化模态框，确保DOM已完全渲染
      setTimeout(() => {
        const modalElement = document.getElementById('categoryModal')
        if (modalElement) {
          modalInstance = new Modal(modalElement)
        }
      }, 100)
    })
    
    return {
      categoryStats,
      searchQuery,
      refreshTrigger,
      categoryModal,
      isEditing,
      formData,
      searchCategories,
      showAddModal,
      saveCategory,
      exportData
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

.search-section {
  max-width: 500px;
}

/* 表单样式 */
.form-group {
  margin-bottom: 1rem;
}

.form-label {
  margin-bottom: 0.5rem;
  font-weight: 500;
}

.form-control, .form-select {
  padding: 0.75rem 1rem;
  border: 1px solid #ced4da;
  border-radius: 0.375rem;
  font-size: 1rem;
  transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}

.form-control:focus, .form-select:focus {
  border-color: #86b7fe;
  outline: 0;
  box-shadow: 0 0 0 0.25rem rgba(13, 110, 253, 0.25);
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