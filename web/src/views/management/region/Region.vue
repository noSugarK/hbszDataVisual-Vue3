<template>
  <AppHeader />
  <main class="main-content">
    <SidebarNavigation class="d-none d-md-block" />
    <div class="content-area" :class="{ 'modal-open': isModalOpen }">
      <MobileNavigation />
      <div class="page-header d-flex justify-content-between align-items-center mb-4">
        <h1 class="h3 mb-0">区域管理</h1>
        <button class="btn btn-primary" @click="showCreateForm">
          <i class="bi bi-plus-circle me-1"></i>添加区域
        </button>
      </div>
      <StatsCards :stats="statsData" />
      <RegionList
          @view-region="viewRegion"
          @edit-region="editRegion"
          @create-region="showCreateForm"
          @delete-region="handleDeleteRegion"
      @modal-status-change="handleModalStatusChange"
      />
    </div>
  </main>
  <AppFooter />

  <DeleteConfirm
      :visible="showDeleteConfirm"
      :item-name="regionToDelete?.name"
      @confirm="confirmDelete"
      @cancel="cancelDelete"
  />
  <RegionForm
    v-if="showCreateFormModal"
    :visible="showCreateFormModal"
    form-type="create"
    @close="handleCreateFormClose"
    @success="handleCreateFormSuccess"
  />
</template>

<script>
import { ref, onMounted } from 'vue'
import AppHeader from "@/components/layout/AppHeader.vue"
import AppFooter from "@/components/layout/AppFooter.vue"
import SidebarNavigation from "@/components/layout/SidebarNavigation.vue"
import MobileNavigation from "@/components/layout/MobileNavigation.vue"
import StatsCards from "@/components/common/StatsCards.vue"
import RegionList from "@/components/region/RegionList.vue"
import DeleteConfirm from '@/components/common/DeleteConfirm.vue'
import RegionService from '@/api/region.api.js'
import RegionForm from '@/components/region/RegionForm.vue'

export default {
  name: 'RegionManagement',
  components: {
    AppHeader, AppFooter, SidebarNavigation, MobileNavigation,
    StatsCards, RegionList, DeleteConfirm, RegionForm
  },
  setup() {
    const isModalOpen = ref(false)
    const statsData = ref([])
    const showDeleteConfirm = ref(false)
    const regionToDelete = ref(null)
    const showCreateFormModal = ref(false)

    const fetchStats = async () => {
      try {
        const data = await RegionService.getRegionStats()
        statsData.value = [
          { value: data.projectedCount, label: '项目区域', color: '#0d6efd' },
          { value: data.nonProjectedCount, label: '无项目区域', color: '#6c757d' },
          { value: data.totalCount, label: '总区域数', color: '#28a745' },
        ]
      } catch (error) {
        console.error('获取统计信息失败:', error)
      }
    }

    onMounted(() => {
      fetchStats()
    })

    const viewRegion = (region) => console.log('查看区域:', region)
    const editRegion = (region) => console.log('编辑区域:', region)

    const showCreateForm = () => {
      showCreateFormModal.value = true
      isModalOpen.value = true
    }
    
    const handleCreateFormClose = () => {
      showCreateFormModal.value = false
      isModalOpen.value = false
    }
    
    const handleCreateFormSuccess = async () => {
      showCreateFormModal.value = false
      isModalOpen.value = false
      // 刷新统计数据
      await fetchStats()
      // 通知 RegionList 组件刷新列表
      // 可以通过事件总线或状态管理来实现
    }
    // ✅ 接收删除请求
    const handleDeleteRegion = (region) => {
      regionToDelete.value = region
      showDeleteConfirm.value = true
    }

    // ✅ 执行删除
    const confirmDelete = async () => {
      if (!regionToDelete.value) return
      try {
        await RegionService.deleteRegion(regionToDelete.value.id)
        alert(`✅ 区域 "${regionToDelete.value.name}" 删除成功！`)
        await fetchStats() // 刷新统计
      } catch (error) {
        console.error('删除失败:', error)
        alert('❌ 删除失败，请重试')
      } finally {
        cancelDelete()
      }
    }

    const cancelDelete = () => {
      showDeleteConfirm.value = false
      regionToDelete.value = null
    }

    const handleModalStatusChange = (status) => {
      isModalOpen.value = status
    }

    return {
      isModalOpen, 
      statsData, 
      showDeleteConfirm, 
      regionToDelete,
      showCreateFormModal,
      viewRegion, 
      editRegion, 
      showCreateForm, 
      handleCreateFormClose,
      handleCreateFormSuccess,
      handleDeleteRegion,
      confirmDelete, 
      cancelDelete, 
      handleModalStatusChange
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