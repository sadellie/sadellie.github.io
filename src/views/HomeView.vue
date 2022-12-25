<script setup lang="ts">
import ProjectElement from '@/components/HomeProjectElement.vue'
import Header from '@/components/HomeHeader.vue';
import type { Project } from '@/common/Interfaces';

let allProjects: Project[] = [
  {
    projectName: "Indexxo",
    shortDescription: "File indexer with web frontend",
    features: [
      "Fast file search from any device",
      "Secure remote access to your files",
      "User friendly experience",
      "Highly customizable"
    ],
    stack: [
      "Vue.js",
      "Vue Router",
      "TypeScript",
      "Python",
      "Flask",
      "SQL",
      "Tailwind CSS",
    ],
    projectLink: "https://github.com/sadellie/indexxo",
    cover: './src/assets/home-cover-indexxo.svg',
  },
  {
    projectName: "Unitto",
    shortDescription: "Unit converter and calculator",
    features: [
      "More than 430 units",
      "Very precise conversion",
      "SI Standard",
      "Dynamic Theming",
      "Highly customizable",
    ],
    stack: [
      "Kotlin and Coroutines",
      "Jetpack Compose",
      "Jetpack Navigation",
      "Jetpack DataStore",
      "Hilt/Dagger2",
      "Material Design 3 Components",
      "Retrofit",
      "Moshi",
      "Firebase Analytics",
      "Firebase Crashlytics",
    ],
    projectLink: "/unitto",
    cover: './src/assets/home-cover-unitto.svg',
  },
  {
    projectName: "sadBot",
    shortDescription: "VK chat bot for students",
    features: [
      "Easily adapts to your needs",
      "Teachers names database",
      "Exams schedule database",
      "Keeps your chats clean",
    ],
    stack: [
      "Python",
      "VK API",
      "vkbottle",
      "aiohttp",
      "xlwt",
      "xlrd",
      "pandas",
    ],
    projectLink: "https://vk.link/sadb0t",
    cover: './src/assets/home-cover-sadbot.svg',
  },
  {
    projectName: "Web",
    shortDescription: "This and other webpages",
    features: [
      "Responsive",
      "CSS Animations",
      "SVG Morphing",
      "It looks nice, facts",
    ],
    stack: [
      "HTML5",
      "CSS",
      "Vue",
      "Tailwind",
      "TypeScript",
      "JavaScript",
      "Bootstrap 5",
      "GitHub Pages",
      "Figma",
    ],
    projectLink: "#",
    cover: './src/assets/home-cover-web.svg',
  },
  {
    projectName: "Others",
    shortDescription: "Secret commercial projects",
    features: [
      "You can't learn more, lol"
    ],
    stack: [
      "Python",
      "Bash",
      "CSV",
      "JSON",
      "VBA",
      "C#"
    ],
    projectLink: "#",
    cover: './src/assets/home-cover-other.svg',
  },
]

function scrollToPortfolio() {
  document.getElementById('about')?.scrollIntoView({behavior: 'smooth'})
}

</script>

