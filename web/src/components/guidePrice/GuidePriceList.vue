<template>
  <div class="guide-price-list">
    <div class="list-header">
      <h4 class="list-title">指导价列表</h4>
      <div class="list-actions">
        <button class="btn btn-success" @click="exportData">
          <i class="bi bi-download me-1"></i>导出Excel
        </button>
        <button class="btn btn-primary" @click="showAddModal">
          <i class="bi bi-plus-circle me-1"></i>新增指导价
        </button>
        <button class="btn btn-outline-secondary ms-2" @click="refreshData">
          <i class="bi bi-arrow-clockwise me-1"></i>刷新
        </button>
      </div>
    </div>
    
    <div class="list-content">
      <div class="table-responsive">
        <table class="table table-striped table-hover">
          <thead>
            <tr>
              <th>地区</th>
              <th>物资类别</th>
              <th>规格</th>
              <th>信息价(元)</th>
              <th>日期</th>
              <th>操作</th>
            </tr>
          </thead>
          <tbody>
            <tr v-if="loading">
              <td colspan="9" class="text-center py-4">
                <div class="spinner-border text-primary" role="status">
                  <span class="visually-hidden">加载中...</span>
                </div>
              </td>
            </tr>
            <tr v-else-if="guidePrices.length === 0">
              <td colspan="6" class="text-center py-4 text-muted">
                暂无数据
              </td>
            </tr>
            <tr v-else v-for="item in guidePrices" :key="item.id">
              <td>{{ item.region_name }}</td>
              <td>{{ item.category_name }}</td>
              <td>{{ item.specification_name }}</td>
              <td>{{ item.unit_price }}</td>
              <td>{{ formatDate(item.date) }}</td>
              <td>
                <div class="btn-group btn-group-sm">
                  <button class="btn btn-outline-primary" @click="viewItem(item)">
                    <i class="bi bi-eye"></i>
                  </button>
                  <button class="btn btn-outline-secondary" @click="editItem(item)">
                    <i class="bi bi-pencil"></i>
                  </button>
                  <button class="btn btn-outline-danger" @click="deleteItem(item.id)">
                    <i class="bi bi-trash"></i>
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      
      <div class="pagination-wrapper" v-if="totalPages > 1">
        <nav>
          <ul class="pagination">
            <li class="page-item" :class="{ disabled: currentPage === 1 }">
              <a class="page-link" href="#" @click.prevent="changePage(currentPage - 1)">上一页</a>
            </li>
            <li 
              v-for="page in displayedPages" 
              :key="page" 
              class="page-item" 
              :class="{ active: page === currentPage }"
            >
              <a class="page-link" href="#" @click.prevent="changePage(page)">{{ page }}</a>
            </li>
            <li class="page-item" :class="{ disabled: currentPage === totalPages }">
              <a class="page-link" href="#" @click.prevent="changePage(currentPage + 1)">下一页</a>
            </li>
          </ul>
        </nav>
        <div class="pagination-info">
          显示 {{ (currentPage - 1) * pageSize + 1 }} - {{ Math.min(currentPage * pageSize, totalCount) }} 条，共 {{ totalCount }} 条
        </div>
      </div>
    </div>
    
    <!-- 添加/编辑模态框 -->
    <div class="modal fade" id="guidePriceModal" tabindex="-1" ref="guidePriceModal">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">{{ isEditing ? '编辑指导价' : '新增指导价' }}</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="saveItem">
              <div class="form-group">
                <label for="region" class="form-label">地区</label>
                <select id="region" class="form-select" v-model="formData.region_id" required>
                  <option value="">请选择地区</option>
                  <option v-for="region in regions" :key="region.id" :value="region.id">
                    {{ region.name }}
                  </option>
                </select>
              </div>
              
              <div class="form-group">
                <label for="category" class="form-label">物资类别</label>
                <select id="category" class="form-select" v-model="formData.category_id" @change="onCategoryChange" required>
                  <option value="">请选择物资类别</option>
                  <option v-for="category in categories" :key="category.id" :value="category.id">
                    {{ category.category_name }}
                  </option>
                </select>
              </div>
              
              <div class="form-group">
                <label for="specification" class="form-label">规格</label>
                <select id="specification" class="form-select" v-model="formData.specification_id" required>
                  <option value="">请选择规格</option>
                  <option v-for="specification in specifications" :key="specification.id" :value="specification.id">
                    {{ specification.specification_name }}
                  </option>
                </select>
              </div>
              
              <div class="form-group">
                <label for="date" class="form-label">日期</label>
                <input 
                  type="date" 
                  id="date" 
                  class="form-control" 
                  v-model="formData.date" 
                  required
                >
              </div>
              
              <div class="form-group">
                <label for="unit_price" class="form-label">信息价(元)</label>
                <input 
                  type="number" 
                  id="unit_price" 
                  class="form-control" 
                  v-model="formData.unit_price" 
                  step="0.01"
                  min="0"
                  required
                >
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">取消</button>
            <button type="button" class="btn btn-primary" @click="saveItem">保存</button>
          </div>
        </div>
      </div>
    </div>
    
    <!-- 查看详情模态框 -->
    <div class="modal fade" id="viewModal" tabindex="-1" ref="viewModal">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">指导价详情</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body" v-if="viewData">
            <div class="row">
              <div class="col-md-6 mb-3">
                <strong>地区：</strong>{{ viewData.region_name }}
              </div>
              <div class="col-md-6 mb-3">
                <strong>物资类别：</strong>{{ viewData.category_name }}
              </div>
              <div class="col-md-6 mb-3">
                <strong>规格：</strong>{{ viewData.specification_name }}
              </div>
              <div class="col-md-6 mb-3">
                <strong>日期：</strong>{{ formatDate(viewData.date) }}
              </div>
              <div class="col-md-6 mb-3">
                <strong>信息价：</strong>{{ viewData.unit_price }} 元
              </div>
              <div class="col-md-6 mb-3">
                <strong>创建时间：</strong>{{ formatDateTime(viewData.created_at) }}
              </div>
              <div class="col-md-6 mb-3">
                <strong>更新时间：</strong>{{ formatDateTime(viewData.updated_at) }}
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
import { ref, onMounted, computed } from 'vue'
import { Modal } from 'bootstrap'
import RegionApi from '@/api/region.api.js'
import GuidePriceApi from '@/api/guidePrice.api.js'

