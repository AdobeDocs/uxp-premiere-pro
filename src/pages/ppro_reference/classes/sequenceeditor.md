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
  - Premiere
---

# SequenceEditor

## Static Methods

### getEditor

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_SequenceEditor_

Get Sequence Editor reference for editing the sequence timeline

#### Parameters

| Name           | Type                                            | Description |
| :------------- | :---------------------------------------------- | :---------- |
| sequenceObject | [_Sequence_](/ppro_reference/classes/sequence/) | -           |

---

### getInstalledMogrtPath

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_String_

Get local directory path to adobe mogrt files

---

## Instance Methods

### createCloneTrackItemAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Duplicate trackItem using an insert or overwrite edit method to a destination track. Target track and start time of trackItem is determined using an offset value from the original trackItem position.

#### Parameters

| Name                     | Type                                                                                                                                       | Description |
| :----------------------- | :----------------------------------------------------------------------------------------------------------------------------------------- | :---------- |
| trackItem                | [_VideoClipTrackItem_](/ppro_reference/classes/videocliptrackitem/) or [_AudioClipTrackItem_](/ppro_reference/classes/audiocliptrackitem/) | -           |
| timeOffset               | [_TickTime_](/ppro_reference/classes/ticktime/)                                                                                            | -           |
| videoTrackVerticalOffset | _number_                                                                                                                                   | -           |
| audioTrackVerticalOffset | _number_                                                                                                                                   | -           |
| alignToVideo             | _boolean_                                                                                                                                  | -           |
| isInsert                 | _boolean_                                                                                                                                  | -           |

---

### createInsertProjectItemAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Create insert ProjectItem into Sequence Action. Note: If you pass a track index greater than the number of existing tracks, a new track will be created.

#### Parameters

| Name            | Type                                                  | Description |
| :-------------- | :---------------------------------------------------- | :---------- |
| projectItem     | [_ProjectItem_](/ppro_reference/classes/projectitem/) | -           |
| time            | [_TickTime_](/ppro_reference/classes/ticktime/)       | -           |
| videoTrackIndex | [_Number_](/ppro_reference/classes/number/)           | -           |
| audioTrackIndex | [_Number_](/ppro_reference/classes/number/)           | -           |
| limitShift      | [_Boolean_](/ppro_reference/classes/boolean/)         | -           |

---

### createOverwriteItemAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Create overwrite Sequence with ProjectItem Action

#### Parameters

| Name            | Type                                                  | Description |
| :-------------- | :---------------------------------------------------- | :---------- |
| projectItem     | [_ProjectItem_](/ppro_reference/classes/projectitem/) | -           |
| time            | [_TickTime_](/ppro_reference/classes/ticktime/)       | -           |
| videoTrackIndex | [_Number_](/ppro_reference/classes/number/)           | -           |
| audioTrackIndex | [_Number_](/ppro_reference/classes/number/)           | -           |

---

### createRemoveItemsAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Create remove action for sequence

#### Parameters

| Name               | Type                                                                | Description |
| :----------------- | :------------------------------------------------------------------ | :---------- |
| trackItemSelection | [_TrackItemSelection_](/ppro_reference/classes/trackitemselection/) | -           |
| ripple             | _boolean_                                                           | -           |
| mediaType          | [_Constants.MediaType_](/ppro_reference/constants)                  | -           |
| shiftOverLapping   | _boolean_                                                           | -           |

---

### insertMogrtFromLibrary

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_(VideoClipTrackItem | AudioClipTrackItem)[]_

Insert input MGT into sequence with time and index defined

#### Parameters

| Name              | Type                                            | Description |
| :---------------- | :---------------------------------------------- | :---------- |
| inLibraryName     | _string_                                        | -           |
| inElementName     | _string_                                        | -           |
| inTime            | [_TickTime_](/ppro_reference/classes/ticktime/) | -           |
| inVideoTrackIndex | [_Number_](/ppro_reference/classes/number/)     | -           |
| inAudioTrackIndex | [_Number_](/ppro_reference/classes/number/)     | -           |

---

### insertMogrtFromPath

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_(VideoClipTrackItem | AudioClipTrackItem)[]_

Insert input MGT into sequence with time and index defined

#### Parameters

| Name              | Type                                            | Description |
| :---------------- | :---------------------------------------------- | :---------- |
| inMGTPath         | _string_                                        | -           |
| inTime            | [_TickTime_](/ppro_reference/classes/ticktime/) | -           |
| inVideoTrackIndex | [_Number_](/ppro_reference/classes/number/)     | -           |
| inAudioTrackIndex | [_Number_](/ppro_reference/classes/number/)     | -           |

---
