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

## Properties

| Name | Type | Access | Min Version | Description |
| :------ | :------ | :------ | :------ | :------ |
| name | *string* | R | 25.0 | Get the name of the track |
| id | *number* | R | 25.0 | The ID of the track within the TrackGroup |

## Instance Methods

### getIndex

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*number*
  
Index representing the track index of this track within the track group.

<HorizontalLine />

### getMediaType

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Guid*
  
UUID representing the underlying media type of this track

<HorizontalLine />

### getTrackItems

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*[]*
  
Returns the track items of the specified media type from the given track

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| trackItemType | *number* | - |
| includeEmptyTrackItems | *boolean* | - |

<HorizontalLine />

### isMuted

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Get mute state of the track

<HorizontalLine />

### setMute

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
sets the mute state of the track to muted/unmuted

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| mute | *boolean* | - |

<HorizontalLine />
