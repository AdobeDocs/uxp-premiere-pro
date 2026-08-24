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

Since: **25.6**

## Properties

| Name | Type | Access | Min Version | Description |
| :--- | :--- | :----- | :---------- | :---------- |
| guid | [*Guid*](guid.md) | R | 25.6 | The unique identifier of the project. |
| name | *string* | R | 25.6 | The project name. |
| path | *string* | R | 25.6 | The absolute file path to the project file. |

## Static Methods

### createProject

Create a new project

Since: **25.6**

Returns: Promise\<[*Project*](project.md)\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| path | *string* | - |

<HorizontalLine />

### getActiveProject

Currently active project.

Since: **25.6**

Returns: Promise\<[*Project*](project.md)\>

<HorizontalLine />

### getProject

Get project referenced by given UID

Since: **25.6**

Returns: [*Project*](project.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| projectGuid | [*Guid*](guid.md) | - |

<HorizontalLine />

### isProject

Returns true if the file at the given path is openable as a Premiere project

Since: **26.2**

Returns: *boolean*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| projectPath | *string* | - |

<HorizontalLine />

### open

Open a project

Since: **25.6**

Returns: Promise\<[*Project*](project.md)\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| path | *string* | - |
| openProjectOptions | [*OpenProjectOptions*](openprojectoptions.md) | - |

<HorizontalLine />

## Instance Methods

### close

Close a project

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| closeProjectOptions | [*CloseProjectOptions*](closeprojectoptions.md) | - |

<HorizontalLine />

### closeSequence

Close a sequence and return true if successful.

Since: **26.2**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| sequence | [*Sequence*](sequence.md) | - |

<HorizontalLine />

### createSequence

Create a new sequence with the default preset path - Parameter presetPath is deprecated, instead use createSequenceWithPresetPath()

Since: **25.6**

Returns: Promise\<[*Sequence*](sequence.md)\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| name | *string* | - |
| presetPath | *string* | - |

<HorizontalLine />

### createSequenceFromMedia

Create a new sequence with a given name and media

Since: **25.6**

Returns: Promise\<[*Sequence*](sequence.md)\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| name | *string* | - |
| clipProjectItems | [*ClipProjectItem[]*](clipprojectitem.md) | - |
| targetBin | [*ProjectItem*](projectitem.md) | - |

<HorizontalLine />

### createSequenceWithPresetPath

Create a new sequence with a preset path

Since: **26.3**

Returns: Promise\<[*Sequence*](sequence.md)\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| name | *string* | - |
| presetPath | *string* | - |

<HorizontalLine />

### deleteSequence

Delete a given sequence from the project

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| sequence | [*Sequence*](sequence.md) | - |

<HorizontalLine />

### executeTransaction

Execute undoable transaction by passing compound action

Since: **25.6**

Returns: *boolean*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| callback | *(compoundAction: CompoundAction) =\> void* | - |
| undoString | *string* | - |

<HorizontalLine />

### getActiveSequence

Get the active sequence of the project

Since: **25.6**

Returns: Promise\<[*Sequence*](sequence.md)\>

<HorizontalLine />

### getColorSettings

Get project color settings object

Since: **25.6**

Returns: Promise\<[*ProjectColorSettings*](projectcolorsettings.md)\>

<HorizontalLine />

### getInsertionBin

Get current insertion bin

Since: **25.6**

Returns: Promise\<[*ProjectItem*](projectitem.md)\>

<HorizontalLine />

### getRootItem

The root item of the project which contains all items of the project on the lowest level.

Since: **25.6**

Returns: Promise\<[*FolderItem*](folderitem.md)\>

<HorizontalLine />

### getSequence

Get sequence by id from the project

Since: **25.6**

Returns: [*Sequence*](sequence.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| guid | [*Guid*](guid.md) | - |

<HorizontalLine />

### getSequences

Get an array of all sequences in this project.

Since: **25.6**

Returns: Promise\<[*Sequence[]*](sequence.md)\>

<HorizontalLine />

### importAEComps

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| aepPath | *string* | - |
| compNames | *string[]* | - |
| targetBin | [*ProjectItem*](projectitem.md) | - |

<HorizontalLine />

### importAllAEComps

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| aepPath | *string* | - |
| targetBin | [*ProjectItem*](projectitem.md) | - |

<HorizontalLine />

### importFiles

Import files in root/target bin of the project

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| filePaths | *string[]* | - |
| suppressUI | *boolean* | - |
| targetBin | [*ProjectItem*](projectitem.md) | - |
| asNumberedStills | *boolean* | - |

<HorizontalLine />

### importSequences

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| projectPath | *string* | - |
| sequenceIds | [*Guid[]*](guid.md) | - |

<HorizontalLine />

### lockedAccess

Get a read/upgrade locked access to Project, project state will not change during the execution of callback function. Can call executeTransaction while having locked access.

Since: **25.6**

Returns: *void*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| callback | *() =\> void* | - |

<HorizontalLine />

### openSequence

Open a sequence and return true if successful.

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| sequence | [*Sequence*](sequence.md) | - |

<HorizontalLine />

### pauseGrowing

Pauses or resumes monitoring of actively-captured (growing) media files in the project. When paused, Premiere stops refreshing clips whose source files are still being written to disk, allowing stable playback at the current captured duration. Pass true to pause, false to resume.

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| pause | *boolean* | - |

<HorizontalLine />

### save

Save the project

Since: **25.6**

Returns: Promise\<*boolean*\>

<HorizontalLine />

### saveAs

Saves a copy of the project at the provided path, mirroring the 'File > Save As' behavior in Premiere Pro: the newly saved copy becomes the active project, just as it would after using 'Save As' in the application. Separately, and perhaps unexpectedly, the `Project` object `saveAs()` was called on is itself updated in place to represent that new copy. It does not stay pinned to the original project file. This also affects chained calls, meaning calling `saveAs()` again on the same object saves a copy of that new file, not the original. To continue working with the original project--for example, to derive several independent copies from the same source--reopen it explicitly via `Project.open()` before each subsequent `saveAs()` call, rather than assuming the existing handle still refers to it.

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| path | *string* | - |

<HorizontalLine />

### setActiveSequence

Set the active sequence of the project

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| sequence | [*Sequence*](sequence.md) | - |

<HorizontalLine />
