<template>
  <div class="features-section py-5 bg-light">
    <div class="container">
      <div class="row mb-5">
        <div class="col-lg-8 mx-auto text-center">
          <h2 class="display-5 fw-bold mb-3">核心功能</h2>
          <p class="lead text-muted">
            我们提供全面的数据可视化解决方案，帮助您更好地理解和展示数据
          </p>
        </div>
      </div>
      
      <div class="row g-4">
        <div class="col-md-6 col-lg-4" v-for="(feature, index) in features" :key="index">
          <div class="card h-100 border-0 shadow-sm hover-effect">
            <div class="card-body text-center p-4">
              <div class="feature-icon bg-primary bg-opacity-10 text-primary rounded-circle mx-auto mb-4 d-flex align-items-center justify-content-center" style="width: 80px; height: 80px;">
                <i :class="feature.icon" style="font-size: 2rem;"></i>
              </div>
              <h5 class="card-title fw-bold mb-3">{{ feature.title }}</h5>
              <p class="card-text text-muted">{{ feature.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.hover-effect {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.hover-effect:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
}

.feature-icon {
  transition: transform 0.3s ease;
}

.hover-effect:hover .feature-icon {
  transform: scale(1.1);
}
</style>

<script setup>
const features = [
  {
    icon: 'bi bi-bar-chart-line',
    title: '丰富图表类型',
    description: '支持柱状图、折线图、饼图、散点图等多种图表类型，满足各种数据展示需求。'
  },
  {
    icon: 'bi bi-lightning',
    title: '实时数据',
    description: '实时监控关键业务指标，及时发现数据异常，为决策提供有力支持。'
  },
  {
    icon: 'bi bi-phone',
    title: '响应式设计',
    description: '完美适配各种设备屏幕，无论是桌面端还是移动端都能获得最佳体验。'
  },
  {
    icon: 'bi bi-shield-lock',
    title: '安全保障',
    description: '采用先进的加密技术，确保您的数据安全，保护您的隐私。'
  },
  {
    icon: 'bi bi-cloud-arrow-up',
    title: '云端同步',
    description: '数据云端存储，随时随地访问您的可视化项目，永不丢失。'
  },
  {
    icon: 'bi bi-share',
    title: '轻松分享',
    description: '一键分享您的可视化成果，支持多种格式导出，便于协作和展示。'
  }
]
</script>