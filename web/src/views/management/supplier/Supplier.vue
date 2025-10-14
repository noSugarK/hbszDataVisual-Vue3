<template>
  <div class="supplier-management-container">
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
          <h1 class="h3 mb-0">供应商管理</h1>
          <div class="btn-group">
            <button type="button" class="btn btn-primary" @click="showAddModal">
              <i class="bi bi-plus-circle me-1"></i>添加供应商
            </button>
            <button type="button" class="btn btn-outline-secondary" @click="exportData">
              <i class="bi bi-download me-1"></i>导出数据
            </button>
          </div>
        </div>

        <!-- 使用 StatsCards 组件展示统计信息 -->
        <StatsCards :stats="supplierStats" />
        
        <!-- 搜索和筛选 -->
        <div class="search-section mb-4">
          <div class="input-group">
            <span class="input-group-text"><i class="bi bi-search"></i></span>
            <input type="text" class="form-control" placeholder="搜索供应商名称..." v-model="searchQuery" @keyup.enter="searchSuppliers">
            <button class="btn btn-outline-secondary" type="button" @click="searchSuppliers">搜索</button>
          </div>
        </div>

        <!-- 列表 -->
        <SupplierList :refresh-trigger="refreshTrigger" />
      </div>
    </main>
    
    <!-- 添加/编辑模态框 -->
    <div class="modal fade" id="supplierModal" tabindex="-1" ref="supplierModal">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">{{ isEditing ? '编辑供应商' : '添加供应商' }}</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="saveSupplier">
              <div class="form-group">
                <label for="supplierName" class="form-label">供应商名称</label>
                <input type="text" class="form-control" id="supplierName" v-model="formData.supplier_name" required>
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">取消</button>
            <button type="button" class="btn btn-primary" @click="saveSupplier">保存</button>
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
import SupplierList from '@/components/supplier/SupplierList.vue'
import StatsCards from '@/components/common/StatsCards.vue'
import SupplierApi from '@/api/supplier.api.js'
import { Modal } from 'bootstrap'

export default {
  name: 'Supplier',
  components: {
    AppHeader,
    SidebarNavigation,
    MobileNavigation,
    SupplierList,
    StatsCards
  },
  setup() {
    const supplierStats = ref([
      { value: 18, label: '总供应商数', color: '#0d6efd' },
      { value: 2, label: '本月新增', color: '#198754' },
      { value: 15, label: '活跃供应商', color: '#ffc107' },
      { value: '2023-11-15', label: '最近更新', color: '#6c757d' }
    ])
    
    const searchQuery = ref('')
    const refreshTrigger = ref(0)
    const supplierModal = ref(null)
    let modalInstance = null
    
    const isEditing = ref(false)
    const currentSupplierId = ref(null)
    const formData = ref({
      supplier_name: ''
    })
    
    // 加载统计数据
    const loadStats = async () => {
      try {
        // 模拟统计数据，实际应该从API获取
        supplierStats.value = [
          { value: 18, label: '总供应商数', color: '#0d6efd' },
          { value: 2, label: '本月新增', color: '#198754' },
          { value: 15, label: '活跃供应商', color: '#ffc107' },
          { value: '2023-11-15', label: '最近更新', color: '#6c757d' }
        ]
      } catch (error) {
        console.error('加载统计数据失败:', error)
      }
    }
    
    // 搜索供应商
    const searchSuppliers = () => {
      refreshTrigger.value++
    }
    
    // 显示添加模态框
    const showAddModal = () => {
      isEditing.value = false
      currentSupplierId.value = null
      formData.value = {
        supplier_name: ''
      }
      modalInstance.show()
    }
    
    // 保存供应商
    const saveSupplier = async () => {
      try {
        if (isEditing.value) {
          await SupplierApi.updateSupplier(currentSupplierId.value, formData.value)
        } else {
          await SupplierApi.createSupplier(formData.value)
        }
        
        modalInstance.hide()
        refreshTrigger.value++
        loadStats()
      } catch (error) {
        console.error('保存供应商失败:', error)
      }
    }
    
    // 导出数据
    const exportData = async () => {
      try {
        // 模拟导出功能
        console.log('导出供应商数据')
      } catch (error) {
        console.error('导出数据失败:', error)
      }
    }
    
    onMounted(() => {
      loadStats()
      modalInstance = new Modal(supplierModal.value)
    })
    
    return {
      supplierStats,
      searchQuery,
      refreshTrigger,
      supplierModal,
      isEditing,
      formData,
      searchSuppliers,
      showAddModal,
      saveSupplier,
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