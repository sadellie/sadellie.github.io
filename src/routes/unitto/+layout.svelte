<script lang="ts">
  import { page } from "$app/stores";
  import type { DrawerItem } from "./IDrawerItem";
  import Scrim from "./Scrim.svelte";
  import TabListItemHorizontal from "./TabListItemHorizontal.svelte";
  import TabListItemVertical from "./TabListItemVertical.svelte";
  import TopBar from "./TopBar.svelte";

  const drawerItems: Array<DrawerItem> = [
    {
      href: "/unitto",
      titls: "Overview",
      icon: "home",
    },
    {
      href: "/unitto/privacy",
      titls: "Privacy",
      icon: "policy",
    },
    {
      href: "/unitto/terms",
      titls: "Terms and Conditions",
      icon: "privacy_tip",
    },
    {
      href: "/unitto/help",
      titls: "Help",
      icon: "help",
    },
  ];

  function openMenu() {
    document
      .getElementById("drawer")
      ?.classList.replace("-translate-x-full", "translate-x-0");
    document.getElementById("scrim")?.classList.replace("hidden", "visible");
  }

  function closeMenu() {
    document
      .getElementById("drawer")
      ?.classList.replace("translate-x-0", "-translate-x-full");
    document.getElementById("scrim")?.classList.replace("visible", "hidden");
  }

  console.log($page.route.id)
</script>

<div class="relative bg-unitto-dark-background text-unitto-dark-onBackground">
  <!-- Top bar -->
  <TopBar on:menuClick={openMenu} />

  <!-- Scrim -->
  <Scrim on:menuClick={closeMenu} />

  <!-- Nav bar -->
  <div
    class="lg:hidden z-20 fixed top-0 h-full transition-transform -translate-x-full px-2 w-80 rounded-e-3xl bg-unitto-dark-surface text-unitto-dark-onSurface"
    id="drawer"
  >
    <button on:click={closeMenu}>
      <span
        class="material-symbols-outlined hover:bg-unitto-dark-surfaceContainer-inactive-hover rounded-full p-3 m-2"
      >
        menu_open
      </span>
    </button>
    {#each drawerItems as item}
      <TabListItemHorizontal
        title={item.titls}
        icon={item.icon}
        isSelected={$page.route.id === item.href}
        href={item.href}
        on:onNavigate={closeMenu}
      />
    {/each}
  </div>

  <div class="flex flex-row relative">
    <div
      class="hidden lg:block sticky top-0 h-screen bg-unitto-dark-surface text-unitto-dark-onSurface"
    >
      <!-- Navigation rail -->
      <div class="flex flex-col gap-4 pt-6">
        {#each drawerItems as item}
          <TabListItemVertical
            title={item.titls}
            icon={item.icon}
            isSelected={$page.route.id === item.href}
            href={item.href}
          />
        {/each}
      </div>
    </div>
    <slot />
  </div>
</div>
