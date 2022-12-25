<script setup lang="ts">
defineProps<{
    name: string,
    icon: string,
    selected?: boolean
}>()
</script>

<template>
    <div class="group/item flex flex-col place-items-center text-center">
        <span class="material-symbols-outlined px-4 py-1 rounded-full group-hover/item:font-medium transition-all" :class="selected ? 'bg-green-400 group-hover/item:bg-green-500' : 'group-hover/item:bg-green-200' ">
            {{ icon }}
        </span>
        <p class="text-xs font-semibold">{{ name }}</p>
    </div>
</template>