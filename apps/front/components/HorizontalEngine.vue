<template>
  <div class="horizontal-engine">
    <div v-for="row in layout" class="horizontal-engine__row">
      <div v-for="item in row" class="horizontal-engine__item">
        <post-block :post="item"/>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import {defineComponent} from 'vue'

export default defineComponent({
  name: 'HorizontalEngine',
  async setup() {
    const { data, error, status } = await useFetch('http://localhost:8000/posts')
    const layout = computed(() => {
      const layout = [[], [], [], []]
      data.value.forEach((item, index) => {
        layout[index % 4].push(item)
      })
      return layout
    })
    return {
      data,
      layout
    }
  }
})
</script>
<style lang="scss">
.horizontal-engine {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
  padding: 10px;

  .horizontal-engine__row {
    display: flex;
    flex-direction: row;

    .horizontal-engine__item {
      padding: 10px;
      height: 186px;
    }
  }
}

.placeholder {
  background-color: teal;
  height: 150px;
}
</style>
