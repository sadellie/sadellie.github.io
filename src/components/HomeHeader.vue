<script setup lang="ts">
defineProps<{
    name: string
}>()
</script>

<template>
    <p class="text-4xl text-center font-bold text-fuchsia-700">{{ name }}</p>
</template>