<script lang="ts">
  import { IndexxoTheme } from "./IndexxoTheme";
  let className = "";
  export { className as class };

  export let img: string;
  export let title: string;
  export let support: string;
</script>

<div
  class="flex flex-col rounded-2xl {IndexxoTheme.secondaryContainer} {className} overflow-hidden"
>
  <img src={img} alt={title} class="w-full"/>
  <div class="flex flex-col gap-2 p-4 {IndexxoTheme.onSecondaryContainerText}">
    <p class="text-2xl">{title}</p>
    <p>{support}</p>
  </div>
</div>
