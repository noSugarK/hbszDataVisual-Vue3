<template>
  <div class="category-list">
    <div class="table-responsive">
      <table class="table table-striped table-hover">
        <thead class="table-dark">
          <tr>
            <th>ID</th>
            <th>物资类别名称</th>
            <th>规格型号</th>
            <th>操作</th>
          </tr>
        </thead>
        <tbody>
          <tr v-if="loading">
            <td colspan="4" class="text-center">
              <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">加载中...</span>
              </div>
            </td>
          </tr>
          <tr v-else-if="categories.length === 0">
            <td colspan="4" class="text-center text-muted">暂无数据</td>
          </tr>
          <template v-else v-for="category in categories" :key="category.id">
            <tr>
              <td>{{ category.id }}</td>
              <td>{{ category.category_name }}</td>
              <td>
                <span v-if="category.specifications && category.specifications.length > 0">
                  {{ category.specifications.map(s => s.specification_name).join(', ') }}
                </span>
                <span v-else class="text-muted">暂无规格</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-sm btn-outline-primary" @click="editCategory(category)">
                    <i class="bi bi-pencil"></i>
                  </button>
                  <button type="button" class="btn btn-sm btn-outline-info" @click="manageSpecifications(category)">
                    <i class="bi bi-list-ul"></i>
                  </button>
                  <button type="button" class="btn btn-sm btn-outline-danger" @click="deleteCategory(category.id)">
                    <i class="bi bi-trash"></i>
                  </button>
                </div>
              </td>
            </tr>
          </template>
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
    
    <!-- 添加/编辑类别模态框 -->
    <div class="modal fade" id="categoryModal" tabindex="-1" aria-labelledby="categoryModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="categoryModalLabel">{{ isEditing ? '编辑物资类别' : '添加物资类别' }}</h5>
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

    <!-- 规格管理模态框 -->
    <div class="modal fade" id="specificationModal" tabindex="-1" aria-labelledby="specificationModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="specificationModalLabel">管理规格型号</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <h6>物资类别: {{ currentCategory ? currentCategory.category_name : '' }}</h6>
            
            <!-- 添加新规格 -->
            <div class="mb-3">
              <div class="input-group">
                <input type="text" class="form-control" v-model="newSpecificationName" placeholder="输入新规格名称">
                <button class="btn btn-outline-primary" type="button" @click="addSpecification">
                  <i class="bi bi-plus-lg"></i> 添加
                </button>
              </div>
            </div>
            
            <!-- 现有规格列表 -->
            <div class="list-group">
              <div v-if="currentSpecifications.length === 0" class="text-center text-muted py-3">
                暂无规格型号
              </div>
              <div v-else v-for="(spec, index) in currentSpecifications" :key="spec.id" class="list-group-item d-flex justify-content-between align-items-center">
                <div v-if="spec.editing">
                  <input type="text" class="form-control form-control-sm" v-model="spec.tempName" @keyup.enter="saveSpecification(spec)">
                </div>
                <div v-else>{{ spec.specification_name }}</div>
                <div>
                  <button v-if="spec.editing" class="btn btn-sm btn-outline-success me-1" @click="saveSpecification(spec)">
                    <i class="bi bi-check-lg"></i>
                  </button>
                  <button v-else class="btn btn-sm btn-outline-primary me-1" @click="editSpecification(spec)">
                    <i class="bi bi-pencil"></i>
                  </button>
                  <button class="btn btn-sm btn-outline-danger" @click="deleteSpecification(spec.id)">
                    <i class="bi bi-trash"></i>
                  </button>
                </div>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">关闭</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, watch } from 'vue'
import CategoryApi from '@/api/category.api.js'
import CategorySpecificationApi from '@/api/categorySpecification.api.js'
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
    const specificationModal = ref(null)
    let modalInstance = null
    let specificationModalInstance = null
    
    const isEditing = ref(false)
    const currentCategoryId = ref(null)
    const currentCategory = ref(null)
    const currentSpecifications = ref([])
    const newSpecificationName = ref('')
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
        
        // 确保每个类别都有specifications字段
        categories.value = categories.value.map(category => ({
          ...category,
          specifications: category.specifications || []
        }))
        
        console.log('加载的类别数据:', categories.value)
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
      if (!modalInstance) {
        modalInstance = new Modal(document.getElementById('categoryModal'))
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
      if (!modalInstance) {
        modalInstance = new Modal(document.getElementById('categoryModal'))
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
    
    // 管理规格
    const manageSpecifications = async (category) => {
      currentCategory.value = category
      await fetchSpecifications(category.id)
      if (!specificationModalInstance) {
        specificationModalInstance = new Modal(document.getElementById('specificationModal'))
      }
      specificationModalInstance.show()
    }

    // 获取规格列表
    const fetchSpecifications = async (categoryId) => {
      try {
        const response = await CategorySpecificationApi.getByCategory(categoryId)
        currentSpecifications.value = response.data.results || response.data || []
        currentSpecifications.value = currentSpecifications.value.map(spec => ({
          ...spec,
          editing: false,
          tempName: spec.specification_name
        }))
      } catch (error) {
        console.error('获取规格失败:', error)
        currentSpecifications.value = []
      }
    }

    // 添加规格
    const addSpecification = async () => {
      if (!newSpecificationName.value.trim()) return
      
      try {
        await CategorySpecificationApi.create({
          category: currentCategory.value.id,
          specification_name: newSpecificationName.value
        })
        newSpecificationName.value = ''
        fetchSpecifications(currentCategory.value.id)
      } catch (error) {
        console.error('添加规格失败:', error)
      }
    }

    // 编辑规格
    const editSpecification = (spec) => {
      spec.editing = true
      spec.tempName = spec.specification_name
    }

    // 保存规格
    const saveSpecification = async (spec) => {
      if (!spec.tempName.trim()) return
      
      try {
        await CategorySpecificationApi.update(spec.id, {
          specification_name: spec.tempName
        })
        spec.editing = false
        fetchSpecifications(currentCategory.value.id)
      } catch (error) {
        console.error('更新规格失败:', error)
      }
    }

    // 删除规格
    const deleteSpecification = async (specId) => {
      if (confirm('确定要删除这个规格吗？')) {
        try {
          await CategorySpecificationApi.delete(specId)
          fetchSpecifications(currentCategory.value.id)
        } catch (error) {
          console.error('删除规格失败:', error)
        }
      }
    }
    
    onMounted(() => {
      loadCategories()
      // 延迟初始化模态框，确保DOM已完全渲染
      setTimeout(() => {
        const modalElement = document.getElementById('categoryModal')
        if (modalElement) {
          modalInstance = new Modal(modalElement)
        }
      }, 100)
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
      currentCategory,
      currentSpecifications,
      newSpecificationName,
      showAddModal,
      editCategory,
      saveCategory,
      deleteCategory,
      changePage,
      manageSpecifications,
      addSpecification,
      editSpecification,
      saveSpecification,
      deleteSpecification
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