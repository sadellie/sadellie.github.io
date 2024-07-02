<script lang="ts">
  import type { DrawerItem } from "../../components/IDrawerItem";
  import { UnittoTheme } from "./UnittoTheme";
  import AdaptiveLayout from "../../components/AdaptiveLayout.svelte";
  import unittoLogo from "$lib/images/unitto/unitto-logo.svg";
  import { onMount } from "svelte";

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

  onMount(async () => {
    const root: HTMLElement = document?.querySelector(":root") as HTMLElement;
    root.style?.setProperty(
      "scrollbar-color",
      "rgba(0, 0, 0, 0.7) rgb(16, 21, 16)"
    );
  });
</script>

<AdaptiveLayout
  theme={UnittoTheme}
  {drawerItems}
  title="Unitto"
  homeHref="/unitto"
  logo={unittoLogo}
>
  <slot></slot>
</AdaptiveLayout>

<style>
  :root {
    scrollbar-width: auto;
  }
</style>
