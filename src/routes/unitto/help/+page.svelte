<script>
  import TextBodyLink from "../../../components/TextBodyLink.svelte";
  import Footer from "../Footer.svelte";
  import TextHeader1 from "../../../components/TextHeader1.svelte";
  import TextHeader2 from "../../../components/TextHeader2.svelte";
  import TextHeader3 from "../../../components/TextHeader3.svelte";
  import TextHeader4 from "../../../components/TextHeader4.svelte";
  import TextTitle from "../../../components/TextTitle.svelte";
  import { UnittoTheme } from "../UnittoTheme";
  import WallOfText from "../../../components/WallOfText.svelte";

  let addTimeZoneDetail = false;

  function toggleTimeZoneDetails() {
    addTimeZoneDetail = !addTimeZoneDetail;
  }
</script>

<WallOfText>
  <TextTitle>Help</TextTitle>
  <TextHeader1 theme={UnittoTheme} id="add-time-zones"
    >⌚ Add more time zones?</TextHeader1
  >
  <p>No.</p>
  <div class="{UnittoTheme.secondaryContainer} rounded-2xl p-4">
    <div class="flex flex-row items-center">
      <TextHeader2>But… why?</TextHeader2>
      <button on:click={toggleTimeZoneDetails}>
        <span
          class="transition-transform material-symbols-outlined rounded-full p-3 m-2 {UnittoTheme.onSecondaryContainerHover} cursor-pointer"
          class:rotate-180={addTimeZoneDetail}>expand_more</span
        >
      </button>
    </div>
    <div
      class="overflow-hidden"
      id="add-time-zones-detailed"
      class:max-h-0={!addTimeZoneDetail}
    >
      <p>Each time zone has its' own set of rules:</p>
      <ul class="list-disc list-inside">
        <li>Offset from GMT</li>
        <li>Daylight saving time offset</li>
        <li>Date when daylight saving time is used</li>
      </ul>
      <p>This data always changes.</p>
      <p>There are 3 solutions:</p>
      <TextHeader3>1. Paid API service</TextHeader3>
      <TextHeader4>✅Pros:</TextHeader4>
      <ul class="list-disc list-inside">
        <li>Almost all time zones and cities</li>
        <li>Always up-to-date</li>
      </ul>
      <TextHeader4>❌Cons:</TextHeader4>
      <ul class="list-disc list-inside">
        <li>Costs money</li>
        <li>Needs Internet, can go down, needs a caching mechanism</li>
        <li>Can change API and break Unitto</li>
        <li>Needs to be translated</li>
      </ul>
      <TextHeader3>2. Create my own API service</TextHeader3>
      <p>
        Pros and cons are same, except this one is free cheaper (you still need
        to pay).
      </p>
      <TextHeader3>
        3. Android's time zone provider (this is what Unitto uses)
      </TextHeader3>
      <p>
        read more: <TextBodyLink
          href="https://source.android.com/docs/core/permissions/timezone-rules"
          >https://source.android.com/docs/core/permissions/timezone-rules</TextBodyLink
        >
      </p>
      <TextHeader4>✅Pros:</TextHeader4>
      <ul class="list-disc list-inside">
        <li>Almost all time zones</li>
        <li>Free</li>
        <li>No need to translate (provided by system)</li>
        <li>Doesn't break Unitto</li>
        <li>Works offline, never goes down</li>
      </ul>
      <TextHeader4>❌Cons:</TextHeader4>
      <ul class="list-disc list-inside">
        <li>Less cities</li>
        <li>Less frequent updates (or none if you are unlucky)</li>
      </ul>
    </div>
  </div>
  <hr />
  <TextHeader1 theme={UnittoTheme} id="body-mass-index"
    >👩‍⚕️ Body Mass Index</TextHeader1
  >
  <p>
    Please note that the values displayed in the app are intended for
    entertainment purposes only. They can not replace professional medical
    advice. Please <b>don't</b> use Body Mass calculator if you are:
  </p>
  <ul class="list-disc list-inside">
    <li>Under 21</li>
    <li>Pregnant</li>
    <li>Diagnosed with an eating disorder</li>
  </ul>
  <p>Please contact your care provider for more information.</p>
  <hr />
  <Footer />
</WallOfText>
