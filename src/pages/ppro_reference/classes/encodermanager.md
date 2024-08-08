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
| isAMEInstalled | *boolean* | R | 23.0 | Check if AME is installed. |

## Methods

### exportSequence

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*boolean*

Export a sequence. If no output file and preset is specified, the sequence will be exported with the applied export settings or standard export rules will be applied.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| sequence | *object* | - |
| exportType | *string* | - |
| outputFile | *string* | - |
| presetFile | *string* | - |
| exportFull | *boolean* | - |

___

### getManager

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*EncoderManager*

Get the Encoder Manager object.

___

### subscribeToEvent

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*boolean*

Propagates the given event on this object.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| eventKey | *string* | - |

___

## Events

| Name | Version | Description |
| :------ | :------ | :------ || EVENT_RENDER_COMPLETE | 23.0 | Broadcast when AME is finished rendering |
