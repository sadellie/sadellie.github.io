<script lang="ts">
  import unittoLogo from "$lib/images/unitto/unitto-logo.svg";
  import TextBodyLink from "../../components/TextBodyLink.svelte";
  import { UnittoTheme } from "./UnittoTheme";
</script>

<footer>
  <div class="grid grid-cols-1 p-4 gap-4">
    <div class="flex justify-start items-center gap-4">
      <img
        class="w-28 p-2 rounded-3xl border-2 {UnittoTheme.outlineBorder} hover:scale-110 hover:-translate-y-5 transition-all hover:shadow-2xl"
        src={unittoLogo}
        alt="unitto"
      />
      <p>
        Unitto is a unique modern calculator and unit converter for mobile
        devices.
      </p>
    </div>
    <div class="flex flex-wrap gap-x-8">
      <TextBodyLink href="/">
        <p class="font-bold hover:underline">by Sad Ellie</p>
      </TextBodyLink>
      <TextBodyLink href="https://forms.gle/YRKapCk91J63gzM27"
        >Anonymous request</TextBodyLink
      >
      <TextBodyLink href="https://github.com/sadellie/unitto"
        >GitHub</TextBodyLink
      >
      <TextBodyLink href="mailto:sadellie.dev@gmail.com">Email</TextBodyLink>
      <TextBodyLink href="https://github.com/users/sadellie/projects/2"
        >Task tracker</TextBodyLink
      >
    </div>
    <div>
      <p>
        Photos by <TextBodyLink href="https://unsplash.com/@diegocarneiro"
          >Diego Carneiro</TextBodyLink
        >,
        <TextBodyLink href="https://unsplash.com/@martz90"
          >Martin Martz</TextBodyLink
        > and
        <TextBodyLink href="https://unsplash.com/@pawel_czerwinski"
          >Pawel Czerwinski</TextBodyLink
        >
        on
        <TextBodyLink href="https://unsplash.com/">Unsplash</TextBodyLink>
      </p>
    </div>
  </div>
</footer>
