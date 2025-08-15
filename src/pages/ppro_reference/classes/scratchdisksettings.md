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
  - Premiere Pro
---

# ScratchDiskSettings  

## Instance Methods

### getScratchDiskPath

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*string*
  
Gets the scratchDisk location for specific disktype - may return symbolic paths for reserved types like 'MyDocuments'

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| ScratchDiskType | [*Constants.ScratchDiskFolderType*](/ppro_reference/constants) | - |

___

### setScratchDiskPath

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Sets project ScratchDisk Path

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| ScratchDiskType | [*Constants.ScratchDiskFolderType*](/ppro_reference/constants) | - |
| ScratchDiskValue | [*Constants.ScratchDiskFolder*](/ppro_reference/constants) | - |

___
