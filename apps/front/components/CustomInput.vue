<script setup lang="ts">
import { ref } from 'vue';

const inputValue = ref('');

</script>

<template>
  <div class="group">
    <label class="label">Label</label>
    <div class="input-wrapper">
      <slot name="left"></slot>
      <input
        type="text"
        class="input"
        v-model="inputValue"
      />
      <slot name="right"></slot>
    </div>
  </div>
</template>

<style scoped lang="scss">
.group {
  display: flex;
  flex-direction: column;
  margin-bottom: 20px;

  .label {
    font-weight: bold;
    margin-bottom: 5px;
    display: none;
  }

  .input-wrapper {
    display: flex;
    align-items: center;

    .input {
      flex: 1;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 5px;
      margin: 0 5px;
      transition: border-color 0.3s ease;

      &:focus {
        outline: none;
        border-color: #42b983;
      }
    }
  }

  .error {
    color: red;
    font-size: 12px;
    margin-top: 5px;
  }
}
</style>