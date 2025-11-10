---
id: "captiontrack"
title: "CaptionTrack"
sidebar_label: "CaptionTrack"
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

# CaptionTrack

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

_[]_

Returns the track items of the specified media type from the given track

#### Parameters

| Name                   | Type      | Description |
| :--------------------- | :-------- | :---------- |
| trackItemType          | _number_  | -           |
| includeEmptyTrackItems | _boolean_ | -           |

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
