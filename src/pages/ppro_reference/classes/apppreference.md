---
id: "apppreference"
title: "AppPreference"
sidebar_label: "AppPreference"
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

# AppPreference  

## Static Methods

### getValue

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*string*
  
Get preference value in native string form

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| preferenceKey | *string* | Specify entry of preference we’d like to update (ex. auto peak generation preference settings) |
| value | *string/number/boolean* | |
| persistentFlag | *string* | Mark if this change is persistent or not |

___

### setValue

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Set backend preference using given list of property keys.

#### Parameters


| Name | Type | Description |
| :------ | :------ | :------ |
| preferenceKey | *string* | - |
| value | *string/number/boolean* | |
| persistentFlag | *string* | Mark if this change is persistent or not |


___
