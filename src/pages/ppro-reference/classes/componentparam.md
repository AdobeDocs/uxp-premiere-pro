---
description: Overview of ComponentParam
id: componentparam
title: ComponentParam
sidebar_label: ComponentParam
repo: uxp-premierepro
product: premierepro
keywords: 
---

# ComponentParam

Since: **25.6**

## Properties

| Name | Type | Access | Min Version | Description |
| :--- | :--- | :----- | :---------- | :---------- |
| displayName | *string* | R | 25.6 | Returns the display name of the component param |

## Instance Methods

### areKeyframesSupported

Returns bool whether keyframes are supported for this component parameter

Since: **25.6**

Returns: Promise\<*boolean*\>

<HorizontalLine />

### createAddKeyframeAction

Creates and returns an action object which can be used to add a keyframe component

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| inKeyFrame | [*Keyframe*](keyframe.md) | - |

<HorizontalLine />

### createKeyframe

Creates and returns a keyframe initialised with the ComponentParam's type and passed in value. This throws if the passed in value is not compatible with the component param type

Since: **25.6**

Returns: [*Keyframe*](keyframe.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| inValue | *number* or *string* or *boolean* or [*PointF*](pointf.md) or [*Color*](color.md) | Input could be number, string, boolean, PointF, or Color depend on effect param type |

<HorizontalLine />

### createRemoveKeyframeAction

Returns an action which removes keyframe at specific time

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| inTime | [*TickTime*](ticktime.md) | - |
| UpdateUI | *boolean* | - |

<HorizontalLine />

### createRemoveKeyframeRangeAction

Returns an action which removes keyframe at specific time range

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| inTime | [*TickTime*](ticktime.md) | - |
| outTime | [*TickTime*](ticktime.md) | - |
| UpdateUI | *boolean* | - |

<HorizontalLine />

### createSetInterpolationAtKeyframeAction

Returns an action which sets the interpolation mode of keyframe at the given time

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| inTime | [*TickTime*](ticktime.md) | - |
| InterpolationMode | *number* | - |
| UpdateUI | *boolean* | - |

<HorizontalLine />

### createSetTimeVaryingAction

Creates and returns an action object to set the component to be time varying

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| inTimeVarying | *boolean* | - |

<HorizontalLine />

### createSetValueAction

Creates and returns an action object which can be used to set the value of a non-time varying component

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| inKeyFrame | [*Keyframe*](keyframe.md) | - |
| inSafeForPlayback | *boolean* | - |

<HorizontalLine />

### findNearestKeyframe

Find sthe nearest key for the given time

Since: **25.6**

Returns: [*Keyframe*](keyframe.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| inTime | [*TickTime*](ticktime.md) | - |
| outTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### findNextKeyframe

find the next keyframe for the given time

Since: **25.6**

Returns: [*Keyframe*](keyframe.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| inTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### findPreviousKeyframe

find the previous keyframe for the given time

Since: **25.6**

Returns: [*Keyframe*](keyframe.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| inTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### getKeyframeListAsTickTimes

Get a list of tickTime for the keyframes of this component param

Since: **25.6**

Returns: [*TickTime[]*](ticktime.md)

<HorizontalLine />

### getKeyframePtr

Get the Keyframe at the given tickTime postion

Since: **25.6**

Returns: [*Keyframe*](keyframe.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| time | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### getStartValue

Returned promise will be fullfilled with the start value (keyframe) of the component param

Since: **25.6**

Returns: Promise\<[*Keyframe*](keyframe.md)\>

<HorizontalLine />

### getValueAtTime

Gets the value of component Param at the given time

Since: **25.6**

Returns: Promise\<*number | string | boolean | [PointF](pointf.md) | [Color*](color.md)\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| time | [*TickTime*](ticktime.md) | The time at which to get the value of the component param |

<HorizontalLine />

### isTimeVarying

Returns true if the parameter value varies over time (for the duration of the item)

Since: **25.6**

Returns: *boolean*

<HorizontalLine />
