---
id: "folderitem"
title: "FolderItem"
sidebar_label: "FolderItem"
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

# FolderItem

## Properties

| Name | Type     | Access | Min Version | Description                       |
| :--- | :------- | :----- | :---------- | :-------------------------------- |
| type | _number_ | R      | 25.0        | Get the type of the Project Item. |
| name | _string_ | R      | 25.0        | The name of this project item.    |

## Static Methods

### cast

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_FolderItem_

Cast ProjectItem in to FolderItem

#### Parameters

| Name        | Type                                                  | Description |
| :---------- | :---------------------------------------------------- | :---------- |
| projectItem | [_ProjectItem_](/ppro_reference/classes/projectitem/) | -           |

---

## Instance Methods

### createBinAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Returns an action that lets users create a new bin.

#### Parameters

| Name       | Type      | Description |
| :--------- | :-------- | :---------- |
| name       | _string_  | -           |
| makeUnique | _boolean_ | -           |

---

### createMoveItemAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Creates an action that moves the given item to the provided folder item newParent.

#### Parameters

| Name      | Type                                                  | Description |
| :-------- | :---------------------------------------------------- | :---------- |
| item      | [_ProjectItem_](/ppro_reference/classes/projectitem/) | -           |
| newParent | [_FolderItem_](/ppro_reference/classes/folderitem/)   | -           |

---

### createRemoveItemAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Creates an action that removes the given item from this folder.

#### Parameters

| Name | Type                                                  | Description |
| :--- | :---------------------------------------------------- | :---------- |
| item | [_ProjectItem_](/ppro_reference/classes/projectitem/) | -           |

---

### createRenameBinAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Rename the Bin and return true if it's successful

#### Parameters

| Name | Type     | Description |
| :--- | :------- | :---------- |
| name | _string_ | -           |

---

### createSetColorLabelAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Create an action for set color label to projectItem by index

#### Parameters

| Name              | Type     | Description |
| :---------------- | :------- | :---------- |
| inColorLabelIndex | _number_ | -           |

---

### createSetNameAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Returns action that renames projectItem

#### Parameters

| Name   | Type     | Description |
| :----- | :------- | :---------- |
| inName | _string_ | -           |

---

### createSmartBinAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Creates a smart bin with given name and returns the Folder object

#### Parameters

| Name        | Type     | Description |
| :---------- | :------- | :---------- |
| name        | _string_ | -           |
| searchQuery | _string_ | -           |

---

### getColorLabelIndex

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_number_

Get color label index of projectItem

---

### getItems

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_ProjectItem[]_

Collection of child items of this folder.

---

### getProject

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Project_

Get the parent Project of this projectItem.

---
