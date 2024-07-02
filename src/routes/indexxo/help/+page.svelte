<script lang="ts">
  import WallOfText from "../../../components/WallOfText.svelte";
  import TextTitle from "../../../components/TextTitle.svelte";
  import { IndexxoTheme } from "../IndexxoTheme";
  import TextHeader1 from "../../../components/TextHeader1.svelte";
  import TextHeader2 from "../../../components/TextHeader2.svelte";
  import Footer from "../Footer.svelte";
</script>

<WallOfText>
  <TextTitle>Help</TextTitle>
  <div class="{IndexxoTheme.secondaryContainer} rounded-2xl p-4">
    <p>❗ Images will be added in open beta stage.</p>
  </div>

  <TextHeader1 theme={IndexxoTheme} id="help2">Working with presets</TextHeader1
  >

  <p>
    When launching Indexxo for the first time, you will be asked to create a
    preset. If you have multiple storages (folders) and want them to be
    processed differently, you can create a preset for each of your storages.
    Presets help you organize Indexxo settings.
  </p>

  <TextHeader2>What is a preset?</TextHeader2>
  <p>
    Preset is a saved set of settings that you can instantly switch between. You
    can create and edit as much presets as you want.
  </p>

  <hr class={IndexxoTheme.outlineVariantBorder} />

  <TextHeader1 theme={IndexxoTheme} id="files-and-folders"
    >How to choose files and directories</TextHeader1
  >
  <p>Indexxo needs at least 1 file or folder to index.</p>
  <ul class="list-disc list-inside">
    <li>Open preset settings</li>
    <li>
      Click on one of the <b>Add</b> buttons depending on what you want to include
    </li>
    <li>Switch to <b>Excluded</b> tab if you want to exclude something</li>
  </ul>

  <hr class={IndexxoTheme.outlineVariantBorder} />

  <TextHeader1 theme={IndexxoTheme} id="duplicate-files"
    >Find duplicate files</TextHeader1
  >
  <p>
    Indexxo decides whether files are identical or not based on their hash.
    Empty files and folders are not analyzed.
  </p>

  <ul class="list-disc list-inside">
    <li>Choose files that you want to analyze</li>
    <li>Open <b>Analyzers</b> in preset settings</li>
    <li>Turn on <b>Duplicate hashes</b></li>
    <li>Return to preset settings</li>
    <li>Click <b>Start</b></li>
    <li>
      Click <b>Resolve duplicate hashes</b> card. It will be present if there are
      files with duplicate hashes in your storage.
    </li>

    <li>You can now select and delete files that you do not need</li>
  </ul>

  <hr class={IndexxoTheme.outlineVariantBorder} />

  <TextHeader1 theme={IndexxoTheme} id="empty-files"
    >Find empty files</TextHeader1
  >
  <p>Indexxo decides whether files are empty based on their size.</p>

  <ul class="list-disc list-inside">
    <li>Choose files that you want to analyze</li>
    <li>Open <b>Analyzers</b> in preset settings</li>
    <li>Turn on <b>Empty files</b></li>
    <li>Return to preset settings</li>
    <li>Click <b>Start</b></li>
    <li>
      Click <b>Resolve empty files</b> card. It will be present if there are empty
      files in your storage.
    </li>
    <li>You can now select and delete files that you do not need</li>
  </ul>

  <hr class={IndexxoTheme.outlineVariantBorder} />

  <TextHeader1 theme={IndexxoTheme} id="empty-folders"
    >Find empty folders</TextHeader1
  >
  <p>
    Indexxo decides whether folders are empty based on their content. Be aware
    that folder can still have files if have explicitly excluded them.
  </p>

  <ul class="list-disc list-inside">
    <li>Choose folders that you want to analyze</li>
    <li>Open <b>Analyzers</b> in preset settings</li>
    <li>Turn on <b>Empty folders</b></li>
    <li>Return to preset settings</li>
    <li>Click <b>Start</b></li>
    <li>
      Click <b>Resolve empty folders</b> card. It will be present if there are empty
      folders in your storage.
    </li>
    <li>You can now select and delete files that you do not need</li>
  </ul>

  <hr class={IndexxoTheme.outlineVariantBorder} />

  <TextHeader1 theme={IndexxoTheme} id="duplicate-names"
    >Find files and folders with identical names</TextHeader1
  >
  <p>
    Indexxo decides whether names are identical based on their full name,
    including extension. This analyzer is case-insensitive.
  </p>

  <ul class="list-disc list-inside">
    <li>Choose files and folders that you want to analyze</li>
    <li>Open <b>Analyzers</b> in preset settings</li>
    <li>
      Turn on <b>Duplicate file names</b> and/or <b>Duplicate folder names</b>
    </li>
    <li>Return to preset settings</li>
    <li>Click <b>Start</b></li>
    <li>
      Click <b>Resolve duplicate file names</b> or
      <b>Resolve duplicate folders names</b> cards. They will be present if there
      are duplicate file/folder names in your storage.
    </li>
    <li>You can now select and delete files that you do not need</li>
  </ul>

  <hr class={IndexxoTheme.outlineVariantBorder} />

  <TextHeader1 theme={IndexxoTheme} id="similar-images"
    >Find similar images</TextHeader1
  >
  <p>Indexxo can find similar images even if they were modified.</p>

  <ul class="list-disc list-inside">
    <li>Choose files that you want to analyze</li>
    <li>Open <b>Analyzers</b> in preset settings</li>
    <li>Turn on <b>Similar images</b></li>
    <li>Modify this settings if needed by clicking the gear button</li>
    <li>Return to preset settings</li>
    <li>Click <b>Start</b></li>
    <li>
      Click <b>Resolve similar images</b> card. It will be present if there are similar
      images in your storage.
    </li>
    <li>You can now select and delete files that you do not need</li>
  </ul>

  <hr class={IndexxoTheme.outlineVariantBorder} />

  <TextHeader1 theme={IndexxoTheme} id="similar-videos"
    >Find similar videos</TextHeader1
  >
  <p>
    Indexxo can find similar videos even if they vary in length and were edited.
  </p>

  <ul class="list-disc list-inside">
    <li>Choose files that you want to analyze</li>
    <li>Open <b>Analyzers</b> in preset settings</li>
    <li>Turn on <b>Similar videos</b></li>
    <li>Modify this settings if needed by clicking the gear button</li>
    <li>Return to preset settings</li>
    <li>Click <b>Start</b></li>
    <li>
      Click <b>Resolve similar videos</b> card. It will be present if there are similar
      videos in your storage.
    </li>
    <li>You can now select and delete files that you do not need</li>
  </ul>

  <hr class={IndexxoTheme.outlineVariantBorder} />

  <TextHeader1 theme={IndexxoTheme} id="export"
    >Export indexed files</TextHeader1
  >
  <p>Indexxo can export indexed files in JSON format.</p>

  <ul class="list-disc list-inside">
    <li>Choose files that you want to index</li>
    <li>Click <b>Start</b></li>
    <li>Open <b>Export</b> tab</li>
    <li>Click <b>Export</b> button (above table)</li>
    <li>Select location</li>
  </ul>

  <Footer />
</WallOfText>
