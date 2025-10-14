import api from './api'

class SupplierApi {
  // 获取供应商列表
  async getSupplierList(params = {}) {
    const response = await api.get('/supplier/', { params })
    return response.data
  }

  // 获取单个供应商详情
  async getSupplierDetail(id) {
    const response = await api.get(`/supplier/${id}/`)
    return response.data
  }

  // 创建新供应商
  async createSupplier(supplierData) {
    const response = await api.post('/supplier/', supplierData)
    return response.data
  }

  // 更新供应商信息
  async updateSupplier(id, supplierData) {
    const response = await api.put(`/supplier/${id}/`, supplierData)
    return response.data
  }

  // 删除供应商
  async deleteSupplier(id) {
    const response = await api.delete(`/supplier/${id}/`)
    return response.data
  }
}

export default new SupplierApi()