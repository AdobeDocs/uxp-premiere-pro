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

Since: **25.6**

## Static Methods

### getEditor

Get Sequence Editor reference for editing the sequence timeline

Since: **25.6**

Returns: [*SequenceEditor*](sequenceeditor.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| sequenceObject | [*Sequence*](sequence.md) | - |

<HorizontalLine />

### getInstalledMogrtPath

Get local directory path to adobe mogrt files

Since: **25.6**

Returns: Promise\<*string*\>

<HorizontalLine />

## Instance Methods

### createCloneTrackItemAction

Duplicate trackItem using an insert or overwrite edit method to a destination track. Target track and start time of trackItem is determined using an offset value from the original trackItem position.

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| trackItem | [*VideoClipTrackItem*](videocliptrackitem.md) or [*AudioClipTrackItem*](audiocliptrackitem.md) | - |
| timeOffset | [*TickTime*](ticktime.md) | - |
| videoTrackVerticalOffset | *number* | - |
| audioTrackVerticalOffset | *number* | - |
| alignToVideo | *boolean* | - |
| isInsert | *boolean* | - |

<HorizontalLine />

### createInsertProjectItemAction

Create insert ProjectItem into Sequence Action. Note: If you pass a track index greater than the number of existing tracks, a new track will be created.

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| projectItem | [*ProjectItem*](projectitem.md) | - |
| time | [*TickTime*](ticktime.md) | - |
| videoTrackIndex | *number* | - |
| audioTrackIndex | *number* | - |
| limitShift | *boolean* | - |

<HorizontalLine />

### createOverwriteItemAction

Create overwrite Sequence with ProjectItem Action

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| projectItem | [*ProjectItem*](projectitem.md) | - |
| time | [*TickTime*](ticktime.md) | - |
| videoTrackIndex | *number* | - |
| audioTrackIndex | *number* | - |

<HorizontalLine />

### createRemoveItemsAction

Create remove action for sequence

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| trackItemSelection | [*TrackItemSelection*](trackitemselection.md) | - |
| ripple | *boolean* | - |
| mediaType | [*Constants.MediaType*](../constants/index.md#mediatype) | - |
| shiftOverLapping | *boolean* | - |

<HorizontalLine />

### insertMogrtFromLibrary

Insert input MGT into sequence with time and index defined

Since: **25.6**

Returns: *Array\<VideoClipTrackItem | AudioClipTrackItem\>*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| inLibraryName | *string* | - |
| inElementName | *string* | - |
| inTime | [*TickTime*](ticktime.md) | - |
| inVideoTrackIndex | *number* | - |
| inAudioTrackIndex | *number* | - |

<HorizontalLine />

### insertMogrtFromPath

Insert input MGT into sequence with time and index defined

Since: **25.6**

Returns: *Array\<VideoClipTrackItem | AudioClipTrackItem\>*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| inMGTPath | *string* | - |
| inTime | [*TickTime*](ticktime.md) | - |
| inVideoTrackIndex | *number* | - |
| inAudioTrackIndex | *number* | - |

<HorizontalLine />
