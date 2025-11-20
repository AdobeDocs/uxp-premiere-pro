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
  - Premiere
---

# Transcript

## Static Methods

### createImportTextSegmentsAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Create action that import external transcripts to ClipProjectItem

#### Parameters

| Name            | Type                                                          | Description |
| :-------------- | :------------------------------------------------------------ | :---------- |
| textSegments    | [_TextSegments_](/ppro_reference/classes/textsegments/)       | -           |
| clipProjectItem | [_ClipProjectItem_](/ppro_reference/classes/clipprojectitem/) | -           |

---

### exportToJSON

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_string_

Export transcripts inside of clipProjectItem as JSON string if transcript exist

#### Parameters

| Name            | Type                                                          | Description |
| :-------------- | :------------------------------------------------------------ | :---------- |
| clipProjectItem | [_ClipProjectItem_](/ppro_reference/classes/clipprojectitem/) | -           |

---

### importFromJSON

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_TextSegments_

Returns TextSegments object initialized from jsonString

#### Parameters

| Name       | Type     | Description |
| :--------- | :------- | :---------- |
| jsonString | _string_ | -           |

---
