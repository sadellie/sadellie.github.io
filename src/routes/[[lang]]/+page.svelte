<script lang="ts">
  import hero from "$lib/images/hero.jpg";
  import Product from "./Product.svelte";
  import Chip from "./Chip.svelte";

  import unittoImg from "$lib/images/unitto.png";
  import sukkoImg from "$lib/images/sukko.png";
  import indexxoImg from "$lib/images/indexxo.png";
  import sadbotImg from "$lib/images/sadbot.png";
  import webImg from "$lib/images/web.png";
  import idiot from "$lib/images/outofcontext.png";
  import secretImg from "$lib/images/secret.png";

  import Contact from "./Contact.svelte";
  import Email from "./Email.svelte";
  import Github from "./Github.svelte";
  import Telegram from "./Telegram.svelte";
  import { onMount } from "svelte";

  import type { PageData } from "./$types";
  export let data: PageData;
  const { labels } = data;
  onMount(async () => {
    const darkScheme = window.matchMedia("(prefers-color-scheme: dark)");
    const root: HTMLElement = document?.querySelector(":root") as HTMLElement;

    darkScheme.addEventListener("change", function () {
      let scrollbarColor: string;
      if (this.matches) {
        scrollbarColor = "rgba(0, 0, 0, 0.4) #4a044e";
      } else {
        scrollbarColor = "rgba(0, 0, 0, 0.3) #fdf4ff";
      }
      root.style?.setProperty("scrollbar-color", scrollbarColor);
    });
  });
</script>

<div
  class="flex flex-col place-items-center p-8 bg-fuchsia-50 dark:bg-fuchsia-950 text-black dark:text-white"
>
  <div
    class="flex flex-col py-16 xl:py-32 rounded-3xl place-items-center gap-8 bg-center bg-cover w-full relative dark:invert"
    style="background-image: url({hero});"
  >
    <div class="flex flex-col place place-items-center dark:invert">
      <p class="text-6xl md:text-8xl xl:text-9xl text-center font-medium">
        {labels.name}
      </p>
      <p class="text-xl md:text-2xl text-center">{labels.hero}</p>
    </div>
    <a href="#contact">
      <button
        class="py-6 px-12 bg-fuchsia-600 dark:bg-fuchsia-800 hover:bg-fuchsia-500 dark:hover:bg-fuchsia-700 transition-colors rounded-full text-2xl font-medium text-white dark:invert cursor-pointer"
      >
        {labels.heroAction}
      </button>
    </a>
  </div>

  <div class="max-w-7xl text-black dark:text-fuchsia-50">
    <p class="text-4xl font-medium pt-16 pb-4 w-full">
      {labels.aboutTitle}
    </p>

    <p class="w-full text-lg pb-2">
      {labels.aboutBody}
    </p>
    <ol class="flex flex-col w-full gap-6 text-xl font-medium">
      <div class="flex flex-col gap-2">
        <p>{labels.systemAnalystTitle}</p>
        <div class="flex flex-wrap gap-2">
          <Chip>UML</Chip>
          <Chip>OpenAPI</Chip>
          <Chip>Linux</Chip>
          <Chip>{labels.systemAnalystDocumentation}</Chip>
          <Chip>Git</Chip>
        </div>
      </div>

      <div class="flex flex-col gap-2">
        <p>{labels.businessAnalystTitle}</p>
        <div class="flex flex-wrap gap-2">
          <Chip>BPMN 2.0</Chip>
          <Chip>{labels.businessAnalystMarketAnalysis}</Chip>
          <Chip>{labels.businessAnalystProjectManagement}</Chip>
        </div>
      </div>

      <div class="flex flex-col gap-2">
        <p>{labels.designerTitle}</p>
        <div class="flex flex-wrap gap-2">
          <Chip>Figma</Chip>
          <Chip>Photoshop</Chip>
          <Chip>Davince Resolve</Chip>
          <Chip>Material design</Chip>
        </div>
      </div>

      <div class="flex flex-col gap-2">
        <p>{labels.developerTitle}</p>
        <div class="flex flex-wrap gap-2">
          <Chip>{labels.developerMobile}</Chip>
          <Chip>{labels.developerWeb}</Chip>
          <Chip>{labels.developerDesktop}</Chip>
          <Chip>CLI</Chip>
        </div>
      </div>
    </ol>

    <p class="w-full text-lg pt-4">
      {labels.aboutBodySecondary}
    </p>

    <p class="text-4xl font-medium pt-16 pb-4 w-full">
      {labels.successfulProjects}
    </p>

    <div
      class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4 items-stretch"
    >
      <div>
        <Product
          title="Indexxo"
          support={labels.indexxoBody}
          imgSrc={indexxoImg}
          href="/indexxo"
        />
      </div>
      <div>
        <Product
          title="Sukko"
          support={labels.sukkoBody}
          imgSrc={sukkoImg}
          href="https://sadellie.github.io/sukko/"
        />
      </div>
      <div>
        <Product
          title="Unitto"
          support={labels.unittoBody}
          imgSrc={unittoImg}
          href="/unitto"
        />
      </div>
      <div>
        <Product
          title="sadBot"
          support={labels.sadbotBody}
          imgSrc={sadbotImg}
          href="https://github.com/sadellie/sadbot"
        />
      </div>
      <div>
        <Product
          title={labels.webIdiotTitle}
          support={labels.webIdiotBody}
          imgSrc={idiot}
          href="https://outofcontext.me/"
        />
      </div>
      <div>
        <Product
          title={labels.webPersonalTitle}
          support={labels.webPersonalBody}
          imgSrc={webImg}
          href="#"
        />
      </div>
      <div>
        <Product
          title={labels.commercialProjectsTitle}
          support={labels.commercialProjectsBody}
          imgSrc={secretImg}
          href="#contact"
        />
      </div>
    </div>

    <p class="text-4xl font-medium pt-16 pb-4 w-full">
      {labels.failedProductTitle}
    </p>

    <p>{labels.failedProductBody}</p>

    <p class="text-4xl font-medium pt-16 pb-4 w-full">{labels.contactMe}</p>

    <div
      class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4 items-stretch"
      id="contact"
    >
      <Contact title="Email" href="mailto:sadellie.dev@gmail.com" img={hero}>
        <Email />
      </Contact>
      <Contact title="Telegram" href="https://t.me/sadellie" img={hero}>
        <Telegram />
      </Contact>
      <Contact title="Github" href="https://github.com/sadellie" img={hero}>
        <Github />
      </Contact>
    </div>
  </div>
  <footer>
    <div class="pt-16">
      <p>
        Photos by <a
          class="font-medium text-blue-600 hover:text-blue-900 hover:underline"
          href="https://unsplash.com/@anniespratt">Annie Spratt</a
        >,
        <a
          class="font-medium text-blue-600 hover:text-blue-900 hover:underline"
          href="https://unsplash.com/@philipsfuture">Philip Oroni</a
        >
        and
        <a
          class="font-medium text-blue-600 hover:text-blue-900 hover:underline"
          href="https://unsplash.com/@pawel_czerwinski">Pawel Czerwinski</a
        >
        on
        <a
          class="font-medium text-blue-600 hover:text-blue-900 hover:underline"
          href="https://unsplash.com/">Unsplash</a
        >
      </p>
    </div>
  </footer>
</div>

<style>
  :root {
    scrollbar-width: auto;
  }
</style>
