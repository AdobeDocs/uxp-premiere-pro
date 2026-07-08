---
description: Overview of Properties
id: properties
title: Properties
sidebar_label: Properties
repo: uxp-premierepro
product: premierepro
keywords: 
---

# Properties

Since: **25.6**

## Static Methods

### getProperties

Return Property Owner Object

Since: **25.6**

Returns: Promise\<[*Properties*](properties.md)\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| propertyOwnerObject | [*Project*](project.md) or [*Sequence*](sequence.md) | This can also be object instance of Project, Sequence etc.. |

<HorizontalLine />

## Instance Methods

### createClearValueAction

Create an action to clear the value with the given name. This method can fail if e.g. the underlying properties object does not support action based setting of properties.

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| name | *string* | - |

<HorizontalLine />

### createSetValueAction

Create an action to set a named value through scripting. This method can fail if e.g. the underlying properties object does not support action based setting of properties.

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| name | *string* | property name |
| value | *boolean* or *string* or *number* | Value to set for the property key |
| persistenceFlag | [*Constants.PropertyType*](../constants/index.md#propertytype) | Indicates whether the property should be persisted or not |

<HorizontalLine />

### getValue

Get named value in native string form

Since: **25.6**

Returns: *string*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| name | *string* | - |

<HorizontalLine />

### getValueAsBool

Get named value as boolean

Since: **25.6**

Returns: *boolean*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| name | *string* | - |

<HorizontalLine />

### getValueAsFloat

Get named value as float number

Since: **25.6**

Returns: *number*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| name | *string* | - |

<HorizontalLine />

### getValueAsInt

Get named value as integer number

Since: **25.6**

Returns: *number*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| name | *string* | - |

<HorizontalLine />

### hasValue

Check if a named value exists under this name.

Since: **25.6**

Returns: *boolean*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| name | *string* | - |

<HorizontalLine />
