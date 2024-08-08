---
id: "ticktime"
title: "TickTime"
sidebar_label: "TickTime"
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

# TickTime  ## Properties

| Name | Type | Access | Min Version | Description |
| :------ | :------ | :------ | :------ | :------ |
| seconds | *number* | R | 23.0 | Get the TickTime in seconds |
| ticks | *string* | R | 23.0 | Get the TickTime in ticks as a string |
| ticksNumber | *number* | R | 23.0 | Get the TickTime in ticks as a number |

## Methods

### createWithFrameAndFrameRate

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*TickTime*

Constructs a TickTime object with a frame and a frame rate.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| frameCount | *number* | - |
| frameRate | [*FrameRate*](/ppro_reference/classes/framerate/) | - |

___

### createWithSeconds

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*TickTime*

Constructs a TickTime object with seconds.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| seconds | *number* | - |

___

### createWithTicks

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*TickTime*

Constructs a TickTime object with ticks as a string.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| ticks | *string* | - |

___

### equals

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*boolean*

Returns true if the given TickTime is equal to the TickTime object

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| tickTime | [*TickTime*](/ppro_reference/classes/ticktime/) | - |

___




