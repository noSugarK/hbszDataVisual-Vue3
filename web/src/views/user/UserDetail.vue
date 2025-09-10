<template>
  <AppHeader />
  <div class="user-detail-container">
    <el-card class="detail-card">
      <template #header>
        <div class="card-header">
          <span>用户详情</span>
          <el-button @click="goBack">返回</el-button>
        </div>
      </template>

      <el-skeleton :loading="loading" animated>
        <template #template>
          <el-descriptions :column="1" border>
            <el-descriptions-item label="用户名">
              <el-skeleton-item variant="text" style="width: 30%" />
            </el-descriptions-item>
            <el-descriptions-item label="姓名">
              <el-skeleton-item variant="text" style="width: 30%" />
            </el-descriptions-item>
            <el-descriptions-item label="邮箱">
              <el-skeleton-item variant="text" style="width: 50%" />
            </el-descriptions-item>
            <el-descriptions-item label="手机号">
              <el-skeleton-item variant="text" style="width: 30%" />
            </el-descriptions-item>
            <el-descriptions-item label="用户类型">
              <el-skeleton-item variant="text" style="width: 20%" />
            </el-descriptions-item>
            <el-descriptions-item label="账户状态">
              <el-skeleton-item variant="text" style="width: 20%" />
            </el-descriptions-item>
            <el-descriptions-item label="创建时间">
              <el-skeleton-item variant="text" style="width: 40%" />
            </el-descriptions-item>
            <el-descriptions-item label="最后登录">
              <el-skeleton-item variant="text" style="width: 40%" />
            </el-descriptions-item>
            <el-descriptions-item label="创建者">
              <el-skeleton-item variant="text" style="width: 30%" />
            </el-descriptions-item>
          </el-descriptions>
        </template>

        <template #default>
          <div v-if="user">
            <UserInfo :user="user" :show-creator="true" />
          </div>
        </template>
      </el-skeleton>
    </el-card>
  </div>
  <AppFooter />
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import UserService from '@/services/user.service.js'
import { ElMessage } from 'element-plus'
import AppHeader from '@/components/layout/AppHeader.vue'
import AppFooter from '@/components/layout/AppFooter.vue'
import UserInfo from '@/components/user/UserInfo.vue'

const route = useRoute()
const router = useRouter()

const loading = ref(false)
const user = ref(null)

const userId = route.params.id

// 获取用户详情
const loadUserDetail = async () => {
  if (!userId) {
    ElMessage.error('用户ID无效')
    router.push('/users')
    return
  }

  loading.value = true
  try {
    const data = await UserService.getUserDetail(userId)
    user.value = data
  } catch (error) {
    ElMessage.error(error.message || '获取用户详情失败')
    router.push('/users')
  } finally {
    loading.value = false
  }
}

// 返回上一页
const goBack = () => {
  router.go(-1)
}

onMounted(() => {
  loadUserDetail()
})
</script>

<style scoped>
.user-detail-container {
  padding: 20px;
  max-width: 800px;
  margin: 0 auto;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.detail-card {
  margin-bottom: 20px;
}
</style>