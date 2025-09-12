<template>
  <header class="app-header">
    <div class="container">
      <div class="d-flex flex-wrap align-items-center justify-content-center py-2 mb-3 border-bottom">
        <a href="/" class="d-flex align-items-center me-md-auto text-dark text-decoration-none">
          <LogoHeader />
        </a>

        <ul class="nav nav-pills">
          <li class="nav-item"><a href="#" class="nav-link" :class="{ active: isActive('/') }" @click.prevent="goTo('/')">首页</a></li>
          <li class="nav-item"><a href="#" class="nav-link" :class="{ active: isActive('/projects') }" @click.prevent="goTo('/projects')">项目管理</a></li>
          <li class="nav-item"><a href="#" class="nav-link" :class="{ active: isActive('/visualizations') }" @click.prevent="goTo('/visualizations')">可视化</a></li>
          <li class="nav-item"><a href="#" class="nav-link" :class="{ active: isActive('/reports') }" @click.prevent="goTo('/reports')">报表</a></li>
          <li class="nav-item"><a href="#" class="nav-link" :class="{ active: isActive('/analytics') }" @click.prevent="goTo('/analytics')">数据分析</a></li>
        </ul>

        <div class="d-flex align-items-center ms-md-auto" v-if="accountStore.isAuthenticated">
          <el-dropdown @command="handleUserCommand">
            <span class="el-dropdown-link nav-link px-2 link-dark">
              {{ accountStore.user?.username }}
              <el-icon class="el-icon--right">
                <arrow-down />
              </el-icon>
            </span>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item command="profile">个人中心</el-dropdown-item>
                <el-dropdown-item command="profile-edit">修改信息</el-dropdown-item>
                <el-dropdown-item command="user-list" v-if="accountStore.user?.is_staff || accountStore.user?.is_superuser">用户列表</el-dropdown-item>
                <el-dropdown-item divided command="logout">退出登录</el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </div>
        <div class="d-flex align-items-center ms-md-auto" v-else>
          <button type="button" class="btn btn-outline-primary me-2" @click="$router.push('/login')">登录</button>
          <button type="button" class="btn btn-primary" @click="$router.push('/register')">注册</button>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router';
import { useAccountStore } from '@/stores/account.js';
import { ArrowDown } from '@element-plus/icons-vue';
import LogoHeader from '../common/LogoHeader.vue';

const route = useRoute();
const router = useRouter();
const accountStore = useAccountStore();

const goTo = (path) => {
  router.push(path);
};

const isActive = (path) => {
  return route.path === path;
};

const handleUserCommand = (command) => {
  switch (command) {
    case 'logout':
      accountStore.clear();
      router.push('/login');
      break;
    case 'profile':
      router.push('/profile');
      break;
    case 'profile-edit':
      router.push('/profile/edit');
      break;
    case 'settings':
      router.push('/settings');
      break;
    case 'help':
      console.log('打开帮助文档');
      break;
    case 'user-list':
      router.push('/users');
      break;
  }
};
</script>

<style scoped>
.app-header {
  background-color: #ffffff;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.1);
  padding: 0;
  z-index: 1000;
}

.logo :deep(.login-logo) {
  width: 36px;
  height: 30px;
  margin: 0;
}

.logo :deep(h2) {
  display: none;
}

.nav-link {
  cursor: pointer;
  font-size: 1rem;
  font-weight: 500;
}

.nav-link:hover {
  color: #0d6efd !important;
}

.nav-link.active {
  color: #fff !important;
  background-color: #0d6efd !important;
}

.link-dark {
  color: #212529 !important;
}

.link-dark:hover, .link-dark:focus {
  color: #0d6efd !important;
}

.el-dropdown-link {
  cursor: pointer;
  display: flex;
  align-items: center;
  font-size: 1rem;
  font-weight: 500;
}

.btn-outline-primary {
  color: #0d6efd;
  border-color: #0d6efd;
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
}

.btn-outline-primary:hover {
  color: #fff;
  background-color: #0d6efd;
  border-color: #0d6efd;
}

.btn-primary {
  color: #fff;
  background-color: #0d6efd;
  border-color: #0d6efd;
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
}

.btn-primary:hover {
  color: #fff;
  background-color: #0b5ed7;
  border-color: #0a58ca;
}
</style>
