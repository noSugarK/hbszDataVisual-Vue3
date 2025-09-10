<template>
  <div class="d-flex justify-content-center align-items-end" style="min-height: 7vh;">
    <div class="text-center mb-4 animate__animated animate__fadeInDown">
      <img
          :src="logoSrc"
          alt="Logo"
          class="login-logo img-fluid"
      />
    </div>
  </div>
</template>

<script setup>
defineProps({
  logoSrc: {
    type: String,
    default: '/images/logo.png'
  },
})
</script>

<style scoped>
.login-logo {
  width: 200px;
  height: auto;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.05); }
  100% { transform: scale(1); }
}
</style>
