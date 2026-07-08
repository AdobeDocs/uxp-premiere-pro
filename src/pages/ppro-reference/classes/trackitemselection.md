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

Create empty selection

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
