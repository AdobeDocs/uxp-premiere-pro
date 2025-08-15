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
  - Premiere Pro
---

# FolderItem  

## Properties

| Name | Type | Access | Min Version | Description |
| :------ | :------ | :------ | :------ | :------ |
| name | *string* | R | 25.0 | The name of this project item. |

## Static Methods

### cast

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*FolderItem*
  
Cast ProjectItem in to FolderItem

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| projectItem | [*ProjectItem*](/ppro_reference/classes/projectitem/) | - |

___

## Instance Methods

### createBinAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Returns an action that lets users create a new bin.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| name | *string* | - |
| makeUnique | *boolean* | - |

___

### createMoveItemAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Creates an action that moves the given item to the provided folder item newParent.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| item | [*ProjectItem*](/ppro_reference/classes/projectitem/) | - |
| newParent | [*FolderItem*](/ppro_reference/classes/folderitem/) | - |

___

### createRemoveItemAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Creates an action that removes the given item from this folder.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| item | [*ProjectItem*](/ppro_reference/classes/projectitem/) | - |

___

### createRenameBinAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Rename the Bin and return true if it's successful

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| name | *string* | - |

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

### createSmartBinAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Creates a smart bin with given name and returns the Folder object

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| name | *string* | - |
| searchQuery | *string* | - |

___

### getItems

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*ProjectItem[]*
  
Collection of child items of this folder.

___

### getParent

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*ProjectItem*
  
Get the parent project item of this project item.

___

### getProject

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Project*
  
Get the parent Project of this projectItem.

___
