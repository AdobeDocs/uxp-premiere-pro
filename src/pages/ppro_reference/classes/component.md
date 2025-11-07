---
id: "component"
title: "Component"
sidebar_label: "Component"
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

# Component  

## Instance Methods

### getDisplayName

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*string*
  
Returned Promise will be fullfilled with the value of display name for this component

___

### getMatchName

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*string*
  
Returned Promise will be fullfilled with the value of internal matchname for this component

___

### getParam

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*ComponentParam*
  
Get a parameter from the component based on the given input index. Parameter indexes are zero-based, and the actual is defined exclusively by the component itself.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| paramIndex | *number* | - |

___

### getParamCount

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*number*
  
Gets the number of param in the component

___
