<script lang="ts">
    import unittoLogo from "$lib/images/unitto/unitto-logo.svg";
</script>

<footer>
    <div class="grid grid-cols-1 p-4 gap-4">
        <div class="flex justify-start items-center gap-4">
            <img
                class="w-28 p-2 rounded-3xl border-2 bg-unitto-background hover:scale-110 hover:-translate-y-5 transition-all hover:shadow-2xl"
                src={unittoLogo}
                alt="unitto"
            />
            <p>
                Unitto is a unique modern calculator and unit converter for mobile
                devices.
            </p>
        </div>
        <div class="flex flex-wrap gap-x-8">
            <a href="/" class=""
                ><p class="font-bold hover:underline">by Sad Ellie</p></a
            ><a
                class="font-medium text-blue-600 visited:text-fuchsia-700 hover:text-blue-900 hover:underline"
                href="https://forms.gle/YRKapCk91J63gzM27">Anonymous request</a
            ><a
                class="font-medium text-blue-600 visited:text-fuchsia-700 hover:text-blue-900 hover:underline"
                href="https://github.com/sadellie/unitto">GitHub</a
            ><a
                class="font-medium text-blue-600 visited:text-fuchsia-700 hover:text-blue-900 hover:underline"
                href="mailto:sadellie.dev@gmail.com">Email</a
            ><a
                class="font-medium text-blue-600 visited:text-fuchsia-700 hover:text-blue-900 hover:underline"
                href="https://trello.com/b/cxAbRlvu/unitto">Trello board</a
            >
        </div>
        <div>
            <p>
                Photos by <a
                    class="font-medium text-blue-600 hover:text-blue-900 hover:underline"
                    href="https://unsplash.com/@diegocarneiro">Diego Carneiro</a
                >,
                <a
                    class="font-medium text-blue-600 hover:text-blue-900 hover:underline"
                    href="https://unsplash.com/@martz90">Martin Martz</a
                > and
                <a
                    class="font-medium text-blue-600 hover:text-blue-900 hover:underline"
                    href="https://unsplash.com/@pawel_czerwinski"
                    >Pawel Czerwinski</a
                >
                on
                <a
                    class="font-medium text-blue-600 hover:text-blue-900 hover:underline"
                    href="https://unsplash.com/">Unsplash</a
                >
            </p>
        </div>
    </div>
</footer>
