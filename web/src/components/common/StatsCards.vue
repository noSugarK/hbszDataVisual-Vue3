<template>
  <div class="stats-cards">
    <div v-for="(stat, index) in stats" :key="index" class="stat-card">
      <div class="stat-value" :style="{ color: stat.color }">{{ stat.value }}</div>
      <div class="stat-label">{{ stat.label }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'StatsCards',
  props: {
    // 接收来自父组件的统计信息数组
    stats: {
      type: Array,
      required: true,
      validator: (value) => {
        return value.every(item =>
            typeof item.value === 'number' &&
            typeof item.label === 'string' &&
            typeof item.color === 'string'
        )
      }
    }
  }
}
</script>

<style scoped>
/* 统计卡片 */
.stats-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.stat-card {
  background-color: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.stat-value {
  font-size: 2rem;
  font-weight: 600;
  margin-bottom: 5px;
}

.stat-label {
  font-size: 0.9rem;
  color: #6c757d;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .stats-cards {
    grid-template-columns: 1fr 1fr;
  }
}

@media (max-width: 480px) {
  .stats-cards {
    grid-template-columns: 1fr;
  }
}
</style>