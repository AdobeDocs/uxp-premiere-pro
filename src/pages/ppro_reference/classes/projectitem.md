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
  - Premiere Pro
---

# ProjectItem  

## Properties

| Name | Type | Access | Min Version | Description |
| :------ | :------ | :------ | :------ | :------ |
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

It may be desirable to access attributes associated with ProjectItem after a ClipProjectItem object has been retrieved.  This can be achieved by casting a ClipProjectItem to a ProjectItem.

```typescript
let myProjItem = await ppro.ProjectItem.cast(myClipProjItem);
```

___

## Instance Methods

### createSetNameAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Returns action that renames projectItem

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| inName | *string* | - |

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
