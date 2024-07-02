<script>
  import Footer from "./Footer.svelte";
  import { IndexxoTheme } from "./IndexxoTheme";

  const demoLink = "./demo/index.html";
</script>

<div class="w-full">
  <div class="max-w-7xl m-auto px-4">
    <div class="w-full flex flex-col gap-4">
      <div class="flex flex-col py-12 gap-4 items-center">
        <p
          class="{IndexxoTheme.onBackgroundText} text-3xl md:text-5xl text-center"
        >
          Indexxo. File management for humans
        </p>
        <p class="{IndexxoTheme.onBackgroundText} text-center">
          Find similar, duplicate and empty files in your storage. Free up space
          for what really matters.
        </p>

        <div class="flex flex-col sm:flex-row gap-2 items-center">
          <a href="https://github.com/sadellie/indexxo/">
            <button
              type="button"
              class="rounded-full overflow-hidden {IndexxoTheme.primary}"
            >
              <div
                class="flex flex-row justify-center items-center h-12 sm:h-16 px-8 sm:px-10 {IndexxoTheme.onPrimaryHover}"
              >
                <p class="text-md sm:text-2xl {IndexxoTheme.onPrimaryText}">
                  Download
                </p>
              </div>
            </button>
          </a>
          <a href={demoLink}>
            <button
              type="button"
              class="rounded-full overflow-hidden {IndexxoTheme.outlineVariantBorder}"
            >
              <div
                class="flex flex-row justify-center items-center h-12 sm:h-16 px-8 sm:px-10 {IndexxoTheme.onSurfaceHover}"
              >
                <p
                  class="text-md sm:text-2xl text-center {IndexxoTheme.onSurfaceText}"
                >
                  Try in browser
                </p>
              </div>
            </button>
          </a>
        </div>
      </div>

      <a href={demoLink} class="flex flex-col items-center">
        <button
          style="background-image: url(/src/lib/images/indexxo/hero.png);"
          class="group max-w-screen-sm w-full aspect-[840/900] bg-center bg-cover flex flex-col justify-center hover:brightness-50 place-items-center rounded-xl hover:rounded-2xl transition-all bg-origin-content bg-no-repeat hover:p-2 {IndexxoTheme.secondaryContainer}"
        />
      </a>
      <Footer />
    </div>
  </div>
</div>
