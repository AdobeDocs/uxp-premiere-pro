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

| Name | Type | Access | Min Version | Description |
| :------ | :------ | :------ | :------ | :------ |
| type | *number* | R | 25.0 | Get the type of the Project Item. |
| name | *string* | R | 25.0 | The name of this project item. |

## Static Methods

### cast

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*ProjectItem*
  
Cast FolderItem or ClipProjectItem in to ProjectItem

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| item | [*FolderItem*](/ppro_reference/classes/folderitem/) or [*ClipProjectItem*](/ppro_reference/classes/clipprojectitem/) | - |

___

## Instance Methods

### createSetColorLabelAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Create an action for set color label to projectItem by index

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| inColorLabelIndex | *number* | - |

___

### createSetNameAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Returns action that renames projectItem

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| inName | *string* | - |

___

### getColorLabelIndex

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*number*
  
Get color label index of projectItem

___

### getId

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*string*
  
Get id of projectItem

___

### getParentBin

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*FolderItem*
  
Get parent FolderItem of projectItem

___

### getProject

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Project*
  
Get the parent Project of this projectItem.

___
