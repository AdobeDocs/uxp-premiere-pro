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

Since: **25.6**

## Instance Methods

### getAudioChannelCount

Get number of channels in the sequence

Since: **25.6**

Returns: Promise\<*number*\>

<HorizontalLine />

### getAudioChannelType

Get Audio channel type of sequence. Could be 0 (Mono), 1 (Stereo), 2 (5.1), or 3 (multichannel)

Since: **25.6**

Returns: Promise\<*number*\>

<HorizontalLine />

### getAudioDisplayFormat

Get Audio display format

Since: **25.6**

Returns: Promise\<[*TimeDisplay*](timedisplay.md)\>

<HorizontalLine />

### getAudioSampleRate

Get audio sample rate

Since: **25.6**

Returns: Promise\<[*FrameRate*](framerate.md)\>

<HorizontalLine />

### getCompositeInLinearColor

Get if composite in linear color is checked

Since: **25.6**

Returns: Promise\<*boolean*\>

<HorizontalLine />

### getEditingMode

Get editing mode of sequence

Since: **25.6**

Returns: Promise\<*string*\>

<HorizontalLine />

### getMaximumBitDepth

Find if maximum bit depth is set

Since: **25.6**

Returns: Promise\<*boolean*\>

<HorizontalLine />

### getMaxRenderQuality

Find if maximum render quality is set

Since: **25.6**

Returns: Promise\<*boolean*\>

<HorizontalLine />

### getPreviewCodec

Get preview codec of sequence

Since: **25.6**

Returns: Promise\<*string*\>

<HorizontalLine />

### getPreviewFileFormat

Get preview file format of sequence

Since: **25.6**

Returns: Promise\<*string*\>

<HorizontalLine />

### getPreviewFrameRect

Get preview video frame rect in the sequence

Since: **25.6**

Returns: Promise\<[*RectF*](rectf.md)\>

<HorizontalLine />

### getVideoDisplayFormat

Get Video display format

Since: **25.6**

Returns: Promise\<[*TimeDisplay*](timedisplay.md)\>

<HorizontalLine />

### getVideoFieldType

Get video field type in the sequence

Since: **25.6**

Returns: Promise\<*number*\>

<HorizontalLine />

### getVideoFrameRate

Get video frame rate in the sequence

Since: **26.2**

Returns: [*FrameRate*](framerate.md)

<HorizontalLine />

### getVideoFrameRect

Get video frame rect in the sequence

Since: **25.6**

Returns: Promise\<[*RectF*](rectf.md)\>

<HorizontalLine />

### getVideoPixelAspectRatio

Get Video display format

Since: **25.6**

Returns: Promise\<*string*\>

<HorizontalLine />

### setAudioDisplayFormat

Set audio display format of sequence.

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| audioDisplay | [*TimeDisplay*](timedisplay.md) | - |

<HorizontalLine />

### setAudioSampleRate

Set audio sample rate

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| inRate | [*FrameRate*](framerate.md) | - |

<HorizontalLine />

### setCompositeInLinearColor

Set if composite in linear color is checked

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| useCompositeInLinearColor | *boolean* | - |

<HorizontalLine />

### setEditingMode

Set editing mode of sequence

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| inEditingModeName | *string* | - |

<HorizontalLine />

### setMaximumBitDepth

Set maximum bit depth to true/false

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| useMaxBitDepth | *boolean* | - |

<HorizontalLine />

### setMaxRenderQuality

Set maximum render quality to true/false

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| useMaxRenderQuality | *boolean* | - |

<HorizontalLine />

### setPreviewCodec

Set preview codec of sequence

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| inPreviewCodec | *string* | - |

<HorizontalLine />

### setPreviewFileFormat

Set preview file format of sequence

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| inPreviewCodec | *string* | - |

<HorizontalLine />

### setPreviewFrameRect

Set preview video frame rect in sequence

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| inPreviewVideoRect | [*RectF*](rectf.md) | - |

<HorizontalLine />

### setVideoDisplayFormat

Set video display format of sequence

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| audioDisplay | [*TimeDisplay*](timedisplay.md) | - |

<HorizontalLine />

### setVideoFieldType

Set video field type in sequence

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| videoFiledType | *number* | - |

<HorizontalLine />

### setVideoFrameRate

Set video frame rate in the sequence

Since: **26.2**

Returns: *boolean*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| inVideoFrameRate | [*FrameRate*](framerate.md) | - |

<HorizontalLine />

### setVideoFrameRect

Set video frame rect in sequence

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| inVideoFrameRect | [*RectF*](rectf.md) | - |

<HorizontalLine />

### setVideoPixelAspectRatio

Set video display format of sequence

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| inPixelAspectRatio | *string* | - |

<HorizontalLine />
