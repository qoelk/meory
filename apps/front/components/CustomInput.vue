<script setup lang="ts">
import {defineComponent} from "@vue/runtime-core";

defineComponent({
  name: 'CustomInput',
  setup() {
    return {}
  }
})
</script>

<template>
  <div class="group">
    <label class="label">Label</label>
    <input type="text" class="input">
  </div>
</template>

<style scoped lang="scss">
.group {
  display: flex;
  flex-direction: column;
  margin-bottom: 20px;
  .input {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin-top: 5px;
  }
}


</style>