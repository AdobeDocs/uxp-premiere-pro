---
description: Overview of Exporter
id: exporter
title: Exporter
sidebar_label: Exporter
repo: uxp-premierepro
product: premierepro
keywords: 
---

# Exporter

Since: **25.6**

## Static Methods

### exportSequenceFrame

Exports from a sequence. Supported formats are bmp, dpx, gif, jpg, exr, png, tga and tif

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| sequence | [*Sequence*](sequence.md) | - |
| time | [*TickTime*](ticktime.md) | - |
| filename | *string* | Filename to be exported , example 'C:/temp/exportedFrame.png' |
| filepath | *string* | Directory to be exported, example 'C:/temp/' |
| width | *number* | - |
| height | *number* | - |

<HorizontalLine />
