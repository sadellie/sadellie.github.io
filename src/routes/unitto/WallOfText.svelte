<script lang="ts">
  import Footer from "./Footer.svelte";
</script>

<div class="flex flex-col gap-8 p-4 w-full">
  <div class="flex flex-col gap-4">
    <slot />
  </div>
  <hr />
  <Footer />
</div>
