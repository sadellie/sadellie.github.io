<script setup lang="ts">

defineProps<{
  title: string,
  body: string
}>()
</script>

<template>
  <div class="grid grid-cols-1 md:grid-cols-5 gap-5">
    <div class="col-span-2 flex flex-col gap-2">
      <p class="text-2xl font-medium">{{ title }}</p>
      <p>{{ body }}</p>
    </div>
    <div class="col-span-3">
      <slot></slot>
    </div>
  </div>
</template>

<style scoped>

</style>