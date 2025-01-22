---
id: "project"
title: "Project"
sidebar_label: "Project"
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

# Project  

## Properties

| Name | Type | Access | Min Version | Description |
| :------ | :------ | :------ | :------ | :------ |
| guid | *Guid* | R | 25.0 | The unique identifier of the project. |
| name | *string* | R | 25.0 | The project name. |
| path | *string* | R | 25.0 | The absolute file path to the project file. |

## Static Methods

### createProject

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Project*
  
Create a new project

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| path | *string* | - |

___

### getActiveProject

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Project*
  
Currently active project.

___

### getProject

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Project*
  
Get project referenced by given UID

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| projectGuid | [*Guid*](/ppro_reference/classes/guid/) | - |

___

### open

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Project*
  
Open a project

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| path | *string* | - |
| openProjectOptions | [*OpenProjectOptions*](/ppro_reference/classes/openprojectoptions/) | - |

___

## Instance Methods

### close

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Close a project

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| closeProjectOptions | [*CloseProjectOptions*](/ppro_reference/classes/closeprojectoptions/) | - |

___

### createSequence

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Sequence*
  
Create a new sequence with the default preset path - Parameter presetPath is deprecated, instead use createSequenceWithPresetPath()

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| name | *string* | - |
| presetPath | *string* | - |

___

### createSequenceFromMedia

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Sequence*
  
Create a new sequence with a given name and medias

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| name | *string* | - |
| clipProjectItems | *Array* | - |
| targetBin | [*ProjectItem*](/ppro_reference/classes/projectitem/) | - |

___

### deleteSequence

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Delete a given sequence from the project

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| sequence | [*Sequence*](/ppro_reference/classes/sequence/) | - |

___

### executeTransaction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*any*
  
Execute undoable transaction by passing compound action

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| callback | *any* | - |
| undoString? | *any* | - |

___

### getActiveSequence

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Sequence*
  
Get the active sequence of the project

___

### getColorSettings

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*ProjectColorSettings*
  
Get project color settings object

___

### getInsertionBin

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*ProjectItem*
  
Get current insertion bin

___

### getRootItem

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*FolderItem*
  
The root item of the project which contains all items of the project on the lowest level.

___

### getSequence

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Sequence*
  
Get sequence by id from the project

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| guid | [*Guid*](/ppro_reference/classes/guid/) | - |

___

### getSequences

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Array*
  
Get an array of all sequences in this project.

___

### importAEComps

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| aepPath | *string* | - |
| compNames | *Array* | - |
| TargetBin | [*ProjectItem*](/ppro_reference/classes/projectitem/) | - |

___

### importAllAEComps

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| aepPath | *string* | - |
| TargetBin | [*ProjectItem*](/ppro_reference/classes/projectitem/) | - |

___

### importFiles

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Import files in root/target bin of the project

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| filePaths | *Array* | - |
| suppressUI | *boolean* | - |
| targetBin | [*ProjectItem*](/ppro_reference/classes/projectitem/) | - |
| asNumberedStills | *boolean* | - |

___

### importSequences

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| projectPath | *string* | - |
| sequenceIds | *Array* | - |

___

### lockedAccess

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*any*
  
Get a read/upgrade locked access to Project, project state will not change during the execution of callback function. Can call executeTransaction while having locked access.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| callback | *any* | - |

___

### openSequence

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Open a sequence and return true if successful.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| sequence | [*Sequence*](/ppro_reference/classes/sequence/) | - |

___

### pauseGrowing

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Pause growing of files instead swap the files

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| pause | *boolean* | - |

___

### save

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Save the project

___

### saveAs

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Save the project at the provided path

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| path | *string* | - |

___

### setActiveSequence

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Set the active sequence of the project

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| sequence | [*Sequence*](/ppro_reference/classes/sequence/) | - |

___
