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
| preferenceKey | [*Constants.PreferenceKey*](/ppro_reference/constants) | App preference key to get |

___

### setValue

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Set backend preference using given list of property keys. The parameters are <key, value (number, boolean or string), persistence flag>

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| key | [*Constants.PreferenceKey*](/ppro_reference/constants) | App preference key to set |
| value | *boolean* or *string* or *number* | Value to set for the preference key |
| persistenceFlag | [*Constants.PropertyType*](/ppro_reference/constants) | Indicates whether the preference should be persisted or not |

___
