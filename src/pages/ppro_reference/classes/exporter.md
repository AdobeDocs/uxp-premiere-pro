---
id: "exporter"
title: "Exporter"
sidebar_label: "Exporter"
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

# Exporter  

## Static Methods

### exportSequenceFrame

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Exports from a sequence. Supported formats are bmp, dpx, gif, jpg, exr, png, tga and tif

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| sequence | *object* | - |
| time | [*TickTime*](/ppro_reference/classes/ticktime/) | - |
| filename | *string* | Filename to be exported , example 'C:/temp/exportedFrame.png' |
| filepath | *string* | Directory to be exported, example 'C:/temp/' |
| width | *number* | - |
| height | *number* | - |

___
