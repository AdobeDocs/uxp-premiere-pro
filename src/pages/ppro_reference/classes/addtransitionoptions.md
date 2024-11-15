---
id: "addtransitionoptions"
title: "AddTransitionOptions"
sidebar_label: "AddTransitionOptions"
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

# AddTransitionOptions  

## Properties

| Name | Type | Access | Min Version | Description |
| :------ | :------ | :------ | :------ | :------ |
| applyToStart | *boolean* | R | 25.0 | Get whether to apply transition to the start or end of trackitem |
| forceSingleSided | *boolean* | R | 25.0 | Get whether transition should be applied one/both sides |
| transitionAlignment | *number* | R | 25.0 | Gets the transitionAlignment of transition |
| duration | *TickTime* | R | 25.0 | Gets the duration of transition |


## Instance Methods

### setApplyToStart

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*AddTransitionOptions*
  
Set whether to apply transition to the start or end of trackitem

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| applyToStart | *boolean* | - |

___

### setDuration

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*AddTransitionOptions*
  
Sets the duration of transition

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| tickTime | [*TickTime*](/ppro_reference/classes/ticktime/) | Sets the duration of transition in TickTime |

___

### setForceSingleSided

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*AddTransitionOptions*
  
Set whether transition should be applied one/both sides

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| forceSingleSided | *boolean* | - |

___

### setTransitionAlignment

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*AddTransitionOptions*
  
Sets the transitionAlignment of transition

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| transitionAlignment | *number* | - |

___
