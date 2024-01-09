<script lang="ts">
    export let url: string
    export let id: string
</script>

<div
    class="h-full w-full object-scale-down bg-cover bg-center absolute top-0 rounded-3xl transition-opacity ease-[cubic-bezier(0.12,0,0.39,0)] opacity-100"
    style="background-image: url({url});"
    id={id}
/>
