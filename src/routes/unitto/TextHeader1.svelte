<script lang="ts">
    export let id: string = "";
</script>

<p class="text-3xl md:text-4xl py-2 w-fit font-medium" id={id}>
    <slot></slot>
</p>
