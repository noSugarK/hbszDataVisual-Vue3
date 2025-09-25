<!-- src/components/brand/BrandList.vue -->
<template>
  <div class="brand-list-container">
    <div class="search-bar mb-3">
      <input
          type="text"
          class="form-control"
          placeholder="搜索品牌名称..."
          v-model="searchQuery"
          @input="handleSearch"
      >
    </div>
    <div class="table-responsive">
      <table class="table table-striped table-hover">
        <thead>
        <tr>
          <th>ID</th>
          <th>品牌名称</th>
          <th>品牌描述</th>
          <th>操作</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="brand in brands" :key="brand.id">
          <td>{{ brand.id }}</td>
          <td>{{ brand.brand_name }}</td>
          <td>{{ brand.description || '-' }}</td>
          <td>
            <button class="btn btn-sm btn-outline-primary me-1" @click="viewBrand(brand)">查看</button>
            <button class="btn btn-sm btn-outline-secondary me-1" @click="editBrand(brand)">编辑</button>
            <button class="btn btn-sm btn-outline-danger" @click="deleteBrand(brand)">删除</button>
          </td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import BrandService from '@/api/brand.api.js'

export default {
  name: 'BrandList',
  emits: ['view-brand', 'edit-brand', 'create-brand', 'delete-brand', 'modal-status-change'],
  setup(props, { emit }) {
    const brands = ref([])
    const searchQuery = ref('')
    const allBrands = ref([])

    const fetchBrands = async () => {
      try {
        const data = await BrandService.getBrands()
        brands.value = data
        allBrands.value = data
      } catch (error) {
        console.error('获取品牌列表失败:', error)
      }
    }

    const handleSearch = () => {
      if (searchQuery.value.trim() === '') {
        brands.value = allBrands.value
      } else {
        // 这里可以调用搜索接口或者前端过滤
        brands.value = allBrands.value.filter(brand =>
            brand.brand_name.toLowerCase().includes(searchQuery.value.toLowerCase())
        )
      }
    }

    const viewBrand = (brand) => {
      emit('view-brand', brand)
    }

    const editBrand = (brand) => {
      emit('edit-brand', brand)
    }

    const deleteBrand = (brand) => {
      emit('delete-brand', brand)
    }

    onMounted(() => {
      fetchBrands()
    })

    return {
      brands,
      searchQuery,
      handleSearch,
      viewBrand,
      editBrand,
      deleteBrand
    }
  }
}
</script>

<style scoped>
.brand-list-container {
  background: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.search-bar {
  max-width: 300px;
}

.table th {
  font-weight: 600;
}
</style>
