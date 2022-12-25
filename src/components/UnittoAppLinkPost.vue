<script setup lang="ts">

defineProps<{
  title: string,
  body: string,
  backgroundSrc: string,
}>()
</script>

<template>
  <a class="group/item flex flex-col rounded-2xl hover:rounded-3xl bg-slate-100 hover:bg-green-300 overflow-hidden transition-all">
    <div
      class="relative flex place-content-center place-items-center rounded-b-2xl bg-gradient-to-tl overflow-hidden from-green-100 via-emerald-100 to-lime-100">
      <img class="opacity-0 group-hover/item:opacity-100 transition-all rounded-b-2xl"
        :src="backgroundSrc" alt="">
      <div
        class="absolute rounded-full flex fill-green-700 bg-gradient-to-bl from-green-300 via-emerald-200 to-lime-100">
        <slot></slot>
      </div>
    </div>
    <div class="px-6 pb-6 pt-2">
      <p class="text-xl font-medium">{{ title }}</p>
      <p>{{ body }}</p>
    </div>
  </a>
</template>
