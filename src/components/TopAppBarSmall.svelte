<script lang="ts">
  import { createEventDispatcher } from "svelte";
  import type M3Theme from "./M3Theme";
  export let theme: M3Theme;
  export let title: string;
  export let logo: string;
  export let logoHref: string;

  const dispatch = createEventDispatcher();
  let y: number;

  function click() {
    dispatch("menuClick");
  }
</script>

<div
  class="lg:hidden flex place-items-center sticky px-2 top-0 z-10 transition-colors {theme.background} {theme.onBackgroundText}"
>
  <button on:click={click}>
    <span
      class="material-symbols-outlined rounded-full p-3 m-2 {theme.onSurfaceHover} cursor-pointer"
      >menu</span
    >
  </button>
  <a
    class="rounded-full flex flex-row items-center gap-4 p-2 {theme.onSurfaceHover}"
    href={logoHref}
  >
    <img class="w-8" src={logo} alt="" />
    <p class="text-lg font-medium">{title}</p>
  </a>
</div>

<svelte:window bind:scrollY={y} />
