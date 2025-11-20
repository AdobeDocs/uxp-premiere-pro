---
id: "projectitem"
title: "ProjectItem"
sidebar_label: "ProjectItem"
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

# ProjectItem

## Properties

| Name | Type     | Access | Min Version | Description                       |
| :--- | :------- | :----- | :---------- | :-------------------------------- |
| type | _number_ | R      | 25.0        | Get the type of the Project Item. |
| name | _string_ | R      | 25.0        | The name of this project item.    |

## Static Methods

### cast

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_ProjectItem_

Cast FolderItem or ClipProjectItem in to ProjectItem

#### Parameters

| Name | Type                                                                                                                 | Description |
| :--- | :------------------------------------------------------------------------------------------------------------------- | :---------- |
| item | [_FolderItem_](/ppro_reference/classes/folderitem/) or [_ClipProjectItem_](/ppro_reference/classes/clipprojectitem/) | -           |

---

## Instance Methods

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

### getColorLabelIndex

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_number_

Get color label index of projectItem

---

### getId

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_string_

Get id of projectItem

---

### getParentBin

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_FolderItem_

Get parent FolderItem of projectItem

---

### getProject

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Project_

Get the parent Project of this projectItem.

---
