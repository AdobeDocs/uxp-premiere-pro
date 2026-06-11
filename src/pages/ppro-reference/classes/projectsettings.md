---
description: Overview of ProjectSettings
id: projectsettings
title: ProjectSettings
sidebar_label: ProjectSettings
repo: uxp-premierepro
product: premierepro
keywords: 
---

# ProjectSettings

Since: **25.6**

## Static Methods

### createSetIngestSettingsAction

Returns an action which sets IngestSettings

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| project | [*Project*](project.md) | - |
| ingestSettings | [*IngestSettings*](ingestsettings.md) | - |

<HorizontalLine />

### createSetScratchDiskSettingsAction

Returns an action which sets ScratchDiskSetting

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| project | [*Project*](project.md) | - |
| scratchDiskSettings | [*ScratchDiskSettings*](scratchdisksettings.md) | - |

<HorizontalLine />

### getIngestSettings

Returns project ingest settings

Since: **25.6**

Returns: Promise\<[*IngestSettings*](ingestsettings.md)\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| project | [*Project*](project.md) | - |

<HorizontalLine />

### getScratchDiskSettings

Returns project ScratchDiskSettings

Since: **25.6**

Returns: Promise\<[*ScratchDiskSettings*](scratchdisksettings.md)\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| project | [*Project*](project.md) | - |

<HorizontalLine />
