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

## Premiere Pro v26.3.0

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

  project.executeTransasction((compoundAction: CompoundAction) => {
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

A number of new APIs have been added in this release. More details on each can be seen in each class's documentation page.

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
- You can set the [`SourceMonitor`s](../ppro-reference/classes/sourcemonitor.md) current position using [`setPosition`](../ppro-reference/classes/sourcemonitor.md#setposition).
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
