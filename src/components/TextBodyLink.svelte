<script lang="ts">
  export let href: string;
</script>

<a class="font-medium text-blue-600 visited:text-fuchsia-700 hover:text-blue-900 hover:underline" href={href}>
    <slot></slot>
</a>
