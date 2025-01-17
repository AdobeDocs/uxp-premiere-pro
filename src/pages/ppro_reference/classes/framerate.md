---
id: "framerate"
title: "FrameRate"
sidebar_label: "FrameRate"
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

# FrameRate  

## Properties

| Name | Type | Access | Min Version | Description |
| :------ | :------ | :------ | :------ | :------ |
| ticksPerFrame | *number* | W | 25.0 | Read/Write property to get/set ticks per frame. |
| value | *number* | R | 25.0 | Get the number of frames per second. |

## Static Methods

### createWithValue

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*FrameRate*
  
Create frame rate object with a value

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| value | *number* | - |

___

## Instance Methods

### equals

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Returns true if the given FrameRate is equal to this FrameRate object

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| frameRate | [*FrameRate*](/ppro_reference/classes/framerate/) | - |

___
