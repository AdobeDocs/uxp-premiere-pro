---
description: Overview of ScratchDiskSettings
id: scratchdisksettings
title: ScratchDiskSettings
sidebar_label: ScratchDiskSettings
repo: uxp-premierepro
product: premierepro
keywords: 
---

# ScratchDiskSettings

Since: **25.6**

## Instance Methods

### getScratchDiskPath

Gets the scratchDisk location for specific disktype - may return symbolic paths for reserved types like 'MyDocuments'

Since: **25.6**

Returns: *string*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| ScratchDiskType | [*Constants.ScratchDiskFolderType*](../constants/index.md#scratchdiskfoldertype) | - |

<HorizontalLine />

### setScratchDiskPath

Sets project ScratchDisk Path

Since: **25.6**

Returns: *boolean*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| ScratchDiskType | [*Constants.ScratchDiskFolderType*](../constants/index.md#scratchdiskfoldertype) | - |
| ScratchDiskValue | [*Constants.ScratchDiskFolder*](../constants/index.md#scratchdiskfolder) | - |

<HorizontalLine />
