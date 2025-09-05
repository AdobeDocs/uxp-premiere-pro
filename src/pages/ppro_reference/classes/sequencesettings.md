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
  - Premiere Pro
---

# SequenceSettings  

## Instance Methods

### getAudioChannelCount

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*number*
  
Get number of channels in the sequence

___

### getAudioChannelType

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*number*
  
Get Audio channel type of sequence. Could be 0 (Mono), 1 (Stereo), 2 (5.1), or 3 (multichannel)

___

### getAudioDisplayFormat

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*TimeDisplay*
  
Get Audio display format

___

### getAudioSampleRate

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*FrameRate*
  
Get audio sample rate

___

### getCompositeInLinearColor

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Get if composite in linear color is checked

___

### getEditingMode

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*string*
  
Get editing mode of sequence

___

### getMaximumBitDepth

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Find if maximum bit depth is set

___

### getMaxRenderQuality

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Find if maximum render quality is set

___

### getPreviewCodec

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*string*
  
Get preview codec of sequence

___

### getPreviewFileFormat

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*string*
  
Get preview file format of sequence

___

### getPreviewFrameRect

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*RectF*
  
Get preview video frame rect in the sequence

___

### getVideoDisplayFormat

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*TimeDisplay*
  
Get Video display format

___

### getVideoFieldType

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*number*
  
Get video field type in the sequence

___

### getVideoFrameRect

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*RectF*
  
Get video frame rect in the sequence

___

### getVideoPixelAspectRatio

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*string*
  
Get Video display format

___

### setAudioDisplayFormat

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Set audio display format of sequence.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| audioDisplay | [*TimeDisplay*](/ppro_reference/classes/timedisplay/) | - |

___

### setAudioSampleRate

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Set audio sample rate

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| inRate | [*FrameRate*](/ppro_reference/classes/framerate/) | - |

___

### setCompositeInLinearColor

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Set if composite in linear color is checked

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| useCompositeInLinearColor | *boolean* | - |

___

### setEditingMode

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Set editing mode of sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| inEditingModeName | *string* | - |

___

### setMaximumBitDepth

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Set maximum bit depth to true/false

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| useMaxBitDepth | *boolean* | - |

___

### setMaxRenderQuality

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Set maximum render quality to true/false

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| useMaxRenderQuality | *boolean* | - |

___

### setPreviewCodec

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Set preview codec of sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| inPreviewCodec | *string* | - |

___

### setPreviewFileFormat

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Set preview file format of sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| inPreviewCodec | *string* | - |

___

### setPreviewFrameRect

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Set preview video frame rect in sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| inPreviewVideoRect | [*RectF*](/ppro_reference/classes/rectf/) | - |

___

### setVideoDisplayFormat

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Set video display format of sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| audioDisplay | [*TimeDisplay*](/ppro_reference/classes/timedisplay/) | - |

___

### setVideoFieldType

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Set video field type in sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| videoFiledType | *number* | - |

___

### setVideoFrameRect

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Set video frame rect in sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| inVideoFrameRect | [*RectF*](/ppro_reference/classes/rectf/) | - |

___

### setVideoPixelAspectRatio

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Set video display format of sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| inPixelAspectRatio | *string* | - |

___
