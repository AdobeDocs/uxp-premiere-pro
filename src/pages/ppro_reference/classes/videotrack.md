---
id: "videotrack"
title: "VideoTrack"
sidebar_label: "VideoTrack"
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
  - Premiere
---

# VideoTrack

## Properties

| Name | Type     | Access | Min Version | Description                               |
| :--- | :------- | :----- | :---------- | :---------------------------------------- |
| name | _string_ | R      | 25.0        | Get the name of the track                 |
| id   | _number_ | R      | 25.0        | The ID of the track within the TrackGroup |

## Instance Methods

### getIndex

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_number_

Index representing the track index of this track within the track group.

---

### getMediaType

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Guid_

UUID representing the underlying media type of this track

---

### getTrackItems

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_VideoClipTrackItem[]_

Returns array of VideoClipTrackItem from the track item type

#### Parameters

| Name                   | Type                                                   | Description                                                                         |
| :--------------------- | :----------------------------------------------------- | :---------------------------------------------------------------------------------- |
| trackItemType          | [_Constants.TrackItemType_](/ppro_reference/constants) | This values can be Empty (0), Clip (1), Transition (2), Preview (3) or Feedback (4) |
| includeEmptyTrackItems | _boolean_                                              | -                                                                                   |

---

### isMuted

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Get mute state of the track

---

### setMute

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

sets the mute state of the track to muted/unmuted

#### Parameters

| Name | Type      | Description |
| :--- | :-------- | :---------- |
| mute | _boolean_ | -           |

---

## Events

| Name                     | Version | Description                         |
| :----------------------- | :------ | :---------------------------------- |
| EVENT_TRACK_CHANGED      | 25.0    | Event Object for Track changed      |
| EVENT_TRACK_INFO_CHANGED | 25.0    | Event Object for Track Info Changed |
| EVENT_TRACK_LOCK_CHANGED | 25.0    | Event Object for Track Lock Changed |
