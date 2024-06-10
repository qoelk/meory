<template>
  <div class="content">
    <custom-header/>
    <horizontal-engine/>
  </div>
</template>
<script lang="ts">
import {defineComponent} from "vue";
import CustomHeader from "~/components/CustomHeader.vue";

export default defineComponent({
  components: {CustomHeader}
})
</script>
<style lang="scss">
.content {
  margin-top: 120px;
}
</style>