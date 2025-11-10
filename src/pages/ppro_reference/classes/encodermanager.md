---
id: "encodermanager"
title: "EncoderManager"
sidebar_label: "EncoderManager"
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

# EncoderManager

## Properties

| Name           | Type      | Access | Min Version | Description                |
| :------------- | :-------- | :----- | :---------- | :------------------------- |
| isAMEInstalled | _boolean_ | R      | 25.0        | Check if AME is installed. |

## Static Methods

### getExportFileExtension

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_string_

Get the Export File Extension of Input Preset file

#### Parameters

| Name           | Type                                            | Description |
| :------------- | :---------------------------------------------- | :---------- |
| sequence       | [_Sequence_](/ppro_reference/classes/sequence/) | -           |
| presetFilePath | _string_                                        | -           |

---

### getManager

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_EncoderManager_

Get the Encoder Manager object.

---

## Instance Methods

### encodeFile

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Encode input media file in AME

#### Parameters

| Name                  | Type                                            | Description |
| :-------------------- | :---------------------------------------------- | :---------- |
| filePath              | _string_                                        | -           |
| outputFile            | _string_                                        | -           |
| presetFile            | _string_                                        | -           |
| inPoint               | [_TickTime_](/ppro_reference/classes/ticktime/) | -           |
| outPoint              | [_TickTime_](/ppro_reference/classes/ticktime/) | -           |
| workArea              | _number_                                        | -           |
| removeUponCompletion  | _boolean_                                       | -           |
| startQueueImmediately | _boolean_                                       | -           |

---

### encodeProjectItem

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Encode input clipProjectItem in AME

#### Parameters

| Name                  | Type                                                          | Description |
| :-------------------- | :------------------------------------------------------------ | :---------- |
| clipProjectItem       | [_ClipProjectItem_](/ppro_reference/classes/clipprojectitem/) | -           |
| outputFile            | _string_                                                      | -           |
| presetFile            | _string_                                                      | -           |
| workArea              | _number_                                                      | -           |
| removeUponCompletion  | _boolean_                                                     | -           |
| startQueueImmediately | _boolean_                                                     | -           |

---

### exportSequence

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Export a sequence. If no output file and preset is specified, the sequence will be exported with the applied export settings or standard export rules will be applied.

#### Parameters

| Name       | Type                                                | Description                                                               |
| :--------- | :-------------------------------------------------- | :------------------------------------------------------------------------ |
| sequence   | [_Sequence_](/ppro_reference/classes/sequence/)     | -                                                                         |
| exportType | [_Constants.ExportType_](/ppro_reference/constants) | Constants.ExportType.IMMEDIATELY, Constants.ExportType.QUEUE_TO_AME etc.. |
| outputFile | _string_                                            | -                                                                         |
| presetFile | _string_                                            | -                                                                         |
| exportFull | _boolean_                                           | -                                                                         |

---

## Events

| Name                  | Version | Description                                 |
| :-------------------- | :------ | :------------------------------------------ |
| EVENT_RENDER_COMPLETE | 25.0    | Broadcast when AME is finished rendering    |
| EVENT_RENDER_ERROR    | 25.0    | Broadcast when AME gives back error message |
| EVENT_RENDER_CANCEL   | 25.0    | Broadcast when AME job is canceled          |
| EVENT_RENDER_QUEUE    | 25.0    | Broadcast when AME job is queued            |
| EVENT_RENDER_PROGRESS | 25.0    | Broadcast when AME job is rendering the job |
