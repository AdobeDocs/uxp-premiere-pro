---
id: "transcript"
title: "Transcript"
sidebar_label: "Transcript"
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
  - Premiere Pro
---

# Transcript  

## Static Methods

### createImportTextSegmentsAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Create action that import external transcripts to ClipProjectItem

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| textSegments | [*TextSegments*](/ppro_reference/classes/textsegments/) | - |
| clipProjectItem | [*ClipProjectItem*](/ppro_reference/classes/clipprojectitem/) | - |

___

### exportToJSON

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*string*
  
Export transcripts inside of clipProjectItem as JSON string if transcript exist

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| clipProjectItem | [*ClipProjectItem*](/ppro_reference/classes/clipprojectitem/) | - |

___

### importFromJSON

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*TextSegments*
  
Returns TextSegments object initialized from jsonString

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| jsonString | *string* | - |

___
