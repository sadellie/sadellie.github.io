<script lang="ts">
    import unittoLogo from "$lib/images/unitto/unitto-logo.svg";
    import { createEventDispatcher } from "svelte";
    const dispatch = createEventDispatcher();
    let y: number

    function click() {
        console.log(y);
        
        dispatch('menuClick')
    }
</script>

<div class="lg:hidden flex place-items-center sticky px-2 top-0 z-10 transition-colors bg-unitto-dark-background text-unitto-dark-onBackground">
    <button on:click={click}>
        <span
            class="material-symbols-outlined rounded-full p-3 m-2 hover:bg-unitto-dark-surfaceContainer-inactive-hover"
            >menu</span
        >
    </button>
    <a
        class="rounded-full flex flex-row items-center gap-4 p-2 hover:bg-unitto-dark-surfaceContainer-inactive-hover"
        href="/unitto"
    >
        <img class="w-8" src={unittoLogo} alt="" />
        <p class="text-lg font-medium">Unitto</p>
    </a>
</div>

<svelte:window bind:scrollY={y} />