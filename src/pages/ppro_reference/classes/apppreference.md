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
  - Premiere
---

# AppPreference

## Static Methods

### getValue

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_string_

Get preference value in native string form

#### Parameters

| Name          | Type                                                   | Description               |
| :------------ | :----------------------------------------------------- | :------------------------ |
| preferenceKey | [_Constants.PreferenceKey_](/ppro_reference/constants) | App preference key to get |

---

### setValue

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Set backend preference using given list of property keys. The parameters are <key, value (number, boolean or string), persistence flag>

#### Parameters

| Name            | Type                                                   | Description                                                 |
| :-------------- | :----------------------------------------------------- | :---------------------------------------------------------- |
| key             | [_Constants.PreferenceKey_](/ppro_reference/constants) | App preference key to set                                   |
| value           | _boolean_ or _string_ or _number_                      | Value to set for the preference key                         |
| persistenceFlag | [_Constants.PropertyType_](/ppro_reference/constants)  | Indicates whether the preference should be persisted or not |

---
