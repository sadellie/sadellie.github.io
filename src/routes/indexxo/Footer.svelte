<script lang="ts">
  import TextBodyLink from "../../components/TextBodyLink.svelte";
  import { IndexxoTheme } from "./IndexxoTheme";
  import logoImg from "$lib/images/indexxo/logo_dark_color.svg";
</script>

<footer>
  <hr class={IndexxoTheme.outlineVariantBorder} />
  <div class="grid grid-cols-1 group p-4 gap-4 mb-2">
    <div class="flex justify-start items-center gap-4">
      <img
        class="w-28 rounded-3xl group-hover:scale-110 group-hover:-translate-y-1 transition-all group-hover:shadow-2xl"
        src={logoImg}
        alt="indexxo"
      />
      <p>Indexxo is an app for file management.</p>
    </div>
    <div class="flex flex-wrap gap-x-8">
      <TextBodyLink href="/">
        <p class="font-bold hover:underline">by Sad Ellie</p>
      </TextBodyLink>
      <TextBodyLink href="https://github.com/sadellie/indexxo"
        >GitHub</TextBodyLink
      >
      <TextBodyLink href="mailto:sadellie.dev@gmail.com">Email</TextBodyLink>
      <TextBodyLink href="https://github.com/users/sadellie/projects/4"
        >Task tracker</TextBodyLink
      >
    </div>
  </div>
</footer>
