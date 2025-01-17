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
| guid | *Guid* | R | 25.0 | The unique identifier of the sequence. |
| name | *string* | R | 25.0 | The sequence name. |


## Instance Methods

### clearSelection

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Clears TrackItem Selection

___

### createCloneAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Creates an action to clone the given sequence

___

### createSetZeroPointAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Create an action to set an InPoint for the sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| tickTime | [*TickTime*](/ppro_reference/classes/ticktime/) | - |

___

### createSubsequence

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Sequence*
  
Returns a new sequence, which is a sub-sequence of the existing sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| ignoreTrackTargeting | *boolean* | - |

___

### getAudioTrack

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*AudioTrack*
  
Get audio track from track index

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| trackIndex | *number* | - |

___

### getAudioTrackCount

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*number*
  
Get audio track count from this sequence

___

### getCaptionTrack

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*CaptionTrack*
  
Get caption track from track index

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| trackIndex | *number* | - |

___

### getCaptionTrackCount

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*number*
  
Get caption track count from this sequence

___

### getEndTime

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*TickTime*
  
Time representing the end of the sequence

___

### getFrameSize

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*RectF*
  
Gets the size of the frame

___

### getInPoint

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*TickTime*
  
Get time representing the inPoint of sequence.

___

### getOutPoint

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*TickTime*
  
Get time representing the inPoint of sequence.

___

### getPlayerPosition

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*TickTime*
  
Get the player's current position

___

### getProjectItem

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*ProjectItem*
  
Get the associated projectItem of the sequence.

___

### getSelection

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*TrackItemSelection*
  
Returns the current selection group of the sequence.

___

### getSequenceAudioTimeDisplayFormat

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*TimeDisplay*
  
Get audio time display format of this sequence

___

### getSequenceVideoTimeDisplayFormat

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*TimeDisplay*
  
Get video time display format of this sequence

___

### getSettings

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*SequenceSettings*
  
Get sequence settings object

___

### getTimebase

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*string*
  
Gets the time base of sequence

___

### getVideoTrack

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*VideoTrack*
  
Get video track from track index

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| trackIndex | *number* | - |

___

### getVideoTrackCount

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*number*
  
Get video track count from this sequence

___

### getZeroPoint

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*TickTime*
  
Time representing the zero point of the sequence.

___

### isDoneAnalyzingForVideoEffects

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Returns whether or not the sequence is done analyzing for video effects

___

### setPlayerPosition

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Set the player's current position

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| positionTime | [*TickTime*](/ppro_reference/classes/ticktime/) | - |

___

### setSelection

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Updates sequence selection using the given track item selection.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| trackItemSelection | [*TrackItemSelection*](/ppro_reference/classes/trackitemselection/) | - |

___

### setSettings

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Set sequence settings

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| sequenceSettings | [*SequenceSettings*](/ppro_reference/classes/sequencesettings/) | - |

___
