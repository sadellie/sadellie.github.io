<script lang="ts">
  import FeatureItem from "./FeatureItem.svelte";
  import { UnittoTheme } from "./UnittoTheme";

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
          support:
            "Settings are applied across the app. Change once and everywhere",
        },
      ],
    },
    {
      titls: "Download",
      id: "feature4",
      support: "Get the app now",
      description: "Get the app for your Android device",
      postHorizontal: postHorizontal4,
      postVertical: postVertical4,
      postVerticalId: "vert4",
      details: [
        {
          title: "Play Store",
          support: "Get the app and leave a review",
          href: "https://play.google.com/store/apps/details?id=com.sadellie.unitto",
        },
        {
          title: "Obtainium",
          support: "Automatically receive new versions frm GitHub",
          href: "https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/%7B%22id%22%3A%22com.sadellie.unitto%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2Fsadellie%2Funitto%22%2C%22author%22%3A%22sadellie%22%2C%22name%22%3A%22Calculator%22%2C%22preferredApkIndex%22%3A0%2C%22additionalSettings%22%3A%22%7B%5C%22includePrereleases%5C%22%3Afalse%2C%5C%22fallbackToOlderReleases%5C%22%3Atrue%2C%5C%22filterReleaseTitlesByRegEx%5C%22%3A%5C%22%5C%22%2C%5C%22filterReleaseNotesByRegEx%5C%22%3A%5C%22%5C%22%2C%5C%22verifyLatestTag%5C%22%3Afalse%2C%5C%22dontSortReleasesList%5C%22%3Afalse%2C%5C%22useLatestAssetDateAsReleaseDate%5C%22%3Afalse%2C%5C%22releaseTitleAsVersion%5C%22%3Afalse%2C%5C%22trackOnly%5C%22%3Afalse%2C%5C%22versionExtractionRegEx%5C%22%3A%5C%22%5C%22%2C%5C%22matchGroupToUse%5C%22%3A%5C%22%5C%22%2C%5C%22versionDetection%5C%22%3Atrue%2C%5C%22releaseDateAsVersion%5C%22%3Afalse%2C%5C%22useVersionCodeAsOSVersion%5C%22%3Atrue%2C%5C%22apkFilterRegEx%5C%22%3A%5C%22%5C%22%2C%5C%22invertAPKFilter%5C%22%3Afalse%2C%5C%22autoApkFilterByArch%5C%22%3Atrue%2C%5C%22appName%5C%22%3A%5C%22%5C%22%2C%5C%22shizukuPretendToBeGooglePlay%5C%22%3Afalse%2C%5C%22allowInsecure%5C%22%3Afalse%2C%5C%22exemptFromBackgroundUpdates%5C%22%3Afalse%2C%5C%22skipUpdateNotifications%5C%22%3Afalse%2C%5C%22about%5C%22%3A%5C%22%5C%22%2C%5C%22github-creds%5C%22%3A%5C%22%5C%22%7D%22%2C%22overrideSource%22%3A%22GitHub%22%7D",
        },
        {
          title: "GitHub",
          support: "Latest version",
          href: "https://github.com/sadellie/unitto/releases/latest",
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

    <div class="sticky top-0 h-screen w-1/2 hidden xl:block p-2 overflow-clip">
      <div class="w-full h-full relative">
        {#each features as feat}
          <SideImage url={feat.postVertical} id={feat.postVerticalId} />
        {/each}
      </div>
    </div>
  </div>

  <hr class="{UnittoTheme.outlineBorder}" />
  <Footer />
</div>
