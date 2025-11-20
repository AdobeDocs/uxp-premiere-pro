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
  - Premiere
---

# Exporter

## Static Methods

### exportSequenceFrame

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Exports from a sequence. Supported formats are bmp, dpx, gif, jpg, exr, png, tga and tif

#### Parameters

| Name     | Type                                            | Description                                                   |
| :------- | :---------------------------------------------- | :------------------------------------------------------------ |
| sequence | [_Sequence_](/ppro_reference/classes/sequence/) | -                                                             |
| time     | [_TickTime_](/ppro_reference/classes/ticktime/) | -                                                             |
| filename | _string_                                        | Filename to be exported , example 'C:/temp/exportedFrame.png' |
| filepath | _string_                                        | Directory to be exported, example 'C:/temp/'                  |
| width    | _number_                                        | -                                                             |
| height   | _number_                                        | -                                                             |

---
