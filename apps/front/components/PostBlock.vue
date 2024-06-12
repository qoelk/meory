<script setup lang="ts">
const props = defineProps(['post'])
</script>

<template>
  <custom-block>
    <div class="post">
      <div class="post__content">
        <img :src="post.content.thumbnail_url" alt="Keanu" class="post__image">
      </div>
      <div class="post__overlay">
        <div class="overlay__item">
          <post-counter type="views" :value="post.views"/>
        </div>
        <div class="overlay__item">
          <post-counter type="likes" :value="post.likes"/>
        </div>
        <div class="overlay__item">
          <post-counter type="downloads" :value="post.views + post.likes"/>
        </div>
      </div>
    </div>
  </custom-block>
</template>

<style scoped lang="scss">
.post {
  position: relative;
}
.post__image {
  max-height: 186px;
}
.post__overlay {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  padding: 20px;

  display: flex;
  flex-direction: column;
  justify-content: space-between;

  background: linear-gradient(270deg, #000000 14.58%, rgba(0, 0, 0, 0) 100%);
}
</style>