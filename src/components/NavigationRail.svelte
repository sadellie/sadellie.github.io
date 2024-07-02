<script lang="ts">
    import type M3Theme from "./M3Theme";
    export let theme: M3Theme
</script>

<div
  class="hidden lg:block sticky top-0 h-screen w-20 {theme.surfaceContainerLow} {theme.onSurfaceText}"
>
  <!-- Navigation rail -->
  <div class="flex flex-col gap-4 pt-6">
    <slot />
  </div>
</div>
