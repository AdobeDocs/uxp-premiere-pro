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

## Properties

| Name | Type | Access | Min Version | Description |
| :------ | :------ | :------ | :------ | :------ |
| mixdownVideo | *boolean* | R | 25.0 | True if the exporter will render a single mixed-down video file |
| explodeToMono | *boolean* | R | 25.0 | True if multichannel audio is exported as separate mono files per channel |
| sampleRate | *number* | R | 25.0 | Get the audio sample rate |
| bitsPerSample | *number* | R | 25.0 | Get the audio bits per sample |
| embedAudio | *boolean* | R | 25.0 | Get whether to embed audio in the AAF file |
| audioFileFormat | *number* | R | 25.0 | Get the audio file format (0 for AIFF, 1 for WAV) |
| trimSources | *boolean* | R | 25.0 | Get whether to trim sources |
| handleFrames | *number* | R | 25.0 | Get the number of handle frames |
| videoMixdownPresetPath | *string* | R | 25.0 | Get the video mixdown preset path |
| renderAudioEffects | *boolean* | R | 25.0 | Get whether to render audio effects |
| interleaveWithoutEffects | *boolean* | R | 25.0 | Get whether to interleave without effects |
| preserveParentFolder | *boolean* | R | 25.0 | Get whether to preserve parent folder |


## Instance Methods

### setAudioFileFormat

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*AAFExportOptions*
  
Set the audio file format (0 for AIFF, 1 for WAV)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| audioFileFormat | [*Constants.AAFExportAudioFormat*](../constants/index.md) | - |

<HorizontalLine />

### setBitsPerSample

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*AAFExportOptions*
  
Set the audio bits per sample

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| bitsPerSample | *number* | - |

<HorizontalLine />

### setEmbedAudio

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*AAFExportOptions*
  
Set whether to embed audio in the AAF file

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| embedAudio | *boolean* | - |

<HorizontalLine />

### setExplodeToMono

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*AAFExportOptions*
  
When true, exports multichannel audio as separate mono media files (one file per channel)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| explodeToMono | *boolean* | - |

<HorizontalLine />

### setHandleFrames

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*AAFExportOptions*
  
Set the number of handle frames

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| handleFrames | *number* | - |

<HorizontalLine />

### setInterleaveWithoutEffects

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*AAFExportOptions*
  
Set whether to interleave without effects

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| interleaveWithoutEffects | *boolean* | - |

<HorizontalLine />

### setMixdownVideo

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*AAFExportOptions*
  
When true, renders the sequence video to a single media file for AAF export (video mixdown) instead of relying only on linked source clips

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| mixdownVideo | *boolean* | - |

<HorizontalLine />

### setPreserveParentFolder

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*AAFExportOptions*
  
When true, exploded mono audio is written under a subdirectory named after the folder that contained each clip's source media on disk

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| preserveParentFolder | *boolean* | - |

<HorizontalLine />

### setRenderAudioEffects

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*AAFExportOptions*
  
Set whether to render audio effects

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| renderAudioEffects | *boolean* | - |

<HorizontalLine />

### setSampleRate

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*AAFExportOptions*
  
Set the audio sample rate

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| sampleRate | *number* | - |

<HorizontalLine />

### setTrimSources

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*AAFExportOptions*
  
Set whether to trim sources

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| trimSources | *boolean* | - |

<HorizontalLine />

### setVideoMixdownPresetPath

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*AAFExportOptions*
  
Path to the encoder preset file (.epr) used when mixdown video is enabled

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| videoMixdownPresetPath | *string* | - |

<HorizontalLine />
