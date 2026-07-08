---
description: Overview of EncoderManager
id: encodermanager
title: EncoderManager
sidebar_label: EncoderManager
repo: uxp-premierepro
product: premierepro
keywords: 
---

# EncoderManager

Since: **25.6**

## Properties

| Name | Type | Access | Min Version | Description |
| :--- | :--- | :----- | :---------- | :---------- |
| isAMEInstalled | *boolean* | R | 25.6 | Check if AME is installed. |

## Static Methods

### getExportFileExtension

Get the Export File Extension of Input Preset file

Since: **25.6**

Returns: Promise\<*string*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| sequence | [*Sequence*](sequence.md) | - |
| presetFilePath | *string* | - |

<HorizontalLine />

### getManager

Get the Encoder Manager object.

Since: **25.6**

Returns: [*EncoderManager*](encodermanager.md)

<HorizontalLine />

## Instance Methods

### encodeFile

Encode input media file in AME

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| filePath | *string* | - |
| outputFile | *string* | - |
| presetFile | *string* | - |
| inPoint | [*TickTime*](ticktime.md) | - |
| outPoint | [*TickTime*](ticktime.md) | - |
| workArea | *number* | - |
| removeUponCompletion | *boolean* | - |
| startQueueImmediately | *boolean* | - |

<HorizontalLine />

### encodeProjectItem

Encode input clipProjectItem in AME

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| clipProjectItem | [*ClipProjectItem*](clipprojectitem.md) | - |
| outputFile | *string* | - |
| presetFile | *string* | - |
| workArea | *number* | - |
| removeUponCompletion | *boolean* | - |
| startQueueImmediately | *boolean* | - |

<HorizontalLine />

### exportSequence

Export a sequence. If no output file and preset is specified, the sequence will be exported with the applied export settings or standard export rules will be applied.

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| sequence | [*Sequence*](sequence.md) | - |
| exportType | [*Constants.ExportType*](../constants/index.md#exporttype) | Constants.ExportType.IMMEDIATELY, Constants.ExportType.QUEUE_TO_AME etc..  |
| outputFile | *string* | - |
| presetFile | *string* | - |
| exportFull | *boolean* | - |

<HorizontalLine />

### launchEncoder

Launch AME asynchronously if not already running.

Since: **26.3**

Returns: Promise\<*boolean*\>

<HorizontalLine />

### setEmbeddedXMPEnabled

Set whether to enable embedded XMP when exporting a sequence.

Since: **26.3**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| enabled | *boolean* | - |

<HorizontalLine />

### setSidecarXMPEnabled

Set whether to enable sidecar XMP when exporting a sequence.

Since: **26.3**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| enabled | *boolean* | - |

<HorizontalLine />

### startBatchEncode

Start encoding the AME batch queue.

Since: **26.3**

Returns: Promise\<*boolean*\>

<HorizontalLine />

## Events

| Name | Version | Description |
| :--- | :------ | :---------- |
| EVENT_RENDER_COMPLETE | 25.6 | Broadcast when AME is finished rendering |
| EVENT_RENDER_ERROR | 25.6 | Broadcast when AME gives back error message |
| EVENT_RENDER_CANCEL | 25.6 | Broadcast when AME job is canceled |
| EVENT_RENDER_QUEUE | 25.6 | Broadcast when AME job is queued |
| EVENT_RENDER_PROGRESS | 25.6 | Broadcast when AME job is rendering the job |
