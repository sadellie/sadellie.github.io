<script setup lang="ts">
</script>

<template>
  <div class="flex flex-col p-4 w-full h-screen place-content-center place-items-center">
    <div>
      <p>Oopsie, you were not to see this...</p>
      <div class="flex place-content-center">
          <button
            class="flex bg-fuchsia-700 rounded-full text-white font-medium text-xl px-8 py-4 my-2 transition-all ease-linear shadow-2xl hover:shadow-fuchsia-700 hover:bg-fuchsia-900">
            <RouterLink to="/">
              Go home
            </RouterLink>
          </button>
        </div>
    </div>
  </div>
</template>
