<!-- src/components/layout/SidebarNavigation.vue -->
<template>
  <aside class="sidebar">
    <div class="sidebar-header">
      <h3>前端技术</h3>
      <p>探索前端开发的最新趋势和最佳实践</p>
      <button class="follow-btn">关注</button>
    </div>

    <!-- 二级导航 - 技术栈过滤（改为路由导航） -->
    <div class="tech-filters-container">
      <h4 class="filters-title">全部内容</h4>
      <div class="tech-filters">
        <router-link to="/projects" class="filter-btn" active-class="active" exact>项目</router-link>
        <router-link to="/orders" class="filter-btn" active-class="active">订单</router-link>
        <router-link to="/region" class="filter-btn" active-class="active">区域</router-link>
      </div>
    </div>

    <!-- 热门标签 -->
    <div class="tags-section">
      <h4>热门标签</h4>
      <div class="tags-container">
        <span v-for="tag in hotTags" :key="tag" class="tag">#{{ tag }}</span>
      </div>
    </div>
  </aside>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'SidebarNavigation',
  setup() {
    // 热门标签
    const hotTags = ref(['Webpack', 'Vite', 'Next.js', 'CSS3', '性能优化'])

    return {
      hotTags
    }
  }
}
</script>

<style scoped>
/* 侧边栏 */
.sidebar {
  width: 250px; /* 设置固定宽度，原来是默认宽度 */
  /* 整体侧边栏粘性定位 */
  position: sticky;
  top: 60px; /* 与顶部导航栏高度一致，确保在其下方 */
  z-index: 80; /* 低于顶部导航栏z-index */
  /* 确保侧边栏有足够高度以触发粘性效果 */
  height: calc(100vh - 60px); /* 视口高度减去顶部导航高度 */
  overflow-y: auto; /* 侧边栏内容过长时可滚动 */
  max-height: calc(100vh - 60px); /* 限制最大高度 */
}

.sidebar-header {
  background-color: white;
  border-radius: 8px;
  padding: 15px;
  margin-bottom: 20px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.sidebar-header h3 {
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 6px;
  color: #1a73e8;
}

.sidebar-header p {
  font-size: 0.85rem;
  color: #5f6368;
  margin-bottom: 12px;
}

.follow-btn {
  background-color: #1a73e8;
  color: white;
  border: none;
  padding: 6px 12px;
  border-radius: 4px;
  font-size: 0.85rem;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.follow-btn:hover {
  background-color: #1557b0;
}

/* 二级导航 - 技术栈过滤 */
.tech-filters-container {
  background-color: white;
  border-radius: 8px;
  padding: 12px 15px;
  margin-bottom: 20px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  width: 100%;
}

.filters-title {
  font-size: 0.95rem;
  font-weight: 600;
  margin-bottom: 10px;
  color: #333;
}

.tech-filters {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.filter-btn {
  background-color: transparent;
  color: #5f6368;
  border: none;
  padding: 6px 10px;
  border-radius: 4px;
  font-size: 0.85rem;
  cursor: pointer;
  text-align: left;
  transition: all 0.2s ease;
  text-decoration: none; /* 移除链接下划线 */
  display: block; /* 使链接表现为块级元素 */
}

.filter-btn:hover {
  background-color: #f0f2f5;
  color: #1a73e8;
}

.filter-btn.active {
  background-color: #f0f2f5;
  color: #1a73e8;
  font-weight: 500;
}

/* 热门标签 */
.tags-section h4 {
  font-size: 0.95rem;
  font-weight: 600;
  margin-bottom: 10px;
  color: #333;
}

.tags-container {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.tag {
  background-color: #f0f2f5;
  color: #5f6368;
  padding: 5px 10px;
  border-radius: 16px;
  font-size: 0.75rem;
  font-weight: 500;
}

.tag:hover {
  background-color: #e0e2e5;
  cursor: pointer;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .sidebar {
    position: static;
    height: auto;
    max-height: none;
    overflow-y: visible;
    display: none;
  }

  /* 小屏仍隐藏桌面端二级导航 */
  .tech-filters-container {
    display: none;
  }

  /* 调整侧边栏间距 */
  .sidebar-header {
    margin-bottom: 0;
  }

  .tags-section {
    margin-top: 20px;
  }
}

/* 深色模式支持（可选） */
@media (prefers-color-scheme: dark) {
  .sidebar {
    background-color: #1a1a1a; /* 深色背景 */
  }

  .sidebar-header {
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
    background-color: #1f1f1f;
  }

  .tech-filters-container {
    background-color: #1f1f1f;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3); /* 增强阴影，与header区分 */
  }

  .tag, .filter-btn {
    background-color: #333;
    color: #e0e0e0;
  }

  .tag:hover, .filter-btn:hover {
    background-color: #444;
  }

  .filter-btn.active {
    background-color: #2a2a2a;
    color: #9acafa;
  }
}
</style>
