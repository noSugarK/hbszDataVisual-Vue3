<template>
  <div class="devhub-container">
    <!-- 头部导航 -->
    <AppHeader />

    <!-- 主要内容区域 -->
    <main class="main-content">
      <!-- 侧边栏 -->
      <aside class="sidebar">
        <div class="sidebar-header">
          <h3>前端技术</h3>
          <p>探索前端开发的最新趋势和最佳实践</p>
          <button class="follow-btn">关注</button>
        </div>

        <!-- 二级导航 - 技术栈过滤 -->
        <div class="tech-filters-container">
          <h4 class="filters-title">全部内容</h4>
          <div class="tech-filters">
            <button
                v-for="tech in techFilters"
                :key="tech"
                :class="['filter-btn', { active: activeTech === tech }]"
                @click="setActiveTech(tech)"
            >
              {{ tech }}
            </button>
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

      <!-- 内容区 -->
      <div class="content-area">
        <!-- 移动端二级导航（仅在小屏幕显示） -->
        <div v-if="isMobile" class="mobile-filters">
          <div class="tech-filters">
            <button
                v-for="tech in techFilters"
                :key="tech"
                :class="['filter-btn', { active: activeTech === tech }]"
                @click="setActiveTech(tech)"
            >
              {{ tech }}
            </button>
          </div>
        </div>

        <!-- 文章列表 -->
        <div class="articles-container">
          <article v-for="(post, index) in filteredArticles" :key="index" class="article-card">
            <h2 class="article-title">{{ post.title }}</h2>
            <p class="article-excerpt">{{ post.excerpt }}</p>
            <div class="article-meta">
              <span class="author">{{ post.author }}</span>
              <span class="views">{{ post.views }}k</span>
              <span class="comments">{{ post.comments }} 评论</span>
              <span class="likes">{{ post.likes }} 点赞</span>
            </div>
          </article>
        </div>

        <!-- 加载更多 -->
        <div class="load-more">
          <button @click="loadMore">加载更多</button>
        </div>
      </div>
    </main>

    <!-- 页脚 -->
    <AppFooter />
  </div>
</template>

<script>
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'
import AppHeader from "@/components/layout/AppHeader.vue";
import AppFooter from "@/components/layout/AppFooter.vue";

