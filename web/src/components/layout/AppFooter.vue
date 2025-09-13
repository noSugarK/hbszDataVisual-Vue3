<!-- src/components/layout/AppFooter.vue -->
<template>
  <div class="footer-wrapper">
    <div class="container">
      <footer class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
        <p class="col-md-4 mb-0 text-muted">&copy; 2025 湖北市政集团. All rights reserved.</p>

        <a href="/" class="col-md-4 d-flex align-items-center justify-content-center mb-3 mb-md-0 me-md-auto link-dark text-decoration-none">
          <LogoHeader />
        </a>

        <ul class="nav col-md-4 justify-content-end">
          <li class="nav-item"><a href="#" class="nav-link px-2 text-muted" @click.prevent="$router.push('/')">首页</a></li>
          <li class="nav-item"><a href="#" class="nav-link px-2 text-muted" @click.prevent="$router.push('/about')">关于我们</a></li>
          <li class="nav-item"><a href="#" class="nav-link px-2 text-muted" @click.prevent="$router.push('/contact')">联系我们</a></li>
          <li class="nav-item"><a href="#" class="nav-link px-2 text-muted" @click.prevent="$router.push('/help')">帮助</a></li>
        </ul>
      </footer>
    </div>
  </div>
</template>

<script setup>
import LogoHeader from '../common/LogoHeader.vue'
</script>

<style scoped>
.footer-wrapper {
  width: 100%;
  display: flex;
  justify-content: center;
}

.container {
  max-width: 1400px;
}

.logo :deep(.login-logo) {
  width: 40px;
  height: 32px;
  margin: 0;
}

.logo :deep(h2) {
  display: none;
}

.nav-link {
  cursor: pointer;
}

.nav-link:hover {
  color: #0d6efd !important;
}

.link-dark {
  color: #212529 !important;
}

.link-dark:hover, .link-dark:focus {
  color: #0d6efd !important;
}

.text-muted {
  color: #6c757d !important;
}

.text-muted:hover {
  color: #0d6efd !important;
}
</style>
