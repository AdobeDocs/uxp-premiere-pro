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

Since: **25.6**

## Properties

| Name | Type | Access | Min Version | Description |
| :--- | :--- | :----- | :---------- | :---------- |
| guid | [*Guid*](guid.md) | R | 25.6 | The unique identifier of the sequence. |
| name | *string* | R | 25.6 | The sequence name. |

## Instance Methods

### clearSelection

Clears TrackItem Selection

Since: **25.6**

Returns: Promise\<*boolean*\>

<HorizontalLine />

### createCloneAction

Creates an action to clone the given sequence

Since: **25.6**

Returns: [*Action*](action.md)

<HorizontalLine />

### createSetInPointAction

Create SetInPointAction for sequence

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| tickTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### createSetOutPointAction

Create SetOutPointAction for sequence

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| tickTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### createSetSettingsAction

Returns action that set sequence settings

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| sequenceSettings | [*SequenceSettings*](sequencesettings.md) | - |

<HorizontalLine />

### createSetZeroPointAction

Create an action to set an InPoint for the sequence

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| tickTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### createSubsequence

Returns a new sequence, which is a sub-sequence of the existing sequence

Since: **25.6**

Returns: Promise\<[*Sequence*](sequence.md)\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| ignoreTrackTargeting | *boolean* | - |

<HorizontalLine />

### getAudioTrack

Get audio track from track index

Since: **25.6**

Returns: Promise\<[*AudioTrack*](audiotrack.md)\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| trackIndex | *number* | - |

<HorizontalLine />

### getAudioTrackCount

Get audio track count from this sequence

Since: **25.6**

Returns: Promise\<*number*\>

<HorizontalLine />

### getCaptionTrack

Get caption track from track index

Since: **25.6**

Returns: Promise\<[*CaptionTrack*](captiontrack.md)\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| trackIndex | *number* | - |

<HorizontalLine />

### getCaptionTrackCount

Get caption track count from this sequence

Since: **25.6**

Returns: Promise\<*number*\>

<HorizontalLine />

### getEndTime

Time representing the end of the sequence

Since: **25.6**

Returns: Promise\<[*TickTime*](ticktime.md)\>

<HorizontalLine />

### getFrameSize

Gets the size of the frame

Since: **25.6**

Returns: Promise\<[*RectF*](rectf.md)\>

<HorizontalLine />

### getInPoint

Get time representing the inPoint of sequence.

Since: **25.6**

Returns: Promise\<[*TickTime*](ticktime.md)\>

<HorizontalLine />

### getOutPoint

Get time representing the inPoint of sequence.

Since: **25.6**

Returns: Promise\<[*TickTime*](ticktime.md)\>

<HorizontalLine />

### getPlayerPosition

Get the player's current position

Since: **25.6**

Returns: Promise\<[*TickTime*](ticktime.md)\>

<HorizontalLine />

### getProjectItem

Get the associated projectItem of the sequence.

Since: **25.6**

Returns: Promise\<[*ProjectItem*](projectitem.md)\>

<HorizontalLine />

### getSelection

Returns the current selection group of the sequence.

Since: **25.6**

Returns: Promise\<[*TrackItemSelection*](trackitemselection.md)\>

<HorizontalLine />

### getSequenceAudioTimeDisplayFormat

Get audio time display format of this sequence

Since: **25.6**

Returns: Promise\<[*TimeDisplay*](timedisplay.md)\>

<HorizontalLine />

### getSequenceVideoTimeDisplayFormat

Get video time display format of this sequence

Since: **25.6**

Returns: Promise\<[*TimeDisplay*](timedisplay.md)\>

<HorizontalLine />

### getSettings

Get sequence settings object

Since: **25.6**

Returns: Promise\<[*SequenceSettings*](sequencesettings.md)\>

<HorizontalLine />

### getTimebase

Gets the time base of sequence

Since: **25.6**

Returns: Promise\<*string*\>

<HorizontalLine />

### getVideoTrack

Get video track from track index

Since: **25.6**

Returns: Promise\<[*VideoTrack*](videotrack.md)\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| trackIndex | *number* | - |

<HorizontalLine />

### getVideoTrackCount

Get video track count from this sequence

Since: **25.6**

Returns: Promise\<*number*\>

<HorizontalLine />

### getZeroPoint

Time representing the zero point of the sequence.

Since: **25.6**

Returns: Promise\<[*TickTime*](ticktime.md)\>

<HorizontalLine />

### isDoneAnalyzingForVideoEffects

Returns whether or not the sequence is done analyzing for video effects

Since: **25.6**

Returns: Promise\<*boolean*\>

<HorizontalLine />

### setPlayerPosition

Set the player's current position

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| positionTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### setSelection

Updates sequence selection using the given track item selection.

Since: **25.6**

Since: **26.3**: This function is now synchronous and returns a *boolean* instead of a Promise\<*boolean*\>.

Returns: *boolean*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| trackItemSelection | [*TrackItemSelection*](trackitemselection.md) | - |

<HorizontalLine />
