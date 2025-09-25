<template>
  <Teleport to="body">
    <div v-if="visible" class="region-detail-overlay" @click="handleBackdropClick">
      <div class="region-detail-modal" @click.stop>
        <!-- 头部 -->
        <div class="region-detail-header">
          <h5 class="region-detail-title">区域详情</h5>
          <button type="button" class="btn-close" @click="close"></button>
        </div>

        <!-- 内容 -->
        <div class="region-detail-body">
          <div v-if="loading" class="text-center py-5">
            <div class="spinner-border text-primary" role="status"></div>
            <p class="mt-2 text-muted">加载中...</p>
          </div>
          <div v-else-if="region" class="region-info">
            <div class="row mb-3">
              <div class="col-md-3 fw-bold">区域名称:</div>
              <div class="col-md-9">{{ region.name }}</div>
            </div>
            <div class="row mb-3">
              <div class="col-md-3 fw-bold">区域级别:</div>
              <div class="col-md-9">{{ getLevelLabel(region.level) }}</div>
            </div>
            <div class="row mb-3">
              <div class="col-md-3 fw-bold">上级区域:</div>
              <div class="col-md-9">{{ region.parent_name || '无' }}</div>
            </div>
            <div class="row mb-3">
              <div class="col-md-3 fw-bold">项目统计:</div>
              <div class="col-md-9">{{ region.project_count || 0 }} 个项目</div>
            </div>
          </div>
          <div v-else class="text-center text-muted py-4">
            未找到该区域信息
          </div>
        </div>

        <!-- 底部 -->
        <div class="region-detail-footer">
          <button type="button" class="btn btn-secondary" @click="close">关闭</button>
        </div>
      </div>
    </div>
  </Teleport>
</template>

<script>
import { ref, watch } from 'vue'
import RegionService from '@/services/region.service.js'

export default {
  name: 'RegionDetail',
  props: {
    visible: {
      type: Boolean,
      default: false
    },
    regionId: {
      type: [Number, String],
      default: null
    }
  },
  emits: ['close'],
  setup(props, { emit }) {
    const region = ref(null)
    const loading = ref(false)

    const loadRegionDetail = async () => {
      if (!props.regionId) {
        region.value = null
        return
      }
      
      loading.value = true
      // console.log('开始加载区域详情，regionId:', props.regionId)
      try {
        const data = await RegionService.getRegion(props.regionId)
        region.value = data
      } catch (error) {
        console.error('加载区域详情失败:', error)
        region.value = null
      } finally {
        loading.value = false
      }
    }

    // 同时监听 visible 和 regionId 的变化
    watch([() => props.visible, () => props.regionId], async ([newVisible, newRegionId]) => {
      // console.log('watch 触发:', { visible: newVisible, regionId: newRegionId })
      if (newVisible && newRegionId) {
        await loadRegionDetail()
      } else if (!newVisible) {
        // 当关闭弹窗时清空数据
        region.value = null
      }
    }, { immediate: true })

    const getLevelLabel = (level) => {
      const levelMap = {
        province: '省',
        city: '市',
        district: '区/县'
      }
      return levelMap[level] || level
    }

    const close = () => {
      emit('close')
    }

    const handleBackdropClick = () => {
      // 查看详情一般允许点击遮罩关闭
      close()
    }

    return {
      region,
      loading,
      close,
      getLevelLabel,
      handleBackdropClick
    }
  }
}
</script>

<style scoped>
.region-detail-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1050;
  backdrop-filter: blur(1px);
}

.region-detail-modal {
  background: white;
  border-radius: 8px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
  width: 500px;
  max-width: 90vw;
  max-height: 90vh;
  overflow: hidden;
}

.region-detail-header {
  padding: 16px 20px;
  border-bottom: 1px solid #e9ecef;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.region-detail-title {
  margin: 0;
  font-size: 1.1rem;
  font-weight: 600;
  color: #333;
}

.region-detail-body {
  padding: 20px;
  font-size: 0.95rem;
  color: #555;
  max-height: 60vh;
  overflow-y: auto;
}

.region-detail-footer {
  padding: 16px 20px;
  border-top: 1px solid #e9ecef;
  text-align: right;
}

.btn-close {
  background: none;
  border: none;
  font-size: 1.25rem;
  color: #6c757d;
  cursor: pointer;
  padding: 0;
  line-height: 1;
}

.btn-close:hover {
  color: #000;
}
</style>