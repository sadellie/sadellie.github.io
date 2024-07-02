<script lang="ts">
  import { page } from "$app/stores";
  import type { DrawerItem } from "./IDrawerItem";
  import type M3Theme from "./M3Theme";
  import Scrim from "./Scrim.svelte";
  import NavigationDrawerItem from "./NavigationDrawerItem.svelte";
  import NavigationRailItem from "./NavigationRailItem.svelte";
  import TopAppBarSmall from "./TopAppBarSmall.svelte";
  import NavigationRail from "./NavigationRail.svelte";
  import NavigationDrawer from "./NavigationDrawer.svelte";

  export let theme: M3Theme;
  export let drawerItems: Array<DrawerItem>;
  export let title: string;
  export let logo: string
  export let homeHref: string;

  const drawerId = "drawer";
  const scrimId = "scrim";

  function openMenu() {
    document
      .getElementById(drawerId)
      ?.classList.replace("-translate-x-full", "translate-x-0");
    document.getElementById(scrimId)?.classList.replace("hidden", "visible");
  }

  function closeMenu() {
    document
      .getElementById(drawerId)
      ?.classList.replace("translate-x-0", "-translate-x-full");
    document.getElementById(scrimId)?.classList.replace("visible", "hidden");
  }

  console.log($page.route.id);
</script>

<div class="relative {theme.background} {theme.onBackgroundText} min-h-screen">
  <!-- Top bar -->
  <TopAppBarSmall
    on:menuClick={openMenu}
    {theme}
    title={title}
    logo={logo}
    logoHref={homeHref}
  />

  <!-- Scrim -->
  <Scrim on:menuClick={closeMenu} id={scrimId} />

  <NavigationDrawer {theme} on:menuClick={closeMenu} id={drawerId}>
    {#each drawerItems as item}
      <NavigationDrawerItem
        title={item.titls}
        icon={item.icon}
        isSelected={$page.route.id === item.href}
        href={item.href}
        {theme}
        on:onTabClick={closeMenu}
      />
    {/each}
  </NavigationDrawer>

  <div class="flex flex-row relative">
    <NavigationRail {theme}>
      {#each drawerItems as item}
        <NavigationRailItem
          title={item.titls}
          icon={item.icon}
          isSelected={$page.route.id === item.href}
          href={item.href}
          {theme}
        />
      {/each}
    </NavigationRail>
    <slot />
  </div>
</div>
