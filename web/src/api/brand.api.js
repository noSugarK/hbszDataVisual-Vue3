// src/api/brand.api.js
import api from './api'

class BrandService {
    // 获取品牌列表
    async getBrands(params = {}) {
        const response = await api.get('/brand/', { params })
        return response.data.results || response.data
    }

    // 获取品牌详情
    async getBrand(id) {
        const response = await api.get(`/brand/${id}/`)
        return response.data
    }

    // 搜索品牌
    async searchBrands(name) {
        const response = await api.get('/brand/search/', { params: { name } })
        return response.data
    }

    // 创建品牌
    async createBrand(data) {
        // 适配后端需要的字段格式
        const requestData = {
            brand_name: data.brand_name,
            description: data.description
        }
        const response = await api.post('/brand/', requestData)
        return response.data
    }

    // 更新品牌
    async updateBrand(id, data) {
        // 适配后端需要的字段格式
        const requestData = {
            brand_name: data.brand_name,
            description: data.description
        }
        const response = await api.put(`/brand/${id}/`, requestData)
        return response.data
    }

    // 删除品牌
    async deleteBrand(id) {
        const response = await api.delete(`/brand/${id}/`)
        return response.data
    }

    // 获取品牌统计信息
    async getBrandStats() {
        const response = await api.get('/brand/')
        const brands = response.data
        return {
            totalCount: brands.count,
        }
    }
}

export default new BrandService()
