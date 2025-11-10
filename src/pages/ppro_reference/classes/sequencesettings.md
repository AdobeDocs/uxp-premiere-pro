---
id: "sequencesettings"
title: "SequenceSettings"
sidebar_label: "SequenceSettings"
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

# SequenceSettings

## Instance Methods

### getAudioChannelCount

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_number_

Get number of channels in the sequence

---

### getAudioChannelType

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_number_

Get Audio channel type of sequence. Could be 0 (Mono), 1 (Stereo), 2 (5.1), or 3 (multichannel)

---

### getAudioDisplayFormat

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_TimeDisplay_

Get Audio display format

---

### getAudioSampleRate

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_FrameRate_

Get audio sample rate

---

### getCompositeInLinearColor

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Get if composite in linear color is checked

---

### getEditingMode

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_string_

Get editing mode of sequence

---

### getMaximumBitDepth

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Find if maximum bit depth is set

---

### getMaxRenderQuality

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Find if maximum render quality is set

---

### getPreviewCodec

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_string_

Get preview codec of sequence

---

### getPreviewFileFormat

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_string_

Get preview file format of sequence

---

### getPreviewFrameRect

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_RectF_

Get preview video frame rect in the sequence

---

### getVideoDisplayFormat

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_TimeDisplay_

Get Video display format

---

### getVideoFieldType

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_number_

Get video field type in the sequence

---

### getVideoFrameRect

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_RectF_

Get video frame rect in the sequence

---

### getVideoPixelAspectRatio

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_string_

Get Video display format

---

### setAudioDisplayFormat

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Set audio display format of sequence.

#### Parameters

| Name         | Type                                                  | Description |
| :----------- | :---------------------------------------------------- | :---------- |
| audioDisplay | [_TimeDisplay_](/ppro_reference/classes/timedisplay/) | -           |

---

### setAudioSampleRate

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Set audio sample rate

#### Parameters

| Name   | Type                                              | Description |
| :----- | :------------------------------------------------ | :---------- |
| inRate | [_FrameRate_](/ppro_reference/classes/framerate/) | -           |

---

### setCompositeInLinearColor

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Set if composite in linear color is checked

#### Parameters

| Name                      | Type      | Description |
| :------------------------ | :-------- | :---------- |
| useCompositeInLinearColor | _boolean_ | -           |

---

### setEditingMode

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Set editing mode of sequence

#### Parameters

| Name              | Type     | Description |
| :---------------- | :------- | :---------- |
| inEditingModeName | _string_ | -           |

---

### setMaximumBitDepth

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Set maximum bit depth to true/false

#### Parameters

| Name           | Type      | Description |
| :------------- | :-------- | :---------- |
| useMaxBitDepth | _boolean_ | -           |

---

### setMaxRenderQuality

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Set maximum render quality to true/false

#### Parameters

| Name                | Type      | Description |
| :------------------ | :-------- | :---------- |
| useMaxRenderQuality | _boolean_ | -           |

---

### setPreviewCodec

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Set preview codec of sequence

#### Parameters

| Name           | Type     | Description |
| :------------- | :------- | :---------- |
| inPreviewCodec | _string_ | -           |

---

### setPreviewFileFormat

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Set preview file format of sequence

#### Parameters

| Name           | Type     | Description |
| :------------- | :------- | :---------- |
| inPreviewCodec | _string_ | -           |

---

### setPreviewFrameRect

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Set preview video frame rect in sequence

#### Parameters

| Name               | Type                                      | Description |
| :----------------- | :---------------------------------------- | :---------- |
| inPreviewVideoRect | [_RectF_](/ppro_reference/classes/rectf/) | -           |

---

### setVideoDisplayFormat

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Set video display format of sequence

#### Parameters

| Name         | Type                                                  | Description |
| :----------- | :---------------------------------------------------- | :---------- |
| audioDisplay | [_TimeDisplay_](/ppro_reference/classes/timedisplay/) | -           |

---

### setVideoFieldType

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Set video field type in sequence

#### Parameters

| Name           | Type     | Description |
| :------------- | :------- | :---------- |
| videoFiledType | _number_ | -           |

---

### setVideoFrameRect

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Set video frame rect in sequence

#### Parameters

| Name             | Type                                      | Description |
| :--------------- | :---------------------------------------- | :---------- |
| inVideoFrameRect | [_RectF_](/ppro_reference/classes/rectf/) | -           |

---

### setVideoPixelAspectRatio

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Set video display format of sequence

#### Parameters

| Name               | Type     | Description |
| :----------------- | :------- | :---------- |
| inPixelAspectRatio | _string_ | -           |

---
