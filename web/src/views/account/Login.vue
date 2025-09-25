<template>
  <div class="login-container">
    <div class="login-card card shadow-lg border-0">
      <!-- Logo 区域 -->
      <LogoHeader />
      
      <h2 class="mt-3 fw-bold text-primary animate__animated animate__fadeInUp text-center">欢迎登录</h2>
      <!-- 登录表单 -->
      <form @submit.prevent="handleLogin">
        <div class="mb-3 animate__animated animate__fadeInLeft">
          <label for="username" class="form-label">用户名</label>
          <input
              id="username"
              v-model="form.username"
              type="text"
              class="form-control custom-input"
              placeholder="请输入用户名"
              required
          />
        </div>

        <div class="mb-3 animate__animated animate__fadeInRight">
          <label for="password" class="form-label">密码</label>
          <input
              id="password"
              v-model="form.password"
              type="password"
              class="form-control custom-input"
              placeholder="请输入密码"
              required
          />
        </div>

        <div class="d-flex justify-content-between align-items-center mb-3 animate__animated animate__fadeInUp">
          <div class="form-check">
            <input
                id="remember_me"
                v-model="form.remember_me"
                class="form-check-input custom-control-input"
                type="checkbox"
            />
            <label class="form-check-label" for="remember_me">记住我</label>
          </div>
          <a href="#" class="text-decoration-none" @click.prevent="gotoForgotPassword">忘记密码？</a>
        </div>

        <button
            type="submit"
            :disabled="loading"
            class="btn custom-btn w-100 mb-3 animate__animated animate__pulse animate__delay-1s"
        >
          <span v-if="loading" class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
          {{ loading ? ' 登录中...' : '登 录' }}
        </button>
      </form>

      <!-- 其他登录方式 (预留) -->
      <div class="text-center mt-4 animate__animated animate__fadeInUp animate__delay-1s">
        <p class="text-muted">或使用以下方式登录</p>
        <div class="d-flex justify-content-center gap-3">
          <!-- 示例图标，可替换为实际第三方登录图标 -->
          <button class="btn btn-outline-secondary btn-sm rounded-circle custom-social-btn">
            <i class="bi bi-google"></i>
          </button>
          <button class="btn btn-outline-secondary btn-sm rounded-circle custom-social-btn">
            <i class="bi bi-facebook"></i>
          </button>
          <button class="btn btn-outline-secondary btn-sm rounded-circle custom-social-btn">
            <i class="bi bi-github"></i>
          </button>
        </div>
      </div>
      <AccountFooter />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAccountStore } from '@/stores/account.js'
import { JSEncrypt } from 'encryptlong'
import AccountService from '@/api/account.api.js'
import LogoHeader from "@/components/common/LogoHeader.vue";
import AccountFooter from "@/components/layout/AccountFooter.vue";

// 路由与状态
const router = useRouter()
const accountStore = useAccountStore()

// 表单数据
const form = ref({
  username: '',
  password: '',
  remember_me: false,
})

// 状态控制
const loading = ref(false)
const publicKey = ref('')

// 页面加载时获取公钥
onMounted(async () => {
  try {
    const res = await AccountService.getPublicKey()
    publicKey.value = res.public_key
    console.log('✅ 公钥加载成功')
  } catch (err) {
    console.error('❌ 获取公钥失败:', err)
    alert('系统初始化失败，请刷新重试！')
  }
})

const gotoForgotPassword = () => {
  router.push('/forgot-password')
}

