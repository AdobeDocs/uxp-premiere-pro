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
  - Premiere Pro
---

# EncoderManager  

## Properties

| Name | Type | Access | Min Version | Description |
| :------ | :------ | :------ | :------ | :------ |
| isAMEInstalled | *boolean* | R | 25.0 | Check if AME is installed. |

## Static Methods

### getExportFileExtension

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*string*
  
Get the Export File Extension of Input Preset file

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| sequence | [*Sequence*](/ppro_reference/classes/sequence/) | - |
| presetFilePath | *string* | - |

___

### getManager

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*EncoderManager*
  
Get the Encoder Manager object.

___

## Instance Methods

### exportSequence

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Export a sequence. If no output file and preset is specified, the sequence will be exported with the applied export settings or standard export rules will be applied.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| sequence | [*Sequence*](/ppro_reference/classes/sequence/) | - |
| exportType | [*Constants.ExportType*](/ppro_reference/constants) | Constants.ExportType.IMMEDIATELY, Constants.ExportType.QUEUE_TO_AME etc..  |
| outputFile | *string* | - |
| presetFile | *string* | - |
| exportFull | *boolean* | - |

___

## Events

| Name | Version | Description |
| :------ | :------ | :------ |
| EVENT_RENDER_COMPLETE | 25.0 | Broadcast when AME is finished rendering |
| EVENT_RENDER_ERROR | 25.0 | Broadcast when AME gives back error message |
| EVENT_RENDER_CANCEL | 25.0 | Broadcast when AME job is canceled |
| EVENT_RENDER_QUEUE | 25.0 | Broadcast when AME job is queued |
| EVENT_RENDER_PROGRESS | 25.0 | Broadcast when AME job is rendering the job |
