<script lang="ts">
    export let url: string
    export let id: string
</script>

<div
    class="h-full w-full object-scale-down bg-cover bg-center absolute top-0 rounded-3xl transition-opacity opacity-100"
    style="background-image: url({url});"
    id={id}
/>
