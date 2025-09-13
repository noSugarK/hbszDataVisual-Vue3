<!-- src/components/layout/MobileNavigation.vue -->
<template>
  <div class="mobile-filters">
    <div class="tech-filters">
      <router-link to="/projects" class="filter-btn" active-class="active" exact>项目</router-link>
      <router-link to="/orders" class="filter-btn" active-class="active">订单</router-link>
      <router-link to="/region" class="filter-btn" active-class="active">区域</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MobileNavigation'
}
</script>

<style scoped>
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
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  overflow-x: auto;
  padding-bottom: 5px;
  white-space: nowrap;
  gap: 5px;
}

.mobile-filters .filter-btn {
  flex-shrink: 0;
  background-color: transparent;
  color: #5f6368;
  border: none;
  padding: 6px 10px;
  border-radius: 4px;
  font-size: 0.85rem;
  cursor: pointer;
  text-align: left;
  transition: all 0.2s ease;
  text-decoration: none;
  display: inline-block;
}

.mobile-filters .filter-btn:hover {
  background-color: #f0f2f5;
  color: #1a73e8;
}

.mobile-filters .filter-btn.active {
  background-color: #f0f2f5;
  color: #1a73e8;
  font-weight: 500;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .mobile-filters {
    display: block;
  }

  .mobile-filters {
    margin: 0 -15px 20px -15px;
  }
}

/* 深色模式支持 */
@media (prefers-color-scheme: dark) {
  .mobile-filters {
    background-color: #1f1f1f;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
  }

  .mobile-filters .filter-btn {
    background-color: #333;
    color: #e0e0e0;
  }

  .mobile-filters .filter-btn:hover {
    background-color: #444;
  }

  .mobile-filters .filter-btn.active {
    background-color: #2a2a2a;
    color: #9acafa;
  }
}
</style>
