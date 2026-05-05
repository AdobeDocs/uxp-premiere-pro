---
description: Overview of SequenceSettings
id: sequencesettings
title: SequenceSettings
sidebar_label: SequenceSettings
repo: uxp-premierepro
product: premierepro
keywords: 
---

# SequenceSettings  

## Instance Methods

### getAudioChannelCount

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*number*
  
Get number of channels in the sequence

<HorizontalLine />

### getAudioChannelType

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*number*
  
Get Audio channel type of sequence. Could be 0 (Mono), 1 (Stereo), 2 (5.1), or 3 (multichannel)

<HorizontalLine />

### getAudioDisplayFormat

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*TimeDisplay*
  
Get Audio display format

<HorizontalLine />

### getAudioSampleRate

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*FrameRate*
  
Get audio sample rate

<HorizontalLine />

### getCompositeInLinearColor

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Get if composite in linear color is checked

<HorizontalLine />

### getEditingMode

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*string*
  
Get editing mode of sequence

<HorizontalLine />

### getMaximumBitDepth

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Find if maximum bit depth is set

<HorizontalLine />

### getMaxRenderQuality

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Find if maximum render quality is set

<HorizontalLine />

### getPreviewCodec

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*string*
  
Get preview codec of sequence

<HorizontalLine />

### getPreviewFileFormat

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*string*
  
Get preview file format of sequence

<HorizontalLine />

### getPreviewFrameRect

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*RectF*
  
Get preview video frame rect in the sequence

<HorizontalLine />

### getVideoDisplayFormat

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*TimeDisplay*
  
Get Video display format

<HorizontalLine />

### getVideoFieldType

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*number*
  
Get video field type in the sequence

<HorizontalLine />

### getVideoFrameRate

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*FrameRate*
  
Get video frame rate in the sequence

<HorizontalLine />

### getVideoFrameRect

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*RectF*
  
Get video frame rect in the sequence

<HorizontalLine />

### getVideoPixelAspectRatio

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*string*
  
Get Video display format

<HorizontalLine />

### setAudioDisplayFormat

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Set audio display format of sequence.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| audioDisplay | [*TimeDisplay*](timedisplay.md) | - |

<HorizontalLine />

### setAudioSampleRate

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Set audio sample rate

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| inRate | [*FrameRate*](framerate.md) | - |

<HorizontalLine />

### setCompositeInLinearColor

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Set if composite in linear color is checked

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| useCompositeInLinearColor | *boolean* | - |

<HorizontalLine />

### setEditingMode

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Set editing mode of sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| inEditingModeName | *string* | - |

<HorizontalLine />

### setMaximumBitDepth

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Set maximum bit depth to true/false

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| useMaxBitDepth | *boolean* | - |

<HorizontalLine />

### setMaxRenderQuality

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Set maximum render quality to true/false

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| useMaxRenderQuality | *boolean* | - |

<HorizontalLine />

### setPreviewCodec

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Set preview codec of sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| inPreviewCodec | *string* | - |

<HorizontalLine />

### setPreviewFileFormat

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Set preview file format of sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| inPreviewCodec | *string* | - |

<HorizontalLine />

### setPreviewFrameRect

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Set preview video frame rect in sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| inPreviewVideoRect | [*RectF*](rectf.md) | - |

<HorizontalLine />

### setVideoDisplayFormat

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Set video display format of sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| audioDisplay | [*TimeDisplay*](timedisplay.md) | - |

<HorizontalLine />

### setVideoFieldType

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Set video field type in sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| videoFiledType | *number* | - |

<HorizontalLine />

### setVideoFrameRate

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Set video frame rate in the sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| inVideoFrameRate | [*FrameRate*](framerate.md) | - |

<HorizontalLine />

### setVideoFrameRect

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Set video frame rect in sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| inVideoFrameRect | [*RectF*](rectf.md) | - |

<HorizontalLine />

### setVideoPixelAspectRatio

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Set video display format of sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| inPixelAspectRatio | *string* | - |

<HorizontalLine />
