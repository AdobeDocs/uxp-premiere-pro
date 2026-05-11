---
description: Overview of Sequence
id: sequence
title: Sequence
sidebar_label: Sequence
repo: uxp-premierepro
product: premierepro
keywords: 
---

# Sequence  

## Properties

| Name | Type | Access | Min Version | Description |
| :------ | :------ | :------ | :------ | :------ |
| guid | *Guid* | R | 25.0 | The unique identifier of the sequence. |
| name | *string* | R | 25.0 | The sequence name. |

## Instance Methods

### clearSelection

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Clears TrackItem Selection

<HorizontalLine />

### createCloneAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Creates an action to clone the given sequence

<HorizontalLine />

### createSetInPointAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Create SetInPointAction for sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| tickTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### createSetOutPointAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Create SetOutPointAction for sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| tickTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### createSetSettingsAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Returns action that set sequence settings

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| sequenceSettings | [*SequenceSettings*](sequencesettings.md) | - |

<HorizontalLine />

### createSetZeroPointAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Create an action to set an InPoint for the sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| tickTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### createSubsequence

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Sequence*
  
Returns a new sequence, which is a sub-sequence of the existing sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| ignoreTrackTargeting | *boolean* | - |

<HorizontalLine />

### getAudioTrack

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*AudioTrack*
  
Get audio track from track index

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| trackIndex | *number* | - |

<HorizontalLine />

### getAudioTrackCount

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*number*
  
Get audio track count from this sequence

<HorizontalLine />

### getCaptionTrack

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*CaptionTrack*
  
Get caption track from track index

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| trackIndex | *number* | - |

<HorizontalLine />

### getCaptionTrackCount

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*number*
  
Get caption track count from this sequence

<HorizontalLine />

### getEndTime

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*TickTime*
  
Time representing the end of the sequence

<HorizontalLine />

### getFrameSize

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*RectF*
  
Gets the size of the frame

<HorizontalLine />

### getInPoint

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*TickTime*
  
Get time representing the inPoint of sequence.

<HorizontalLine />

### getOutPoint

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*TickTime*
  
Get time representing the outPoint of sequence.

<HorizontalLine />

### getPlayerPosition

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*TickTime*
  
Get the player's current position

<HorizontalLine />

### getProjectItem

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*ProjectItem*
  
Get the associated projectItem of the sequence.

<HorizontalLine />

### getSelection

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*TrackItemSelection*
  
Returns the current selection group of the sequence.

<HorizontalLine />

### getSequenceAudioTimeDisplayFormat

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*TimeDisplay*
  
Get audio time display format of this sequence

<HorizontalLine />

### getSequenceVideoTimeDisplayFormat

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*TimeDisplay*
  
Get video time display format of this sequence

<HorizontalLine />

### getSettings

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*SequenceSettings*
  
Get sequence settings object

<HorizontalLine />

### getTimebase

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*string*
  
Gets the time base of sequence

<HorizontalLine />

### getVideoTrack

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*VideoTrack*
  
Get video track from track index

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| trackIndex | *number* | - |

<HorizontalLine />

### getVideoTrackCount

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*number*
  
Get video track count from this sequence

<HorizontalLine />

### getZeroPoint

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*TickTime*
  
Time representing the zero point of the sequence.

<HorizontalLine />

### isDoneAnalyzingForVideoEffects

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Returns whether or not the sequence is done analyzing for video effects

<HorizontalLine />

### setPlayerPosition

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Set the player's current position

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| positionTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### setSelection

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Updates sequence selection using the given track item selection.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| trackItemSelection | [*TrackItemSelection*](trackitemselection.md) | - |

<HorizontalLine />
