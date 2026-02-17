<script lang="ts">
  import { createEventDispatcher } from "svelte";
  import type M3Theme from "./M3Theme";
  export let theme: M3Theme;
  export let id: string;

  const dispatch = createEventDispatcher();
  function click() {
    dispatch("menuClick");
  }
</script>

<div
  class="lg:hidden z-20 fixed top-0 h-full transition-transform -translate-x-full px-2 w-80 rounded-e-3xl {theme.surface} {theme.onSurfaceText}"
  id={id}
>
  <button on:click={click}>
    <span
      class="material-symbols-outlined {theme.onSurfaceHover} rounded-full p-3 m-2 cursor-pointer"
    >
      menu_open
    </span>
  </button>
  <slot />
</div>
