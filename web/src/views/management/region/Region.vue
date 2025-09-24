<template>
  <div class="region-management-container">
    <!-- 头部导航 -->
    <AppHeader />

    <!-- 主要内容区域 -->
    <main class="main-content">
      <!-- 侧边栏 - 仅在中等屏幕及以上显示 -->
      <SidebarNavigation class="d-none d-md-block" />

      <!-- 内容区 -->
      <div class="content-area">
        <!-- 移动端二级导航 -->
        <MobileNavigation />

        <!-- 页面标题 -->
        <div class="page-header d-flex justify-content-between align-items-center mb-4">
          <h1 class="h3 mb-0">区域管理</h1>
          <button class="btn btn-primary" @click="showCreateModal = true">
            <i class="bi bi-plus-circle me-1"></i>添加区域
          </button>
        </div>

        <!-- 区域统计卡片 -->
        <StatsCards :stats="statsData" />

        <!-- 区域列表 -->
        <RegionList @view-region="viewRegion" @edit-region="editRegion" />

        <!-- 添加区域模态框 -->
        <div v-if="showCreateModal" class="modal fade show d-block" tabindex="-1" role="dialog">
          <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title">添加新区域</h5>
                <button type="button" class="btn-close" @click="showCreateModal = false"></button>
              </div>
              <div class="modal-body">
                <form @submit.prevent="createRegion">
                  <div class="mb-3">
                    <label for="regionName" class="form-label">区域名称</label>
                    <input type="text" class="form-control" id="regionName" v-model="newRegion.name" required>
                  </div>
                  <div class="mb-3">
                    <label for="regionManager" class="form-label">负责人</label>
                    <input type="text" class="form-control" id="regionManager" v-model="newRegion.manager" required>
                  </div>
                  <div class="mb-3">
                    <label for="partners" class="form-label">合作单位</label>
                    <input type="text" class="form-control" id="partners" v-model="newRegion.partners">
                  </div>
                  <div class="mb-3">
                    <label for="regionDescription" class="form-label">区域描述</label>
                    <textarea class="form-control" id="regionDescription" v-model="newRegion.description" rows="3"></textarea>
                  </div>
                  <div class="d-flex justify-content-end gap-2">
                    <button type="button" class="btn btn-secondary" @click="showCreateModal = false">取消</button>
                    <button type="submit" class="btn btn-primary">添加区域</button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>

        <!-- 模态框背景遮罩 -->
        <div v-if="showCreateModal" class="modal-backdrop fade show"></div>
      </div>
    </main>

    <!-- 页脚 -->
    <AppFooter />
  </div>
</template>


<script>
import { ref, onMounted } from 'vue'
import AppHeader from "@/components/layout/AppHeader.vue"
import AppFooter from "@/components/layout/AppFooter.vue"
import SidebarNavigation from "@/components/layout/SidebarNavigation.vue"
import MobileNavigation from "@/components/layout/MobileNavigation.vue"
import StatsCards from "@/components/common/StatsCards.vue"
import RegionList from "@/components/region/RegionList.vue"
import RegionService from '@/services/region.service'

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

    // 在 setup() 函数中添加
    const statsData = ref([])

    // 获取统计信息的函数
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

    // 在 mounted 或组件初始化时调用
    onMounted(() => {
      fetchStats()
    })

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
      viewRegion,
      editRegion,
      createRegion
    }
  }
}
</script>

<style scoped>
/* 全局容器 */
.region-management-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

/* 主要内容区域 */
.main-content {
  width: 70%;
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

/* 响应式设计 */
@media (max-width: 1024px) {
  .main-content {
    flex-direction: column;
  }

  .content-area {
    width: 100%;
  }
}

@media (max-width: 768px) {
  .main-content {
    padding: 15px;
    gap: 15px;
  }

  .page-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 15px;
  }
}
</style>

