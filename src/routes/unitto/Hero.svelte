<script lang="ts">
    import type { Feature } from "./IFeature";

    export let features: Array<Feature>
    import FeatureItem from "./FeatureItem.svelte";
    import hero from "$lib/images/unitto/hero.png";
</script>

<div
    class="flex flex-col py-24 xl:py-32 rounded-3xl place-items-center gap-16 bg-center bg-cover backdrop-invert-0 bg-white/30"
    style="background-image: url({hero});"
>
    <div class="flex flex-col place place-items-center">
        <p class="text-6xl md:text-8xl xl:text-9xl text-center font-medium">
            Unitto
        </p>
        <p class="text-xl md:text-2xl text-center">
            Calculate and convert, but better
        </p>
    </div>

    <div class="hidden xl:block">
        <div class="grid grid-cols-2 gap-2 w-[64rem]">
            {#each features as feat}
                <FeatureItem
                    title={feat.titls}
                    support={feat.support}
                    href="#{feat.id}"
                />
            {/each}
        </div>
    </div>
</div>
