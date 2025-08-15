---
id: "constants"
title: "Constants"
sidebar_label: "Constants"
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
---

# Constants

To use any constant, import the `constants` object from the premiere pro module first.

## Enumerations

### MediaType

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

| Name | Description |
| :------ | :------ |
| ANY | - |
| DATA | - |
| VIDEO | - |
| AUDIO | - |

___

### ContentType

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

| Name | Description |
| :------ | :------ |
| ANY | - |
| SEQUENCE | - |
| MEDIA | - |

___

### TransitionPosition

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

| Name | Description |
| :------ | :------ |
| START | - |
| END | - |

___

### TrackItemType

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

| Name | Description |
| :------ | :------ |
| EMPTY | - |
| CLIP | - |
| TRANSITION | - |
| PREVIEW | - |
| FEEDBACK | - |

___

### ProjectEvent

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

| Name | Description |
| :------ | :------ |
| OPENED | - |
| CLOSED | - |
| DIRTY | - |
| ACTIVATED | - |
| PROJECT_ITEM_SELECTION_CHANGED | - |

___

### InterpolationMode

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

| Name | Description |
| :------ | :------ |
| BEZIER | - |
| HOLD | - |
| LINEAR | - |
| TIME | - |
| TIME_TRANSITION_END | - |
| TIME_TRANSITION_START | - |

___

### SequenceOperation

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

| Name | Description |
| :------ | :------ |
| APPLYCUT | - |
| CREATEMARKER | - |
| CREATESUBCLIP | - |

___

### PropertyType

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

| Name | Description |
| :------ | :------ |
| PERSISTENT | - |
| NON_PERSISTENT | - |

___

### SequenceEvent

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

| Name | Description |
| :------ | :------ |
| ACTIVATED | - |
| CLOSED | - |
| SELECTION_CHANGED | - |

___

### VideoTrackEvent

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

| Name | Description |
| :------ | :------ |
| TRACK_CHANGED | - |
| INFO_CHANGED | - |
| LOCK_CHANGED | - |

___

### AudioTrackEvent

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

| Name | Description |
| :------ | :------ |
| TRACK_CHANGED | - |
| INFO_CHANGED | - |
| LOCK_CHANGED | - |

___

### EncoderEvent

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

| Name | Description |
| :------ | :------ |
| RENDER_COMPLETE | - |
| RENDER_ERROR | - |
| RENDER_CANCEL | - |
| RENDER_QUEUE | - |
| RENDER_PROGRESS | - |

___

### ScratchDiskFolderType

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

| Name | Description |
| :------ | :------ |
| CAPTURE | - |
| AUDIO_CAPTURE | - |
| VIDEO_CAPTURE | - |
| AUDIO_PREVIEW | - |
| VIDEO_PREVIEW | - |
| AUTO_SAVE | - |
| CCL_LIBRARIES | - |
| CAPSULE_MEDIA | - |

___

### ScratchDiskFolder

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

| Name | Description |
| :------ | :------ |
| SAME_AS_PROJECT | - |
| MY_DOCUMENTS | - |

___

### MetadataType

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

| Name | Description |
| :------ | :------ |
| INTEGER | - |
| REAL | - |
| TEXT | - |
| BOOLEAN | - |

___

### ExportType

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

| Name | Description |
| :------ | :------ |
| QUEUE_TO_AME | - |
| QUEUE_TO_APP | - |
| IMMEDIATELY | - |

___

### PreferenceKey

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

| Name | Description |
| :------ | :------ |
| AUTO_PEAK_GENERATION | - |
| IMPORT_WORKSPACE | - |
| SHOW_QUICKSTART_DIALOG | - |

___

### SnapEvent

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

| Name | Description |
| :------ | :------ |
| KEYFRAME | - |
| RAZOR_PLAYHEAD | - |
| RAZOR_MARKER | - |
| TRACKITEM | - |
| GUIDES | - |

___

### OperationCompleteEvent

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

| Name | Description |
| :------ | :------ |
| CLIP_EXTEND_REACHED | - |
| EFFECT_DROP_COMPLETE | - |
| EXPORT_MEDIA_COMPLETE | - |
| GENERATIVE_EXTEND_COMPLETE | - |
| IMPORT_MEDIA_COMPLETE | - |

___

### OperationCompleteState

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

| Name | Description |
| :------ | :------ |
| SUCCESS | - |
| CANCELLED | - |
| FAILED | - |

___

### PixelAspectRatio

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

| Name | Description |
| :------ | :------ |
| SQUARE | - |
| DVNTSC | - |
| DVNTSCWide | - |
| DVPAL | - |
| DVPALWide | - |
| Anamorphic | - |
| HDAnamorphic1080 | - |
| DVCProHD | - |

___

### VideoFieldType

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

| Name | Description |
| :------ | :------ |
| PROGRESSIVE | - |
| UPPER_FIRST | - |
| LOWER_FIRST | - |

___

### VideoDisplayFormatType

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

| Name | Description |
| :------ | :------ |
| FPS_23_976 | - |
| FPS_25 | - |
| FPS_29_97 | - |
| FPS_29_97_NON_DROP | - |
| FEET_FRAME_16mm | - |
| FEET_FRAME_35mm | - |
| FRAMES | - |

___

### AudioChannelType

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

| Name | Description |
| :------ | :------ |
| MONO | - |
| STEREO | - |
| SURROUND_51 | - |
| MULTI | - |

___

### AudioDisplayFormatType

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

| Name | Description |
| :------ | :------ |
| SAMPLE_RATE | - |
| MILLISECONDS | - |

___
