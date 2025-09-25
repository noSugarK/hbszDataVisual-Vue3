<template>
  <AppHeader />
  <main class="main-content">
    <SidebarNavigation class="d-none d-md-block" />
    <div class="content-area">
      <MobileNavigation />
      <div class="page-header d-flex justify-content-between align-items-center mb-4">
        <h1 class="h3 mb-0">信息管理</h1>
        <button class="btn btn-primary" @click="showCreateForm">
          <i class="bi bi-plus-circle me-1"></i>添加信息
        </button>
      </div>
    </div>
  </main>
  <AppFooter />
</template>

<script>
</script>

<style scoped>
.main-content {
  max-width: 1500px;
  margin: 0 auto;
  padding: 20px;
  display: flex;
  flex: 1;
  gap: 20px;
}

.content-area {
  flex: 1;
  transition: filter 0.3s ease;
  position: relative;
}

@media (max-width: 1024px) {
  .main-content { flex-direction: column; }
  .content-area { width: 100%; }
}

@media (max-width: 768px) {
  .main-content { padding: 15px; gap: 15px; }
  .page-header { flex-direction: column; align-items: flex-start; gap: 15px; }
}
</style>