---
id: "footageinterpretation"
title: "FootageInterpretation"
sidebar_label: "FootageInterpretation"
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

# FootageInterpretation

## Properties

| Name                       | Type     | Access | Min Version | Description                 |
| :------------------------- | :------- | :----- | :---------- | :-------------------------- |
| ALPHACHANNEL_NONE          | _number_ | R      | 25.0        | alpha channel none          |
| ALPHACHANNEL_STRAIGHT      | _number_ | R      | 25.0        | alpha channel straight      |
| ALPHACHANNEL_PREMULTIPLIED | _number_ | R      | 25.0        | alpha channel premultiplied |
| ALPHACHANNEL_IGNORE        | _number_ | R      | 25.0        | alpha channel ignore        |
| FIELD_TYPE_DEFAULT         | _number_ | R      | 25.0        | default filed type invalid  |
| FIELD_TYPE_PROGRESSIVE     | _number_ | R      | 25.0        | field type progressive      |
| FIELD_TYPE_UPPERFIRST      | _number_ | R      | 25.0        | field type upperfirst       |
| FIELD_TYPE_LOWERFIRST      | _number_ | R      | 25.0        | field type lowerfirst       |

## Instance Methods

### getAlphaUsage

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_number_

Get alpha usage type property of footage

---

### getFieldType

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_number_

Get field type of footage

---

### getFrameRate

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_number_

Get frame rate of footage

---

### getIgnoreAlpha

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Get ignore alpha property of footage

---

### getInputLUTID

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_string_

Get input LUTID of footage

---

### getInvertAlpha

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Get invert alpha property of footage

---

### getPixelAspectRatio

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_number_

Get pixel aspect ratio of footage

---

### getRemovePullDown

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Get removePullDown property of footage

---

### getVrConform

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_number_

Get vr conform projection type of footage

---

### getVrHorzView

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_number_

Get vr horizontal view of footage

---

### getVrLayout

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_number_

Get vr layout type of footage

---

### getVrVertView

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_number_

Get vr vertical view of footage

---

### setAlphaUsage

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Set alpha usage type property of footage

#### Parameters

| Name       | Type     | Description |
| :--------- | :------- | :---------- |
| alphaUsage | _number_ | -           |

---

### setFieldType

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Set field type of footage

#### Parameters

| Name      | Type     | Description |
| :-------- | :------- | :---------- |
| fieldType | _number_ | -           |

---

### setFrameRate

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Set frame rate of footage

#### Parameters

| Name      | Type     | Description |
| :-------- | :------- | :---------- |
| frameRate | _number_ | -           |

---

### setIgnoreAlpha

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Set ignore alpha property of footage

#### Parameters

| Name        | Type      | Description |
| :---------- | :-------- | :---------- |
| ignoreAlpha | _boolean_ | -           |

---

### setInputLUTID

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Set input LUTID of footage

#### Parameters

| Name       | Type     | Description |
| :--------- | :------- | :---------- |
| inputLUTID | _string_ | -           |

---

### setInvertAlpha

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Set invert alpha property of footage

#### Parameters

| Name        | Type      | Description |
| :---------- | :-------- | :---------- |
| invertAlpha | _boolean_ | -           |

---

### setPixelAspectRatio

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Set pixel aspect ratio of footage

#### Parameters

| Name             | Type     | Description |
| :--------------- | :------- | :---------- |
| pixelAspectRatio | _number_ | -           |

---

### setRemovePullDown

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Set removePullDown property of footage

#### Parameters

| Name           | Type      | Description |
| :------------- | :-------- | :---------- |
| removePulldown | _boolean_ | -           |

---

### setVrConform

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Set vr conform projection type of footage

#### Parameters

| Name      | Type     | Description |
| :-------- | :------- | :---------- |
| vrConform | _number_ | -           |

---

### setVrHorzView

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Set vr horizontal view of footage

#### Parameters

| Name       | Type     | Description |
| :--------- | :------- | :---------- |
| vrHorzView | _number_ | -           |

---

### setVrLayout

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Set vr layout type of footage

#### Parameters

| Name     | Type     | Description |
| :------- | :------- | :---------- |
| vrLayOut | _number_ | -           |

---

### setVrVertView

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Set vr horizontal view of footage

#### Parameters

| Name       | Type     | Description |
| :--------- | :------- | :---------- |
| vrVertView | _number_ | -           |

---
