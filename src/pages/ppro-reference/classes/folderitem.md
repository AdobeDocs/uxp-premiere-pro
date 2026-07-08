---
description: Overview of FolderItem
id: folderitem
title: FolderItem
sidebar_label: FolderItem
repo: uxp-premierepro
product: premierepro
keywords: 
---

# FolderItem

Since: **25.6**

## Properties

| Name | Type | Access | Min Version | Description |
| :--- | :--- | :----- | :---------- | :---------- |
| type | *number* | R | 25.6 | Get the type of the Project Item. |
| name | *string* | R | 25.6 | The name of this project item. |

## Static Methods

### cast

Cast ProjectItem in to FolderItem

Since: **25.6**

Returns: [*FolderItem*](folderitem.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| projectItem | [*ProjectItem*](projectitem.md) | - |

<HorizontalLine />

## Instance Methods

### createBinAction

Returns an action that lets users create a new bin.

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| name | *string* | - |
| makeUnique | *boolean* | - |

<HorizontalLine />

### createMoveItemAction

Creates an action that moves the given item to the provided folder item newParent.

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| item | [*ProjectItem*](projectitem.md) | - |
| newParent | [*FolderItem*](folderitem.md) | - |

<HorizontalLine />

### createRemoveItemAction

Creates an action that removes the given item from this folder.

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| item | [*ProjectItem*](projectitem.md) | - |

<HorizontalLine />

### createRenameBinAction

Rename the Bin and return true if it's successful

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| name | *string* | - |

<HorizontalLine />

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

### createSmartBinAction

Creates a smart bin with given name and returns the Folder object

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| name | *string* | - |
| searchQuery | *string* | - |

<HorizontalLine />

### getColorLabelIndex

Get color label index of projectItem

Since: **25.6**

Returns: Promise\<*number*\>

<HorizontalLine />

### getItems

Collection of child items of this folder.

Since: **25.6**

Returns: Promise\<[*ProjectItem[]*](projectitem.md)\>

<HorizontalLine />

### getProject

Get the parent Project of this projectItem.

Since: **25.6**

Returns: Promise\<[*Project*](project.md)\>

<HorizontalLine />
