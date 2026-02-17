<script lang="ts">
  import { page } from "$app/stores";
  import type M3Theme from "./M3Theme";
  export let theme: M3Theme;
  export let id: string = "";

  let showTooltip = false;

  function copyAnchor() {
    document.location.href =
      document.location.origin + document.location.pathname + "#" + id;
    navigator.clipboard.writeText(document.location.href);

    showTooltip = true;
    setTimeout(() => {
      showTooltip = false;
    }, 400);
  }
</script>

<div class="group flex flex-row items-center">
  <p class="text-3xl md:text-4xl py-2 w-fit font-medium" {id}>
    <slot />
  </p>
  <button
    on:click={copyAnchor}
    class:hidden={id === ""}
    class="relative group/button cursor-pointer"
  >
    <span
      class="transition-transform group-hover:opacity-100 opacity-0 material-symbols-outlined rounded-full p-3 m-2 {theme.onSurfaceHover}"
      class:rotate-180={copyAnchor}>link</span
    >

    <span
      class="absolute transition-all bottom-full left-1/2 transform -translate-x-1/2 mt-2 px-2 py-1 text-sm {theme.inverseSurface} {theme.inverseOnSurfaceText} rounded group-hover/button:opacity-100 pointer-events-none"
      class:opacity-0={!showTooltip}
    >
      Copy
    </span>
    <span
      class="absolute transition-all bottom-full left-1/2 transform -translate-x-1/2 mt-2 px-2 py-1 text-sm {theme.inverseSurface} {theme.inverseOnSurfaceText} rounded pointer-events-none"
      class:opacity-0={!showTooltip}
      class:opacity-100={showTooltip}
    >
      Copied
    </span>
  </button>
</div>
