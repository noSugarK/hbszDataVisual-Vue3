<!-- src/views/account/ResetPassword.vue -->
<template>
  <div class="login-container">
    <div class="login-card card shadow-lg border-0">
      <!-- Logo 区域 -->
      <LogoHeader />
      
      <h2 class="mt-3 fw-bold text-primary animate__animated animate__fadeInUp">设置新密码</h2>
      <!-- 验证中状态 -->
      <div v-if="loading" class="text-center animate__animated animate__fadeIn">
        <div class="spinner-border text-primary" role="status">
          <span class="visually-hidden">验证中...</span>
        </div>
        <p class="mt-2 text-muted">正在验证链接...</p>
      </div>

      <!-- 链接无效 -->
      <div v-else-if="!validLink" class="animate__animated animate__fadeIn">
        <div class="text-center mb-4">
          <i class="bi bi-x-circle-fill text-danger" style="font-size: 3rem;"></i>
        </div>
        <p class="text-danger text-center fw-bold mb-3">
          链接无效或已过期
        </p>
        <p class="text-muted text-center mb-4">
          请重新申请密码重置链接
        </p>
        <button
            type="button"
            class="btn custom-secondary-btn w-100 mb-3 animate__animated animate__pulse animate__delay-1s"
            @click="$router.push('/forgot-password')"
        >
          重新申请
        </button>
        <div class="text-center mt-3">
          <a href="#" class="text-decoration-none" @click.prevent="$router.push('/login')">← 返回登录</a>
        </div>
      </div>

      <!-- 重置密码表单 -->
      <div v-else class="animate__animated animate__fadeIn">
        <p class="text-muted mb-4">
          请输入您的新密码，至少8位字符。
        </p>

        <form @submit.prevent="submitNewPassword">
          <div class="mb-3 animate__animated animate__fadeInLeft">
            <label for="password" class="form-label">新密码</label>
            <input
                id="password"
                v-model="password"
                type="password"
                class="form-control custom-input"
                placeholder="至少 8 位"
                required
            />
          </div>

          <div class="mb-3 animate__animated animate__fadeInRight">
            <label for="confirmPassword" class="form-label">确认新密码</label>
            <input
                id="confirmPassword"
                v-model="confirmPassword"
                type="password"
                class="form-control custom-input"
                placeholder="请再次输入"
                required
            />
          </div>

          <div v-if="error" class="text-danger small mb-3">
            {{ error }}
          </div>

          <button
              type="submit"
              :disabled="!formValid || submitting"
              class="btn custom-btn w-100 mb-3 animate__animated animate__pulse animate__delay-1s"
          >
            <span v-if="submitting" class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
            {{ submitting ? '保存中...' : '保存新密码' }}
          </button>
        </form>

        <div class="text-center mt-3">
          <a href="#" class="text-decoration-none" @click.prevent="$router.push('/login')">← 返回登录</a>
        </div>
        <AccountFooter />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import AccountService from '@/services/account.services.js'
import LogoHeader from "@/components/common/LogoHeader.vue";
import AccountFooter from "@/components/layout/AccountFooter.vue";

const route = useRoute()
const router = useRouter()

// URL 参数
const uid = ref(route.params.uid)
const token = ref(route.params.token)

// 页面状态
const loading = ref(true)
const validLink = ref(false)
const submitting = ref(false)
const error = ref('')

// 表单数据
const password = ref('')
const confirmPassword = ref('')
const formValid = ref(false)

// 检查链接有效性
onMounted(async () => {
  if (!uid.value || !token.value) {
    loading.value = false
    return
  }

  try {
    const res = await AccountService.validatePasswordResetToken(uid.value, token.value)
    validLink.value = res.valid
  } catch (err) {
    console.error('验证失败:', err)
  } finally {
    loading.value = false
  }
})

// 实时校验表单
const validateForm = () => {
  if (password.value.length < 8) {
    error.value = '密码至少 8 位'
    formValid.value = false
    return
  }
  if (password.value !== confirmPassword.value) {
    error.value = '两次输入不一致'
    formValid.value = false
    return
  }
  error.value = ''
  formValid.value = true
}

// 监听密码输入变化以实时验证
watch([password, confirmPassword], () => {
  validateForm()
})

// 提交新密码
const submitNewPassword = async () => {
  validateForm()
  if (!formValid.value) return

  submitting.value = true
  try {
    await AccountService.resetPassword(uid.value, token.value, password.value)

    alert('密码已重置，请使用新密码登录')
    router.push('/login')
  } catch (err) {
    const msg = err.response?.data?.message || '重置失败，请重新申请'
    error.value = msg
  } finally {
    submitting.value = false
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

/* 自定义输入框样式 */
.custom-input {
  padding: 0.75rem 1rem;
  border: 2px solid #e1e5eb;
  border-radius: 8px;
  transition: all 0.3s ease;
  background-color: #fff;
  font-size: 1rem;
}

.custom-input:focus {
  border-color: #667eea;
  box-shadow: 0 0 0 0.25rem rgba(102, 126, 234, 0.25);
  outline: 0;
}

/* 自定义主要按钮样式 */
.custom-btn {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border: none;
  color: white;
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  border-radius: 8px;
  transition: all 0.3s ease;
  font-weight: 500;
  letter-spacing: 1px;
}

.custom-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.custom-btn:active:not(:disabled) {
  transform: translateY(0);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.custom-btn:disabled {
  opacity: 0.65;
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
}

/* 自定义次要按钮样式 */
.custom-secondary-btn {
  background-color: #6c757d;
  border-color: #6c757d;
  color: white;
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  border-radius: 8px;
  transition: all 0.3s ease;
  font-weight: 500;
  letter-spacing: 1px;
}

.custom-secondary-btn:hover:not(:disabled) {
  background-color: #5c636a;
  border-color: #565e64;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.custom-secondary-btn:active:not(:disabled) {
  background-color: #565e64;
  border-color: #51585e;
  transform: translateY(0);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.custom-secondary-btn:disabled {
  background-color: #6c757d;
  border-color: #6c757d;
  opacity: 0.65;
  cursor: not-allowed;
}
</style>