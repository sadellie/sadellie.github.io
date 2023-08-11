<script lang="ts">
    import snake from "$lib/images/unitto/snake.svg";
    import Snake from "./Snake.svelte";
    export let image: string;
    export let title: string;
    export let detail: string;
    export let id: string;
</script>

<div class="flex flex-col py-8 place-items-center xl:h-screen" id="{id}">
    <img class="rounded-3xl w-full xl:hidden" src="{image}" alt="post" />
    <div class="md:max-w-2xl m-auto w-full">
        <div class="px-4 py-12">
            <p class="text-4xl md:text-5xl xl:text-6xl py-2 w-fit font-medium">{title}</p>
            <p>{@html detail}</p>
        </div>
        <div class="flex flex-col gap-2">
            <slot />
        </div>
    </div>
    <div class="w-full flex flex-col place-items-center py-12">
        <Snake></Snake>
    </div>
</div>
