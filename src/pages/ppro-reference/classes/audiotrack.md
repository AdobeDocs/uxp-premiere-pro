---
description: Overview of AudioTrack
id: audiotrack
title: AudioTrack
sidebar_label: AudioTrack
repo: uxp-premierepro
product: premierepro
keywords: 
---

# AudioTrack

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

Returns array of AudioClipTrackItem from the track item type

Since: **25.6**

Returns: [*AudioClipTrackItem[]*](audiocliptrackitem.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| trackItemType | [*Constants.TrackItemType*](../constants/index.md#trackitemtype) | Constants.TrackItemType.CLIP, Constants.TrackItemType.TRANSITION etc..  |
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
