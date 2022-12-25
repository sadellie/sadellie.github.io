<script setup lang="ts">
import UnittoBlockWithImage from './UnittoBlockWithImage.vue';
import UnittoTextH1 from './UnittoTextH1.vue';
import UnittoTextLink from './UnittoTextLink.vue';

</script>

<template>
  <div class="flex flex-col gap-8">
    <p class="text-3xl font-bold">
      Press kit
    </p>
    <UnittoTextH1>
      General information
    </UnittoTextH1>
    <p>
      Developer:
      <RouterLink to="/">
        <UnittoTextLink>
          Sad Ellie
        </UnittoTextLink>
      </RouterLink>
    </p>
    <p>Release date: February 19th 2022</p>
    <UnittoTextH1>
      What is Unitto?
    </UnittoTextH1>
    <p>
      Unitto is a free modern unit converter and calculator. It's an Open source project.
    </p>
    <UnittoTextH1>
      Goals
    </UnittoTextH1>
    <p>
      Make an easy to use yet powerful and customizable app that doesn't reinvent the wheel.
    </p>
    <UnittoBlockWithImage title="Design guidelines"
      body="Unitto's design is based on Google's Material Design 3 guidelines. As a lot of people are already familiar with language translators, such apps were used as design references: buttons placement, units selection screen, main app logic in general. It keeps it's users as efficient as possible, allowing them to convert units and resume their activity as quick as possible.">
      <img class="border-2 rounded-3xl p-2" src="@/assets/unitto-press-design.svg" alt="design">
    </UnittoBlockWithImage>
    <UnittoBlockWithImage title="More than 430 units"
      body="Even though this number will grow, finding and choosing needed units stays simple and quick thanks to group filters, favorites filter and search functionality.">
      <img class="border-2 rounded-3xl" src="@/assets/unitto-press-units.svg" alt="units">
    </UnittoBlockWithImage>
    <UnittoBlockWithImage title="SI Standard*"
      body="For example, kilobyte is equal to 1000 bytes, not 1024. Many competitors fail to understand this user need.">
      <img class="border-2 rounded-3xl p-2" src="@/assets/unitto-press-si.svg" alt="si">
    </UnittoBlockWithImage>
    <UnittoBlockWithImage title="Personalized experience"
      body="Unitto provides a wide range of different settings, which allows the application to adapt to each user individually.">
      <img class="border-2 rounded-3xl p-2" src="@/assets/unitto-press-experience.svg" alt="experience">
    </UnittoBlockWithImage>

    <UnittoTextH1>
      App name
    </UnittoTextH1>

    <UnittoBlockWithImage title="" body="App is called 'Unitto' after one of the variables in source code — 'unitTo' — which comes from 'unit to converter
      to'">
      <img class="border-2 rounded-3xl p-2" src="@/assets/unitto-press-name.svg" alt="name">
    </UnittoBlockWithImage>

    <UnittoBlockWithImage title="Version codenames"
      body="Color names are used for codenames. They go in alphabetical order. Each update is unique and always makes the app better, bringing new features, improving UX and increasing app's stability.">
      <img class="border-2 rounded-3xl p-2" src="@/assets/unitto-press-codenames.svg" alt="codenames">
    </UnittoBlockWithImage>

    <UnittoTextH1>
      It's cool and all… but how?
    </UnittoTextH1>
    <p>
      Unitto is my first Android project. I tried to use all the latest technologies and libraries:
    </p>
    <ul class="flex flex-col gap-1 list-decimal list-inside">
      <li>Jetpack Compose</li>
      <li>Room</li>
      <li>Hilt</li>
      <li>DataStore</li>
      <li>Firebase</li>
      <li>Material Design 3 Components</li>
      <li>Retrofit</li>
      <li>Moshi</li>
      <li>Currency API</li>
      <li>ExprK</li>
    </ul>

    <UnittoTextH1>
      Background images by:
    </UnittoTextH1>
    <ul class="flex flex-col gap-1 list-disc list-inside">
      <li>
        <UnittoTextLink href="https://unsplash.com/@pawel_czerwinski">Pawel Czerwinski</UnittoTextLink>
      </li>
      <li>
        <UnittoTextLink href="https://unsplash.com/@hans_isaacson">Hans Isaacson</UnittoTextLink>
      </li>
      <li>
        <UnittoTextLink href="https://unsplash.com/@flyd2069">FLY:D</UnittoTextLink>
      </li>
    </ul>

  </div>
</template>
