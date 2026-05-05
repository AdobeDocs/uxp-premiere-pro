---
description: Overview of Project
id: project
title: Project
sidebar_label: Project
repo: uxp-premierepro
product: premierepro
keywords: 
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

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Project*
  
Create a new project

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| path | *string* | - |

<HorizontalLine />

### getActiveProject

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Project*
  
Currently active project.

<HorizontalLine />

### getProject

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Project*
  
Get project referenced by given UID

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| projectGuid | [*Guid*](guid.md) | - |

<HorizontalLine />

### isProject

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Returns true if the file at the given path is openable as a Premiere project

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| projectPath | *string* | - |

<HorizontalLine />

### open

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Project*
  
Open a project

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| path | *string* | - |
| openProjectOptions | [*OpenProjectOptions*](openprojectoptions.md) | - |

<HorizontalLine />

## Instance Methods

### close

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Close a project

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| closeProjectOptions | [*CloseProjectOptions*](closeprojectoptions.md) | - |

<HorizontalLine />

### closeSequence

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Close a sequence and return true if successful.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| sequence | [*Sequence*](sequence.md) | - |

<HorizontalLine />

### createSequence

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Sequence*

Create a new sequence using the default preset path.

 **Note:** The `presetPath` parameter is deprecated. Use `createSequenceWithPresetPath()` instead.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| name | *string* | - |
| presetPath | *string* | - |

<HorizontalLine />

### createSequenceFromMedia

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Sequence*
  
Create a new sequence with a given name and medias

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| name | *string* | - |
| clipProjectItems | [*ClipProjectItem[]*](/ppro-reference/classes/clipprojectitem[]/) | - |
| targetBin | [*ProjectItem*](projectitem.md) | - |

<HorizontalLine />

### deleteSequence

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Delete a given sequence from the project

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| sequence | [*Sequence*](sequence.md) | - |

<HorizontalLine />

### executeTransaction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Execute undoable transaction by passing compound action

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| callback | *(compoundAction: CompoundAction) => void* | - |
| undoString? | *string* | - |

<HorizontalLine />

### getActiveSequence

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Sequence*
  
Get the active sequence of the project

<HorizontalLine />

### getColorSettings

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*ProjectColorSettings*
  
Get project color settings object

<HorizontalLine />

### getInsertionBin

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*ProjectItem*
  
Get current insertion bin

<HorizontalLine />

### getRootItem

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*FolderItem*
  
The root item of the project which contains all items of the project on the lowest level.

<HorizontalLine />

### getSequence

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Sequence*
  
Get sequence by id from the project

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| guid | [*Guid*](guid.md) | - |

<HorizontalLine />

### getSequences

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Sequence[]*
  
Get an array of all sequences in this project.

<HorizontalLine />

### importAEComps

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| aepPath | *string* | - |
| compNames | [*string[]*](/ppro-reference/classes/string[]/) | - |
| TargetBin | [*ProjectItem*](projectitem.md) | - |

<HorizontalLine />

### importAllAEComps

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| aepPath | *string* | - |
| TargetBin | [*ProjectItem*](projectitem.md) | - |

<HorizontalLine />

### importFiles

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Import files in root/target bin of the project

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| filePaths | [*string[]*](/ppro-reference/classes/string[]/) | - |
| suppressUI | *boolean* | - |
| targetBin | [*ProjectItem*](projectitem.md) | - |
| asNumberedStills | *boolean* | - |

<HorizontalLine />

### importSequences

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| projectPath | *string* | - |
| sequenceIds | [*Guid[]*](/ppro-reference/classes/guid[]/) | - |

<HorizontalLine />

### lockedAccess

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*void*
  
Get a read/upgrade locked access to Project, project state will not change during the execution of callback function. Can call executeTransaction while having locked access.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| callback | *() => void* | - |

<HorizontalLine />

### openSequence

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Open a sequence and return true if successful.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| sequence | [*Sequence*](sequence.md) | - |

<HorizontalLine />

### pauseGrowing

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Pause growing of files instead swap the files

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| pause | *boolean* | - |

<HorizontalLine />

### save

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Save the project

<HorizontalLine />

### saveAs

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Save the project at the provided path

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| path | *string* | - |

<HorizontalLine />

### setActiveSequence

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Set the active sequence of the project

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| sequence | [*Sequence*](sequence.md) | - |

<HorizontalLine />
