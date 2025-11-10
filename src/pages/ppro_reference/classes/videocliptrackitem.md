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
  - Premiere
---

# VideoClipTrackItem

## Instance Methods

### createAddVideoTransitionAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Create add transition action for sequence

#### Parameters

| Name                           | Type                                                                    | Description |
| :----------------------------- | :---------------------------------------------------------------------- | :---------- |
| videoTransition                | [_VideoTransition_](/ppro_reference/classes/videotransition/)           | -           |
| addTransitionOptionsProperties | [_AddTransitionOptions_](/ppro_reference/classes/addtransitionoptions/) | -           |

---

### createMoveAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Returns an action that moves the inPoint of the track item to a new time, by shifting it by a number of seconds.

#### Parameters

| Name     | Type                                            | Description |
| :------- | :---------------------------------------------- | :---------- |
| tickTime | [_TickTime_](/ppro_reference/classes/ticktime/) | -           |

---

### createRemoveVideoTransitionAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Returns true if trackItem has transition

#### Parameters

| Name               | Type                                                        | Description                         |
| :----------------- | :---------------------------------------------------------- | :---------------------------------- |
| transitionPosition | [_Constants.TransitionPosition_](/ppro_reference/constants) | Start or end position of transition |

---

### createSetDisabledAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Returns an action that enables/disables the trackItem

#### Parameters

| Name     | Type      | Description |
| :------- | :-------- | :---------- |
| disabled | _boolean_ | -           |

---

### createSetEndAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Create set end time action for sequence

#### Parameters

| Name     | Type                                            | Description |
| :------- | :---------------------------------------------- | :---------- |
| tickTime | [_TickTime_](/ppro_reference/classes/ticktime/) | -           |

---

### createSetInPointAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Create SetInPointAction for setting the track item in point relative to the start time of the project item referenced by this track item

#### Parameters

| Name     | Type                                            | Description |
| :------- | :---------------------------------------------- | :---------- |
| tickTime | [_TickTime_](/ppro_reference/classes/ticktime/) | -           |

---

### createSetNameAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Returns an action that renames the trackItem

#### Parameters

| Name   | Type     | Description |
| :----- | :------- | :---------- |
| inName | _string_ | -           |

---

### createSetOutPointAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Create SetOutPointAction for setting the track item out point relative to the start time of the project item referenced by this track item

#### Parameters

| Name     | Type                                            | Description |
| :------- | :---------------------------------------------- | :---------- |
| tickTime | [_TickTime_](/ppro_reference/classes/ticktime/) | -           |

---

### createSetStartAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Create set start time action for sequence

#### Parameters

| Name     | Type                                            | Description |
| :------- | :---------------------------------------------- | :---------- |
| tickTime | [_TickTime_](/ppro_reference/classes/ticktime/) | -           |

---

### getComponentChain

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_VideoComponentChain_

Returns VideoComponentChain

---

### getDuration

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_TickTime_

Returns timecode representing the duration of this track item relative to the sequence start.

---

### getEndTime

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_TickTime_

Returns a TickTime object representing the ending sequence time of this track item relative to the sequence start time.

---

### getInPoint

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_TickTime_

Returns a TickTime object representing the track item in point relative to the start time of the project item referenced by this track item.

---

### getIsSelected

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Returns if trackItem is selected or not

---

### getMatchName

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_string_

Returns the value of internal matchname for this trackItem

---

### getMediaType

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Guid_

Returns UUID representing the underlying media type of this track item

---

### getName

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_string_

Returns the display name for trackItem

---

### getOutPoint

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_TickTime_

Returns a TickTime object representing the track item out point relative to the start time of the project item referenced by this track item.

---

### getProjectItem

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_ProjectItem_

Returns the project item for this track item.

---

### getSpeed

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_number_

Returns the value of speed of the trackItem

---

### getStartTime

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_TickTime_

Returns a TickTime object representing the starting sequence time of this track item relative to the sequence start time.

---

### getTrackIndex

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_number_

Index representing the track index of the track this track item belongs to

---

### getType

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_number_

Index representing the type of this track item.

---

### isAdjustmentLayer

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Returns true if the trackitem is an adjustment layer

---

### isDisabled

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Returns true if trackitem is muted/disabled

---

### isSpeedReversed

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_number_

Returns true if the trackitem is reversed

---
