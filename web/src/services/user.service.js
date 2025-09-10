import api from './api'

class UserService {
  // 获取当前用户信息
  async getProfile() {
    const response = await api.get('/users/profile/')
    return response.data
  }

  // 更新当前用户信息
  async updateProfile(userData) {
    const response = await api.put('/users/profile/', userData)
    return response.data
  }

  // 获取指定用户详情
  async getUserDetail(userId) {
    const response = await api.get(`/users/${userId}/`)
    return response.data
  }

  // 获取用户列表
  async getUsers(params = {}) {
    const response = await api.get('/users/', { params })
    return response.data
  }

  // 创建用户
  async createUser(userData) {
    const response = await api.post('/users/', userData)
    return response.data
  }

  // 更新用户
  async updateUser(userId, userData) {
    const response = await api.put(`/users/${userId}/`, userData)
    return response.data
  }

  // 删除用户
  async deleteUser(userId) {
    const response = await api.delete(`/users/${userId}/`)
    return response.data
  }
}

export default new UserService()