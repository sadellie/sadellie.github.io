<script setup lang="ts">
import type { Project } from '@/common/Interfaces';

defineProps<{
  project: Project
}>()
</script>

<template>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
    <div class="">
      <p class="text-4xl font-bold text-fuchsia-700">
        {{ project.projectName }}
      </p>
      <p class="text-2xl font-medium">
        {{ project.shortDescription }}
      </p>
      <div class="my-4">
        <li class="list-disc" v-for="feature in project.features">
          {{ feature }}
        </li>
      </div>
      <a class="text-2xl font-semibold text-fuchsia-700 hover:underline" :href=project.projectLink>Learn more ></a>
    </div>
    <div class="relative flex overflow-hidden rounded-3xl glow">
      <img class="object-fit w-full h-full" :src="project.cover" alt="cover">
      <div class="absolute flex w-full h-full top-0 transition-all overlay p-4 text-xl font-medium">{{ project.stack.join(" - ") }}</div>
    </div>
  </div>
</template>

<style>
.overlay {
  opacity: 0;
  background-color: rgba(177, 0, 175, 0.5);
  backdrop-filter: blur(10px);
  color: white;
  transition: ease-in-out;
}

.overlay:hover {
  opacity: 1;
}

.glow {
  transition: ease-in-out;
  box-shadow: none;
  -moz-box-shadow: none;
  -webkit-box-shadow: none;
  -khtml-box-shadow: none;
}

.glow:hover {
  box-shadow: 0px 4px 25px rgba(177, 0, 175, 0.69);
  -moz-box-shadow: 0px 4px 25px rgba(177, 0, 175, 0.69);
  -webkit-box-shadow: 0px 4px 25px rgba(177, 0, 175, 0.69);
  -khtml-box-shadow: 0px 4px 25px rgba(177, 0, 175, 0.69);
}
</style>