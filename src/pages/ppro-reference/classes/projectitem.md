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

## Properties

| Name | Type | Access | Min Version | Description |
| :------ | :------ | :------ | :------ | :------ |
| type | *number* | R | 25.0 | Get the type of the Project Item. |
| name | *string* | R | 25.0 | The name of this project item. |

## Static Methods

### cast

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*ProjectItem*
  
Cast FolderItem or ClipProjectItem in to ProjectItem

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| item | [*FolderItem*](folderitem.md) or [*ClipProjectItem*](clipprojectitem.md) | - |

<HorizontalLine />

## Instance Methods

### createSetColorLabelAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Create an action for set color label to projectItem by index

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| inColorLabelIndex | *number* | - |

<HorizontalLine />

### createSetNameAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Returns action that renames projectItem

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| inName | *string* | - |

<HorizontalLine />

### getColorLabelIndex

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*number*
  
Get color label index of projectItem

<HorizontalLine />

### getId

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*string*
  
Get id of projectItem

<HorizontalLine />

### getParentBin

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*FolderItem*
  
Get parent FolderItem of projectItem

<HorizontalLine />

### getProject

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Project*
  
Get the parent Project of this projectItem.

<HorizontalLine />
