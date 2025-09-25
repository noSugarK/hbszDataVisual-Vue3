<template>
  <aside class="sidebar">
    <div class="card mb-4 sidebar-card">
      <div class="card-body">
        <h5 class="card-title sidebar-title">数据管理</h5>
        <p class="card-text sidebar-subtitle">管理界面，下方为管理界面导航</p>
      </div>
    </div>

    <!-- 二级导航 - 技术栈过滤 -->
    <div class="card mb-4 sidebar-card">
      <div class="card-body">
        <h5 class="card-title sidebar-section-title">全部内容</h5>
        <div class="d-flex flex-column gap-2">
          <router-link to="/projects" class="btn sidebar-nav-btn" active-class="sidebar-nav-btn-active" exact>项目</router-link>
          <router-link to="/orders" class="btn sidebar-nav-btn" active-class="sidebar-nav-btn-active">订单</router-link>
          <router-link to="/region" class="btn sidebar-nav-btn" active-class="sidebar-nav-btn-active">区域</router-link>
          <router-link to="/brand" class="btn sidebar-nav-btn" active-class="sidebar-nav-btn-active">品牌</router-link>
          <router-link to="/category" class="btn sidebar-nav-btn" active-class="sidebar-nav-btn-active">物资</router-link>
          <router-link to="/supplier" class="btn sidebar-nav-btn" active-class="sidebar-nav-btn-active">供应商</router-link>
        </div>
      </div>
    </div>

    <!-- 近期项目 -->
    <div class="card sidebar-card">
      <div class="card-body">
        <h5 class="card-title sidebar-section-title">近期项目</h5>
        <div class="d-flex flex-wrap gap-2">
          <span v-for="tag in hotTags" :key="tag" class="badge sidebar-tag">#{{ tag }}</span>
        </div>
      </div>
    </div>
  </aside>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'SidebarNavigation',
  setup() {
    // 近期项目
    const hotTags = ref(['项目1', '项目2', '项目3', '项目4', '项目5'])

    return {
      hotTags
    }
  }
}
</script>

<style scoped>
/* 侧边栏 */
.sidebar {
  width: 250px;
  /* 使用sticky定位使侧边栏跟随滚动 */
  position: sticky;
  top: 20px; /* 距离顶部的距离 */
  z-index: 80;
  /* 设置最大高度并允许内部滚动 */
  max-height: calc(100vh - 40px);
  overflow-y: auto;
  align-self: flex-start; /* 确保在Flex容器中正确对齐 */
}

/* 侧边栏卡片 */
.sidebar-card {
  border: none;
  box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075);
  border-radius: 0.5rem;
}

.sidebar-card:hover {
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
}

/* 标题样式 */
.sidebar-title {
  color: #0d6efd;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.sidebar-section-title {
  color: #212529;
  font-weight: 600;
  margin-bottom: 1rem;
  font-size: 1.1rem;
}

/* 副标题样式 */
.sidebar-subtitle {
  color: #495057;
  font-size: 0.9rem;
  margin-bottom: 0;
}

/* 导航按钮样式 */
.sidebar-nav-btn {
  background-color: #f8f9fa;
  color: #495057;
  border: 1px solid #e9ecef;
  padding: 0.5rem 1rem;
  text-align: left;
  transition: all 0.2s ease-in-out;
  border-radius: 0.375rem;
}

.sidebar-nav-btn:hover {
  background-color: #e9ecef;
  color: #0d6efd;
  border-color: #0d6efd;
  transform: translateX(5px);
}

.sidebar-nav-btn-active {
  background-color: #0d6efd;
  color: white !important;
  border-color: #0d6efd;
}

.sidebar-nav-btn-active:hover {
  background-color: #0b5ed7;
  border-color: #0a58ca;
  transform: translateX(5px);
}

/* 标签样式 */
.sidebar-tag {
  background-color: #e7f1ff;
  color: #0d6efd;
  font-weight: 500;
  padding: 0.5em 0.75em;
  font-size: 0.8rem;
}

.sidebar-tag:hover {
  background-color: #d0e1ff;
  cursor: pointer;
}

/* 响应式设计 - 隐藏桌面端侧边栏在小屏幕设备上 */
@media (max-width: 768px) {
  .sidebar {
    display: none;
  }
}

/* 深色模式支持 */
@media (prefers-color-scheme: dark) {
  .sidebar-card {
    background-color: #2d3748;
    box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.2);
  }

  .sidebar-title {
    color: #63b3ed;
  }

  .sidebar-section-title,
  .sidebar-subtitle {
    color: #e2e8f0;
  }

  .sidebar-nav-btn {
    background-color: #4a5568;
    color: #e2e8f0;
    border-color: #718096;
  }

  .sidebar-nav-btn:hover {
    background-color: #718096;
    color: #63b3ed;
    border-color: #63b3ed;
  }

  .sidebar-nav-btn-active {
    background-color: #3182ce;
    border-color: #3182ce;
  }

  .sidebar-tag {
    background-color: #2c5282;
    color: #90cdf4;
  }

  .sidebar-tag:hover {
    background-color: #3182ce;
  }
}
</style>
