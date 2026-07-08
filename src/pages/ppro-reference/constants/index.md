---
description: To use any constant, import the constants object from the premiere pro module first.
id: constants
title: Constants
sidebar_label: Constants
repo: uxp-premierepro
product: premierepro
keywords:
---

# Constants

Constants are available on the `Constants` namespace of the `premierepro` module:

```
const app = require('premierepro');

const myFavoriteColor = app.Constants.ProjectItemColorLabel.BLUE;
```

## Enumerations

Since: **25.6**

### AAFExportAudioFormat

Since: **26.3**

| Name | Min Version | Description |
| :--- | :---------- | :---------- |
| AIFF | 26.3 | - |
| WAV | 26.3 | - |

<HorizontalLine />

### AudioChannelType

Since: **25.6**

| Name | Min Version | Description |
| :--- | :---------- | :---------- |
| MONO | 25.6 | - |
| STEREO | 25.6 | - |
| SURROUND_51 | 25.6 | - |
| MULTI | 25.6 | - |

<HorizontalLine />

### AudioDisplayFormatType

Since: **25.6**

| Name | Min Version | Description |
| :--- | :---------- | :---------- |
| SAMPLE_RATE | 25.6 | - |
| MILLISECONDS | 25.6 | - |

<HorizontalLine />

### AudioTrackEvent

Since: **25.6**

| Name | Min Version | Description |
| :--- | :---------- | :---------- |
| TRACK_CHANGED | 25.6 | - |
| INFO_CHANGED | 25.6 | - |
| LOCK_CHANGED | 25.6 | - |

<HorizontalLine />

### ContentType

Since: **25.6**

| Name | Min Version | Description |
| :--- | :---------- | :---------- |
| ANY | 25.6 | - |
| SEQUENCE | 25.6 | - |
| MEDIA | 25.6 | - |

<HorizontalLine />

### EncoderEvent

Since: **25.6**

| Name | Min Version | Description |
| :--- | :---------- | :---------- |
| RENDER_COMPLETE | 25.6 | - |
| RENDER_ERROR | 25.6 | - |
| RENDER_CANCEL | 25.6 | - |
| RENDER_QUEUE | 25.6 | - |
| RENDER_PROGRESS | 25.6 | - |

<HorizontalLine />

### ExportType

Since: **25.6**

| Name | Min Version | Description |
| :--- | :---------- | :---------- |
| QUEUE_TO_AME | 25.6 | - |
| QUEUE_TO_APP | 25.6 | - |
| IMMEDIATELY | 25.6 | - |

<HorizontalLine />

### InterpolationMode

Since: **25.6**

| Name | Min Version | Description |
| :--- | :---------- | :---------- |
| BEZIER | 25.6 | - |
| HOLD | 25.6 | - |
| LINEAR | 25.6 | - |
| TIME | 25.6 | - |
| TIME_TRANSITION_END | 25.6 | - |
| TIME_TRANSITION_START | 25.6 | - |

<HorizontalLine />

### MarkerColor

Since: **25.6**

| Name | Min Version | Description |
| :--- | :---------- | :---------- |
| GREEN | 25.6 | - |
| RED | 25.6 | - |
| MAGNETA | 25.6 | - |
| ORANGE | 25.6 | - |
| YELLOW | 25.6 | - |
| BLUE | 25.6 | - |
| CYAN | 25.6 | - |

<HorizontalLine />

### MediaType

Since: **25.6**

| Name | Min Version | Description |
| :--- | :---------- | :---------- |
| ANY | 25.6 | - |
| DATA | 25.6 | - |
| VIDEO | 25.6 | - |
| AUDIO | 25.6 | - |

<HorizontalLine />

### MetadataType

Since: **25.6**

| Name | Min Version | Description |
| :--- | :---------- | :---------- |
| INTEGER | 25.6 | - |
| REAL | 25.6 | - |
| TEXT | 25.6 | - |
| BOOLEAN | 25.6 | - |

<HorizontalLine />

### OperationCompleteEvent

Since: **25.6**

| Name | Min Version | Description |
| :--- | :---------- | :---------- |
| CLIP_EXTEND_REACHED | 25.6 | - |
| EFFECT_DROP_COMPLETE | 25.6 | - |
| EFFECT_DRAG_OVER | 25.6 | - |
| EXPORT_MEDIA_COMPLETE | 25.6 | - |
| GENERATIVE_EXTEND_COMPLETE | 25.6 | - |
| IMPORT_MEDIA_COMPLETE | 25.6 | - |

<HorizontalLine />

### OperationCompleteState

Since: **25.6**

| Name | Min Version | Description |
| :--- | :---------- | :---------- |
| SUCCESS | 25.6 | - |
| CANCELLED | 25.6 | - |
| FAILED | 25.6 | - |

<HorizontalLine />

### PixelAspectRatio

Since: **25.6**

| Name | Min Version | Description |
| :--- | :---------- | :---------- |
| SQUARE | 25.6 | - |
| DVNTSC | 25.6 | - |
| DVNTSCWide | 25.6 | - |
| DVPAL | 25.6 | - |
| DVPALWide | 25.6 | - |
| Anamorphic | 25.6 | - |
| HDAnamorphic1080 | 25.6 | - |
| DVCProHD | 25.6 | - |

