---
id: "projectutils"
title: "ProjectUtils"
sidebar_label: "ProjectUtils"
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

# ProjectUtils

## Definition of Terms

**project views**

Given the Premiere Pro User Interface, a **project view** is defined as a project panel instance that is displaying any part of a project's contents. Upon opening a Premiere Pro project, a single project view for that project will be instantiated displaying all contents of a project from its root level. Additional project views can be spawned in the UI from any project bin within the project (by double-clicking on the bin in the UI), resulting in additional UI project panel windows which display project contents constrained to the contents of the selected bin. These additional views, along with the initial project root view, are all uniquely identifiable by their project view ID, and are all considered views of the same project.

## Static Methods

### getProjectFromViewId

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*object*
  
Get project based on input view guid

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| guid | [*Guid*](/ppro_reference/classes/guid/) | - |

___

### getProjectViewIds

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Array*
  
Get array of project view ids

___

### getSelection

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*ProjectItemSelection*
  
Get array of selected project items in project view

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| project | [*Project*](/ppro_reference/classes/project/) | - |

___

### getSelectionFromViewId

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*ProjectItemSelection*
  
Get array of selected projectItem based on input view guid

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| guid | [*Guid*](/ppro_reference/classes/guid/) | - |

___
