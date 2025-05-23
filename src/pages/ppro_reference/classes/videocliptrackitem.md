---
id: "videocliptrackitem"
title: "VideoClipTrackItem"
sidebar_label: "VideoClipTrackItem"
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

# VideoClipTrackItem  

## Instance Methods

### createAddVideoTransitionAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Create add transition action for sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| videoTransition | [*VideoTransition*](/ppro_reference/classes/videotransition/) | - |
| addTransitionOptionsProperties | [*AddTransitionOptions*](/ppro_reference/classes/addtransitionoptions/) | - |

___

### createMoveAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Returns an action moves the inPoint of the track item to a new time, by shifting it by a number of seconds.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| tickTime | [*TickTime*](/ppro_reference/classes/ticktime/) | - |

___

### createRemoveVideoTransitionAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Returns true if trackItem has transition

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| transitionPosition | *number* | - |

___

### createSetDisabledAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Returns an action that enables/disables the trackItem

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| disabled | *boolean* | - |

___

### createSetEndAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Create set end time action for sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| tickTime | [*TickTime*](/ppro_reference/classes/ticktime/) | - |

___

### createSetInPointAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Create SetInPointAction for sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| tickTime | [*TickTime*](/ppro_reference/classes/ticktime/) | - |

___

### createSetOutPointAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Create SetInPointAction for sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| tickTime | [*TickTime*](/ppro_reference/classes/ticktime/) | - |

___

### createSetStartAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Create set start time action for sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| tickTime | [*TickTime*](/ppro_reference/classes/ticktime/) | - |

___

### getComponentChain

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*VideoComponentChain*
  
Returns VideoComponentChain

___

### getDuration

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*TickTime*
  
Timecode representing the duration of this track item relative to the sequence start.

___

### getEndTime

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*TickTime*
  
Timecode representing the end of this track item relative to the sequence start.

___

### getInPoint

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*TickTime*
  
Get timecode representing the inPoint of sequence.

___

### getIsSelected

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Returns if trackItem is selected or not

___

### getMatchName

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*string*
  
Returns the value of internal matchname for this trackItem

___

### getMediaType

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Guid*
  
UUID representing the underlying media type of this track item

___

### getName

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*string*
  
Returns the display name for trackItem

___

### getOutPoint

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*TickTime*
  
Get timecode representing the outPoint of sequence.

___

### getProjectItem

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*ProjectItem*
  
The project item for this track item.

___

### getSpeed

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*number*
  
Returns the value of speed of the trackItem

___

### getStartTime

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*TickTime*
  
Timecode representing the start of this track item relative to the sequence start.

___

### getTrackIndex

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*number*
  
Index representing the track index of the track this track item belongs to

___

### getType

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*number*
  
Index representing the type of this track item.

___

### isAdjustmentLayer

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Returns true if the trackitem is an adjustment layer

___

### isDisabled

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Returns true if rackitem is muted/disabled

___

### isSpeedReversed

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*number*
  
Returns true if the trackitem is reversed

___
