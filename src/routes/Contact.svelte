<script lang="ts">
    export let title: string;
    export let href: string;
    export let img: string;
</script>

<a
    class="group/item flex flex-col rounded-2xl hover:rounded-3xl bg-fuchsia-100 dark:bg-fuchsia-900 hover:bg-fuchsia-200 dark:hover:bg-fuchsia-800 overflow-hidden transition-all h-full"
    {href}
    ><div
        class="relative flex place-content-center place-items-center rounded-b-2xl bg-gradient-to-tl overflow-hidden from-fuchsia-800 via-pink-900 to-blue-900"
    >
        <div class="opacity-0 group-hover/item:opacity-100 transition-all rounded-b-2xl h-48 w-full bg-cover bg-center object-scale-down" style="background-image: url({img})"/>
        <div
            class="absolute rounded-full flex fill-fuchsia-700 bg-gradient-to-bl from-fuchsia-300 via-pink-200 to-blue-100 p-6"
        >
            <slot></slot>
        </div>
    </div>
    <div class="px-6 py-6">
        <p class="text-xl font-semibold">{title}</p>
        <!-- <p>Get the app for your Android device.</p> -->
    </div>
</a>
