<template>
  <div class="guide-price-chart">
    <div class="chart-header">
      <h4 class="chart-title">价格趋势图</h4>
      <div class="chart-info" v-if="chartData.category_name || chartData.region_name">
        <span v-if="chartData.category_name" class="badge bg-primary me-2">
          {{ chartData.category_name }}
        </span>
        <span v-if="chartData.specification_name" class="badge bg-secondary me-2">
          {{ chartData.specification_name }}
        </span>
        <span v-if="chartData.region_name" class="badge bg-info">
          {{ chartData.region_name }}
        </span>
      </div>
    </div>
    
    <div class="chart-container">
      <div v-if="loading" class="chart-loading">
        <div class="spinner-border text-primary" role="status">
          <span class="visually-hidden">加载中...</span>
        </div>
      </div>
      <div v-else-if="chartData.data && chartData.data.length > 0" class="chart-wrapper">
        <canvas ref="chartCanvas"></canvas>
      </div>
      <div v-else class="chart-empty">
        <div class="empty-message">
          <i class="bi bi-graph-up empty-icon"></i>
          <p>暂无数据</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, watch, nextTick } from 'vue'
import { Chart, registerables } from 'chart.js/auto'
import GuidePriceApi from '@/api/guidePrice.api.js'

export default {
  name: 'GuidePriceChart',
  props: {
    filters: {
      type: Object,
      default: () => ({})
    }
  },
  setup(props) {
    const chartCanvas = ref(null)
    const chartInstance = ref(null)
    const loading = ref(false)
    const chartData = ref({
      category_name: '',
      specification_name: '',
      region_name: '',
      data: []
    })
    
    // 注册Chart.js组件
    Chart.register(...registerables)

    // 加载图表数据
    const loadChartData = async () => {
      loading.value = true
      try {
        const data = await GuidePriceApi.getGuidePriceChartData(props.filters)
        chartData.value = data
        
        // 渲染图表
        if (data.data && data.data.length > 0) {
          await nextTick()
          renderChart()
        }
      } catch (error) {
        console.error('加载图表数据失败:', error)
      } finally {
        loading.value = false
      }
    }

    // 渲染图表
    const renderChart = () => {
      // 销毁现有图表实例
      if (chartInstance.value) {
        chartInstance.value.destroy()
      }
      
      // 准备数据
      const labels = chartData.value.data.map(item => item.date)
      const unitPrices = chartData.value.data.map(item => item.unit_price)
      
      // 创建新图表
      const ctx = chartCanvas.value.getContext('2d')
      chartInstance.value = new Chart(ctx, {
        type: 'line',
        data: {
          labels,
          datasets: [
            {
              label: '信息价',
              data: unitPrices,
              borderColor: 'rgb(75, 192, 192)',
              backgroundColor: 'rgba(75, 192, 192, 0.2)',
              tension: 0.1
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            y: {
              beginAtZero: false,
              title: {
                display: true,
                text: '价格 (元)'
              }
            },
            x: {
              title: {
                display: true,
                text: '日期'
              }
            }
          },
          plugins: {
            legend: {
              position: 'top',
            },
            title: {
              display: false
            },
            tooltip: {
              callbacks: {
                label: function(context) {
                  return `${context.dataset.label}: ${context.raw.toFixed(2)} 元`
                }
              }
            }
          }
        }
      })
    }

    // 监听筛选条件变化
    watch(() => props.filters, () => {
      loadChartData()
    }, { deep: true })

    onMounted(() => {
      loadChartData()
    })

    return {
      chartCanvas,
      loading,
      chartData
    }
  }
}
</script>

<style scoped>
.guide-price-chart {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
  height: 400px;
  display: flex;
  flex-direction: column;
}

.chart-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.chart-title {
  margin: 0;
  font-size: 18px;
  font-weight: 600;
  color: #333;
}

.chart-container {
  flex: 1;
  position: relative;
}

.chart-wrapper {
  height: 100%;
  width: 100%;
}

.chart-loading, .chart-empty {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.empty-message {
  text-align: center;
  color: #6c757d;
}

.empty-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
  display: block;
}

@media (max-width: 768px) {
  .chart-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
  }
}
</style>