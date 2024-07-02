<script lang="ts">
  import { UnittoTheme } from "./UnittoTheme";
  export let title: string;
  export let support: string;
  export let href: string | null = null;
  export let showIcon: boolean = false;

  function onClick() {
    if (href != null) window.location.href = href;
  }
</script>

<!-- svelte-ignore a11y-no-static-element-interactions -->
<!-- svelte-ignore a11y-click-events-have-key-events -->

<div
  class="rounded-3xl overflow-hidden {UnittoTheme.surfaceContainerLow}"
  class:cursor-pointer={href}
  class:gap-2={support != ""}
  on:click={onClick}
>
  <div class="flex flex-row items-stretch p-6 {UnittoTheme.onSurfaceHover}">
    <div class="grow">
      <p class="text-2xl font-medium">{title}</p>
      <p>{support}</p>
    </div>
    {#if href && showIcon}
      <div class="flex place-items-center">
        <span class="material-symbols-outlined"> arrow_forward </span>
      </div>
    {/if}
  </div>
</div>
