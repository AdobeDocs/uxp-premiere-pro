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
  - Premiere Pro
---

# Marker  

## Instance Methods

### createSetCommentsAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*object*
  
Return an action to set the comments of the marker.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| comments | *string* | - |

___

### createSetDurationAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*object*
  
Return an action to set the duration of the marker.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| tickTime | [*TickTime*](/ppro_reference/classes/ticktime/) | - |

___

### createSetNameAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*object*
  
Return an action to set the name of the marker.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| name | *string* | - |

___

### createSetTypeAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*object*
  
Return an action to set the type of the marker.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| markerType | *string* | This values can be Scale (0), AnchorToInPoint (1) or AnchorToOutPoint (2) |

___

### getComments

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*string*
  
Get comments of the marker.

___

### getDuration

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*object*
  
Get duration time of the marker.

___

### getName

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*string*
  
Get name of the marker.

___

### getStart

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*object*
  
Get start time of the marker.

___

### getTarget

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*string*
  
Get target of the marker. Used together with url for web targets.

___

### getType

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*string*
  
Get type of the marker. e.g. Cue / Track / Subclip / Cart

___

### getUrl

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*string*
  
Get url of the marker.

___
