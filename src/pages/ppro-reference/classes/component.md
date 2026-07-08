---
description: Overview of Component
id: component
title: Component
sidebar_label: Component
repo: uxp-premierepro
product: premierepro
keywords: 
---

# Component

Since: **25.6**

## Instance Methods

### getDisplayName

Returned Promise will be fullfilled with the value of display name for this component

Since: **25.6**

Returns: Promise\<*string*\>

<HorizontalLine />

### getMatchName

Returned Promise will be fullfilled with the value of internal matchname for this component

Since: **25.6**

Returns: Promise\<*string*\>

<HorizontalLine />

### getParam

Get a parameter from the component based on the given input index. Parameter indexes are zero-based, and the actual is defined exclusively by the component itself.

Since: **25.6**

Returns: [*ComponentParam*](componentparam.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| paramIndex | *number* | - |

<HorizontalLine />

### getParamCount

Gets the number of param in the component

Since: **25.6**

Returns: *number*

<HorizontalLine />
