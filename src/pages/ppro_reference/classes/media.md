---
id: "media"
title: "Media"
sidebar_label: "Media"
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

# Media

## Properties

| Name     | Type       | Access | Min Version | Description              |
| :------- | :--------- | :----- | :---------- | :----------------------- |
| start    | _TickTime_ | R      | 25.0        | Get the media start time |
| duration | _TickTime_ | R      | 25.0        | Get the media duration   |

## Instance Methods

### createSetStartAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Returns action that set start of media

#### Parameters

| Name | Type                                            | Description |
| :--- | :---------------------------------------------- | :---------- |
| time | [_TickTime_](/ppro_reference/classes/ticktime/) | -           |

---