export default {
  name: 'DevHub',
  components: {AppFooter, AppHeader},
  setup() {
    // 导航数据
    const mainNav = ['推荐', '关注', '热门', '话题', '发布内容']
    const activeNav = ref('推荐')
    const mobileMenuOpen = ref(false)

    // 技术栈过滤
    const techFilters = ['全部', 'React', 'Vue', 'Angular', 'JavaScript', 'CSS', 'HTML', 'TypeScript', '构建工具']
    const activeTech = ref('全部')

    // 热门标签
    const hotTags = ['Webpack', 'Vite', 'Next.js', 'CSS3', '性能优化']

    // 文章数据
    const articles = [
      {
        title: 'React 18 新特性全解析及迁移指南',
        excerpt: '本文详细介绍了React 18中的并发特性、自动批处理、过渡API等新功能，以及如何平滑迁移现有项目至React 18。',
        author: '前端开发笔记',
        views: 2.4,
        comments: 36,
        likes: 128
      },
      {
        title: 'Vue 3 组件设计模式与最佳实践',
        excerpt: '从基础组件到复杂业务组件，详解Vue 3中组件设计的各种模式，包括组合式API的使用技巧和性能优化方法。',
        author: 'Vue技术栈',
        views: 3.1,
        comments: 52,
        likes: 215
      },
      {
        title: '2023年必学的CSS新特性与技巧',
        excerpt: '介绍容器查询、:has()伪类、ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddCSS嵌套等最新CSS特性，以及如何在实际项目中应用这些特性提升开发效率。',
        author: 'CSS魔法师',
        views: 1.8,
        comments: 28,
        likes: 96
      },
      {
        title: '2023年必学的CSS新特性与技巧',
        excerpt: '介绍容器查询、:has()伪类、CSS嵌套等最新CSS特性，以及如何在实际项目中应用这些特性提升开发效率。',
        author: 'CSS魔法师',
        views: 1.8,
        comments: 28,
        likes: 96
      },
      {
        title: '2023年必学的CSS新特性与技巧',
        excerpt: '介绍容器查询、:has()伪类、CSS嵌套等最新CSS特性，以及如何在实际项目中应用这些特性提升开发效率。',
        author: 'CSS魔法师',
        views: 1.8,
        comments: 28,
        likes: 96
      },
      {
        title: '2023年必学的CSS新特性与技巧',
        excerpt: '介绍容器查询、:has()伪类、CSS嵌套等最新CSS特性，以及如何在实际项目中应用这些特性提升开发效率。',
        author: 'CSS魔法师',
        views: 1.8,
        comments: 28,
        likes: 96
      },
      {
        title: '2023年必学的CSS新特性与技巧',
        excerpt: '介绍容器查询、:has()伪类、CSS嵌套等最新CSS特性，以及如何在实际项目中应用这些特性提升开发效率。',
        author: 'CSS魔法师',
        views: 1.8,
        comments: 28,
        likes: 96
      },
      {
        title: '2023年必学的CSS新特性与技巧',
        excerpt: '介绍容器查询、:has()伪类、CSS嵌套等最新CSS特性，以及如何在实际项目中应用这些特性提升开发效率。',
        author: 'CSS魔法师',
        views: 1.8,
        comments: 28,
        likes: 96
      },
      {
        title: '2023年必学的CSS新特性与技巧',
        excerpt: '介绍容器查询、:has()伪类、CSS嵌套等最新CSS特性，以及如何在实际项目中应用这些特性提升开发效率。',
        author: 'CSS魔法师',
        views: 1.8,
        comments: 28,
        likes: 96
      },
      {
        title: '2023年必学的CSS新特性与技巧',
        excerpt: '介绍容器查询、:has()伪类、CSS嵌套等最新CSS特性，以及如何在实际项目中应用这些特性提升开发效率。',
        author: 'CSS魔法师',
        views: 1.8,
        comments: 28,
        likes: 96
      },
      {
        title: 'TypeScript高级类型与实战技巧',
        excerpt: '深入探讨TypeScript中的高级类型特性，包括条件类型、映射类型和类型守卫，以及在大型项目中的最佳实践。',
        author: 'TS爱好者',
        views: 2.7,
        comments: 42,
        likes: 156
      }
    ]

    // 计算属性 - 过滤文章
    const filteredArticles = computed(() => {
      if (activeTech.value === '全部') {
        return articles
      }
      // 这里可以根据技术栈过滤，示例中所有文章都显示
      return articles
    })

    // 移动端状态
    const isMobile = ref(false)

    // 方法
    const setActiveNav = (nav) => {
      activeNav.value = nav
    }

    const setActiveTech = (tech) => {
      activeTech.value = tech
    }

    const toggleMobileMenu = () => {
      mobileMenuOpen.value = !mobileMenuOpen.value
    }

    const selectMobileNav = (nav) => {
      activeNav.value = nav
      mobileMenuOpen.value = false
    }

    const loadMore = () => {
      // 模拟加载更多内容
      console.log('加载更多内容...')
    }

    // 响应式处理
    const checkScreenSize = () => {
      isMobile.value = window.innerWidth < 768
    }

    onMounted(() => {
      checkScreenSize()
      window.addEventListener('resize', checkScreenSize)
    })

    onBeforeUnmount(() => {
      window.removeEventListener('resize', checkScreenSize)
    })

    return {
      mainNav,
      activeNav,
      mobileMenuOpen,
      techFilters,
      activeTech,
      hotTags,
      filteredArticles,
      isMobile,
      setActiveNav,
      setActiveTech,
      toggleMobileMenu,
      selectMobileNav,
      loadMore
    }
  }
}
</script>

<style scoped>
/* 基础样式重置 */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  line-height: 1.6;
  color: #333;
  background-color: #f8f9fa;
}

/* 全局容器 */
.devhub-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.logo h1 {
  font-size: 1.5rem;
  font-weight: 600;
  color: #1a73e8;
}

.logo span {
  font-size: 0.75rem;
  color: #5f6368;
  margin-top: 2px;
}

/* 桌面端导航 */
.nav-desktop {
  display: flex;
  list-style: none;
}

.nav-desktop .nav-list li {
  padding: 0 15px;
  cursor: pointer;
  font-size: 0.9rem;
  font-weight: 500;
  color: #5f6368;
  transition: color 0.2s ease;
  height: 60px;
  display: flex;
  align-items: center;
}

.nav-desktop .nav-list li:hover {
  color: #1a73e8;
}

.nav-desktop .nav-list li.active {
  color: #1a73e8;
  border-bottom: 2px solid #1a73e8;
}

