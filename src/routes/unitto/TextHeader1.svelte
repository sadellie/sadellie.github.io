<script lang="ts">
  import { page } from "$app/stores";

  export let id: string = "";

  function copyAnchor() {
    navigator.clipboard.writeText($page.url + "#" + id);
  }
</script>

<div class="group flex flex-row items-center">
  <p class="text-3xl md:text-4xl py-2 w-fit font-medium" {id}>
    <slot />
  </p>
  <button on:click={copyAnchor} class:hidden={id === ""}>
    <span
      class="transition-transform group-hover:opacity-100 opacity-0 material-symbols-outlined rounded-full p-3 m-2 hover:bg-unitto-dark-surfaceContainer-inactive-hover"
      class:rotate-180={copyAnchor}>link</span
    >
  </button>
</div>
