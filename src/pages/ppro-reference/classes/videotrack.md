---
description: Overview of VideoTrack
id: videotrack
title: VideoTrack
sidebar_label: VideoTrack
repo: uxp-premierepro
product: premierepro
keywords: 
---

# VideoTrack

Since: **25.6**

## Properties

| Name | Type | Access | Min Version | Description |
| :--- | :--- | :----- | :---------- | :---------- |
| name | *string* | R | 25.6 | Get the name of the track |
| id | *number* | R | 25.6 | The ID of the track within the TrackGroup |

## Instance Methods

### createSetNameAction

Action to change the name of the track

Since: **26.3**

Returns: *object*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| name | *string* | - |

<HorizontalLine />

### getIndex

Index representing the track index of this track within the track group.

Since: **25.6**

Returns: Promise\<*number*\>

<HorizontalLine />

### getMediaType

UUID representing the underlying media type of this track

Since: **25.6**

Returns: Promise\<[*Guid*](guid.md)\>

<HorizontalLine />

### getTrackItems

Returns array of VideoClipTrackItem from the track item type

Since: **25.6**

Returns: [*VideoClipTrackItem[]*](videocliptrackitem.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| trackItemType | [*Constants.TrackItemType*](../constants/index.md#trackitemtype) | This values can be Empty (0), Clip (1), Transition (2), Preview (3) or Feedback (4) |
| includeEmptyTrackItems | *boolean* | - |

<HorizontalLine />

### isMuted

Get mute state of the track

Since: **25.6**

Returns: Promise\<*boolean*\>

<HorizontalLine />

### setMute

sets the mute state of the track to muted/unmuted

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| mute | *boolean* | - |

<HorizontalLine />

## Events

| Name | Version | Description |
| :--- | :------ | :---------- |
| EVENT_TRACK_CHANGED | 25.6 | Event Object for Track changed |
| EVENT_TRACK_INFO_CHANGED | 25.6 | Event Object for Track Info Changed |
| EVENT_TRACK_LOCK_CHANGED | 25.6 | Event Object for Track Lock Changed |
