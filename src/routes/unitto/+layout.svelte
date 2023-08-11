<script lang="ts">
    import { page } from "$app/stores";
    import Scrim from "./Scrim.svelte";
    import TabListItemHorizontal from "./TabListItemHorizontal.svelte";
    import TabListItemVertical from "./TabListItemVertical.svelte";
    import TopBar from "./TopBar.svelte";

    function openMenu() {
        document
            .getElementById("drawer")
            ?.classList.replace("-translate-x-full", "translate-x-0");
        document
            .getElementById("scrim")
            ?.classList.replace("hidden", "visible");
    }

    function closeMenu() {
        document
            .getElementById("drawer")
            ?.classList.replace("translate-x-0", "-translate-x-full");
        document
            .getElementById("scrim")
            ?.classList.replace("visible", "hidden");
    }
</script>

<div class="relative bg-white">
    <!-- Top bar -->
    <TopBar on:menuClick={openMenu} />

    <!-- Scrim -->
    <Scrim on:menuClick={closeMenu} />

    <!-- Nav bar -->
    <div
        class="lg:hidden z-20 fixed top-0 h-full transition-transform -translate-x-full px-2 w-80 rounded-e-3xl bg-unitto-surface"
        id="drawer"
    >
        <button on:click={closeMenu}>
            <span
                class="material-symbols-outlined hover:bg-unitto-surfaceContainer-inactive-hover rounded-full p-3 m-2"
            >
                menu_open
            </span>
        </button>
        <TabListItemHorizontal
            title="Overview"
            icon="home"
            isSelected={$page.url.pathname === "/unitto"}
            href="/unitto"
            on:onNavigate={closeMenu}
        />
        <TabListItemHorizontal
            title="Privacy"
            icon="policy"
            isSelected={$page.url.pathname === "/unitto/privacy"}
            href="/unitto/privacy"
            on:onNavigate={closeMenu}
        />
        <TabListItemHorizontal
            title="Terms and Conditions"
            icon="privacy_tip"
            isSelected={$page.url.pathname === "/unitto/terms"}
            href="/unitto/terms"
            on:onNavigate={closeMenu}
        />
    </div>

    <div class="flex flex-row relative">
        <div class="hidden lg:block sticky top-0 h-screen bg-unitto-surface">
            <!-- Navigation rail -->
            <div class="flex flex-col gap-4 pt-6">
                <TabListItemVertical
                    title="Overview"
                    icon="home"
                    isSelected={$page.url.pathname === "/unitto"}
                    href="/unitto"
                />
                <TabListItemVertical
                    title="Privacy"
                    icon="policy"
                    isSelected={$page.url.pathname === "/unitto/privacy"}
                    href="/unitto/privacy"
                />
                <TabListItemVertical
                    title="Terms and Conditions"
                    icon="privacy_tip"
                    isSelected={$page.url.pathname === "/unitto/terms"}
                    href="/unitto/terms"
                />
            </div>
        </div>
        <slot />
    </div>
</div>
