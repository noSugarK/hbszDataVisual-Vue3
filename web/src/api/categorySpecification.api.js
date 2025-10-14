import axios from 'axios'

const API_URL = '/v1/category/specifications/'

class CategorySpecificationApi {
  // 获取所有规格
  static getAll() {
    return axios.get(API_URL)
  }

  // 根据ID获取规格
  static getById(id) {
    return axios.get(`${API_URL}${id}/`)
  }

  // 根据类别ID获取规格
  static getByCategory(categoryId) {
    return axios.get(`${API_URL}?category=${categoryId}`)
  }

  // 创建规格
  static create(data) {
    return axios.post(API_URL, data)
  }

  // 更新规格
  static update(id, data) {
    return axios.put(`${API_URL}${id}/`, data)
  }

  // 删除规格
  static delete(id) {
    return axios.delete(`${API_URL}${id}/`)
  }
}

export default CategorySpecificationApi