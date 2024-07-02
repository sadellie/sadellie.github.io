<script lang="ts">
  import { IndexxoTheme } from "./IndexxoTheme";

  export let title: string;
  export let support: string;
  export let href: string;

  function onClick() {
    if (href != null) window.location.href = href;
  }
</script>

<!-- svelte-ignore a11y-no-static-element-interactions -->
<!-- svelte-ignore a11y-click-events-have-key-events -->
<div
  class="rounded-3xl overflow-hidden border-2 cursor-pointer w-full {IndexxoTheme.outlineVariantBorder} "
  on:click={onClick}
>
  <div class="flex flex-row gap-2 items-stretch p-6 {IndexxoTheme.onSurfaceHover}">
    <div class="grow {IndexxoTheme.onSurfaceText}">
      <p class="text-2xl font-medium">{title}</p>
      <p>{support}</p>
    </div>
  </div>
</div>