.menu-icon span {
  width: 100%;
  height: 3px;
  background-color: #333;
  margin: 3px 0;
  transition: 0.3s;
  border-radius: 2px;
}

/* 移动端导航 */

.nav-mobile{
  list-style: none;
  padding: 10px 0;
}

.nav-mobile .nav-list li {
  padding: 12px 20px;
  cursor: pointer;
  font-size: 1rem;
  color: #5f6368;
  border-bottom: 1px solid #f0f0f0;
}

.nav-mobile .nav-list li:last-child {
  border-bottom: none;
}

.nav-mobile .nav-list li:hover,
.nav-mobile .nav-list li.active {
  background-color: #f5f5f5;
  color: #1a73e8;
}

/* 主要内容区域 */
.main-content {
  max-width: 1500px;
  margin: 0 auto;
  padding: 20px;
  display: flex;
  flex: 1;
  gap: 20px;
}

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

/* 内容区 */
.content-area {
  flex: 1;
}

/* 移动端二级导航 */
.mobile-filters {
  display: none;
  background-color: white;
  border-radius: 8px;
  padding: 15px 20px;
  margin-bottom: 20px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  margin: 0 -20px 20px -20px;
}

.mobile-filters .tech-filters {
  flex-direction: row;
  flex-wrap: auto;
  overflow-x: auto;
  padding-bottom: 5px;
  white-space: nowrap;
}

.mobile-filters .filter-btn {
  flex-shrink: 0;
}

/* 文章卡片 */
.articles-container {
  display: grid;
  gap: 20px;
}

.article-card {
  background-color: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.article-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.article-title {
  font-size: 1.3rem;
  font-weight: 600;
  margin-bottom: 10px;
  color: #1a73e8;
  cursor: pointer;
}

.article-title:hover {
  text-decoration: underline;
}

.article-excerpt {
  font-size: 0.95rem;
  color: #5f6368;
  line-height: 1.5;
  margin-bottom: 15px;
}

.article-meta {
  display: flex;
  gap: 15px;
  font-size: 0.85rem;
  color: #5f6368;
}

.article-meta .author {
  font-weight: 500;
  color: #333;
}

/* 加载更多 */
.load-more {
  text-align: center;
  margin-top: 30px;
  margin-bottom: 40px;
}

.load-more button {
  background-color: #f0f2f5;
  color: #5f6368;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  font-size: 0.9rem;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.load-more button:hover {
  background-color: #e0e2e5;
}

/* 页脚 */
.footer {
  text-align: center;
  padding: 20px;
  color: #5f6368;
  font-size: 0.85rem;
  margin-top: auto;
}

/* 响应式设计 */
@media (max-width: 1024px) {
  .main-content {
    flex-direction: row;
  }

  .sidebar {
    width: 200px; /* 在中等屏幕上更窄一些 */
  }

  .content-area {
    width: calc(100% - 220px); /* 内容区占剩余宽度 */
    min-width: 0;
  }
}

@media (max-width: 768px) {

  /* 显示移动端二级导航 */
  .mobile-filters {
    display: block;
  }

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

  /* 内容区全宽 */
  .content-area {
    padding: 0 20px;
    width: 100%;
  }
}

@media (max-width: 480px) {

  .logo h1 {
    font-size: 1.3rem;
  }

  .logo span {
    font-size: 0.7rem;
  }

  .article-card {
    padding: 15px;
  }

  .article-title {
    font-size: 1.05rem;
  }

  .article-excerpt {
    font-size: 0.9rem;
  }

  .article-meta {
    gap: 10px;
    font-size: 0.8rem;
  }

  .mobile-filters {
    margin: 0 -15px 20px -15px;
  }
}

/* 滑动动画 */
.slide-enter-active, .slide-leave-active {
  transition: transform 0.3s ease;
}

.slide-enter-from, .slide-leave-to {
  transform: translateX(100%);
}

/* 深色模式支持（可选） */
@media (prefers-color-scheme: dark) {
  body {
    background-color: #121212;
    color: #e0e0e0;
  }

  .header, .sidebar, .content-area, .article-card {
    background-color: #1f1f1f;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
  }

  .sidebar {
    background-color: #1a1a1a; /* 深色背景 */
  }

  .sidebar-header {
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
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

  .article-title {
    color: #9acafa;
  }

  .article-meta, .article-meta .author {
    color: #b0b0b0;
  }

  .footer {
    color: #b0b0b0;
  }
}
</style>
