---
description: Overview of VideoClipTrackItem
id: videocliptrackitem
title: VideoClipTrackItem
sidebar_label: VideoClipTrackItem
repo: uxp-premierepro
product: premierepro
keywords: 
---

# VideoClipTrackItem  

## Instance Methods

### createAddVideoTransitionAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Create add transition action for sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| videoTransition | [*TransitionFactory*](transitionfactory.md) | The transition to apply, obtained from `TransitionFactory`. |
| addTransitionOptionsProperties | [*AddTransitionOptions*](addtransitionoptions.md) | - |

<HorizontalLine />

### createMoveAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Returns an action that moves the inPoint of the track item to a new time, by shifting it by a number of seconds.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| tickTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### createRemoveVideoTransitionAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Returns true if trackItem has transition

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| transitionPosition | [*Constants.TransitionPosition*](../constants/index.md) | Start or end position of transition |

<HorizontalLine />

### createSetDisabledAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Returns an action that enables/disables the trackItem

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| disabled | *boolean* | - |

<HorizontalLine />

### createSetEndAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Create set end time action for sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| tickTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### createSetInPointAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Create SetInPointAction for setting the track item in point relative to the start time of the project item referenced by this track item

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| tickTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### createSetNameAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Returns an action that renames the trackItem

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| inName | *string* | - |

<HorizontalLine />

### createSetOutPointAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Create SetOutPointAction for setting the track item out point relative to the start time of the project item referenced by this track item

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| tickTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### createSetStartAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Create set start time action for sequence

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| tickTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### getComponentChain

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*VideoComponentChain*
  
Returns VideoComponentChain

<HorizontalLine />

### getDuration

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*TickTime*
  
Returns timecode representing the duration of this track item relative to the sequence start.

<HorizontalLine />

### getEndTime

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*TickTime*
  
Returns a TickTime object representing the ending sequence time of this track item relative to the sequence start time.

<HorizontalLine />

### getInPoint

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*TickTime*
  
Returns a TickTime object representing the track item in point relative to the start time of the project item referenced by this track item.

<HorizontalLine />

### getIsSelected

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Returns if trackItem is selected or not

<HorizontalLine />

### getMatchName

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*string*
  
Returns the value of internal matchname for this trackItem

<HorizontalLine />

### getMediaType

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Guid*
  
Returns UUID representing the underlying media type of this track item

<HorizontalLine />

### getName

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*string*
  
Returns the display name for trackItem

<HorizontalLine />

### getOutPoint

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*TickTime*
  
Returns a TickTime object representing the track item out point relative to the start time of the project item referenced by this track item.

<HorizontalLine />

### getProjectItem

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*ProjectItem*
  
Returns the project item for this track item.

<HorizontalLine />

### getSpeed

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*number*
  
Returns the value of speed of the trackItem

<HorizontalLine />

### getStartTime

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*TickTime*
  
Returns a TickTime object representing the starting sequence time of this track item relative to the sequence start time.

<HorizontalLine />

### getTrackIndex

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*number*
  
Index representing the track index of the track this track item belongs to

<HorizontalLine />

### getType

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*number*
  
Index representing the type of this track item.

<HorizontalLine />

### isAdjustmentLayer

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Returns true if the trackitem is an adjustment layer

<HorizontalLine />

### isDisabled

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Returns true if trackitem is muted/disabled

<HorizontalLine />

### isSpeedReversed

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*number*
  
Returns true if the trackitem is reversed

<HorizontalLine />
