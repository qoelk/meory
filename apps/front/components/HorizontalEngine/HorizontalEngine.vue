<template>
  <div class="horizontal-engine">
    <div class="horizontal-engine__row" v-for="row in layout">
      <div class="horizontal-engine__item" v-for="item in row">
        <div class="placeholder">test</div>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import {defineComponent} from 'vue'

export default defineComponent({
  name: 'HorizontalEngine',
  setup() {
    const data = ref([
      {id: 1, name: 'test'},
      {id: 2, name: 'test'},
      {id: 3, name: 'test'},
      {id: 4, name: 'test'},
      {id: 5, name: 'test'},
      {id: 6, name: 'test'},
      {id: 7, name: 'test'},
      {id: 8, name: 'test'},
      {id: 9, name: 'test'},
      {id: 10, name: 'test'},
      {id: 11, name: 'test'},
      {id: 12, name: 'test'},
      {id: 13, name: 'test'},
      {id: 14, name: 'test'},
      {id: 15, name: 'test'},
      {id: 16, name: 'test'},
      {id: 17, name: 'test'},
      {id: 18, name: 'test'},
      {id: 19, name: 'test'},
      {id: 20, name: 'test'},
      {id: 21, name: 'test'},
      {id: 22, name: 'test'},
      {id: 23, name: 'test'},
      {id: 24, name: 'test'},
      {id: 25, name: 'test'},
      {id: 26, name: 'test'},
      {id: 27, name: 'test'},
      {id: 28, name: 'test'},
      {id: 29, name: 'test'},
      {id: 30, name: 'test'},
      {id: 31, name: 'test'},
      {id: 32, name: 'test'},
      {id: 33, name: 'test'},
      {id: 34, name: 'test'},
      {id: 35, name: 'test'},
      {id: 36, name: 'test'},
      {id: 37, name: 'test'},
      {id: 38, name: 'test'},
      {id: 39, name: 'test'}
    ])
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
    }
  }
}

.placeholder {
  background-color: teal;
  width: 150px;
  height: 150px;
}
</style>
