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

## Methods

### getMarkers

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*Array*
  
Get all markers

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| filters | *Array* | - |

___

### createRemoveMarkerAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*object*
  
Remove the given marker

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| marker | [*Marker*](/ppro_reference/classes/marker/) | - |

___

### createMoveMarkerAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*object*
  
Move the given marker at new time value

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| marker | [*Marker*](/ppro_reference/classes/marker/) | - |
| tickTime | [*TickTime*](/ppro_reference/classes/ticktime/) | - |

___

### createAddMarkerAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*object*
  
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

### getMarkers

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*Markers*
  
Returns the Markers object for Sequence Or ProjectItem

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| markerOwnerObject | *any* | - |

___
