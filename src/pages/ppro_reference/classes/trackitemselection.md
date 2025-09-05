---
id: "trackitemselection"
title: "TrackItemSelection"
sidebar_label: "TrackItemSelection"
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

# TrackItemSelection  

## Static Methods

### createEmptySelection

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Create empty selection

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| undefined | *(selection: TrackItemSelection) => void* | - |

___

## Instance Methods

### addItem

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Add a track item to this selection

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| trackItem | [*VideoClipTrackItem*](/ppro_reference/classes/videocliptrackitem/) or [*AudioClipTrackItem*](/ppro_reference/classes/audiocliptrackitem/) | trackItem to be added to selection |
| skipDuplicateCheck | *boolean* | - |

___

### getTrackItems

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*(VideoClipTrackItem | AudioClipTrackItem)[]*
  
return list of trackItems inside of trackItemSelection

___

### removeItem

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Remove a track item from this selection

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| trackItem | [*VideoClipTrackItem*](/ppro_reference/classes/videocliptrackitem/) or [*AudioClipTrackItem*](/ppro_reference/classes/audiocliptrackitem/) | trackItem to be removed from selection |

___
