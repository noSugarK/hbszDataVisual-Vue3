<template>
  <div class="guide-price-filters">
    <div class="filters-header">
      <h4 class="filters-title">筛选条件</h4>
      <button class="btn btn-sm btn-outline-secondary" @click="resetFilters">
        <i class="bi bi-arrow-clockwise me-1"></i>重置
      </button>
    </div>
    
    <div class="filters-content">
      <div class="form-group">
        <label for="region-filter" class="form-label">地区</label>
        <select id="region-filter" class="form-select" v-model="filters.region_id">
          <option value="">全部地区</option>
          <option v-for="region in regions" :key="region.id" :value="region.id">
            {{ region.name }}
          </option>
        </select>
      </div>
      
      <div class="form-group">
        <label for="category-filter" class="form-label">物资类别</label>
        <select id="category-filter" class="form-select" v-model="filters.category_id" @change="onCategoryChange">
          <option value="">全部类别</option>
          <option v-for="category in categories" :key="category.id" :value="category.id">
            {{ category.category_name }}
          </option>
        </select>
      </div>
      
      <div class="form-group">
        <label for="specification-filter" class="form-label">规格</label>
        <select id="specification-filter" class="form-select" v-model="filters.specification_id">
          <option value="">全部规格</option>
          <option v-for="specification in specifications" :key="specification.id" :value="specification.id">
            {{ specification.specification_name }}
          </option>
        </select>
      </div>
      
      <div class="form-group">
        <label for="start-date-filter" class="form-label">开始日期</label>
        <input 
          id="start-date-filter" 
          type="date" 
          class="form-control" 
          v-model="filters.start_date"
        >
      </div>
      
      <div class="form-group">
        <label for="end-date-filter" class="form-label">结束日期</label>
        <input 
          id="end-date-filter" 
          type="date" 
          class="form-control" 
          v-model="filters.end_date"
        >
      </div>
      
      <div class="form-actions">
        <button class="btn btn-primary w-100" @click="applyFilters">
          <i class="bi bi-funnel me-1"></i>应用筛选
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, watch } from 'vue'
import RegionApi from '@/api/region.api.js'
import GuidePriceApi from '@/api/guidePrice.api.js'

export default {
  name: 'GuidePriceFilters',
  emits: ['filter-change'],
  setup(props, { emit }) {
    const regions = ref([])
    const categories = ref([])
    const specifications = ref([])
    
    const filters = ref({
      region_id: '',
      category_id: '',
      specification_id: '',
      start_date: '',
      end_date: ''
    })
    
    // 加载地区数据
    const loadRegions = async () => {
      try {
        const data = await RegionApi.getRegions()
        regions.value = data
      } catch (error) {
        console.error('加载地区数据失败:', error)
      }
    }
    
    // 加载物资类别数据
    const loadCategories = async () => {
      try {
        // 这里假设有一个获取物资类别的API，如果没有，需要创建
        // const data = await CategoryApi.getCategories()
        // categories.value = data
        
        // 临时数据，实际项目中应该从API获取
        categories.value = [
          { id: 1, category_name: '混凝土' },
          { id: 2, category_name: '钢筋' },
          { id: 3, category_name: '水泥' },
          { id: 4, category_name: '砂石' }
        ]
      } catch (error) {
        console.error('加载物资类别数据失败:', error)
      }
    }
    
    // 加载规格数据
    const loadSpecifications = async (categoryId = null) => {
      try {
        // 这里假设有一个获取规格的API，如果没有，需要创建
        // const data = await SpecificationApi.getSpecifications({ category_id: categoryId })
        // specifications.value = data
        
        // 临时数据，实际项目中应该从API获取
        if (categoryId) {
          // 根据类别获取对应的规格
          if (categoryId == 1) { // 混凝土
            specifications.value = [
              { id: 1, specification_name: 'C30' },
              { id: 2, specification_name: 'C35' },
              { id: 3, specification_name: 'C40' }
            ]
          } else if (categoryId == 2) { // 钢筋
            specifications.value = [
              { id: 4, specification_name: 'HRB400' },
              { id: 5, specification_name: 'HRB500' }
            ]
          } else {
            specifications.value = []
          }
        } else {
          // 获取所有规格
          specifications.value = [
            { id: 1, specification_name: 'C30' },
            { id: 2, specification_name: 'C35' },
            { id: 3, specification_name: 'C40' },
            { id: 4, specification_name: 'HRB400' },
            { id: 5, specification_name: 'HRB500' }
          ]
        }
      } catch (error) {
        console.error('加载规格数据失败:', error)
      }
    }
    
    // 类别变化时重新加载规格
    const onCategoryChange = () => {
      filters.value.specification_id = ''
      loadSpecifications(filters.value.category_id)
    }
    
    // 应用筛选
    const applyFilters = () => {
      emit('filter-change', { ...filters.value })
    }
    
    // 重置筛选
    const resetFilters = () => {
      filters.value = {
        region_id: '',
        category_id: '',
        specification_id: '',
        start_date: '',
        end_date: ''
      }
      emit('filter-change', { ...filters.value })
    }
    
    // 监听类别变化
    watch(() => filters.value.category_id, (newVal) => {
      if (newVal) {
        loadSpecifications(newVal)
      } else {
        loadSpecifications()
      }
    })
    
    onMounted(() => {
      loadRegions()
      loadCategories()
      loadSpecifications()
      
      // 设置默认日期范围为最近三个月
      const endDate = new Date()
      const startDate = new Date()
      startDate.setMonth(startDate.getMonth() - 3)
      
      filters.value.end_date = endDate.toISOString().split('T')[0]
      filters.value.start_date = startDate.toISOString().split('T')[0]
    })
    
    return {
      regions,
      categories,
      specifications,
      filters,
      onCategoryChange,
      applyFilters,
      resetFilters
    }
  }
}
</script>

<style scoped>
.guide-price-filters {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
  margin-bottom: 20px;
}

.filters-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.filters-title {
  margin: 0;
  font-size: 18px;
  font-weight: 600;
  color: #333;
}

.filters-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 15px;
}

.form-group {
  margin-bottom: 1rem;
}

.form-label {
  margin-bottom: 0.5rem;
  font-weight: 500;
  color: #555;
}

.form-select, .form-control {
  padding: 0.375rem 0.75rem;
  border: 1px solid #ced4da;
  border-radius: 0.375rem;
  font-size: 1rem;
  transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}

.form-select:focus, .form-control:focus {
  border-color: #86b7fe;
  outline: 0;
  box-shadow: 0 0 0 0.25rem rgba(13, 110, 253, 0.25);
}

.form-actions {
  grid-column: 1 / -1;
  margin-top: 1rem;
}

@media (max-width: 768px) {
  .filters-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
  }
  
  .filters-content {
    grid-template-columns: 1fr;
  }
}
</style>