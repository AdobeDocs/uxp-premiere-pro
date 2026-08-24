---
description: Overview of AAFExportOptions
id: aafexportoptions
title: AAFExportOptions
sidebar_label: AAFExportOptions
repo: uxp-premierepro
product: premierepro
keywords: 
---

# AAFExportOptions

Since: **26.3**

## Constructor

Construct an object that contains properties for AAF export.

Since: **26.3**

<HorizontalLine />

## Properties

| Name | Type | Access | Min Version | Description |
| :--- | :--- | :----- | :---------- | :---------- |
| audioFileFormat | *number* | R | 26.3 | Get the audio file format (0 for AIFF, 1 for WAV) |
| bitsPerSample | *number* | R | 26.3 | Get the audio bits per sample |
| embedAudio | *boolean* | R | 26.3 | Get whether to embed audio in the AAF file |
| explodeToMono | *boolean* | R | 26.3 | True if multichannel audio is exported as separate mono files per channel |
| handleFrames | *number* | R | 26.3 | Get the number of handle frames |
| interleaveWithoutEffects | *boolean* | R | 26.3 | Get whether to interleave without effects |
| mixdownVideo | *boolean* | R | 26.3 | True if the exporter will render a single mixed-down video file |
| preserveParentFolder | *boolean* | R | 26.3 | Get whether to preserve parent folder |
| renderAudioEffects | *boolean* | R | 26.3 | Get whether to render audio effects |
| sampleRate | *number* | R | 26.3 | Get the audio sample rate |
| trimSources | *boolean* | R | 26.3 | Get whether to trim sources |
| videoMixdownPresetPath | *string* | R | 26.3 | Get the video mixdown preset path |

## Instance Methods

### setAudioFileFormat

Set the audio file format (0 for AIFF, 1 for WAV)

Since: **26.3**

Returns: [*AAFExportOptions*](aafexportoptions.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| audioFileFormat | [*Constants.AAFExportAudioFormat*](../constants/index.md#aafexportaudioformat) | - |

<HorizontalLine />

### setBitsPerSample

Set the audio bits per sample

Since: **26.3**

Returns: [*AAFExportOptions*](aafexportoptions.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| bitsPerSample | *number* | - |

<HorizontalLine />

### setEmbedAudio

Set whether to embed audio in the AAF file

Since: **26.3**

Returns: [*AAFExportOptions*](aafexportoptions.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| embedAudio | *boolean* | - |

<HorizontalLine />

### setExplodeToMono

When true, exports multichannel audio as separate mono media files (one file per channel)

Since: **26.3**

Returns: [*AAFExportOptions*](aafexportoptions.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| explodeToMono | *boolean* | - |

<HorizontalLine />

### setHandleFrames

Set the number of handle frames

Since: **26.3**

Returns: [*AAFExportOptions*](aafexportoptions.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| handleFrames | *number* | - |

<HorizontalLine />

### setInterleaveWithoutEffects

Set whether to interleave without effects

Since: **26.3**

Returns: [*AAFExportOptions*](aafexportoptions.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| interleaveWithoutEffects | *boolean* | - |

<HorizontalLine />

### setMixdownVideo

When true, renders the sequence video to a single media file for AAF export (video mixdown) instead of relying only on linked source clips

Since: **26.3**

Returns: [*AAFExportOptions*](aafexportoptions.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| mixdownVideo | *boolean* | - |

<HorizontalLine />

### setPreserveParentFolder

When true, exploded mono audio is written under a subdirectory named after the folder that contained each clip's source media on disk

Since: **26.3**

Returns: [*AAFExportOptions*](aafexportoptions.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| preserveParentFolder | *boolean* | - |

<HorizontalLine />

### setRenderAudioEffects

Set whether to render audio effects

Since: **26.3**

Returns: [*AAFExportOptions*](aafexportoptions.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| renderAudioEffects | *boolean* | - |

<HorizontalLine />

### setSampleRate

Set the audio sample rate

Since: **26.3**

Returns: [*AAFExportOptions*](aafexportoptions.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| sampleRate | *number* | - |

<HorizontalLine />

### setTrimSources

Set whether to trim sources

Since: **26.3**

Returns: [*AAFExportOptions*](aafexportoptions.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| trimSources | *boolean* | - |

<HorizontalLine />

### setVideoMixdownPresetPath

Path to the encoder preset file (.epr) used when mixdown video is enabled

Since: **26.3**

Returns: [*AAFExportOptions*](aafexportoptions.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| videoMixdownPresetPath | *string* | - |

<HorizontalLine />
