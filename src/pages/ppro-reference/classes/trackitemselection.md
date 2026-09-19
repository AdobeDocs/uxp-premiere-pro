---
description: Overview of TrackItemSelection
id: trackitemselection
title: TrackItemSelection
sidebar_label: TrackItemSelection
repo: uxp-premierepro
product: premierepro
keywords: 
---

# TrackItemSelection

Since: **25.6**

## Static Methods

### createEmptySelection

Create an empty TrackItemSelection to add track items to through a callback function. The selection object is valid for the lifetime and scope of the callback; it's not recommended to extract or use the selection object from outside the callback, nor use asynchronous code within the callback, to avoid any lifetime issues with the selection.

Since: **25.6**

Returns: *boolean*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| undefined | *(selection: TrackItemSelection) =\> void* | - |

<HorizontalLine />

## Instance Methods

### addItem

Add a track item to this selection

Since: **25.6**

Returns: *boolean*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| trackItem | [*VideoClipTrackItem*](videocliptrackitem.md) or [*AudioClipTrackItem*](audiocliptrackitem.md) | trackItem to be added to selection |
| skipDuplicateCheck | *boolean* | - |

<HorizontalLine />

### getTrackItems

return list of trackItems inside of trackItemSelection

Since: **25.6**

Returns: Promise\<*Array\<[VideoClipTrackItem](videocliptrackitem.md) | [AudioClipTrackItem](audiocliptrackitem.md)\>*\>

<HorizontalLine />

### removeItem

Remove a track item from this selection

Since: **25.6**

Returns: *boolean*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| trackItem | [*VideoClipTrackItem*](videocliptrackitem.md) or [*AudioClipTrackItem*](audiocliptrackitem.md) | trackItem to be removed from selection |

<HorizontalLine />
