---
description: Overview of SequenceEditor
id: sequenceeditor
title: SequenceEditor
sidebar_label: SequenceEditor
repo: uxp-premierepro
product: premierepro
keywords: 
---

# SequenceEditor  

## Static Methods

### getEditor

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*SequenceEditor*
  
Get Sequence Editor reference for editing the sequence timeline

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| sequenceObject | [*Sequence*](sequence.md) | - |

___

### getInstalledMogrtPath

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*String*
  
Get local directory path to adobe mogrt files

___

## Instance Methods

### createCloneTrackItemAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Duplicate trackItem using an insert or overwrite edit method to a destination track. Target track and start time of trackItem is determined using an offset value from the original trackItem position.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| trackItem | [*VideoClipTrackItem*](videocliptrackitem.md) or [*AudioClipTrackItem*](audiocliptrackitem.md) | - |
| timeOffset | [*TickTime*](ticktime.md) | - |
| videoTrackVerticalOffset | *number* | - |
| audioTrackVerticalOffset | *number* | - |
| alignToVideo | *boolean* | - |
| isInsert | *boolean* | - |

___

### createInsertProjectItemAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Create insert ProjectItem into Sequence Action. Note: If you pass a track index greater than the number of existing tracks, a new track will be created.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| projectItem | [*ProjectItem*](projectitem.md) | - |
| time | [*TickTime*](ticktime.md) | - |
| videoTrackIndex | [*Number*](/ppro-reference/classes/number/index.md) | - |
| audioTrackIndex | [*Number*](/ppro-reference/classes/number/index.md) | - |
| limitShift | [*Boolean*](/ppro-reference/classes/boolean/index.md) | - |

___

### createOverwriteItemAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Create overwrite Sequence with ProjectItem Action

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| projectItem | [*ProjectItem*](projectitem.md) | - |
| time | [*TickTime*](ticktime.md) | - |
| videoTrackIndex | [*Number*](/ppro-reference/classes/number/index.md) | - |
| audioTrackIndex | [*Number*](/ppro-reference/classes/number/index.md) | - |

___

### createRemoveItemsAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Create remove action for sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| trackItemSelection | [*TrackItemSelection*](trackitemselection.md) | - |
| ripple | *boolean* | - |
| mediaType | [*Constants.MediaType*](../constants/index.md) | - |
| shiftOverLapping | *boolean* | - |

___

### insertMogrtFromLibrary

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*(VideoClipTrackItem | AudioClipTrackItem)[]*
  
Insert input MGT into sequence with time and index defined

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| inLibraryName | *string* | - |
| inElementName | *string* | - |
| inTime | [*TickTime*](ticktime.md) | - |
| inVideoTrackIndex | [*Number*](/ppro-reference/classes/number/index.md) | - |
| inAudioTrackIndex | [*Number*](/ppro-reference/classes/number/index.md) | - |

___

### insertMogrtFromPath

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*(VideoClipTrackItem | AudioClipTrackItem)[]*
  
Insert input MGT into sequence with time and index defined

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| inMGTPath | *string* | - |
| inTime | [*TickTime*](ticktime.md) | - |
| inVideoTrackIndex | [*Number*](/ppro-reference/classes/number/index.md) | - |
| inAudioTrackIndex | [*Number*](/ppro-reference/classes/number/index.md) | - |

___
