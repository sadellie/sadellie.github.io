<script lang="ts">
    import FeatureItem from "./FeatureItem.svelte";

    import postHorizontal1 from "$lib/images/unitto/post-horizontal1.png";
    import postHorizontal2 from "$lib/images/unitto/post-horizontal2.png";
    import postHorizontal3 from "$lib/images/unitto/post-horizontal3.png";
    import postHorizontal4 from "$lib/images/unitto/post-horizontal4.png";

    import postVertical1 from "$lib/images/unitto/post-vertical1.png";
    import postVertical2 from "$lib/images/unitto/post-vertical2.png";
    import postVertical3 from "$lib/images/unitto/post-vertical3.png";
    import postVertical4 from "$lib/images/unitto/post-vertical4.png";
    import FeatureDetail from "./FeatureDetail.svelte";

    import { onMount } from "svelte";
    import Hero from "./Hero.svelte";
    import SideImage from "./SideImage.svelte";
    import Footer from "./Footer.svelte";

    import type { Feature } from "./IFeature";
    import Snake from "./Snake.svelte";

    const features: Array<Feature> = [
        {
            titls: "What's Unitto?",
            id: "feature1",
            support: "Learn how Unitto helps people everyday",
            description:
                "Unitto is a collection of useful tools that calculate things for you. Everything is packed into a single Android app. Unitto is unique — it takes the UX-first approach to the next level. User experience is a top priority.</br></br>The goal is to boost user <b>productivity</b> and improve their daily tasks <b>experience</b>.",
            postHorizontal: postHorizontal1,
            postVertical: postVertical1,
            postVerticalId: "vert1",
            details: [
                {
                    title: "Free",
                    support: "No ads, in-app purchases and analytics",
                },
                {
                    title: "Modern",
                    support: "Using latest Android features",
                },
                {
                    title: "Quick",
                    support: "Instant calculations and conversions",
                },
            ],
        },
        {
            titls: "Tools",
            id: "feature2 ",
            support: "Check out what Unitto has to offer for you",
            description:
                "Each tool is made the right way, with equal care and attention to detail. All tools in the app are equally the best. Updates can add new tools or improve existing ones.",
            postHorizontal: postHorizontal2,
            postVertical: postVertical2,
            postVerticalId: "vert2",
            details: [
                {
                    title: "Calculator",
                    support: "Calculate, save to history, share results",
                },
                {
                    title: "Unit converter",
                    support: "570 Units and currencies for every situation",
                },
                {
                    title: "The list goes on",
                    support: "Date calculator, Time zone converter and more",
                },
            ],
        },
        {
            titls: "Customize",
            id: "feature3",
            support: "See why Unitto is the only true customizable calculator",
            description:
                "Unitto offers a wide range of options to personilze your app. Users can change every aspect of the app.<br/><br/>All settings are intuitive and simple, you don't need a degree in science 🤓.",
            postHorizontal: postHorizontal3,
            postVertical: postVertical3,
            postVerticalId: "vert3",
            details: [
                {
                    title: "Themes",
                    support: "Make the app a true eye candy",
                },
                {
                    title: "Formatting",
                    support:
                        "Change the way numbers look in the app: delimeters, decimal places and more",
                },
                {
                    title: "Single source of truth",
                    support: "Settings are applied across the app. Change once and everywhere",
                },
            ],
        },
        {
            titls: "Download",
            id: "feature4",
            support: "Get the app now",
            description: "Get the app for you Android device",
            postHorizontal: postHorizontal4,
            postVertical: postVertical4,
            postVerticalId: "vert4",
            details: [
                {
                    title: "Play Store",
                    support: "Get the app and leave a review",
                    href: "https://play.google.com/store/apps/details?id=com.sadellie.unitto"
                },
                {
                    title: "F-Droid",
                    support: "Support the freedom of choice",
                    href: "https://f-droid.org/packages/com.sadellie.unitto"
                },
                {
                    title: "GitHub",
                    support: "From the developer himself",
                    href: "https://github.com/sadellie/unitto",
                },
            ],
        },
    ];

    function observeElement(
        elem: HTMLElement | null,
        sideImage: HTMLElement | null
    ) {
        if (elem == null) return;
        if (sideImage == null) return;

        new IntersectionObserver(
            function (entries) {
                const intersect = entries[0].isIntersecting;
                if (intersect) {
                    sideImage.classList.replace("opacity-0", "opacity-100");
                } else {
                    sideImage.classList.replace("opacity-100", "opacity-0");
                }
            },
            { threshold: [0.3] }
        ).observe(elem);
    }

    onMount(async () => {
        features.slice(1).forEach((feat) => {
            const psot = document.getElementById(feat.id);
            const vert = document.getElementById(feat.postVerticalId);

            observeElement(psot, vert);
        });
    });
</script>

<div class="px-2 pt-2 w-full scroll-smooth">
    <Hero {features} />

    <div class="xl:hidden grid gap-4 py-8">
        {#each features as feat}
            <FeatureItem
                title={feat.titls}
                support={feat.support}
                href="#{feat.id}"
            />
        {/each}
    </div>

    <div class="w-full xl:hidden flex flex-col place-items-center py-12">
        <Snake></Snake>
    </div>

    <div class="flex flex-row relative gap-2 py-4">
        <div class="xl:w-1/2">
            {#each features as feat}
                <FeatureDetail
                    id={feat.id}
                    image={feat.postHorizontal}
                    title={feat.titls}
                    detail={feat.description}
                >
                    {#each feat.details as detail}
                        <FeatureItem
                            title={detail.title}
                            support={detail.support}
                            href={detail.href}
                            showIcon={true}
                        />
                    {/each}
                </FeatureDetail>
            {/each}
        </div>

        <div
            class="sticky top-0 h-screen w-1/2 hidden xl:block p-2 overflow-clip"
        >
            <div class="w-full h-full relative">
                {#each features as feat}
                    <SideImage
                        url={feat.postVertical}
                        id={feat.postVerticalId}
                    />
                {/each}
            </div>
        </div>
    </div>

    <hr class="border-unitto-dark-outline"/>
    <Footer />
</div>
