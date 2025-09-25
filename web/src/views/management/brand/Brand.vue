<template>
  <AppHeader />
  <main class="main-content">
    <SidebarNavigation class="d-none d-md-block" />
    <div class="content-area" :class="{ 'modal-open': isModalOpen }">
      <MobileNavigation />
      <div class="page-header d-flex justify-content-between align-items-center mb-4">
        <h1 class="h3 mb-0">品牌管理</h1>
        <button class="btn btn-primary" @click="showCreateForm">
          <i class="bi bi-plus-circle me-1"></i>添加品牌
        </button>
      </div>
      <StatsCards :stats="statsData" />
      <BrandList
          @view-brand="viewBrand"
          @edit-brand="editBrand"
          @create-brand="showCreateForm"
          @delete-brand="handleDeleteBrand"
          @modal-status-change="handleModalStatusChange"
      />
    </div>
  </main>
  <AppFooter />

  <DeleteConfirm
      :visible="showDeleteConfirm"
      :item-name="brandToDelete?.brand_name"
      @confirm="confirmDelete"
      @cancel="cancelDelete"
  />
  <BrandForm
      v-if="showBrandFormModal"
      :visible="showBrandFormModal"
      :form-type="formType"
      :brand-data="currentBrand"
      @close="handleBrandFormClose"
      @success="handleBrandFormSuccess"
  />
</template>

<script>
import { ref, onMounted } from 'vue'
import AppHeader from "@/components/layout/AppHeader.vue"
import AppFooter from "@/components/layout/AppFooter.vue"
import SidebarNavigation from "@/components/layout/SidebarNavigation.vue"
import MobileNavigation from "@/components/layout/MobileNavigation.vue"
import StatsCards from "@/components/common/StatsCards.vue"
import BrandList from "@/components/brand/BrandList.vue"
import DeleteConfirm from '@/components/common/DeleteConfirm.vue'
import BrandForm from '@/components/brand/BrandForm.vue'
import BrandService from '@/api/brand.api.js'

export default {
  name: 'BrandManagement',
  components: {
    AppHeader, AppFooter, SidebarNavigation, MobileNavigation,
    StatsCards, BrandList, DeleteConfirm, BrandForm
  },
  setup() {
    const isModalOpen = ref(false)
    const statsData = ref([])
    const showDeleteConfirm = ref(false)
    const brandToDelete = ref(null)
    const showBrandFormModal = ref(false)
    const formType = ref('create')
    const currentBrand = ref(null)

    const fetchStats = async () => {
      try {
        const data = await BrandService.getBrandStats()
        statsData.value = [
          { value: data.totalCount, label: '品牌总数', color: '#0d6efd' },
        ]
      } catch (error) {
        console.error('获取统计信息失败:', error)
      }
    }

    onMounted(() => {
      fetchStats()
    })

    const viewBrand = (brand) => {
      currentBrand.value = brand
      formType.value = 'view'
      showBrandFormModal.value = true
      isModalOpen.value = true
    }

    const editBrand = (brand) => {
      currentBrand.value = brand
      formType.value = 'edit'
      showBrandFormModal.value = true
      isModalOpen.value = true
    }

    const showCreateForm = () => {
      currentBrand.value = null
      formType.value = 'create'
      showBrandFormModal.value = true
      isModalOpen.value = true
    }

    const handleBrandFormClose = () => {
      showBrandFormModal.value = false
      isModalOpen.value = false
      currentBrand.value = null
    }

    const handleBrandFormSuccess = async () => {
      showBrandFormModal.value = false
      isModalOpen.value = false
      currentBrand.value = null
      // 刷新统计数据
      await fetchStats()
      // 通知 BrandList 组件刷新列表
    }

    const handleDeleteBrand = (brand) => {
      brandToDelete.value = brand
      showDeleteConfirm.value = true
    }

    const confirmDelete = async () => {
      if (!brandToDelete.value) return
      try {
        await BrandService.deleteBrand(brandToDelete.value.id)
        alert(`✅ 品牌 "${brandToDelete.value.brand_name}" 删除成功！`)
        await fetchStats() // 刷新统计
        // 通知 BrandList 组件刷新列表
      } catch (error) {
        console.error('删除失败:', error)
        alert('❌ 删除失败，请重试')
      } finally {
        cancelDelete()
      }
    }

    const cancelDelete = () => {
      showDeleteConfirm.value = false
      brandToDelete.value = null
    }

    const handleModalStatusChange = (status) => {
      isModalOpen.value = status
    }

    return {
      isModalOpen,
      statsData,
      showDeleteConfirm,
      brandToDelete,
      showBrandFormModal,
      formType,
      currentBrand,
      viewBrand,
      editBrand,
      showCreateForm,
      handleBrandFormClose,
      handleBrandFormSuccess,
      handleDeleteBrand,
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