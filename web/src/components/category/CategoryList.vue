<template>
  <div class="category-list">
    <div class="table-responsive">
      <table class="table table-striped table-hover">
        <thead class="table-dark">
          <tr>
            <th>ID</th>
            <th>物资类别名称</th>
            <th>操作</th>
          </tr>
        </thead>
        <tbody>
          <tr v-if="loading">
            <td colspan="3" class="text-center">
              <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">加载中...</span>
              </div>
            </td>
          </tr>
          <tr v-else-if="categories.length === 0">
            <td colspan="3" class="text-center text-muted">暂无数据</td>
          </tr>
          <tr v-else v-for="category in categories" :key="category.id">
            <td>{{ category.id }}</td>
            <td>{{ category.category_name }}</td>
            <td>
              <div class="btn-group" role="group">
                <button type="button" class="btn btn-sm btn-outline-primary" @click="editCategory(category)">
                  <i class="bi bi-pencil"></i>
                </button>
                <button type="button" class="btn btn-sm btn-outline-danger" @click="deleteCategory(category.id)">
                  <i class="bi bi-trash"></i>
                </button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    
    <!-- 分页 -->
    <nav v-if="totalPages > 1">
      <ul class="pagination justify-content-center">
        <li class="page-item" :class="{ disabled: currentPage === 1 }">
          <a class="page-link" href="#" @click.prevent="changePage(currentPage - 1)">上一页</a>
        </li>
        <li v-for="page in totalPages" :key="page" class="page-item" :class="{ active: page === currentPage }">
          <a class="page-link" href="#" @click.prevent="changePage(page)">{{ page }}</a>
        </li>
        <li class="page-item" :class="{ disabled: currentPage === totalPages }">
          <a class="page-link" href="#" @click.prevent="changePage(currentPage + 1)">下一页</a>
        </li>
      </ul>
    </nav>
    
    <!-- 添加/编辑模态框 -->
    <div class="modal fade" id="categoryModal" tabindex="-1" ref="categoryModal">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">{{ isEditing ? '编辑物资类别' : '添加物资类别' }}</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="saveCategory">
              <div class="form-group">
                <label for="categoryName" class="form-label">物资类别名称</label>
                <input type="text" class="form-control" id="categoryName" v-model="formData.category_name" required>
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">取消</button>
            <button type="button" class="btn btn-primary" @click="saveCategory">保存</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, watch } from 'vue'
import CategoryApi from '@/api/category.api.js'
import { Modal } from 'bootstrap'

export default {
  name: 'CategoryList',
  props: {
    refreshTrigger: {
      type: Number,
      default: 0
    }
  },
  setup(props) {
    const categories = ref([])
    const loading = ref(false)
    const currentPage = ref(1)
    const totalPages = ref(0)
    const totalCount = ref(0)
    const categoryModal = ref(null)
    let modalInstance = null
    
    const isEditing = ref(false)
    const currentCategoryId = ref(null)
    const formData = ref({
      category_name: ''
    })
    
    // 加载物资类别列表
    const loadCategories = async () => {
      loading.value = true
      try {
        const params = {
          page: currentPage.value
        }
        const response = await CategoryApi.getCategoryList(params)
        
        // 如果API返回的是分页数据
        if (response.results) {
          categories.value = response.results
          totalCount.value = response.count
          totalPages.value = Math.ceil(response.count / (response.page_size || 10))
        } else {
          // 如果API返回的是直接的数据数组
          categories.value = response
          totalCount.value = response.length
          totalPages.value = 1
        }
      } catch (error) {
        console.error('加载物资类别列表失败:', error)
      } finally {
        loading.value = false
      }
    }
    
    // 显示添加模态框
    const showAddModal = () => {
      isEditing.value = false
      currentCategoryId.value = null
      formData.value = {
        category_name: ''
      }
      modalInstance.show()
    }
    
    // 编辑物资类别
    const editCategory = (category) => {
      isEditing.value = true
      currentCategoryId.value = category.id
      formData.value = {
        category_name: category.category_name
      }
      modalInstance.show()
    }
    
    // 保存物资类别
    const saveCategory = async () => {
      try {
        if (isEditing.value) {
          await CategoryApi.updateCategory(currentCategoryId.value, formData.value)
        } else {
          await CategoryApi.createCategory(formData.value)
        }
        
        modalInstance.hide()
        loadCategories()
      } catch (error) {
        console.error('保存物资类别失败:', error)
      }
    }
    
    // 删除物资类别
    const deleteCategory = async (id) => {
      if (confirm('确定要删除这个物资类别吗？')) {
        try {
          await CategoryApi.deleteCategory(id)
          loadCategories()
        } catch (error) {
          console.error('删除物资类别失败:', error)
        }
      }
    }
    
    // 切换页面
    const changePage = (page) => {
      if (page < 1 || page > totalPages.value) return
      currentPage.value = page
      loadCategories()
    }
    
    onMounted(() => {
      loadCategories()
      modalInstance = new Modal(categoryModal.value)
    })
    
    // 监听refreshTrigger变化，刷新列表
    watch(() => props.refreshTrigger, () => {
      loadCategories()
    })
    
    return {
      categories,
      loading,
      currentPage,
      totalPages,
      totalCount,
      categoryModal,
      isEditing,
      formData,
      showAddModal,
      editCategory,
      saveCategory,
      deleteCategory,
      changePage
    }
  }
}
</script>

<style scoped>
.category-list {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
}

.table-responsive {
  margin-bottom: 20px;
}

.btn-group .btn {
  margin-right: 5px;
}

.pagination {
  margin-top: 20px;
}

/* 表单样式 */
.form-group {
  margin-bottom: 1rem;
}

.form-label {
  margin-bottom: 0.5rem;
  font-weight: 500;
}

.form-control, .form-select {
  padding: 0.75rem 1rem;
  border: 1px solid #ced4da;
  border-radius: 0.375rem;
  font-size: 1rem;
  transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}

.form-control:focus, .form-select:focus {
  border-color: #86b7fe;
  outline: 0;
  box-shadow: 0 0 0 0.25rem rgba(13, 110, 253, 0.25);
}
</style>