---
description: Overview of ProjectItem
id: projectitem
title: ProjectItem
sidebar_label: ProjectItem
repo: uxp-premierepro
product: premierepro
keywords: 
---

# ProjectItem

Since: **25.6**

## Properties

| Name | Type | Access | Min Version | Description |
| :--- | :--- | :----- | :---------- | :---------- |
| name | *string* | R | 25.6 | The name of this project item. |
| type | *number* | R | 25.6 | Get the type of the Project Item. |

## Static Methods

### cast

Cast FolderItem or ClipProjectItem in to ProjectItem

Since: **25.6**

Returns: [*ProjectItem*](projectitem.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| item | [*FolderItem*](folderitem.md) or [*ClipProjectItem*](clipprojectitem.md) | - |

<HorizontalLine />

## Instance Methods

### createSetColorLabelAction

Create an action for set color label to projectItem by index

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| inColorLabelIndex | *number* | - |

<HorizontalLine />

### createSetNameAction

Returns action that renames projectItem

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| inName | *string* | - |

<HorizontalLine />

### getColorLabelIndex

Get color label index of projectItem

Since: **25.6**

Returns: Promise\<*number*\>

<HorizontalLine />

### getId

Get id of projectItem

Since: **25.6**

Returns: *string*

<HorizontalLine />

### getParentBin

Get parent FolderItem of projectItem

Since: **25.6**

Returns: [*FolderItem*](folderitem.md)

<HorizontalLine />

### getProject

Get the parent Project of this projectItem.

Since: **25.6**

Returns: Promise\<[*Project*](project.md)\>

<HorizontalLine />
