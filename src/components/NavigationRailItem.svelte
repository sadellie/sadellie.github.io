<script lang="ts">
  import { createEventDispatcher } from "svelte";
  import type M3Theme from "./M3Theme";
  export let title: string;
  export let icon: string;
  export let isSelected: Boolean = false;
  export let href: string;
  export let theme: M3Theme;

  const dispatch = createEventDispatcher();

  $: iconBackground = isSelected ? theme.secondaryContainer : "";

  $: iconBackgroundOnHover = isSelected
    ? theme.onSecondaryGroupHover
    : theme.onSurfaceGroupHover;

  function click() {
    dispatch("onNavigate", href);
  }
</script>

<a {href} class="group flex flex-col gap-1 items-center" on:click={click}>
  <div class="rounded-full overflow-hidden {iconBackground}">
    <div
      class="flex items-center justify-center w-14 h-8 {iconBackgroundOnHover}"
    >
      <span class="material-symbols-outlined w-6 h-6">{icon}</span>
    </div>
  </div>

  <p class="text-xs text-center">
    {title}
  </p>
</a>
