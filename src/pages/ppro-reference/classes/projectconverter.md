---
description: Overview of ProjectConverter
id: projectconverter
title: ProjectConverter
sidebar_label: ProjectConverter
repo: uxp-premierepro
product: premierepro
keywords: 
---

# ProjectConverter

Since: **26.2**

## Static Methods

### exportAAF

Export a sequence as an AAF (Advanced Authoring Format) file to the specified output path.

Since: **26.3**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| sequence | [*Sequence*](sequence.md) | - |
| filePath | *string* | - |
| aafExportOptions | [*AAFExportOptions*](aafexportoptions.md) | - |

<HorizontalLine />

### exportAsFinalCutProXML

Export a sequence as Final Cut Pro XML to the specified output file path.

Since: **26.2**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| sequence | [*Sequence*](sequence.md) | - |
| outputFilePath | *string* | - |
| suppressUI | *boolean* | - |

<HorizontalLine />

### exportAsOpenTimelineIO

Export a sequence as OpenTimelineIO to the specified output file path.

Since: **26.2**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| sequence | [*Sequence*](sequence.md) | - |
| outputFilePath | *string* | - |
| suppressUI | *boolean* | - |

<HorizontalLine />
