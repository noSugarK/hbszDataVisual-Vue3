// src/services/region.service.js
import api from './api'

class RegionService {
  // 获取区域列表
  async getRegions(params = {}) {
    const response = await api.get('/region/', { params })
    return response.data
  }



  // 获取单个区域详情
  async getRegion(id) {
    const response = await api.get(`/region/${id}/`)
    return response.data
  }

  // 创建新区域
  async createRegion(regionData) {
    const response = await api.post('/region/', regionData)
    return response.data
  }

  // 更新区域信息
  async updateRegion(id, regionData) {
    const response = await api.put(`/region/${id}/`, regionData)
    return response.data
  }

  // 删除区域
  async deleteRegion(id) {
    const response = await api.delete(`/region/${id}/`)
    return response.data
  }

  // 获取区域树结构
  async getRegionTree() {
    const response = await api.get('/region/tree/')
    return response.data
  }

  async getRegionStats() {
      const response = await api.get('/region/stats/')
      return response.data
  }

}

export default new RegionService()