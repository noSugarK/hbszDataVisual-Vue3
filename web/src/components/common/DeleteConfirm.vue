<template>
  <Teleport to="body">
    <div v-if="visible" class="delete-confirm-overlay" @click="handleBackdropClick">
      <div class="delete-confirm-modal" @click.stop>
        <!-- 头部 -->
        <div class="delete-confirm-header">
          <h5 class="delete-confirm-title">确认删除</h5>
          <button type="button" class="btn-close" @click="handleCancel"></button>
        </div>

        <!-- 内容 -->
        <div class="delete-confirm-body">
          <p>确定要删除 "{{ itemName }}" 吗？此操作不可撤销。</p>
        </div>

        <!-- 操作按钮 -->
        <div class="delete-confirm-footer">
          <button type="button" class="btn btn-secondary" @click="handleCancel">取消</button>
          <button type="button" class="btn btn-danger" @click="handleConfirm">确定删除</button>
        </div>
      </div>
    </div>
  </Teleport>
</template>

<script>
export default {
  name: 'DeleteConfirm',
  props: {
    visible: {
      type: Boolean,
      default: false
    },
    itemName: {
      type: String,
      default: ''
    }
  },
  emits: ['confirm', 'cancel'],
  methods: {
    handleConfirm() {
      this.$emit('confirm')
    },
    handleCancel() {
      this.$emit('cancel')
    },
    handleBackdropClick() {
      // 可选：点击遮罩是否允许关闭？一般“删除”不建议
      // this.handleCancel()
    }
  }
}
</script>

<style scoped>
.delete-confirm-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  backdrop-filter: blur(1px);
}

.delete-confirm-modal {
  background: white;
  border-radius: 8px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
  width: 400px;
  max-width: 90vw;
  overflow: hidden;
}

.delete-confirm-header {
  padding: 16px 20px;
  border-bottom: 1px solid #e9ecef;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.delete-confirm-title {
  margin: 0;
  font-size: 1.1rem;
  font-weight: 600;
  color: #333;
}

.delete-confirm-body {
  padding: 20px;
  font-size: 0.95rem;
  color: #555;
}

.delete-confirm-footer {
  padding: 16px 20px;
  text-align: right;
  border-top: 1px solid #e9ecef;
  display: flex;
  justify-content: flex-end;
  gap: 8px;
}

.btn-close {
  background: none;
  border: none;
  font-size: 1.25rem;
  color: #6c757d;
  cursor: pointer;
  padding: 0;
  line-height: 1;
}

.btn-close:hover {
  color: #000;
}
</style>