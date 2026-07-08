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

Since: **25.6**

## Instance Methods

### createAddVideoTransitionAction

Create add transition action for sequence

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| videoTransition | [*VideoTransition*](videotransition.md) | - |
| addTransitionOptionsProperties | [*AddTransitionOptions*](addtransitionoptions.md) | - |

<HorizontalLine />

### createMoveAction

Returns an action that moves the inPoint of the track item to a new time, by shifting it by a number of seconds.

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| tickTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### createRemoveVideoTransitionAction

Returns true if trackItem has transition

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| transitionPosition | [*Constants.TransitionPosition*](../constants/index.md#transitionposition) | Start or end position of transition |

<HorizontalLine />

### createSetDisabledAction

Returns an action that enables/disables the trackItem 

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| disabled | *boolean* | - |

<HorizontalLine />

### createSetEndAction

Create set end time action for sequence

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| tickTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### createSetInPointAction

Create SetInPointAction for setting the track item in point relative to the start time of the project item referenced by this track item

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| tickTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### createSetNameAction

Returns an action that renames the trackItem

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| inName | *string* | - |

<HorizontalLine />

### createSetOutPointAction

Create SetOutPointAction for setting the track item out point relative to the start time of the project item referenced by this track item

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| tickTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### createSetStartAction

Create set start time action for sequence

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| tickTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### getComponentChain

Returns VideoComponentChain

Since: **25.6**

Returns: Promise\<[*VideoComponentChain*](videocomponentchain.md)\>

<HorizontalLine />

### getDuration

Returns timecode representing the duration of this track item relative to the sequence start.

Since: **25.6**

Returns: Promise\<[*TickTime*](ticktime.md)\>

<HorizontalLine />

### getEndTime

Returns a TickTime object representing the ending sequence time of this track item relative to the sequence start time.

Since: **25.6**

Returns: Promise\<[*TickTime*](ticktime.md)\>

<HorizontalLine />

### getInPoint

Returns a TickTime object representing the track item in point relative to the start time of the project item referenced by this track item.

Since: **25.6**

Returns: Promise\<[*TickTime*](ticktime.md)\>

<HorizontalLine />

### getIsSelected

Returns if trackItem is selected or not

Since: **25.6**

Returns: Promise\<*boolean*\>

<HorizontalLine />

### getMatchName

Returns the value of internal matchname for this trackItem

Since: **25.6**

Returns: Promise\<*string*\>

<HorizontalLine />

### getMediaType

Returns UUID representing the underlying media type of this track item

Since: **25.6**

Returns: Promise\<[*Guid*](guid.md)\>

<HorizontalLine />

### getName

Returns the display name for trackItem

Since: **25.6**

Returns: Promise\<*string*\>

<HorizontalLine />

### getOutPoint

Returns a TickTime object representing the track item out point relative to the start time of the project item referenced by this track item.

Since: **25.6**

Returns: Promise\<[*TickTime*](ticktime.md)\>

<HorizontalLine />

### getProjectItem

Returns the project item for this track item.

Since: **25.6**

Returns: Promise\<[*ProjectItem*](projectitem.md)\>

<HorizontalLine />

### getSpeed

Returns the value of speed of the trackItem

Since: **25.6**

Returns: Promise\<*number*\>

<HorizontalLine />

### getStartTime

Returns a TickTime object representing the starting sequence time of this track item relative to the sequence start time.

Since: **25.6**

Returns: Promise\<[*TickTime*](ticktime.md)\>

<HorizontalLine />

### getTrackIndex

Index representing the track index of the track this track item belongs to

Since: **25.6**

Returns: Promise\<*number*\>

<HorizontalLine />

### getType

Index representing the type of this track item.

Since: **25.6**

Returns: Promise\<*number*\>

<HorizontalLine />

### isAdjustmentLayer

Returns true if the trackitem is an adjustment layer

Since: **25.6**

Returns: Promise\<*boolean*\>

<HorizontalLine />

### isDisabled

Returns true if trackitem is muted/disabled

Since: **25.6**

Returns: Promise\<*boolean*\>

<HorizontalLine />

### isSpeedReversed

Returns true if the trackitem is reversed

Since: **25.6**

Returns: Promise\<*number*\>

<HorizontalLine />
