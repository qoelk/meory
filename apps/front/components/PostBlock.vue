<script setup lang="ts">
const props = defineProps(['post'])
</script>

<template>
  <custom-block>
    <div class="post">
      <div class="post__content">
        <img :src="post.content.thumbnail_url" alt="Keanu" class="post__image">
      </div>
      <div class="post__overlay">//</div>
    </div>
  </custom-block>
</template>

<style scoped lang="scss">
.post__image {
  max-height: 186px;
}
</style>