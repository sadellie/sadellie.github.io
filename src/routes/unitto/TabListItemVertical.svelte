<script lang="ts">
  import { createEventDispatcher } from "svelte";
  export let title: string;
  export let icon: string;
  export let isSelected: Boolean = false;
  export let href: string;

  const dispatch = createEventDispatcher();

  $: background = isSelected
    ? "bg-unitto-dark-secondaryContainer hover:bg-unitto-dark-surfaceContainer-active-hover"
    : "hover:bg-unitto-dark-surfaceContainer-inactive-hover";

  $: icon_state_class = isSelected
    ? "text-unitto-on-secondary-container bg-unitto-secondaryContainer group-hover/item:bg-unitto-surfaceContainer-active-hover"
    : "text-unitto-on-surface-variant group-hover/item:bg-unitto-surfaceContainer-inactive-hover";

  $: text_state_class = isSelected
    ? "text-unitto-on-secondary-container"
    : "text-unitto-on-surface-variant";

  function click() {
    dispatch("onNavigate", href);
  }
</script>

<a
  {href}
  class="group/item flex flex-col place-items-center text-center w-24 gap-2"
  on:click={click}
>
  <span
    class="material-symbols-outlined px-4 rounded-full group-hover/item:font-semibold transition-all text-2xl {icon_state_class} {background}"
    >{icon}</span
  >

  <p class="text-xs font-semibold {text_state_class}">{title}</p>
</a>
