---
id: "scratchdisksettings"
title: "ScratchDiskSettings"
sidebar_label: "ScratchDiskSettings"
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

# ScratchDiskSettings

## Instance Methods

### getScratchDiskPath

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_string_

Gets the scratchDisk location for specific disktype - may return symbolic paths for reserved types like 'MyDocuments'

#### Parameters

| Name            | Type                                                           | Description |
| :-------------- | :------------------------------------------------------------- | :---------- |
| ScratchDiskType | [_Constants.ScratchDiskFolderType_](/ppro_reference/constants) | -           |

---

### setScratchDiskPath

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Sets project ScratchDisk Path

#### Parameters

| Name             | Type                                                           | Description |
| :--------------- | :------------------------------------------------------------- | :---------- |
| ScratchDiskType  | [_Constants.ScratchDiskFolderType_](/ppro_reference/constants) | -           |
| ScratchDiskValue | [_Constants.ScratchDiskFolder_](/ppro_reference/constants)     | -           |

---