// 登录处理函数
const handleLogin = async () => {
  if (!publicKey.value) {
    alert('公钥未加载，请稍后重试')
    return
  }

  if (!form.value.username || !form.value.password) {
    alert('请填写用户名和密码')
    return
  }

  loading.value = true

  try {
    // 🔐 创建加密器
    const encryptor = new JSEncrypt()
    encryptor.setPublicKey(publicKey.value)

    // 📝 加密用户名和密码
    const encryptedUsername = encryptor.encrypt(form.value.username)
    const encryptedPassword = encryptor.encrypt(form.value.password)

    if (!encryptedUsername || !encryptedPassword) {
      throw new Error('加密失败，请检查公钥格式')
    }

    // 🔁 发送加密后的请求
    const res = await AccountService.login(encryptedUsername, encryptedPassword, form.value.remember_me)

    // ✅ 登录成功
    const { access, refresh, user } = res
    accountStore.setTokens(access, refresh)
    accountStore.setUser(user)

    // 跳转首页
    router.push('/')
  } catch (err) {
    const errorMsg =
        err.response?.data?.detail || '登录失败，请检查用户名或密码'
    alert(errorMsg)
    console.error('登录错误:', err)
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 20px;
}

.login-card {
  width: 100%;
  max-width: 450px;
  padding: 2.5rem;
  border-radius: 15px;
  background-color: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
  animation: float 3s ease-in-out infinite;
}

@keyframes float {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-10px); }
  100% { transform: translateY(0px); }
}

/* --- 改进的交互样式 --- */

/* 自定义输入框样式 */
.custom-input {
  transition: all 0.3s ease; /* 添加过渡效果 */
  border: 2px solid #ced4da; /* 稍微加粗默认边框 */
  padding: 0.5rem 0.75rem; /* 微调内边距 */
  border-radius: 8px; /* 稍微圆润一点 */
}
.custom-input:focus {
  border-color: #0d6efd; /* Bootstrap primary 色 */
  box-shadow: 0 0 0 0.25rem rgba(13, 110, 253, 0.25); /* 更柔和的焦点阴影 */
  outline: 0;
}
/* 悬停效果 */
.custom-input:hover:not(:focus) {
  border-color: #86b7fe; /* 悬停时边框颜色 */
}

/* 自定义主按钮样式 */
.custom-btn {
  background-color: #0d6efd; /* Bootstrap primary */
  border-color: #0d6efd;
  color: white;
  padding: 0.75rem 1.5rem; /* 增大内边距 */
  font-size: 1rem; /* 增大字体 */
  border-radius: 8px; /* 圆角 */
  transition: all 0.3s ease; /* 添加过渡 */
  font-weight: 500; /* 字体加粗 */
  letter-spacing: 1px; /* 字符间距 */
}
/* 悬停效果 */
.custom-btn:hover:not(:disabled) {
  background-color: #0b5ed7; /* 深一点的蓝色 */
  border-color: #0a58ca;
  transform: translateY(-2px); /* 向上轻微移动 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* 增加阴影 */
}
/* 激活/按下效果 */
.custom-btn:active:not(:disabled) {
  background-color: #0a58ca;
  border-color: #0a53be;
  transform: translateY(0); /* 按下时回到原位 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); /* 减小阴影 */
}
/* 禁用状态 */
.custom-btn:disabled {
  background-color: #6c757d; /* 灰色 */
  border-color: #6c757d;
  opacity: 0.65;
  cursor: not-allowed;
}

/* 自定义社交按钮样式 */
.custom-social-btn {
  transition: all 0.2s ease;
  border-width: 2px;
  width: 45px;
  height: 45px;
}
.custom-social-btn:hover {
  transform: scale(1.1);
  border-color: #0d6efd;
  background-color: #e7f1ff; /* 浅蓝色背景 */
}
.custom-social-btn:active {
  transform: scale(1.05);
}

/* 自定义复选框样式 */
.custom-control-input {
  width: 18px;
  height: 18px;
  margin-right: 8px;
  accent-color: #0d6efd;
  border: 2px solid #000; /* 增加黑色边框 */
  border-radius: 4px;
  cursor: pointer;
}

.custom-control-input:checked {
  background-color: #0d6efd;
  border-color: #0d6efd;
}

.custom-control-input:focus {
  outline: 2px solid #0d6efd;
  outline-offset: 2px;
}
</style>