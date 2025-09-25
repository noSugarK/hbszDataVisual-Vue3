<!-- src/components/brand/BrandForm.vue -->
<template>
  <Teleport to="body">
    <div v-if="visible" class="brand-form-overlay" @click="handleBackdropClick">
      <div class="brand-form-modal" @click.stop>
        <div class="brand-form-header">
          <h5 class="brand-form-title">{{ formTitle }}</h5>
          <button type="button" class="btn-close" @click="handleClose"></button>
        </div>

        <div class="brand-form-body">
          <form @submit.prevent="handleSubmit">
            <div class="mb-3">
              <label for="brandName" class="form-label">品牌名称</label>
              <input
                  type="text"
                  class="form-control"
                  id="brandName"
                  v-model="formData.brand_name"
                  :disabled="formType === 'view'"
                  required
              >
            </div>

            <div class="mb-3">
              <label for="brandDescription" class="form-label">品牌描述</label>
              <textarea
                  class="form-control"
                  id="brandDescription"
                  v-model="formData.description"
                  :disabled="formType === 'view'"
                  rows="3"
              ></textarea>
            </div>

            <div class="brand-form-footer" v-if="formType !== 'view'">
              <button type="button" class="btn btn-secondary" @click="handleClose">取消</button>
              <button type="submit" class="btn btn-primary">保存</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </Teleport>
</template>

<script>
import { ref, computed, watch } from 'vue'
import BrandService from '@/api/brand.api.js'

export default {
  name: 'BrandForm',
  props: {
    visible: {
      type: Boolean,
      default: false
    },
    formType: {
      type: String,
      default: 'create' // 'create', 'edit', 'view'
    },
    brandData: {
      type: Object,
      default: null
    }
  },
  emits: ['close', 'success'],
  setup(props, { emit }) {
    const formData = ref({
      brand_name: '',
      description: ''
    })

    const formTitle = computed(() => {
      switch (props.formType) {
        case 'create': return '添加品牌'
        case 'edit': return '编辑品牌'
        case 'view': return '查看品牌'
        default: return '品牌'
      }
    })

    watch(() => props.brandData, (newVal) => {
      if (newVal) {
        formData.value = {
          brand_name: newVal.brand_name || newVal.name || '',
          description: newVal.description || ''
        }
      } else {
        formData.value = { brand_name: '', description: '' }
      }
    }, { immediate: true })

    const handleClose = () => {
      emit('close')
    }

    const handleSubmit = async () => {
      try {
        if (props.formType === 'create') {
          await BrandService.createBrand(formData.value)
          alert('✅ 品牌创建成功！')
        } else if (props.formType === 'edit') {
          await BrandService.updateBrand(props.brandData.id, formData.value)
          alert('✅ 品牌更新成功！')
        }
        emit('success')
      } catch (error) {
        console.error('操作失败:', error)
        alert('❌ 操作失败，请重试')
      }
    }

    const handleBackdropClick = () => {
      handleClose()
    }

    return {
      formData,
      formTitle,
      handleClose,
      handleSubmit,
      handleBackdropClick
    }
  }
}
</script>

<style scoped>
.brand-form-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  backdrop-filter: blur(1px);
}

.brand-form-modal {
  background: white;
  border-radius: 8px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
  width: 500px;
  max-width: 90vw;
  overflow: hidden;
}

.brand-form-header {
  padding: 16px 20px;
  border-bottom: 1px solid #e9ecef;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.brand-form-title {
  margin: 0;
  font-size: 1.1rem;
  font-weight: 600;
  color: #333;
}

.brand-form-body {
  padding: 20px;
}

.brand-form-footer {
  padding: 16px 20px;
  text-align: right;
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
