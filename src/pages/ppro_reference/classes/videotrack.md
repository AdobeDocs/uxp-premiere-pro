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
  - Premiere Pro
---

# VideoTrack  

## Properties

| Name | Type | Access | Min Version | Description |
| :------ | :------ | :------ | :------ | :------ |
| name | *string* | R | 25.0 | Get the name of the track |
| id | *number* | R | 25.0 | The ID of the track within the TrackGroup |

## Instance Methods

### getIndex

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*number*
  
Index representing the track index of this track within the track group.

___

### getMediaType

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Guid*
  
UUID representing the underlying media type of this track

___

### getTrackItems

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*any*
  
Returns array of VideoClipTrackItem from the track item type

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| trackItemType | *number* | This values can be Empty (0), Clip (1), Transition (2), Preview (3) or Feedback (4) |
| includeEmptyTrackItems | *boolean* | - |

___

### isMuted

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Get mute state of the track

___

### setMute

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
sets the mute state of the track to muted/unmuted

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| mute | *boolean* | - |

___

## Events

| Name | Version | Description |
| :------ | :------ | :------ |
| EVENT_TRACK_CHANGED | 25.0 | Event Object for Track changed |
| EVENT_TRACK_INFO_CHANGED | 25.0 | Event Object for Track Info Changed |
| EVENT_TRACK_LOCK_CHANGED | 25.0 | Event Object for Track Lock Changed |
