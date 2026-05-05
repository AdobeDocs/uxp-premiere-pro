---
description: Overview of Marker
id: marker
title: Marker
sidebar_label: Marker
repo: uxp-premierepro
product: premierepro
keywords: 
---

# Marker  

## Instance Methods

### createSetColorByIndexAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Return an action to set the color of the marker by the color index

#### Parameters

| Name       | Type     | Description |
| --- | --- | --- |
| colorIndex | *number* | -           |

<HorizontalLine />

### createSetCommentsAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Return an action to set the comments of the marker.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| comments | *string* | - |

<HorizontalLine />

### createSetDurationAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Return an action to set the duration of the marker.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| tickTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### createSetNameAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Return an action to set the name of the marker.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| name | *string* | - |

<HorizontalLine />

### createSetTypeAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Return an action to set the type of the marker.

#### Parameters

| Name       | Type     | Description                                                               |
| :--------- | :------- | :------------------------------------------------------------------------ |
| markerType | *string* | Can be set to "Comment", "Chapter", "Segmentation", or "WebLink"; verify exact strings against the TypeScript definitions file. |

<HorizontalLine />

### getColor

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Color*
  
Get color code of the marker.

<HorizontalLine />

### getColorIndex

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*number*
  
Get color index of the marker.

<HorizontalLine />

### getComments

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*string*
  
Get comments of the marker.

<HorizontalLine />

### getDuration

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*TickTime*
  
Get duration time of the marker.

<HorizontalLine />

### getName

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*string*
  
Get name of the marker.

<HorizontalLine />

### getStart

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*TickTime*
  
Get start time of the marker.

<HorizontalLine />

### getTarget

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*string*
  
Get target of the marker. Used together with url for web targets.

<HorizontalLine />

### getType

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*string*
  
Get type of the marker. e.g. Cue / Track / Subclip / Cart

<HorizontalLine />

### getUrl

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*string*
  
Get url of the marker.

<HorizontalLine />
