---
description: Overview of AppPreference
id: apppreference
title: AppPreference
sidebar_label: AppPreference
repo: uxp-premierepro
product: premierepro
keywords: 
---

# AppPreference  

## Static Methods

### getValue

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*string*
  
Get preference value in native string form

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| preferenceKey | [*Constants.PreferenceKey*](../constants/index.md) | App preference key to get |

<HorizontalLine />

### setValue

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Set backend preference using given list of property keys. The parameters are \<key, value (number, boolean or string), persistence flag\>

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| key | [*Constants.PreferenceKey*](../constants/index.md) | App preference key to set |
| value | *boolean* or *string* or *number* | Value to set for the preference key |
| persistenceFlag | [*Constants.PropertyType*](../constants/index.md) | Indicates whether the preference should be persisted or not |

<HorizontalLine />
