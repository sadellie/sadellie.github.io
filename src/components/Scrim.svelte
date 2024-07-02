<script lang="ts">
  import { createEventDispatcher } from "svelte";
  export let id: string;
  const dispatch = createEventDispatcher();

  function click() {
    dispatch("menuClick");
  }
</script>

<!-- svelte-ignore a11y-no-static-element-interactions -->
<!-- svelte-ignore a11y-click-events-have-key-events -->
<div
  class="hidden z-20 lg:hidden fixed top-0 w-full h-full bg-black opacity-25"
  id={id}
  on:click={click}
/>
