<template>
  <div class="supplier-list">
    <div class="table-responsive">
      <table class="table table-striped table-hover">
        <thead class="table-dark">
          <tr>
            <th>ID</th>
            <th>供应商名称</th>
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
          <tr v-else-if="suppliers.length === 0">
            <td colspan="3" class="text-center text-muted">暂无数据</td>
          </tr>
          <tr v-else v-for="supplier in suppliers" :key="supplier.id">
            <td>{{ supplier.id }}</td>
            <td>{{ supplier.supplier_name }}</td>
            <td>
              <div class="btn-group" role="group">
                <button type="button" class="btn btn-sm btn-outline-primary" @click="editSupplier(supplier)">
                  <i class="bi bi-pencil"></i>
                </button>
                <button type="button" class="btn btn-sm btn-outline-danger" @click="deleteSupplier(supplier.id)">
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
    <div class="modal fade" id="supplierModal" tabindex="-1" ref="supplierModal">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">{{ isEditing ? '编辑供应商' : '添加供应商' }}</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="saveSupplier">
              <div class="form-group">
                <label for="supplierName" class="form-label">供应商名称</label>
                <input type="text" class="form-control" id="supplierName" v-model="formData.supplier_name" required>
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">取消</button>
            <button type="button" class="btn btn-primary" @click="saveSupplier">保存</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, watch } from 'vue'
import SupplierApi from '@/api/supplier.api.js'
import { Modal } from 'bootstrap'

export default {
  name: 'SupplierList',
  props: {
    refreshTrigger: {
      type: Number,
      default: 0
    }
  },
  setup(props) {
    const suppliers = ref([])
    const loading = ref(false)
    const currentPage = ref(1)
    const totalPages = ref(0)
    const totalCount = ref(0)
    const supplierModal = ref(null)
    let modalInstance = null
    
    const isEditing = ref(false)
    const currentSupplierId = ref(null)
    const formData = ref({
      supplier_name: ''
    })
    
    // 加载供应商列表
    const loadSuppliers = async () => {
      loading.value = true
      try {
        const params = {
          page: currentPage.value
        }
        const response = await SupplierApi.getSupplierList(params)
        
        // 如果API返回的是分页数据
        if (response.results) {
          suppliers.value = response.results
          totalCount.value = response.count
          totalPages.value = Math.ceil(response.count / (response.page_size || 10))
        } else {
          // 如果API返回的是直接的数据数组
          suppliers.value = response
          totalCount.value = response.length
          totalPages.value = 1
        }
      } catch (error) {
        console.error('加载供应商列表失败:', error)
      } finally {
        loading.value = false
      }
    }
    
    // 显示添加模态框
    const showAddModal = () => {
      isEditing.value = false
      currentSupplierId.value = null
      formData.value = {
        supplier_name: ''
      }
      modalInstance.show()
    }
    
    // 编辑供应商
    const editSupplier = (supplier) => {
      isEditing.value = true
      currentSupplierId.value = supplier.id
      formData.value = {
        supplier_name: supplier.supplier_name
      }
      modalInstance.show()
    }
    
    // 保存供应商
    const saveSupplier = async () => {
      try {
        if (isEditing.value) {
          await SupplierApi.updateSupplier(currentSupplierId.value, formData.value)
        } else {
          await SupplierApi.createSupplier(formData.value)
        }
        
        modalInstance.hide()
        loadSuppliers()
      } catch (error) {
        console.error('保存供应商失败:', error)
      }
    }
    
    // 删除供应商
    const deleteSupplier = async (id) => {
      if (confirm('确定要删除这个供应商吗？')) {
        try {
          await SupplierApi.deleteSupplier(id)
          loadSuppliers()
        } catch (error) {
          console.error('删除供应商失败:', error)
        }
      }
    }
    
    // 切换页面
    const changePage = (page) => {
      if (page < 1 || page > totalPages.value) return
      currentPage.value = page
      loadSuppliers()
    }
    
    onMounted(() => {
      loadSuppliers()
      modalInstance = new Modal(supplierModal.value)
    })
    
    // 监听refreshTrigger变化，刷新列表
    watch(() => props.refreshTrigger, () => {
      loadSuppliers()
    })
    
    return {
      suppliers,
      loading,
      currentPage,
      totalPages,
      totalCount,
      supplierModal,
      isEditing,
      formData,
      showAddModal,
      editSupplier,
      saveSupplier,
      deleteSupplier,
      changePage
    }
  }
}
</script>

<style scoped>
.supplier-list {
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