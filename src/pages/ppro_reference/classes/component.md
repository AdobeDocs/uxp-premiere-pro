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
  - Premiere
---

# Component

## Instance Methods

### getDisplayName

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_string_

Returned Promise will be fullfilled with the value of display name for this component

---

### getMatchName

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_string_

Returned Promise will be fullfilled with the value of internal matchname for this component

---

### getParam

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_ComponentParam_

Get a parameter from the component based on the given input index. Parameter indexes are zero-based, and the actual is defined exclusively by the component itself.

#### Parameters

| Name       | Type     | Description |
| :--------- | :------- | :---------- |
| paramIndex | _number_ | -           |

---

### getParamCount

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_number_

Gets the number of param in the component

---
