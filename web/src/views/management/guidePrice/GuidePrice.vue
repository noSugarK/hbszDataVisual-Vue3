<template>
  <div class="guide-price-management-container">
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
          <h1 class="h3 mb-0">指导价管理</h1>
          <button class="btn btn-primary" @click="exportData">
            <i class="bi bi-download me-1"></i>导出数据
          </button>
        </div>

        <!-- 使用 StatsCards 组件展示统计信息 -->
        <StatsCards :stats="guidePriceStats" />
        
        <!-- 图表和筛选条件 -->
        <div class="row mb-4">
          <div class="col-lg-8 mb-4">
            <GuidePriceChart :filters="filters" />
          </div>
          <div class="col-lg-4 mb-4">
            <GuidePriceFilters v-model="filters" @apply="applyFilters" />
          </div>
        </div>
        
        <!-- 列表 -->
        <GuidePriceList :filters="filters" />
      </div>
    </main>

    <!-- 页脚 -->
    <AppFooter />
  </div>
</template>

<script>
import { ref, onMounted, reactive } from 'vue'
import AppHeader from '@/components/layout/AppHeader.vue'
import AppFooter from '@/components/layout/AppFooter.vue'
import SidebarNavigation from '@/components/layout/SidebarNavigation.vue'
import MobileNavigation from '@/components/layout/MobileNavigation.vue'
import StatsCards from '@/components/common/StatsCards.vue'
import GuidePriceChart from '@/components/guidePrice/GuidePriceChart.vue'
import GuidePriceFilters from '@/components/guidePrice/GuidePriceFilters.vue'
import GuidePriceList from '@/components/guidePrice/GuidePriceList.vue'
import GuidePriceApi from '@/api/guidePrice.api.js'

export default {
  name: 'GuidePrice',
  components: {
    AppHeader,
    AppFooter,
    SidebarNavigation,
    MobileNavigation,
    StatsCards,
    GuidePriceChart,
    GuidePriceFilters,
    GuidePriceList
  },
  setup() {
    const guidePriceStats = ref([])
    
    const filters = reactive({
      region_id: '',
      category_id: '',
      specification_id: '',
      start_date: '',
      end_date: ''
    })
    
    // 加载统计数据
    const loadStats = async () => {
      try {
        const data = await GuidePriceApi.getGuidePriceStats()
        guidePriceStats.value = [
          {
            value: data.total_count,
            label: '总记录数',
            color: 'primary'
          },
          {
            value: data.latest_month_count,
            label: '本月新增',
            color: 'success'
          },
          {
            value: `¥${data.avg_price ? parseFloat(data.avg_price).toFixed(2) : '0.00'}`,
            label: '平均价格',
            color: 'info'
          },
          {
            value: data.latest_update || '-',
            label: '最近更新',
            color: 'warning'
          }
        ]
      } catch (error) {
        console.error('加载统计数据失败:', error)
      }
    }
    
    // 应用筛选条件
    const applyFilters = () => {
      // 筛选条件变化会通过v-model自动更新，子组件会触发数据重新加载
      console.log('应用筛选条件:', filters)
    }
    
    // 导出数据
    const exportData = async () => {
      try {
        await GuidePriceApi.exportGuidePriceData(filters)
        // 这里可以添加下载成功的提示
      } catch (error) {
        console.error('导出数据失败:', error)
      }
    }
    
    onMounted(() => {
      loadStats()
    })
    
    return {
      guidePriceStats,
      filters,
      applyFilters,
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

@media (max-width: 1024px) {
  .main-content { flex-direction: row; }
  .content-area { width: 100%; }
}

@media (max-width: 768px) {
  .main-content { padding: 15px; gap: 15px; }
  .page-header { flex-direction: column; align-items: flex-start; gap: 15px; }
}
</style>