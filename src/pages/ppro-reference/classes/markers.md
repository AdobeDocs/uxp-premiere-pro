---
description: Overview of Markers
id: markers
title: Markers
sidebar_label: Markers
repo: uxp-premierepro
product: premierepro
keywords: 
---

# Markers  

## Static Methods

### getMarkers

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Markers*
  
Returns the Markers object for Sequence Or ProjectItem

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| markerOwnerObject | [*Sequence*](sequence.md) or [*ClipProjectItem*](clipprojectitem.md) | - |

<HorizontalLine />

## Instance Methods

### createAddMarkerAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Add a new marker

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| Name | *string* | - |
| markerType | *string* | - |
| startTime | [*TickTime*](ticktime.md) | - |
| duration | [*TickTime*](ticktime.md) | - |
| comments | *string* | - |

<HorizontalLine />

### createMoveMarkerAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Move the given marker at new time value

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| marker | [*Marker*](marker.md) | - |
| tickTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### createRemoveMarkerAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Remove the given marker

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| marker | [*Marker*](marker.md) | - |

<HorizontalLine />

### getMarkers

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Marker[]*
  
Get all markers

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| filters | [*string[]*](/ppro-reference/classes/string[]/) | Marker Type Filter (Optional) |

<HorizontalLine />
