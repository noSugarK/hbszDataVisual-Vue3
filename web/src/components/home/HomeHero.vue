<template>
  <div class="hero-background">
    <div class="container col-xxl-8 px-4 py-5">
      <div class="row flex-lg-row-reverse align-items-center g-5 py-5">
        <div class="col-10 col-sm-8 col-lg-6">
          <img :src="heroImage" class="d-block mx-lg-auto img-fluid hero-image" alt="数据可视化" width="700" height="500" loading="lazy">
        </div>
        <div class="col-lg-6">
          <h1 class="display-5 fw-bold lh-1 mb-3">数据可视化平台</h1>
          <p class="lead">
            将复杂的数据转化为直观的图表和仪表板，帮助您更好地理解业务状况，
            发现数据中的趋势和洞察，为决策提供有力支持。
          </p>
          <div class="d-grid gap-2 d-md-flex justify-content-md-start">
            <button type="button" class="btn btn-primary btn-lg px-4 me-md-2" @click="goToLogin">
              立即开始
            </button>
            <button type="button" class="btn btn-outline-secondary btn-lg px-4" @click="learnMore">
              了解更多
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.hero-background {
  background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
}

.hero-image {
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
  border-radius: 0.5rem;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.hero-image:hover {
  transform: translateY(-5px);
  box-shadow: 0 1rem 2rem rgba(0, 0, 0, 0.2);
}

@media (max-width: 992px) {
  .hero-background {
    padding: 2rem 0;
  }
}
</style>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

// 使用logo图片作为英雄图片
const heroImage = "/images/logo.png"

const goToLogin = () => {
  router.push('/login')
}

const learnMore = () => {
  // 滚动到页面中的功能介绍部分
  const element = document.querySelector('.marketing')
  if (element) {
    element.scrollIntoView({ behavior: 'smooth' })
  }
}
</script>