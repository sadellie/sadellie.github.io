<script setup lang="ts">
defineProps<{
    name: string,
    icon: string,
    selected?: boolean
}>()
</script>

<template>
    <div class="p-3 flex flex-row w-full gap-4 rounded-full" :class="selected ? 'bg-green-400 hover:bg-green-600' : 'hover:bg-slate-200' ">
        <span class="material-symbols-outlined">
            {{ icon }}
        </span>
        <p>{{ name }}</p>
    </div>
</template>