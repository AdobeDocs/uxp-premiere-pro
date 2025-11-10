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
  - Premiere
---

# Project

## Properties

| Name | Type     | Access | Min Version | Description                                 |
| :--- | :------- | :----- | :---------- | :------------------------------------------ |
| guid | _Guid_   | R      | 25.0        | The unique identifier of the project.       |
| name | _string_ | R      | 25.0        | The project name.                           |
| path | _string_ | R      | 25.0        | The absolute file path to the project file. |

## Static Methods

### createProject

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Project_

Create a new project

#### Parameters

| Name | Type     | Description |
| :--- | :------- | :---------- |
| path | _string_ | -           |

---

### getActiveProject

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Project_

Currently active project.

---

### getProject

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Project_

Get project referenced by given UID

#### Parameters

| Name        | Type                                    | Description |
| :---------- | :-------------------------------------- | :---------- |
| projectGuid | [_Guid_](/ppro_reference/classes/guid/) | -           |

---

### open

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Project_

Open a project

#### Parameters

| Name               | Type                                                                | Description |
| :----------------- | :------------------------------------------------------------------ | :---------- |
| path               | _string_                                                            | -           |
| openProjectOptions | [_OpenProjectOptions_](/ppro_reference/classes/openprojectoptions/) | -           |

---

## Instance Methods

### close

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Close a project

#### Parameters

| Name                | Type                                                                  | Description |
| :------------------ | :-------------------------------------------------------------------- | :---------- |
| closeProjectOptions | [_CloseProjectOptions_](/ppro_reference/classes/closeprojectoptions/) | -           |

---

### createSequence

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Sequence_

Create a new sequence with the default preset path - Parameter presetPath is deprecated, instead use createSequenceWithPresetPath()

#### Parameters

| Name       | Type     | Description |
| :--------- | :------- | :---------- |
| name       | _string_ | -           |
| presetPath | _string_ | -           |

---

### createSequenceFromMedia

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Sequence_

Create a new sequence with a given name and medias

#### Parameters

| Name             | Type                                                              | Description |
| :--------------- | :---------------------------------------------------------------- | :---------- |
| name             | _string_                                                          | -           |
| clipProjectItems | [_ClipProjectItem[]_](/ppro_reference/classes/clipprojectitem[]/) | -           |
| targetBin        | [_ProjectItem_](/ppro_reference/classes/projectitem/)             | -           |

---

### deleteSequence

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Delete a given sequence from the project

#### Parameters

| Name     | Type                                            | Description |
| :------- | :---------------------------------------------- | :---------- |
| sequence | [_Sequence_](/ppro_reference/classes/sequence/) | -           |

---

### executeTransaction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Execute undoable transaction by passing compound action

#### Parameters

| Name        | Type                                       | Description |
| :---------- | :----------------------------------------- | :---------- |
| callback    | _(compoundAction: CompoundAction) => void_ | -           |
| undoString? | _string_                                   | -           |

---

### getActiveSequence

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Sequence_

Get the active sequence of the project

---

### getColorSettings

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_ProjectColorSettings_

Get project color settings object

---

### getInsertionBin

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_ProjectItem_

Get current insertion bin

---

### getRootItem

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_FolderItem_

The root item of the project which contains all items of the project on the lowest level.

---

### getSequence

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Sequence_

Get sequence by id from the project

#### Parameters

| Name | Type                                    | Description |
| :--- | :-------------------------------------- | :---------- |
| guid | [_Guid_](/ppro_reference/classes/guid/) | -           |

---

### getSequences

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Sequence[]_

Get an array of all sequences in this project.

---

### importAEComps

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

#### Parameters

| Name      | Type                                                  | Description |
| :-------- | :---------------------------------------------------- | :---------- |
| aepPath   | _string_                                              | -           |
| compNames | [_string[]_](/ppro_reference/classes/string[]/)       | -           |
| TargetBin | [_ProjectItem_](/ppro_reference/classes/projectitem/) | -           |

---

### importAllAEComps

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

#### Parameters

| Name      | Type                                                  | Description |
| :-------- | :---------------------------------------------------- | :---------- |
| aepPath   | _string_                                              | -           |
| TargetBin | [_ProjectItem_](/ppro_reference/classes/projectitem/) | -           |

---

### importFiles

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Import files in root/target bin of the project

#### Parameters

| Name             | Type                                                  | Description |
| :--------------- | :---------------------------------------------------- | :---------- |
| filePaths        | [_string[]_](/ppro_reference/classes/string[]/)       | -           |
| suppressUI       | _boolean_                                             | -           |
| targetBin        | [_ProjectItem_](/ppro_reference/classes/projectitem/) | -           |
| asNumberedStills | _boolean_                                             | -           |

---

### importSequences

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

#### Parameters

| Name        | Type                                        | Description |
| :---------- | :------------------------------------------ | :---------- |
| projectPath | _string_                                    | -           |
| sequenceIds | [_Guid[]_](/ppro_reference/classes/guid[]/) | -           |

---

### lockedAccess

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_void_

Get a read/upgrade locked access to Project, project state will not change during the execution of callback function. Can call executeTransaction while having locked access.

#### Parameters

| Name     | Type         | Description |
| :------- | :----------- | :---------- |
| callback | _() => void_ | -           |

---

### openSequence

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Open a sequence and return true if successful.

#### Parameters

| Name     | Type                                            | Description |
| :------- | :---------------------------------------------- | :---------- |
| sequence | [_Sequence_](/ppro_reference/classes/sequence/) | -           |

---

### pauseGrowing

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Pause growing of files instead swap the files

#### Parameters

| Name  | Type      | Description |
| :---- | :-------- | :---------- |
| pause | _boolean_ | -           |

---

### save

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Save the project

---

### saveAs

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Save the project at the provided path

#### Parameters

| Name | Type     | Description |
| :--- | :------- | :---------- |
| path | _string_ | -           |

---

### setActiveSequence

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Set the active sequence of the project

#### Parameters

| Name     | Type                                            | Description |
| :------- | :---------------------------------------------- | :---------- |
| sequence | [_Sequence_](/ppro_reference/classes/sequence/) | -           |

---
