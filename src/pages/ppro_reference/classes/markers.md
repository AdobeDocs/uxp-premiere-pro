---
id: "markers"
title: "Markers"
sidebar_label: "Markers"
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

# Markers  

## Static Methods

### getMarkers

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Markers*
  
Returns the Markers object for Sequence Or ProjectItem

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| markerOwnerObject | [*Sequence*](/ppro_reference/classes/sequence/) or [*ProjectItem*](/ppro_reference/classes/projectitem/) | - |

___

## Instance Methods

### createAddMarkerAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Add a new marker

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| Name | *string* | - |
| markerType | *string* | - |
| startTime | [*TickTime*](/ppro_reference/classes/ticktime/) | - |
| duration | [*TickTime*](/ppro_reference/classes/ticktime/) | - |
| comments | *string* | - |

___

### createMoveMarkerAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Move the given marker at new time value

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| marker | [*Marker*](/ppro_reference/classes/marker/) | - |
| tickTime | [*TickTime*](/ppro_reference/classes/ticktime/) | - |

___

### createRemoveMarkerAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Remove the given marker

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| marker | [*Marker*](/ppro_reference/classes/marker/) | - |

___

### getMarkers

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Marker[]*
  
Get all markers

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| filters | [*string[]*](/ppro_reference/classes/string[]/) | Marker Type Filter (Optional) |

___
