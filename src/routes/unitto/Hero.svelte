<script lang="ts">
  import type { Feature } from "./IFeature";
  import { UnittoTheme } from "./UnittoTheme";

  export let features: Array<Feature>;
  import FeatureItem from "./FeatureItem.svelte";
  import hero from "$lib/images/unitto/hero.png";
</script>

<div
  class="flex flex-col py-12 xl:py-20 rounded-3xl place-items-center gap-2 bg-center bg-cover backdrop-invert-0 bg-white/30"
  style="background-image: url({hero});"
>
  <div class="flex flex-col place place-items-center mb-4">
    <p class="text-6xl md:text-8xl xl:text-9xl text-center font-medium">
      Unitto
    </p>
    <p class="text-xl md:text-2xl text-center">
      Calculate and convert, but better
    </p>
  </div>

  <a href="./app" target="_blank">
    <div
      class="rounded-full px-10 py-6 {UnittoTheme.primaryContainer} hover:bg-[rgb(28,89,49)] {UnittoTheme.onPrimaryContainerText}"
    >
      <p class="text-2xl">Try now</p>
      <p>No download required</p>
    </div>
  </a>
  <div class="hidden xl:block">
    <div class="grid grid-cols-2 gap-2 w-[64rem]">
      {#each features as feat}
        <FeatureItem
          title={feat.title}
          support={feat.support}
          href="#{feat.id}"
        />
      {/each}
    </div>
  </div>
</div>
