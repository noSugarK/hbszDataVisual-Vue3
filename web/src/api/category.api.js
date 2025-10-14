import api from './api'

class CategoryApi {
  // 获取物资类别列表
  async getCategoryList(params = {}) {
    const response = await api.get('/category/', { params })
    return response.data
  }

  // 获取单个物资类别详情
  async getCategoryDetail(id) {
    const response = await api.get(`/category/${id}/`)
    return response.data
  }

  // 创建新物资类别
  async createCategory(categoryData) {
    const response = await api.post('/category/', categoryData)
    return response.data
  }

  // 更新物资类别信息
  async updateCategory(id, categoryData) {
    const response = await api.put(`/category/${id}/`, categoryData)
    return response.data
  }

  // 删除物资类别
  async deleteCategory(id) {
    const response = await api.delete(`/category/${id}/`)
    return response.data
  }
}

export default new CategoryApi()