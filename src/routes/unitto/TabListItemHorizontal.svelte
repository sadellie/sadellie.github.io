<script lang="ts">
    export let title: string;
    export let icon: string;
    export let isSelected: Boolean = false;
    export let href: string;

    $: background = isSelected
    ? "bg-unitto-dark-secondaryContainer hover:bg-unitto-dark-surfaceContainer-active-hover"
    : "hover:bg-unitto-dark-surfaceContainer-inactive-hover"

    $: icon_state_class = isSelected
        ? "text-unitto-on-secondary-container"
        : "text-unitto-on-surface-variant";

    $: text_state_class = isSelected
        ? "text-unitto-on-secondary-container"
        : "text-unitto-on-surface-variant";

    import { createEventDispatcher } from "svelte";
    const dispatch = createEventDispatcher();

    function click() {
        dispatch("onNavigate");
    }
</script>

<a {href} on:click={click}>
    <div
        class="px-4 py-2 flex flex-row w-full gap-4 rounded-full place-items-center {background}"
    >
        <span class="material-symbols-outlined text-3xl {icon_state_class}">{icon}</span>
        <p class="text-lg {text_state_class}">{title}</p>
    </div>
</a>