<HorizontalLine />

### PreferenceKey

Since: **25.6**

| Name | Min Version | Description |
| :--- | :---------- | :---------- |
| AUTO_PEAK_GENERATION | 25.6 | - |
| IMPORT_WORKSPACE | 25.6 | - |
| SHOW_QUICKSTART_DIALOG | 25.6 | - |

<HorizontalLine />

### ProjectEvent

Since: **25.6**

| Name | Min Version | Description |
| :--- | :---------- | :---------- |
| OPENED | 25.6 | - |
| CLOSED | 25.6 | - |
| DIRTY | 25.6 | - |
| ACTIVATED | 25.6 | - |
| PROJECT_ITEM_SELECTION_CHANGED | 25.6 | - |

<HorizontalLine />

### ProjectItemColorLabel

Since: **25.6**

| Name | Min Version | Description |
| :--- | :---------- | :---------- |
| VIOLET | 25.6 | - |
| IRIS | 25.6 | - |
| LAVENDER | 25.6 | - |
| CERULEAN | 25.6 | - |
| FOREST | 25.6 | - |
| ROSE | 25.6 | - |
| MANGO | 25.6 | - |
| PURPLE | 25.6 | - |
| BLUE | 25.6 | - |
| TEAL | 25.6 | - |
| MAGENTA | 25.6 | - |
| TAN | 25.6 | - |
| GREEN | 25.6 | - |
| BROWN | 25.6 | - |
| YELLOW | 25.6 | - |

<HorizontalLine />

### PropertyType

Since: **25.6**

| Name | Min Version | Description |
| :--- | :---------- | :---------- |
| PERSISTENT | 25.6 | - |
| NON_PERSISTENT | 25.6 | - |

<HorizontalLine />

### ScratchDiskFolder

Since: **25.6**

| Name | Min Version | Description |
| :--- | :---------- | :---------- |
| SAME_AS_PROJECT | 25.6 | - |
| MY_DOCUMENTS | 25.6 | - |

<HorizontalLine />

### ScratchDiskFolderType

Since: **25.6**

| Name | Min Version | Description |
| :--- | :---------- | :---------- |
| CAPTURE | 25.6 | - |
| AUDIO_PREVIEW | 25.6 | - |
| VIDEO_PREVIEW | 25.6 | - |
| AUTO_SAVE | 25.6 | - |
| CCL_LIBRARIES | 25.6 | - |
| CAPSULE_MEDIA | 25.6 | - |

<HorizontalLine />

### SequenceEvent

Since: **25.6**

| Name | Min Version | Description |
| :--- | :---------- | :---------- |
| ACTIVATED | 25.6 | - |
| CLOSED | 25.6 | - |
| SELECTION_CHANGED | 25.6 | - |

<HorizontalLine />

### SequenceOperation

Since: **25.6**

| Name | Min Version | Description |
| :--- | :---------- | :---------- |
| APPLYCUT | 25.6 | - |
| CREATEMARKER | 25.6 | - |
| CREATESUBCLIP | 25.6 | - |

<HorizontalLine />

### SnapEvent

Since: **25.6**

| Name | Min Version | Description |
| :--- | :---------- | :---------- |
| KEYFRAME | 25.6 | - |
| RAZOR_PLAYHEAD | 25.6 | - |
| RAZOR_MARKER | 25.6 | - |
| TRACKITEM | 25.6 | - |
| GUIDES | 25.6 | - |
| PLAYHEAD_TRACKITEM | 25.6 | - |

<HorizontalLine />

### TrackItemType

Since: **25.6**

| Name | Min Version | Description |
| :--- | :---------- | :---------- |
| EMPTY | 25.6 | - |
| CLIP | 25.6 | - |
| TRANSITION | 25.6 | - |
| PREVIEW | 25.6 | - |
| FEEDBACK | 25.6 | - |

<HorizontalLine />

### TransitionPosition

Since: **25.6**

| Name | Min Version | Description |
| :--- | :---------- | :---------- |
| START | 25.6 | - |
| END | 25.6 | - |

<HorizontalLine />

### VideoDisplayFormatType

Since: **25.6**

| Name | Min Version | Description |
| :--- | :---------- | :---------- |
| FPS_23_976 | 25.6 | - |
| FPS_25 | 25.6 | - |
| FPS_29_97 | 25.6 | - |
| FPS_29_97_NON_DROP | 25.6 | - |
| FEET_FRAME_16mm | 25.6 | - |
| FEET_FRAME_35mm | 25.6 | - |
| FRAMES | 25.6 | - |

<HorizontalLine />

### VideoFieldType

Since: **25.6**

| Name | Min Version | Description |
| :--- | :---------- | :---------- |
| PROGRESSIVE | 25.6 | - |
| UPPER_FIRST | 25.6 | - |
| LOWER_FIRST | 25.6 | - |

<HorizontalLine />

### VideoTrackEvent

Since: **25.6**

| Name | Min Version | Description |
| :--- | :---------- | :---------- |
| TRACK_CHANGED | 25.6 | - |
| INFO_CHANGED | 25.6 | - |
| LOCK_CHANGED | 25.6 | - |

<HorizontalLine />
