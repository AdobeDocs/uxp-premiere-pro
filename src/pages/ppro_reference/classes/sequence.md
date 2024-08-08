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
  - Premiere Pro
---

# Sequence  

## Properties

| Name | Type | Access | Min Version | Description |
| :------ | :------ | :------ | :------ | :------ |
| name | *string* | R | 23.0 | The sequence name. |
| id | *Guid* | R | 23.0 | The unique identifier of the sequence. |

## Methods

### getSequenceVideoTimeDisplayFormat

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*TimeDisplay*
  
Get video time display format of this sequence

___

### getSequenceAudioTimeDisplayFormat

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*TimeDisplay*
  
Get audio time display format of this sequence

___

### getPlayerPosition

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*TickTime*
  
Get the player's current position

___

### setPlayerPosition

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*boolean*
  
Set the player's current position

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| positionTime | [*TickTime*](/ppro_reference/classes/ticktime/) | - |

___

### clearSelection

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*boolean*
  
Clears TrackItem Selection

___

### setSelection

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*boolean*
  
Updates sequence selection using the given track item selection.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| TrackItemSelection | [*trackItemSelection*](/ppro_reference/classes/trackitemselection/) | - |

___

### getVideoTrackCount

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*number*
  
Get video track count from this sequence

___

### getAudioTrackCount

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*number*
  
Get audio track count from this sequence

___

### getCaptionTrackCount

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*number*
  
Get caption track count from this sequence

___

### getVideoTrack

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*VideoTrack*
  
Get video track from track index

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| trackIndex | *number* | - |

___

### getAudioTrack

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*AudioTrack*
  
Get audio track from track index

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| trackIndex | *number* | - |

___

### getCaptionTrack

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*CaptionTrack*
  
Get caption track from track index

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| trackIndex | *number* | - |

___

### getSettings

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*SequenceSettings*
  
Get sequence settings object

___

### setSettings

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*boolean*
  
Set sequence settings

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| sequenceSettings | [*SequenceSettings*](/ppro_reference/classes/sequencesettings/) | - |

___

### createCloneAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*Action*
  
Creates an action to clone the given sequence

___

### createSubsequence

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*Sequence*
  
Returns a new sequence, which is a sub-sequence of the existing sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| ignoreTrackTargeting | *boolean* | - |

___

### isDoneAnalyzingForVideoEffects

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*boolean*
  
Returns whether or not the sequence is done analyzing for video effects

___

### getZeroPoint

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*TickTime*
  
Time representing the zero point of the sequence.

___

### getEndTime

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*TickTime*
  
Time representing the end of the sequence

___

### getInPoint

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*TickTime*
  
Get time representing the inPoint of sequence.

___

### getOutPoint

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*TickTime*
  
Get time representing the inPoint of sequence.

___

### createSetZeroPointAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*Action*
  
Create an action to set an InPoint for the sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| tickTime | [*TickTime*](/ppro_reference/classes/ticktime/) | - |

___

### getProjectItem

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*ProjectItem*
  
Get the associated projectItem of the sequence.

___

### getSelection

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*TrackItemSelection*
  
Returns the current selection group of the sequence.

___

### getFrameSize

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*RectF*
  
Gets the size of the frame

___

### getTimebase

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*string*
  
Gets the time base of sequence

___
