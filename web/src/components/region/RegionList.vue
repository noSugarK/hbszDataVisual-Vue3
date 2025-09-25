<template>
  <div class="region-management">
    <h2 class="fs-4 fw-bold mb-4 text-primary">区域列表</h2>

    <!-- 加载状态 -->
    <div v-if="loading" class="text-center py-5">
      <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">加载中...</span>
      </div>
      <p class="mt-2 text-muted">正在加载区域数据...</p>
    </div>

    <!-- 错误状态 -->
    <div v-else-if="error" class="alert alert-danger d-flex justify-content-between align-items-center">
      {{ error }}
      <button @click="fetchRegions" class="btn btn-sm btn-outline-danger">重试</button>
    </div>

    <!-- 表格 -->
    <div v-else class="table-responsive">
      <table class="table table-hover align-middle region-table">
        <thead class="table-light">
        <tr>
          <th style="width: 50%">区域名称</th>
          <th style="width: 30%">关联项目数量</th>
          <th style="width: 20%">操作</th>
        </tr>
        </thead>
        <tbody>
        <template v-for="city in regions" :key="city.id">
          <!-- 市级节点 -->
          <tr>
            <td>
              <div class="d-flex align-items-center tree-cell">
                <i
                    v-if="city.children?.length"
                    class="bi"
                    :class="expanded.has(city.id) ? 'bi-chevron-down' : 'bi-chevron-right'"
                    style="cursor: pointer; font-size: 0.9em; margin-right: 8px"
                    @click="toggleExpand(city.id)"
                ></i>
                <span class="fw-medium text-primary">{{ city.name }}</span>
              </div>
            </td>
            <td>
              <span class="badge bg-primary bg-opacity-10 text-primary">{{ city.projectCount || 0 }}</span>
            </td>
            <td>
              <div class="btn-group btn-group-sm" role="group">
                <button class="btn btn-outline-primary" @click="showDetail(city.id)">查看</button>
                <button class="btn btn-outline-secondary" @click="showEditForm(city)">编辑</button>
              </div>
            </td>
          </tr>

          <!-- 区/县节点 -->
          <tr
              v-for="district in city.children"
              :key="district.id"
              v-show="expanded.has(city.id)"
              class="tree-child-row"
          >
            <td>
              <div class="d-flex align-items-center" style="position: relative; padding-left: 32px">
                <div
                    class="position-absolute"
                    style="left: 16px; top: 0; bottom: 0; width: 1px; background-color: #dee2e6"
                ></div>
                <div
                    class="position-absolute"
                    style="left: 13px; top: 50%; transform: translateY(-50%); width: 6px; height: 6px; background: #0d6efd; border-radius: 50%"
                ></div>
                <span class="text-dark">{{ district.name }}</span>
              </div>
            </td>
            <td>
              <span class="badge bg-secondary bg-opacity-10 text-secondary">{{ district.projectCount || 0 }}</span>
            </td>
            <td>
              <div class="btn-group btn-group-sm" role="group">
                <button class="btn btn-outline-primary" @click="showDetail(district.id)">查看</button>
                <button class="btn btn-outline-secondary" @click="showEditForm(district)">编辑</button>
                <button
                    @click="$emit('delete-region', district)"
                    class="btn btn-outline-danger"
                >
                  <i class="bi bi-trash"></i> 删除
                </button>
              </div>
            </td>
          </tr>
        </template>
        </tbody>
      </table>

      <!-- 空数据 -->
      <div v-if="regions.length === 0" class="text-center text-muted py-4">
        暂无区域数据
      </div>
    </div>

    <teleport to="body">
      <RegionForm
          v-if="showFormModal"
          :visible="showFormModal"
          :form-type="formType"
          :region-data="currentRegion"
          @close="handleFormClose"
          @success="handleFormSuccess"
      />
    </teleport>

    <teleport to="body">
      <RegionDetail
          v-if="showDetailModal"
          :visible="showDetailModal"
          :region-id="currentRegionId"
          @close="handleDetailClose"
      />
    </teleport>
  </div>
</template>

<script>
import RegionService from '@/api/region.api.js';
import RegionForm from '@/components/region/RegionForm.vue'
import RegionDetail from '@/components/region/RegionDetail.vue'

export default {
  name: 'RegionList',
  components: {
    RegionForm,
    RegionDetail,
  },
  data() {
    return {
      regions: [],
      expanded: new Set(),
      loading: false,
      error: null,
      showFormModal: false,
      showDetailModal: false,
      formType: 'create',
      currentRegion: null,
      currentRegionId: null
    };
  },
  async mounted() {
    await this.fetchRegions();
  },
  methods: {
    async fetchRegions() {
      this.loading = true;
      this.error = null;
      try {
        const data = await RegionService.getRegionTree();
        this.regions = Array.isArray(data) ? data : [];
      } catch (err) {
        this.error = err.message || '加载失败，请稍后重试';
      } finally {
        this.loading = false;
      }
    },
    toggleExpand(cityId) {
      if (this.expanded.has(cityId)) {
        this.expanded.delete(cityId);
      } else {
        this.expanded.add(cityId);
      }
    },
    showDetail(regionId) {
      console.log('显示详情，regionId:', regionId);
      this.currentRegionId = regionId;
      this.showDetailModal = true;
      this.$emit('modal-status-change', true);
    },
    showEditForm(region) {
      this.formType = 'edit';
      this.currentRegion = region;
      this.showFormModal = true;
      this.$emit('modal-status-change', true);
    },
    handleFormClose() {
      this.showFormModal = false;
      this.$emit('modal-status-change', false);
    },
    async handleFormSuccess() {
      this.showFormModal = false;
      this.$emit('modal-status-change', false);
      await this.fetchRegions();
    },
    handleDetailClose() {
      this.showDetailModal = false;
      this.$emit('modal-status-change', false);
    }
  },
  emits: [
    'view-region',
    'edit-region',
    'create-region',
    'delete-region',      // ✅ 新增：删除事件
    'modal-status-change'
  ]
};
</script>

<style scoped>
/* 确保子节点行不继承 hover 背景 */
.tree-child-row:hover {
  background-color: #f8f9fa !important;
}

.region-table {
  width: 100%;
  min-width: 500px;
}
</style>