<template>
  <Teleport to="body" :disabled="!visible">
    <div class="region-form-overlay" @click="handleBackdropClick">
      <div class="region-form-modal" @click.stop>
        <!-- 头部 -->
        <div class="region-form-header">
          <h5 class="region-form-title">{{ formType === 'create' ? '添加区域' : '编辑区域' }}</h5>
          <button type="button" class="btn-close" @click="close"></button>
        </div>

        <!-- 内容 -->
        <div class="region-form-body">
          <form @submit.prevent="handleSubmit">
            <div class="mb-3">
              <label for="regionName" class="form-label">区域名称</label>
              <input
                  type="text"
                  class="form-control"
                  id="regionName"
                  v-model="formData.name"
                  required
              >
            </div>
            <div class="mb-3">
              <label for="regionLevel" class="form-label">区域级别</label>
              <select
                  class="form-select"
                  id="regionLevel"
                  v-model="formData.level"
                  @change="handleLevelChange"
                  :disabled="formType === 'edit'"
              >
                <option value="city">市</option>
                <option value="district">区/县</option>
              </select>
            </div>
            <div class="mb-3" v-if="formData.level === 'district'">
              <label for="parentId" class="form-label">上级区域</label>
              <select class="form-select" id="parentId" v-model="formData.parent_id" required>
                <option value="" disabled>请选择市级区域</option>
                <option v-for="region in cityRegions" :key="region.id" :value="region.id">
                  {{ region.name }}
                </option>
              </select>
            </div>
          </form>
        </div>

        <!-- 底部 -->
        <div class="region-form-footer">
          <button type="button" class="btn btn-secondary" @click="close">取消</button>
          <button type="submit" class="btn btn-primary" @click="handleSubmit">
            {{ formType === 'create' ? '添加' : '保存' }}
          </button>
        </div>
      </div>
    </div>
  </Teleport>
</template>

<script>
import { ref, watch, onMounted } from 'vue'
import RegionService from '@/services/region.service'

export default {
  name: 'RegionForm',
  props: {
    visible: {
      type: Boolean,
      default: false
    },
    formType: {
      type: String,
      default: 'create'
    },
    regionData: {
      type: Object,
      default: () => ({})
    }
  },
  emits: ['close', 'success'],
  setup(props, { emit }) {
    const formData = ref({ name: '', level: 'city', parent_id: null })
    const cityRegions = ref([])

    const loadCityRegions = async () => {
      try {
        const data = await RegionService.getRegions({ level: 'city' })
        console.log('[RegionForm] API 返回数据:', data) // 调试
        const regions = Array.isArray(data) ? data : (data.results || [])
        cityRegions.value = regions
      } catch (error) {
        console.error('加载市级区域失败:', error)
        cityRegions.value = []
        alert('加载市级区域失败，请刷新重试')
      }
    }

    const handleLevelChange = () => {
      if (formData.value.level !== 'district') {
        formData.value.parent_id = null
      }
    }

    // ✅ 关键修复：组件初始化时，如果 visible 已为 true，立即加载
    const initialize = async () => {
      if (props.visible) {
        console.log('[RegionForm] 初始化时 visible=true，立即加载市级区域')
        await loadCityRegions()
      }
    }

    // ✅ 修复：watch + onMounted 双保险
    watch(() => props.visible, async (newVal) => {
      if (newVal) {
        console.log('[RegionForm] visible 变为 true，加载市级区域')
        await loadCityRegions()
        
        // 填充表单数据
        if (props.formType === 'edit' && props.regionData) {
          formData.value = {
            name: props.regionData.name || '',
            level: props.regionData.level || 'city',
            parent_id: props.regionData.level === 'district' ? props.regionData.parent_id : null
          }
        } else {
          formData.value = { name: '', level: 'city', parent_id: null }
        }
      }
    }, { immediate: true }) // 🔥 添加 immediate: true

    // ✅ 额外保险：组件挂载后也检查一次
    onMounted(() => {
      console.log('[RegionForm] 组件已挂载')
      if (props.visible) {
        loadCityRegions() // 再次确保
      }
    })

    const close = () => emit('close')

    const handleSubmit = async () => {
      try {
        const payload = {
          name: formData.value.name,
          level: formData.value.level
        }

        // 只有“区/县”才需要 parent_id
        if (formData.value.level === 'district') {
          if (!formData.value.parent_id) {
            alert('请为区/县选择所属的市级区域')
            return
          }
          payload.parent_id = formData.value.parent_id
        }

        if (props.formType === 'create') {
          await RegionService.createRegion(payload)
        } else {
          await RegionService.updateRegion(props.regionData.id, payload)
        }

        emit('success')
        close()
      } catch (error) {
        console.error('保存区域失败:', error)
        alert('保存失败: ' + (error.message || '请重试'))
      }
    }

    const handleBackdropClick = (e) => {
      if (e.target === e.currentTarget) {
        close()
      }
    }

    return {
      formData,
      cityRegions,
      close,
      handleSubmit,
      handleLevelChange,
      handleBackdropClick,
    }
  }
}
</script>

<style scoped>
/* 样式完全保留，未作任何修改 */
.region-form-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1060;
  backdrop-filter: blur(1px);
}

.region-form-modal {
  background: white;
  border-radius: 8px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
  width: 480px;
  max-width: 90vw;
  overflow: hidden;
}

.region-form-header {
  padding: 16px 20px;
  border-bottom: 1px solid #e9ecef;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.region-form-title {
  margin: 0;
  font-size: 1.1rem;
  font-weight: 600;
  color: #333;
}

.region-form-body {
  padding: 20px;
  font-size: 0.95rem;
  color: #555;
}

.region-form-footer {
  padding: 16px 20px;
  border-top: 1px solid #e9ecef;
  display: flex;
  justify-content: flex-end;
  gap: 8px;
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