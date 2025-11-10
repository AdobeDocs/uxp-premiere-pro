---
id: "marker"
title: "Marker"
sidebar_label: "Marker"
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

# Marker

## Instance Methods

### createSetColorByIndexAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Return an action to set the color of the marker by the color index

#### Parameters

| Name       | Type     | Description |
| :--------- | :------- | :---------- |
| colorIndex | _number_ | -           |

---

### createSetCommentsAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Return an action to set the comments of the marker.

#### Parameters

| Name     | Type     | Description |
| :------- | :------- | :---------- |
| comments | _string_ | -           |

---

### createSetDurationAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Return an action to set the duration of the marker.

#### Parameters

| Name     | Type                                            | Description |
| :------- | :---------------------------------------------- | :---------- |
| tickTime | [_TickTime_](/ppro_reference/classes/ticktime/) | -           |

---

### createSetNameAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Return an action to set the name of the marker.

#### Parameters

| Name | Type     | Description |
| :--- | :------- | :---------- |
| name | _string_ | -           |

---

### createSetTypeAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Return an action to set the type of the marker.

#### Parameters

| Name       | Type     | Description                                                               |
| :--------- | :------- | :------------------------------------------------------------------------ |
| markerType | _string_ | This values can be Scale (0), AnchorToInPoint (1) or AnchorToOutPoint (2) |

---

### getColor

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Color_

Get color code of the marker.

---

### getColorIndex

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_number_

Get color index of the marker.

---

### getComments

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_string_

Get comments of the marker.

---

### getDuration

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_TickTime_

Get duration time of the marker.

---

### getName

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_string_

Get name of the marker.

---

### getStart

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_TickTime_

Get start time of the marker.

---

### getTarget

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_string_

Get target of the marker. Used together with url for web targets.

---

### getType

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_string_

Get type of the marker. e.g. Cue / Track / Subclip / Cart

---

### getUrl

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_string_

Get url of the marker.

---
