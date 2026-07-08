---
description: Overview of Metadata
id: metadata
title: Metadata
sidebar_label: Metadata
repo: uxp-premierepro
product: premierepro
keywords: 
---

# Metadata

Since: **25.6**

## Static Methods

### addPropertyToProjectMetadataSchema

Add name and label property to project metadata schema

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| name | *string* | - |
| label | *string* | - |
| type | *number* | - |

<HorizontalLine />

### createSetProjectMetadataAction

Get set project metadata action

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| projectItem | [*ProjectItem*](projectitem.md) | - |
| metadata | *string* | - |
| updatedFields | *string[]* | - |

<HorizontalLine />

### createSetXMPMetadataAction

Get set project XMP metadata action

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| projectItem | [*ProjectItem*](projectitem.md) | - |
| metadata | *string* | - |

<HorizontalLine />

### getProjectColumnsMetadata

Get project column metadata from project item

Since: **25.6**

Returns: Promise\<*string*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| projectItem | [*ProjectItem*](projectitem.md) | - |

<HorizontalLine />

### getProjectMetadata

Get project metadata

Since: **25.6**

Returns: Promise\<*string*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| projectItem | [*ProjectItem*](projectitem.md) | - |

<HorizontalLine />

### getProjectPanelMetadata

Get project panel metadata

Since: **25.6**

Returns: Promise\<*string*\>

<HorizontalLine />

### getXMPMetadata

Get project XMP metadata

Since: **25.6**

Returns: Promise\<*string*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| projectItem | [*ProjectItem*](projectitem.md) | - |

<HorizontalLine />

### setProjectPanelMetadata

Set project panel metadata

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| metadata | *string* | - |

<HorizontalLine />