<template>
  <div class="container mx-auto p-6">
    <div class="grid grid-cols-1 sm:grid-cols-2">
      <div class="flex flex-col place-content-center justify-self-center">
        <p class="text-6xl font-bold">Sad Ellie</p>
        <p class="text-3xl font-bold text-fuchsia-700 my-2">yung developer</p>
        <p class="text-2xl flex gap-2 my-2">Contact me
          <span class="flex gap-2">
            <a href="https://github.com/sadellie/">
              <svg class="w-8 h-8 hover:fill-fuchsia-700 transition ease-in-out" xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 496 512"><!--! Font Awesome Pro 6.2.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. -->
                <path
                  d="M165.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3.3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6zm-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5.3-6.2 2.3zm44.2-1.7c-2.9.7-4.9 2.6-4.6 4.9.3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9zM244.8 8C106.1 8 0 113.3 0 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C428.2 457.8 496 362.9 496 252 496 113.3 383.5 8 244.8 8zM97.2 352.9c-1.3 1-1 3.3.7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1zm-10.8-8.1c-.7 1.3.3 2.9 2.3 3.9 1.6 1 3.6.7 4.3-.7.7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3.7zm32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3.7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1zm-11.4-14.7c-1.6 1-1.6 3.6 0 5.9 1.6 2.3 4.3 3.3 5.6 2.3 1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2z" />
              </svg>
            </a>
            <a href="https://www.linkedin.com/in/sadellie/">
              <svg class="w-8 h-8 hover:fill-fuchsia-700 transition ease-in-out" xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 448 512"><!--! Font Awesome Pro 6.2.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. -->
                <path
                  d="M416 32H31.9C14.3 32 0 46.5 0 64.3v383.4C0 465.5 14.3 480 31.9 480H416c17.6 0 32-14.5 32-32.3V64.3c0-17.8-14.4-32.3-32-32.3zM135.4 416H69V202.2h66.5V416zm-33.2-243c-21.3 0-38.5-17.3-38.5-38.5S80.9 96 102.2 96c21.2 0 38.5 17.3 38.5 38.5 0 21.3-17.2 38.5-38.5 38.5zm282.1 243h-66.4V312c0-24.8-.5-56.7-34.5-56.7-34.6 0-39.9 27-39.9 54.9V416h-66.4V202.2h63.7v29.2h.9c8.9-16.8 30.6-34.5 62.9-34.5 67.2 0 79.7 44.3 79.7 101.9V416z" />
              </svg>
            </a>
            <a href="mailto:sadellie.dev@gmail.com">
              <svg class="w-8 h-8 hover:fill-fuchsia-700 transition ease-in-out" xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 512 512"><!--! Font Awesome Pro 6.2.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. -->
                <path
                  d="M64 112c-8.8 0-16 7.2-16 16v22.1L220.5 291.7c20.7 17 50.4 17 71.1 0L464 150.1V128c0-8.8-7.2-16-16-16H64zM48 212.2V384c0 8.8 7.2 16 16 16H448c8.8 0 16-7.2 16-16V212.2L322 328.8c-38.4 31.5-93.7 31.5-132 0L48 212.2zM0 128C0 92.7 28.7 64 64 64H448c35.3 0 64 28.7 64 64V384c0 35.3-28.7 64-64 64H64c-35.3 0-64-28.7-64-64V128z" />
              </svg>
            </a>
          </span>
        </p>
        <div class="flex place-content-center">
          <button
            class="flex bg-fuchsia-700 rounded-full text-white font-medium text-xl px-8 py-4 my-2 transition-all ease-linear shadow-2xl hover:shadow-fuchsia-700 hover:bg-fuchsia-900"
            @click="scrollToPortfolio()">
            Portfolio
          </button>
        </div>
      </div>
      <div class="w-full flex place-content-center justify-self-center">
        <img class="w-auto h-96 justify-center" src="@/assets/hero-anim.svg" alt="hero logo">
      </div>
    </div>
    <Header name="About me" id="about"></Header>
    <p class="text-center text-xl font-medium mt-4 mb-8">
      I am a self-taught developer. My goal is to create great software products that make life easier.
    </p>
    <Header name="Projects"></Header>
    <div class="grid gap-4 divide-y-2 divide-solid">
      <ProjectElement class="pt-4" v-for="project in allProjects" :project="project"/>
    </div>
  </div>
</template>

<style scoped>
html {
  scroll-behavior: smooth
}

/* SCROLLBAR */
::-webkit-scrollbar {
  width: 15px;
}

::-webkit-scrollbar-thumb {
  background: rgba(177, 0, 175, 0.5);
  border-radius: 15px;
}

::-webkit-scrollbar-thumb:hover {
  background: #B100AF;
}
</style>
