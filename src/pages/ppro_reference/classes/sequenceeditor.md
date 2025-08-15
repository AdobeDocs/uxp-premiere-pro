---
id: "sequenceeditor"
title: "SequenceEditor"
sidebar_label: "SequenceEditor"
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

# SequenceEditor  

Used to add projectItems as trackItems to sequences, clone trackItems, or remove trackItems from sequences.

## Static Methods

### getEditor

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*SequenceEditor*
  
Get Sequence Editor reference for editing the sequence timeline

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| sequenceObject | [*Sequence*](/ppro_reference/classes/sequence/) | - |

___

### getInstalledMogrtPath

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*String*
  
Get local directory path to adobe mogrt files

___

## Instance Methods

### createCloneTrackItemAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Duplicate trackItem using an insert or overwrite edit method to a destination track. Target track and start time of trackItem is determined using an offset value from the original trackItem position.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| trackItem | [*VideoClipTrackItem*](/ppro_reference/classes/videocliptrackitem/) or [*AudioClipTrackItem*](/ppro_reference/classes/audiocliptrackitem/) | - |
| timeOffset | [*TickTime*](/ppro_reference/classes/ticktime/) | - |
| videoTrackVerticalOffset | *number* | - |
| audioTrackVerticalOffset | *number* | - |
| alignToVideo | *boolean* | - |
| isInsert | *boolean* | - |

___

### createInsertProjectItemAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Create insert ProjectItem into Sequence Action

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| projectItem | [*ProjectItem*](/ppro_reference/classes/projectitem/) | - |
| time | [*TickTime*](/ppro_reference/classes/ticktime/) | - |
| videoTrackIndex | [*Number*](/ppro_reference/classes/number/) | - |
| audioTrackIndex | [*Number*](/ppro_reference/classes/number/) | - |
| limitShift | [*Boolean*](/ppro_reference/classes/boolean/) | - |

___

### createOverwriteItemAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Create overwrite Sequence with ProjectItem Action

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| projectItem | [*ProjectItem*](/ppro_reference/classes/projectitem/) | - |
| time | [*TickTime*](/ppro_reference/classes/ticktime/) | - |
| videoTrackIndex | [*Number*](/ppro_reference/classes/number/) | - |
| audioTrackIndex | [*Number*](/ppro_reference/classes/number/) | - |

___

### createRemoveItemsAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Create remove action for sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| trackItemSelection | [*TrackItemSelection*](/ppro_reference/classes/trackitemselection/) | - |
| ripple | *boolean* | - |
| mediaType | [*Constants.MediaType*](/ppro_reference/constants) | - |
| shiftOverLapping | *boolean* | - |

___

### insertMogrtFromLibrary

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*(VideoClipTrackItem | AudioClipTrackItem)[]*
  
Insert input MGT into sequence with time and index defined

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| inLibraryName | *string* | - |
| inElementName | *string* | - |
| inTime | [*TickTime*](/ppro_reference/classes/ticktime/) | - |
| inVideoTrackIndex | [*Number*](/ppro_reference/classes/number/) | - |
| inAudioTrackIndex | [*Number*](/ppro_reference/classes/number/) | - |

___

### insertMogrtFromPath

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*(VideoClipTrackItem | AudioClipTrackItem)[]*
  
Insert input MGT into sequence with time and index defined

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| inMGTPath | *string* | - |
| inTime | [*TickTime*](/ppro_reference/classes/ticktime/) | - |
| inVideoTrackIndex | [*Number*](/ppro_reference/classes/number/) | - |
| inAudioTrackIndex | [*Number*](/ppro_reference/classes/number/) | - |

___
