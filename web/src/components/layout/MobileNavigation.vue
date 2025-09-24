<template>
  <div class="mobile-filters" v-if="isMobile">
    <div class="d-flex overflow-auto gap-2 pb-2">
      <router-link to="/projects" class="btn mobile-nav-btn flex-shrink-0" active-class="mobile-nav-btn-active" exact>项目</router-link>
      <router-link to="/orders" class="btn mobile-nav-btn flex-shrink-0" active-class="mobile-nav-btn-active">订单</router-link>
      <router-link to="/region" class="btn mobile-nav-btn flex-shrink-0" active-class="mobile-nav-btn-active">区域</router-link>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, onBeforeUnmount } from 'vue'

export default {
  name: 'MobileNavigation',
  setup() {
    const isMobile = ref(false)

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
      isMobile
    }
  }
}
</script>

<style scoped>
/* 移动端二级导航 */
.mobile-filters {
  background-color: white;
  border-radius: 8px;
  padding: 15px 20px;
  margin-bottom: 20px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  margin: 0 0 20px 0;
  width: 100%;
}


/* 移动端导航按钮 */
.mobile-nav-btn {
  background-color: #f8f9fa;
  color: #495057;
  border: 1px solid #e9ecef;
  padding: 0.375rem 0.75rem;
  font-size: 0.875rem;
  transition: all 0.2s ease-in-out;
}

.mobile-nav-btn:hover {
  background-color: #e9ecef;
  color: #0d6efd;
  border-color: #0d6efd;
}

.mobile-nav-btn-active {
  background-color: #0d6efd;
  color: white !important;
  border-color: #0d6efd;
}

.mobile-nav-btn-active:hover {
  background-color: #0b5ed7;
  border-color: #0a58ca;
}

/* 深色模式支持 */
@media (prefers-color-scheme: dark) {
  .mobile-filters {
    background-color: #2d3748;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
  }

  .mobile-nav-btn {
    background-color: #4a5568;
    color: #e2e8f0;
    border-color: #718096;
  }

  .mobile-nav-btn:hover {
    background-color: #718096;
    color: #63b3ed;
    border-color: #63b3ed;
  }

  .mobile-nav-btn-active {
    background-color: #3182ce;
    border-color: #3182ce;
  }
}
</style>
