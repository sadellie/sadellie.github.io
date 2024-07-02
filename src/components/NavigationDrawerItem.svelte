<script lang="ts">
  import { createEventDispatcher } from "svelte";
  import type M3Theme from "./M3Theme";
  export let title: string;
  export let icon: string;
  export let isSelected: Boolean = false;
  export let href: string;
  export let theme: M3Theme;

  const dispatch = createEventDispatcher();

  $: background = isSelected ? theme.secondaryContainer : "";

  $: hover = isSelected
    ? theme.onSecondaryHover
    : theme.onSurfaceHover;

  $: textColor = isSelected
    ? theme.onSecondaryContainerText
    : theme.onSurfaceVariantText;

  $: iconColor = textColor;

  function click() {
    dispatch("onTabClick");
  }
</script>

<a {href} on:click={click}>
  <div class="rounded-full overflow-hidden {background}">
    <div class="flex flex-row gap-3 h-14 items-center p-4 {hover}">
      <span class="material-symbols-outlined w-6 h-6 {iconColor}">{icon}</span>
      <p class="{textColor}">{title}</p>
    </div>
  </div>
  
</a>
