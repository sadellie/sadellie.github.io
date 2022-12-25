<script setup lang="ts">
import UnittoCollapsedSidebarElement from '@/components/UnittoCollapsedSidebarElement.vue';
import UnittoSidebarElement from '@/components/UnittoSidebarElement.vue';
import UnittoTextLink from '@/components/UnittoTextLink.vue';
import { ref } from 'vue';
import { RouterLink, RouterView, useRouter } from 'vue-router';

const showSidebar = ref(false)

function toggleSidebar() {
    showSidebar.value = !showSidebar.value
}
function isTabActive(tab: string): boolean {
    return useRouter().currentRoute.value.name == tab
}
</script>

<template>
    <div class="relative bg-white">
        
        <div class="sticky top-0 z-10 md:hidden bg-white w-full flex flex-row p-1 items-center">
            <button @click="toggleSidebar">
                <span class="material-symbols-outlined hover:bg-slate-200 rounded-full p-3 m-2">
                    menu
                </span>
            </button>
            <RouterLink to="/unitto">
                <div class="text-lg font-medium hover:bg-slate-200 rounded-full p-3">Unitto</div>
            </RouterLink>
        </div>

        <transition enter-from-class="opacity-0" leave-to-class="opacity-0" enter-active-class="transition duration-300"
            leave-active-class="transition duration-300">
            <div v-if="showSidebar" class="z-20 md:hidden fixed top-0 w-full h-full bg-black opacity-25"
                @click="toggleSidebar"></div>
        </transition>
        <transition enter-from-class="translate-x-[-150%] opacity-0" leave-to-class="translate-x-[-150%] opacity-0"
            enter-active-class="transition duration-300" leave-active-class="transition duration-300">
            <div v-if="showSidebar" class="z-20 fixed top-0 h-full bg-white md:hidden">
                <div
                    class="text-black grid grid-cols-1 p-4 justify-start justify-items-start justify-self-start content-start place-content-start">
                    <button @click="toggleSidebar">
                        <span class="material-symbols-outlined hover:bg-slate-200 rounded-full p-3 mb-2">
                            menu_open
                        </span>
                    </button>
                    <nav>
                        <RouterLink to="/unitto">
                            <UnittoSidebarElement name="Home" icon="home" :selected="isTabActive('home')"
                                @click="toggleSidebar" />
                        </RouterLink>
                        <RouterLink to="/unitto/privacy">
                            <UnittoSidebarElement name="Privacy policy" icon="policy" :selected="isTabActive('privacy')"
                                @click="toggleSidebar" />
                        </RouterLink>
                        <RouterLink to="/unitto/terms">
                            <UnittoSidebarElement name="Terms and Conditions" icon="privacy_tip"
                                :selected="isTabActive('terms')" @click="toggleSidebar" />
                        </RouterLink>
                        <RouterLink to="/unitto/press">
                            <UnittoSidebarElement name="Press Kit" icon="folder_shared" :selected="isTabActive('press')"
                                @click="toggleSidebar" />
                        </RouterLink>
                    </nav>
                </div>
            </div>
        </transition>
        <!-- Collapsed -->
        <div class="flex flex-row relative">
            <div class="sticky top-0 h-screen py-2 bg-green-100 hidden md:block">
                <div class="flex flex-col w-24 gap-4">
                    <RouterLink to="/unitto">
                        <UnittoCollapsedSidebarElement name="Home" icon="home" :selected="isTabActive('home')"
                            @click="toggleSidebar" />
                    </RouterLink>
                    <RouterLink to="/unitto/privacy">
                        <UnittoCollapsedSidebarElement name="Privacy policy" icon="policy"
                            :selected="isTabActive('privacy')" @click="toggleSidebar" />
                    </RouterLink>
                    <RouterLink to="/unitto/terms">
                        <UnittoCollapsedSidebarElement name="Terms and Conditions" icon="privacy_tip"
                            :selected="isTabActive('terms')" @click="toggleSidebar" />
                    </RouterLink>
                    <RouterLink to="/unitto/press">
                        <UnittoCollapsedSidebarElement name="Press Kit" icon="folder_shared"
                            :selected="isTabActive('press')" @click="toggleSidebar" />
                    </RouterLink>
                </div>
            </div>
            <div class="grid grid-cols-1 gap-8 p-4">

                <router-view v-slot="{ Component }">
                    <transition name="fade">
                        <KeepAlive>
                            <component :is="Component" />
                        </KeepAlive>
                    </transition>
                </router-view>
                
                <hr>
                <footer>
                    <div class="grid grid-cols-1 p-4 gap-4">
                        <div class="flex justify-start items-center gap-4">
                            <img class="w-28 rounded-full border-2 hover:scale-110 hover:-translate-y-5 transition-all hover:shadow-2xl"
                                src="@/assets/icon.png">
                            <p>
                                Unitto is a modern and easy to use unit converter and calculator for Android devices.
                            </p>
                        </div>
                        <div class="flex flex-wrap gap-x-8">
                            <RouterLink to="/">
                                <p class="font-bold hover:underline">by Sad Ellie</p>
                            </RouterLink>
                            <UnittoTextLink href="https://forms.gle/YRKapCk91J63gzM27">Anonymous request</UnittoTextLink>
                            <UnittoTextLink href="https://github.com/sadellie/unitto">GitHub</UnittoTextLink>
                            <UnittoTextLink href="mailto:sadellie.dev@gmail.com">Email</UnittoTextLink>
                            <UnittoTextLink href="https://trello.com/b/cxAbRlvu/unitto">Trello board</UnittoTextLink>
                        </div>
                    </div>
                </footer>
            </div>
        </div>
    </div>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.225s ease-in-out;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}
</style>