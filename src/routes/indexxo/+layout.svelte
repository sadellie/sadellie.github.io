<script lang="ts">
  import type { DrawerItem } from "../../components/IDrawerItem";
  import { IndexxoTheme } from "./IndexxoTheme";
  import AdaptiveLayout from "../../components/AdaptiveLayout.svelte";
  import logoImg from "$lib/images/indexxo/logo_dark_color.svg";
  import { onMount } from "svelte";

  const drawerItems: Array<DrawerItem> = [
    {
      href: "/indexxo",
      title: "Overview",
      icon: "home",
    },
    {
      href: "/indexxo/privacy",
      title: "Privacy",
      icon: "policy",
    },
    {
      href: "/indexxo/terms",
      title: "Terms and Conditions",
      icon: "privacy_tip",
    },
    {
      href: "/indexxo/help",
      title: "Help",
      icon: "help",
    },
  ];

  onMount(async () => {
    const root: HTMLElement = document?.querySelector(":root") as HTMLElement;
    root.style?.setProperty(
      "scrollbar-color",
      "rgb(34, 25, 28) rgb(25, 17, 19)"
    );
  });
</script>

<AdaptiveLayout
  theme={IndexxoTheme}
  {drawerItems}
  title="Indexxo"
  homeHref="/indexxo"
  logo={logoImg}
>
  <slot></slot>
</AdaptiveLayout>

<style>
  :root {
    scrollbar-width: auto;
  }
</style>

<head>
  <link rel="icon" href="{logoImg}">
</head>
