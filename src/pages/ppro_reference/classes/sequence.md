---
id: "sequence"
title: "Sequence"
sidebar_label: "Sequence"
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

# Sequence

## Properties

| Name | Type     | Access | Min Version | Description                            |
| :--- | :------- | :----- | :---------- | :------------------------------------- |
| guid | _Guid_   | R      | 25.0        | The unique identifier of the sequence. |
| name | _string_ | R      | 25.0        | The sequence name.                     |

## Instance Methods

### clearSelection

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Clears TrackItem Selection

---

### createCloneAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Creates an action to clone the given sequence

---

### createSetInPointAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Create SetInPointAction for sequence

#### Parameters

| Name     | Type                                            | Description |
| :------- | :---------------------------------------------- | :---------- |
| tickTime | [_TickTime_](/ppro_reference/classes/ticktime/) | -           |

---

### createSetOutPointAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Create SetOutPointAction for sequence

#### Parameters

| Name     | Type                                            | Description |
| :------- | :---------------------------------------------- | :---------- |
| tickTime | [_TickTime_](/ppro_reference/classes/ticktime/) | -           |

---

### createSetSettingsAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Returns action that set sequence settings

#### Parameters

| Name             | Type                                                            | Description |
| :--------------- | :-------------------------------------------------------------- | :---------- |
| sequenceSettings | [_SequenceSettings_](/ppro_reference/classes/sequencesettings/) | -           |

---

### createSetZeroPointAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Create an action to set an InPoint for the sequence

#### Parameters

| Name     | Type                                            | Description |
| :------- | :---------------------------------------------- | :---------- |
| tickTime | [_TickTime_](/ppro_reference/classes/ticktime/) | -           |

---

### createSubsequence

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Sequence_

Returns a new sequence, which is a sub-sequence of the existing sequence

#### Parameters

| Name                 | Type      | Description |
| :------------------- | :-------- | :---------- |
| ignoreTrackTargeting | _boolean_ | -           |

---

### getAudioTrack

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_AudioTrack_

Get audio track from track index

#### Parameters

| Name       | Type     | Description |
| :--------- | :------- | :---------- |
| trackIndex | _number_ | -           |

---

### getAudioTrackCount

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_number_

Get audio track count from this sequence

---

### getCaptionTrack

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_CaptionTrack_

Get caption track from track index

#### Parameters

| Name       | Type     | Description |
| :--------- | :------- | :---------- |
| trackIndex | _number_ | -           |

---

### getCaptionTrackCount

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_number_

Get caption track count from this sequence

---

### getEndTime

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_TickTime_

Time representing the end of the sequence

---

### getFrameSize

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_RectF_

Gets the size of the frame

---

### getInPoint

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_TickTime_

Get time representing the inPoint of sequence.

---

### getOutPoint

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_TickTime_

Get time representing the inPoint of sequence.

---

### getPlayerPosition

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_TickTime_

Get the player's current position

---

### getProjectItem

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_ProjectItem_

Get the associated projectItem of the sequence.

---

### getSelection

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_TrackItemSelection_

Returns the current selection group of the sequence.

---

### getSequenceAudioTimeDisplayFormat

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_TimeDisplay_

Get audio time display format of this sequence

---

### getSequenceVideoTimeDisplayFormat

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_TimeDisplay_

Get video time display format of this sequence

---

### getSettings

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_SequenceSettings_

Get sequence settings object

---

### getTimebase

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_string_

Gets the time base of sequence

---

### getVideoTrack

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_VideoTrack_

Get video track from track index

#### Parameters

| Name       | Type     | Description |
| :--------- | :------- | :---------- |
| trackIndex | _number_ | -           |

---

### getVideoTrackCount

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_number_

Get video track count from this sequence

---

### getZeroPoint

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_TickTime_

Time representing the zero point of the sequence.

---

### isDoneAnalyzingForVideoEffects

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Returns whether or not the sequence is done analyzing for video effects

---

### setPlayerPosition

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Set the player's current position

#### Parameters

| Name         | Type                                            | Description |
| :----------- | :---------------------------------------------- | :---------- |
| positionTime | [_TickTime_](/ppro_reference/classes/ticktime/) | -           |

---

### setSelection

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Updates sequence selection using the given track item selection.

#### Parameters

| Name               | Type                                                                | Description |
| :----------------- | :------------------------------------------------------------------ | :---------- |
| trackItemSelection | [_TrackItemSelection_](/ppro_reference/classes/trackitemselection/) | -           |

---
