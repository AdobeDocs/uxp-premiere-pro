---
id: "projectconverter"
title: "ProjectConverter"
sidebar_label: "ProjectConverter"
repo: "uxp-premierepro"
product: "premierepro"
keywords:
  - Creative Cloud
  - API Documentation
  - UXP
  - Plugins
  - JavaScript
  - ExtendScript
  - SDK
  - C++
  - Scripting
  - Premiere
---

# ProjectConverter  

## Static Methods

### exportAAF

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Export a sequence as an AAF (Advanced Authoring Format) file to the specified output path.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| sequence | [*Sequence*](/ppro_reference/classes/sequence/) | - |
| filePath | *string* | - |
| mixdownVideo | *boolean* | - |
| explodeToMono | *boolean* | - |
| sampleRate | *number* | - |
| bitsPerSample | *number* | - |
| embedAudio | *boolean* | - |
| audioFileFormat | *number* | - |
| trimSources | *boolean* | - |
| handleFrames | *number* | - |
| videoMixdownPresetPath | *string* | - |
| renderAudioEffects | *boolean* | - |
| interleaveWithoutEffects | *boolean* | - |
| preserveParentFolder | *boolean* | - |

___

### exportAsFinalCutProXML

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Export a sequence as Final Cut Pro XML to the specified output file path.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| sequence | [*Sequence*](/ppro_reference/classes/sequence/) | - |
| outputFilePath | *string* | - |
| suppressUI | *boolean* | - |

___

### exportAsOpenTimelineIO

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Export a sequence as OpenTimelineIO to the specified output file path.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| sequence | [*Sequence*](/ppro_reference/classes/sequence/) | - |
| outputFilePath | *string* | - |
| suppressUI | *boolean* | - |

___
