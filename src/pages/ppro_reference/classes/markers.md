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
  - Premiere
---

# Markers

## Static Methods

### getMarkers

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Markers_

Returns the Markers object for Sequence Or ProjectItem

#### Parameters

| Name              | Type                                                                                                             | Description |
| :---------------- | :--------------------------------------------------------------------------------------------------------------- | :---------- |
| markerOwnerObject | [_Sequence_](/ppro_reference/classes/sequence/) or [_ClipProjectItem_](/ppro_reference/classes/clipprojectitem/) | -           |

---

## Instance Methods

### createAddMarkerAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Add a new marker

#### Parameters

| Name       | Type                                            | Description |
| :--------- | :---------------------------------------------- | :---------- |
| Name       | _string_                                        | -           |
| markerType | _string_                                        | -           |
| startTime  | [_TickTime_](/ppro_reference/classes/ticktime/) | -           |
| duration   | [_TickTime_](/ppro_reference/classes/ticktime/) | -           |
| comments   | _string_                                        | -           |

---

### createMoveMarkerAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Move the given marker at new time value

#### Parameters

| Name     | Type                                            | Description |
| :------- | :---------------------------------------------- | :---------- |
| marker   | [_Marker_](/ppro_reference/classes/marker/)     | -           |
| tickTime | [_TickTime_](/ppro_reference/classes/ticktime/) | -           |

---

### createRemoveMarkerAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Remove the given marker

#### Parameters

| Name   | Type                                        | Description |
| :----- | :------------------------------------------ | :---------- |
| marker | [_Marker_](/ppro_reference/classes/marker/) | -           |

---

### getMarkers

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Marker[]_

Get all markers

#### Parameters

| Name    | Type                                            | Description                   |
| :------ | :---------------------------------------------- | :---------------------------- |
| filters | [_string[]_](/ppro_reference/classes/string[]/) | Marker Type Filter (Optional) |

---