export default {
  name: 'GuidePriceList',
  props: {
    filters: {
      type: Object,
      default: () => ({})
    }
  },
  setup(props) {
    const guidePrices = ref([])
    const regions = ref([])
    const categories = ref([])
    const specifications = ref([])
    const loading = ref(false)
    const currentPage = ref(1)
    const pageSize = ref(10)
    const totalCount = ref(0)
    const totalPages = ref(0)
    
    const guidePriceModal = ref(null)
    const viewModal = ref(null)
    const isEditing = ref(false)
    const viewData = ref(null)
    
    const formData = ref({
      region_id: '',
      category_id: '',
      specification_id: '',
      unit_price: '',
      date: ''
    })
    
    // 计算要显示的页码
    const displayedPages = computed(() => {
      const pages = []
      const maxVisible = 5
      
      if (totalPages.value <= maxVisible) {
        for (let i = 1; i <= totalPages.value; i++) {
          pages.push(i)
        }
      } else {
        const start = Math.max(1, currentPage.value - Math.floor(maxVisible / 2))
        const end = Math.min(totalPages.value, start + maxVisible - 1)
        
        for (let i = start; i <= end; i++) {
          pages.push(i)
        }
      }
      
      return pages
    })
    
    // 加载指导价数据
    const loadGuidePrices = async () => {
      loading.value = true
      try {
        const params = {
          page: currentPage.value,
          page_size: pageSize.value,
          ...props.filters
        }
        
        const data = await GuidePriceApi.getGuidePriceList(params)
        guidePrices.value = data.results
        totalCount.value = data.count
        totalPages.value = Math.ceil(data.count / pageSize.value)
      } catch (error) {
        console.error('加载指导价数据失败:', error)
      } finally {
        loading.value = false
      }
    }
    
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
      formData.value.specification_id = ''
      loadSpecifications(formData.value.category_id)
    }
    
    // 刷新数据
    const refreshData = () => {
      loadGuidePrices()
    }
    
    // 切换页码
    const changePage = (page) => {
      if (page < 1 || page > totalPages.value) return
      currentPage.value = page
      loadGuidePrices()
    }
    
    // 显示添加模态框
    const showAddModal = () => {
      isEditing.value = false
      resetFormData()
      
      // 设置默认日期为今天
      const today = new Date().toISOString().split('T')[0]
      formData.value.date = today
      
      const modal = new Modal(guidePriceModal.value)
      modal.show()
    }
    
    // 查看详情
    const viewItem = (item) => {
      viewData.value = item
      const modal = new Modal(viewModal.value)
      modal.show()
    }
    
    // 编辑项目
    const editItem = (item) => {
      isEditing.value = true
      formData.value = { ...item }
      
      // 加载对应的规格
      loadSpecifications(item.category_id)
      
      const modal = new Modal(guidePriceModal.value)
      modal.show()
    }
    
    // 删除项目
    const deleteItem = async (id) => {
      if (!confirm('确定要删除这条指导价记录吗？')) return
      
      try {
        await GuidePriceApi.deleteGuidePrice(id)
        loadGuidePrices()
      } catch (error) {
        console.error('删除指导价失败:', error)
      }
    }
    
    // 保存项目
    const saveItem = async () => {
      try {
        if (isEditing.value) {
          await GuidePriceApi.updateGuidePrice(formData.value.id, formData.value)
        } else {
          await GuidePriceApi.createGuidePrice(formData.value)
        }
        
        const modal = Modal.getInstance(guidePriceModal.value)
        modal.hide()
        
        loadGuidePrices()
      } catch (error) {
        console.error('保存指导价失败:', error)
      }
    }
    
    // 导出数据
    const exportData = async () => {
      try {
        const params = { ...props.filters }
        await GuidePriceApi.exportGuidePriceData(params)
      } catch (error) {
        console.error('导出数据失败:', error)
      }
    }
    
    // 重置表单数据
    const resetFormData = () => {
      formData.value = {
        region_id: '',
        category_id: '',
        specification_id: '',
        unit_price: '',
        date: ''
      }
    }
    
    // 格式化日期
    const formatDate = (dateString) => {
      if (!dateString) return ''
      const date = new Date(dateString)
      return date.toLocaleDateString('zh-CN')
    }
    
    // 格式化日期时间
    const formatDateTime = (dateString) => {
      if (!dateString) return ''
      const date = new Date(dateString)
      return date.toLocaleString('zh-CN')
    }
    
    onMounted(() => {
      loadGuidePrices()
      loadRegions()
      loadCategories()
      loadSpecifications()
    })
    
    return {
      guidePrices,
      regions,
      categories,
      specifications,
      loading,
      currentPage,
      pageSize,
      totalCount,
      totalPages,
      displayedPages,
      guidePriceModal,
      viewModal,
      isEditing,
      viewData,
      formData,
      onCategoryChange,
      refreshData,
      changePage,
      showAddModal,
      viewItem,
      editItem,
      deleteItem,
      saveItem,
      exportData,
      formatDate,
      formatDateTime
    }
  },
  watch: {
    filters: {
      handler() {
        this.currentPage = 1
        this.loadGuidePrices()
      },
      deep: true
    }
  }
}
</script>

<style scoped>
.guide-price-list {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
}

.list-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.list-title {
  margin: 0;
  font-size: 18px;
  font-weight: 600;
  color: #333;
}

.list-actions {
  display: flex;
  gap: 10px;
}

.table-responsive {
  margin-bottom: 20px;
}

.pagination-wrapper {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 15px;
}

.pagination-info {
  color: #666;
  font-size: 14px;
}

/* 表单样式 */
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

@media (max-width: 768px) {
  .list-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
  }
  
  .pagination-wrapper {
    flex-direction: column;
    align-items: center;
  }
}
</style>