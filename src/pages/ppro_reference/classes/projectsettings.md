---
id: "projectsettings"
title: "ProjectSettings"
sidebar_label: "ProjectSettings"
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

# ProjectSettings

## Static Methods

### createSetIngestSettingsAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Returns an action which sets IngestSettings

#### Parameters

| Name           | Type                                                        | Description |
| :------------- | :---------------------------------------------------------- | :---------- |
| project        | [_Project_](/ppro_reference/classes/project/)               | -           |
| ingestSettings | [_IngestSettings_](/ppro_reference/classes/ingestsettings/) | -           |

---

### createSetScratchDiskSettingsAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Returns an action which sets ScratchDiskSetting

#### Parameters

| Name                | Type                                                                  | Description |
| :------------------ | :-------------------------------------------------------------------- | :---------- |
| project             | [_Project_](/ppro_reference/classes/project/)                         | -           |
| scratchDiskSettings | [_ScratchDiskSettings_](/ppro_reference/classes/scratchdisksettings/) | -           |

---

### getIngestSettings

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_IngestSettings_

Returns project ingest settings

#### Parameters

| Name    | Type                                          | Description |
| :------ | :-------------------------------------------- | :---------- |
| project | [_Project_](/ppro_reference/classes/project/) | -           |

---

### getScratchDiskSettings

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_ScratchDiskSettings_

Returns project ScratchDiskSettings

#### Parameters

| Name    | Type                                          | Description |
| :------ | :-------------------------------------------- | :---------- |
| project | [_Project_](/ppro_reference/classes/project/) | -           |

---
