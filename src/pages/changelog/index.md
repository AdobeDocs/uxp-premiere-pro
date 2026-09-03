---
title: Changelog
description: What's New
keywords:
  - Changelog
  - Update
  - Release Notes
contributors:
  - https://github.com/undavide
  - https://github.com/camlegleiter
---

# Changelog

## Premiere v26.5.0

This release of Premiere comes with a number of added features, bug fixes, and a few deprecations.

### New APIs

A number of new APIs have been added in this release. More details on each can be seen in each class's documentation page. If you'd like to see more examples of using all of these new APIs in action, check out the `premiere-api` sample panel in the [UXP Premiere Pro Samples](https://github.com/AdobeDocs/uxp-premiere-pro-samples) repository.

- A new [`C2PAService`](../ppro-reference/classes/c2paservice.md) class has been added to help with returning CAI-related information associated with a file. Additional constants [`Constants.C2PAManifestLocation`](../ppro-reference/constants/index.md#c2pamanifestlocation) have been added, associated with the manifest location return value from [`C2PAService.getManifest`](../ppro-reference/classes/c2paservice.md#getmanifest)
- [`Media.getDuration`](../ppro-reference/classes/media.md#getduration) and [`Media.getStart`](../ppro-reference/classes/media.md#getstart) _synchronous_ functions have been added. See more about this in the [deprecations](#deprecations) section below.
- A new [`MediaManager`](../ppro-reference/classes/mediamanager.md) class has been added. Currently this supports the ability to purge the media cache.
- The [`Transcript`](../ppro-reference/classes/transcript.md) class continues to get new functionality:
  - [`isLanguagePackAvailable`](../ppro-reference/classes/transcript.md#islanguagepackavailable) can help check if a particular language pack is available for a given language code.
  - [`transcribeClipProjectItem`](../ppro-reference/classes/transcript.md#transcribeclipprojectitem) generates a transcription for a given `ClipProjectItem`, and settles when the transcription completes.
- A new [`WorkAreaUtils`](../ppro-reference/classes/workareautils.md) class includes several functions for setting or clearing in/out points for the current work area.

#### UXP Host Additions

We've also added some new functionality to the [UXP `host` object](../uxp-api/reference-js/Modules/uxp/host-information/host.md).

- `applicationPath: string` is a readonly string property which contains the absolute path to the currently running Premiere application.
    ```ts
    const uxp = require("uxp");
    console.log(uxp.host.applicationPath);
    // e.g., "/Applications/Adobe Premiere Pro (Beta)/Adobe Premiere Pro (Beta).app" on macOS
    //       "C:\\Program Files\\Adobe\\Adobe Premiere Pro (Beta)\\Adobe Premiere Pro (Beta).exe" on Windows
    ```
- `getBackgroundColor(): Promise<string>` provides information on the current background color of the Premiere application.
    ```ts
    const uxp = require("uxp");
    const backgroundColor = JSON.parse(await uxp.host.getBackgroundColor());
    backgroundColor.type; // "rgb"
    backgroundColor.value.alpha; // 1
    // RGB colors are a value between 0 and 1
    backgroundColor.value.blue;
    backgroundColor.value.green;
    backgroundColor.value.red;
    ```


### Bug Fixes

- `ClipProjectItem`'s [`createSetInPointAction`](../ppro-reference/classes/clipprojectitem.md#createsetinpointaction) and [`createSetOutPointAction`](../ppro-reference/classes/clipprojectitem.md#createsetoutpointaction) no longer error when called.
- Calling [`ComponentParam.getValueAtTime`](../ppro-reference/classes/componentparam.md#getvalueattime) without any argument would result in the function returning a `Promise` which would never settle. Now the `Promise` will reject with an error when called this way.
- Calling [`Markers.getMarkers`](../ppro-reference/classes/markers.md#getmarkers-1) with any `filters` argument applied would typically throw an error. This has been fixed and should allow for correctly filtering down to the desired set of Marker types.
    ```ts
    const sequence: Sequence = ...
    const mySquenceMarkers: Markers = await Markers.getMarkers(sequence);
    // Returns any Comment or WebLink markers on the above sequence.
    // Other filter types include "Chapter" and "FLVCuePoint"
    const myMarkers: Marker[] = mySequenceMarkers.getMarkers(["Comment", "WebLink"]);
    ```
- Calling [`Project.importAEComps`](../ppro-reference/classes/project.md#importaecomps) or [`Project.importAllAEComps`](../ppro-reference/classes/project.md#importallaecomps) without a target bin defaults to adding the imported compositions to the root bin of the Project, but this was sometimes inconsistent and would resolve `true` while not actually adding anything to the project. We've fixed this to correctly handle this default and add the imported compositions to the project.

### Deprecations

#### `Media.start` and `Media.duration` properties

Instances of the `Media` class contain two _async_ properties which, in comparison to the rest of the available classes and properties, are a bit unusual and awkward to work with:

```ts
const media: Media = ...
// These properties return Promises and must either be `await`ed or
// require using `.then()` Promise chaining syntax to use correctly
const start = await media.start;
const duration = await media.duration;
```

We've opted to deprecate these properties in favor of newly-added `getStart()`/`getDuration()` _synchronous_ functions. This was chosen primarily for backwards compatibility instead of changing the properties insitu from asynchronous to synchronous:

```ts
const media: Media = ...
// No `async` usage required!
const start = media.getStart();
const duration = media.getDuration();
```

The asynchronous `start` and `duration` properties will be removed in a future version of Premiere.

#### `Constants.MarkerColor.MAGNETA`

It turns out we also had an incorrectly spelled constant for `MarkerColor` called `MAGNETA`. While the value of this constant is correct for API usage, the slight mispelling of `MAGNETA` instead of `MAGENTA` just didn't sit right. We've gone ahead and deprecated the previous `MAGNETA` color in favor of a properly spelled `MAGENTA`, and will plan on removing the mispelled constant in a future version of Premiere.

```diff
- const myFavoriteColor = ppro.Constants.MarkerColor.MAGNETA;
+ const myFavoriteColor = ppro.Constants.MarkerColor.MAGENTA;
```

### Documentation Updates

Outside of the above core changes, we've also updated our documentation and TypeScript declarations to address some inconsistencies. We'll continue reviewing these and working to make sure these are as accurate as possible.

- [`ClipProjectItem.getComponentChain`](../ppro-reference/classes/clipprojectitem.md#getcomponentchain) now correctly documents a `Promise<AudioComponentChain | VideoComponentChain | null>` return type versus the originally mistyped `Promise<string>`
- The return type documented for [`AudioTrack.createSetNameAction`](../ppro-reference/classes/audiotrack.md#createsetnameaction), [`CaptionTrack.createSetNameAction`](../ppro-reference/classes/captiontrack.md#createsetnameaction), and [`VideoTrack.createSetNameAction`](../ppro-reference/classes/videotrack.md#createsetnameaction) have been corrected to an `Action` type instead of `object`.
- [`Project.saveAs`](../ppro-reference/classes/project.md#saveas) documentation is more specific about its behavior: calling this will result in creating a copy of of the project, and the `project` instance itself will refer to the _copy_, not the original project. This is in line with the same behavior you would see when clicking "File > Save As" in the application menu.
    ```ts
    const project = await Project.open("path/to/MyProject.prproj")
    await project.saveAs("path/to/MyCopiedProject.prproj");
    
    // `project` now refers to "MyCopiedProject" instead of "MyProject"
    ```
- Several classes which can be directly constructed (e.g., via `new`) now have a "Constructor" section on their respective documentation pages. These classes include: `AAFExportOptions`, `AddTransitionOptions`, `CloseProjectOptions`, `Color`, `FrameRate`, `Guid`, `OpenProjectOptions`, `PointF`, `RectF`, and `TickTime`. Additional details on available parameters can also be seen with their constructor section. We'll continue improving the documentation for descriptions and usage soon!

## Premiere Pro v26.3.0

This release of Premiere comes with a few breaking changes we want to call out, as well as a swath of new APIs worth looking through.

### Breaking Changes

#### Sequence.setSelection

The `Sequence.setSelection` method is now **synchronous**: calling this will immediately return a `boolean` value instead of a `Promise<boolean>`.

If you are using this API with `async`/`await`, simply remove the use of `await`:

```diff
  const project = await ppro.Project.getActiveProject();
  const sequence = await project.getActiveSequence();

  const selection = await sequence.getSelection();

- const success = await sequence.setSelection(selection);
+ const success = sequence.setSelection(selection);
```

If you are using this API with `Promise.then` method chaining, you'll need a bit more updating to avoid runtime issues, e.g.:

```diff
- sequence.setSelection(selection).then((success) => {
-   if (success) { ... }
- });
+ const success = sequence.setSelection(selection);
+ if (success) { ... }
```

#### Action creation in locks

Creating `Action` instances through the various `create*Action` functions must now be done so while behind a `project.lockedAccess(() => { ... })` call. Previously this wasn't consistently enforced across `create*Action` calls.

```ts
const audioTrack: AudioTrack = ...

project.lockedAccess(() => {
  // Create the action here...
  const action = audioTrack.createSetNameAction("MyAudioTrack");

  project.executeTransaction((compoundAction: CompoundAction) => {
    // ...and use it here
    compoundAction.addAction(action);
  }, "Rename AudioTrack");
});
```

Creating `Action`s within a `lockedAccess` call is important: many `Action`s contain data that can quickly become stale or inconsistent with other actions that might take place in Premiere (e.g., an editor is making changes that might conflict with a UXP plugin operating at the same time). Using the `lockedAccess` makes sure these actions are sequenced and properly applied to the Undo history.

The new `@adobe/eslint-plugin-premierepro` ESLint plugin offers several rules which help catch these cases to help make sure `Action` creation and usage in your plugin follows best practices. For more information see the documentation pages for:
- The [ESLint Support](../resources/fundamentals/eslint-support/index.md) fundamentals page
- The [`adobe/eslint-plugin-premierepro`](https://github.com/adobe/eslint-plugin-premierepro) Github repo which includes setup and configuration details as well as docs for individual rules.

### New APIs

A number of new APIs have been added in this release. More details on each can be seen in each class's documentation page. If you'd like to see more examples of using all of these new APIs in action, check out the `premiere-api` sample panel in the [UXP Premiere Pro Samples](https://github.com/AdobeDocs/uxp-premiere-pro-samples) repository.

- [`AudioTrack`s](../ppro-reference/classes/audiotrack.md#createsetnameaction), [`CaptionTrack`s](../ppro-reference/classes/captiontrack.md#createsetnameaction), and [`VideoTrack`s](../ppro-reference/classes/videotrack.md#createsetnameaction) can now be renamed via a `createSetNameAction` function added to each class.
- [`ClipProjectItem.createSubClipAction`](../ppro-reference/classes/clipprojectitem.md#createsubclipaction) lets you create sub clips from the `ClipProjectItem`.
- [`EncoderManager`](../ppro-reference/classes/encodermanager.md) has a few new functions added for helping with exporting and using AME:
  - [`launchEncoder`](../ppro-reference/classes/encodermanager.md#launchencoder) to launch your local AME instance.
  - [`setEmbeddedXMPEnabled`](../ppro-reference/classes/encodermanager.md#setembeddedxmpenabled) to toggle embedding XMP metadata
  - [`setSidecarXMPEnabled`](../ppro-reference/classes/encodermanager.md#setsidecarxmpenabled) to toggle adding XMP metadata in a sidecar file
  - [`startBatchEncode`](../ppro-reference/classes/encodermanager.md#startbatchencode) to start any queued encodes in AME
- [`Marker`s](../ppro-reference/classes/marker.md) now have a unique `guid` property.
- A new [`ObjectMaskUtils`](../ppro-reference/classes/objectmaskutils.md) class has been added.
- [`Project.createSequenceWithPresetPath`](../ppro-reference/classes/project.md#createsequencewithpresetpath) has been added to compliment [`Project.createSequence`](../ppro-reference/classes/project.md#createsequence) when using a Sequence Preset.
- A new [`ProjectConverter.exportAAF`](../ppro-reference/classes/projectconverter.md#exportaaf) export function has been added for AAF support. You can see what options are available when exporting AAF project files via the separate [`AAFExportOptions`](../ppro-reference/classes/aafexportoptions.md) class.
- You can set the [`SourceMonitor`'s](../ppro-reference/classes/sourcemonitor.md) current position using [`setPosition`](../ppro-reference/classes/sourcemonitor.md#setposition).
- [`Transcript`](../ppro-reference/classes/transcript.md) has added functions for working with transcriptions.
  - [`querySupportedLanguages`](../ppro-reference/classes/transcript.md#querysupportedlanguages) to see what language packs are currently available
  - [`hasTranscript`](../ppro-reference/classes/transcript.md#hastranscript) to check if a `ClipProjectItem` has already been transcribed


## Premiere Pro v26.2.0

### UXP Hybrid Plugin Support

Premiere Pro now officially supports [UXP Hybrid Plugins](../plugins/hybrid-plugins/index.md), allowing developers to extend their UXP plugins with native C++ libraries. Hybrid plugins enable performance-critical workloads—such as audio/video processing, ML inference, and integration with native SDKs—to run as compiled code alongside the JavaScript-based plugin UI and logic.

- **UXP Hybrid Plugin SDK**: download from the [Adobe Developer Console](https://developer.adobe.com/console). The SDK provides C++ headers, utilities, and templates for building native addons (`.uxpaddon` files).
- **New documentation**: [Overview](../plugins/hybrid-plugins/index.md), [Building Hybrid Plugins](../plugins/hybrid-plugins/build.md), and [FAQ](../plugins/hybrid-plugins/faq.md).

## Premiere Pro v25.6.0

### Official Release of UXP extensibility in Premiere Pro

#### New Features

Premiere Pro's UXP APIs are approaching parity with what was previously possible, via CEP and ExtendScript. While the sample plugins don't (yet) exercise every call or listen to every message, the infrastructure is in place; we will continue to expand and improve the samples.

### Documentation update

- **Comprehensive overhaul** across the entire documentation site.
- **New distribution section** including guides covering Adobe Marketplace submission, enterprise and independent distribution, packaging, installation, listing creation, and review guidelines.
- **Expanded tutorials and recipes** featuring major new content on modal dialogs, panels, TypeScript support, filesystem operations, external processes, and inter-plugin communication.
- **Content reorganization** with streamlined navigation, consolidation, and complete rewrites.
- **New Premiere API Reference** updated to v25.6.

## Premiere Pro v25.2.0

### Initial Public Beta Release for UXP in Premiere Pro

**Release Date:** December 4, 2024

#### New Features

- **Unified Extensibility Platform (UXP) Integration:** Premiere Pro Beta now supports UXP, providing a modern and streamlined approach to developing plugins.
- **Enhanced Performance:** UXP integration aims to improve the performance and responsiveness of plugins within Premiere Pro.
- **Developer Tools:** APIs are available for developers to create and manage UXP-based plugins.

#### Known Issues

- **Limited Third-Party Support:** Initial beta release may have limited support for specific third-party development workflows. Full support is expected in future updates.
- Spectrum Web Component support in UXP is not yet fully supported for Premiere Pro
- Command Plugins do not yet work as a standalone plugin
- Unloading/Reloading a plugin from the UXP Developer Tool [UDT] while it's paused on a breakpoint doesn't work

#### Getting Started

- **Community Support:** Join the [Creative Cloud developer forums](https://forums.creativeclouddeveloper.com/) to share feedback, ask questions, and collaborate with other developers.
