---
description: Overview of CaptionTrack
id: captiontrack
title: CaptionTrack
sidebar_label: CaptionTrack
repo: uxp-premierepro
product: premierepro
keywords: 
---

# CaptionTrack

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

Returns the track items of the specified media type from the given track

Since: **25.6**

Returns: *[]*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| trackItemType | *number* | - |
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
