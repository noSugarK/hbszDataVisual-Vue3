import axios from 'axios'

const api = axios.create({
    baseURL: 'http://localhost:8000', // Django 后端地址
    headers: {
        'Content-Type': 'application/json',
    },
})

// 请求拦截器：添加 JWT token
api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('access_token')
        if (token) {
            config.headers.Authorization = `Bearer ${token}`
        }
        return config
    },
    (error) => Promise.reject(error)
)

export default api