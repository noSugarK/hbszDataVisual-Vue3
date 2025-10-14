import api from './api'

class GuidePriceApi {
  // 获取指导价列表
  async getGuidePriceList(params = {}) {
    const response = await api.get('/guide-price/', { params })
    return response.data
  }

  // 获取单个指导价详情
  async getGuidePriceDetail(id) {
    const response = await api.get(`/guide-price/${id}/`)
    return response.data
  }

  // 创建新指导价
  async createGuidePrice(guidePriceData) {
    const response = await api.post('/guide-price/', guidePriceData)
    return response.data
  }

  // 更新指导价信息
  async updateGuidePrice(id, guidePriceData) {
    const response = await api.put(`/guide-price/${id}/`, guidePriceData)
    return response.data
  }

  // 删除指导价
  async deleteGuidePrice(id) {
    const response = await api.delete(`/guide-price/${id}/`)
    return response.data
  }

  // 获取指导价统计信息
  async getGuidePriceStats() {
    const response = await api.get('/guide-price/stats/')
    return response.data
  }

  // 获取指导价图表数据
  async getGuidePriceChartData(params = {}) {
    const response = await api.get('/guide-price/chart-data/', { params })
    return response.data
  }

  // 导出指导价数据
  async exportGuidePriceData(params = {}) {
    const response = await api.get('/guide-price/export/', { 
      params,
      responseType: 'blob'
    })
    
    // 创建下载链接
    const url = window.URL.createObjectURL(new Blob([response.data]))
    const link = document.createElement('a')
    link.href = url
    link.setAttribute('download', `指导价数据_${new Date().toISOString().slice(0, 10)}.xlsx`)
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)
    window.URL.revokeObjectURL(url)
    
    return response.data
  }
}

export default new GuidePriceApi()