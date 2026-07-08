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

Since: **25.6**

## Static Methods

### getValue

Get preference value in native string form

Since: **25.6**

Returns: *string*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| preferenceKey | [*Constants.PreferenceKey*](../constants/index.md#preferencekey) | App preference key to get |

<HorizontalLine />

### setValue

Set backend preference using one of the available property keys

Since: **25.6**

Returns: *boolean*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| key | [*Constants.PreferenceKey*](../constants/index.md#preferencekey) | App preference key to set |
| value | *boolean* or *string* or *number* | Value to set for the preference key |
| persistenceFlag | [*Constants.PropertyType*](../constants/index.md#propertytype) | Indicates whether the preference should be persisted or not |

<HorizontalLine />
