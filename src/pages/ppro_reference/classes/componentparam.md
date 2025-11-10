---
id: "componentparam"
title: "ComponentParam"
sidebar_label: "ComponentParam"
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

# ComponentParam

## Properties

| Name        | Type     | Access | Min Version | Description                                     |
| :---------- | :------- | :----- | :---------- | :---------------------------------------------- |
| displayName | _string_ | R      | 25.0        | Returns the display name of the component param |

## Instance Methods

### areKeyframesSupported

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Returns bool whether keyframes are supported for this component parameter

---

### createAddKeyframeAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Creates and returns an action object which can be used to add a keyframe component

#### Parameters

| Name       | Type                                            | Description |
| :--------- | :---------------------------------------------- | :---------- |
| inKeyFrame | [_Keyframe_](/ppro_reference/classes/keyframe/) | -           |

---

### createKeyframe

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Keyframe_

Creates and returns a keyframe initialised with the ComponentParam's type and passed in value. This throws if the passed in value is not compatible with the component param type

#### Parameters

| Name    | Type                                                                                                                          | Description                                                                          |
| :------ | :---------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------- |
| inValue | _number_ or _string_ or _boolean_ or [_PointF_](/ppro_reference/classes/pointf/) or [_Color_](/ppro_reference/classes/color/) | Input could be number, string, boolean, PointF, or Color depend on effect param type |

---

### createRemoveKeyframeAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Returns an action which removes keyframe at specific time

#### Parameters

| Name     | Type                                            | Description |
| :------- | :---------------------------------------------- | :---------- |
| inTime   | [_TickTime_](/ppro_reference/classes/ticktime/) | -           |
| UpdateUI | _boolean_                                       | -           |

---

### createRemoveKeyframeRangeAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Returns an action which removes keyframe at specific time range

#### Parameters

| Name     | Type                                            | Description |
| :------- | :---------------------------------------------- | :---------- |
| inTime   | [_TickTime_](/ppro_reference/classes/ticktime/) | -           |
| outTime  | [_TickTime_](/ppro_reference/classes/ticktime/) | -           |
| UpdateUI | _boolean_                                       | -           |

---

### createSetInterpolationAtKeyframeAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Returns an action which sets the interpolation mode of keyframe at the given time

#### Parameters

| Name              | Type                                            | Description |
| :---------------- | :---------------------------------------------- | :---------- |
| inTime            | [_TickTime_](/ppro_reference/classes/ticktime/) | -           |
| InterpolationMode | _number_                                        | -           |
| UpdateUI          | _boolean_                                       | -           |

---

### createSetTimeVaryingAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Creates and returns an action object to set the component to be time varying

#### Parameters

| Name          | Type      | Description |
| :------------ | :-------- | :---------- |
| inTimeVarying | _boolean_ | -           |

---

### createSetValueAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Creates and returns an action object which can be used to set the value of a non-time varying component

#### Parameters

| Name              | Type                                            | Description |
| :---------------- | :---------------------------------------------- | :---------- |
| inKeyFrame        | [_Keyframe_](/ppro_reference/classes/keyframe/) | -           |
| inSafeForPlayback | _boolean_                                       | -           |

---

### findNearestKeyframe

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Keyframe_

Find sthe nearest key for the given time

#### Parameters

| Name    | Type                                            | Description |
| :------ | :---------------------------------------------- | :---------- |
| inTime  | [_TickTime_](/ppro_reference/classes/ticktime/) | -           |
| outTime | [_TickTime_](/ppro_reference/classes/ticktime/) | -           |

---

### findNextKeyframe

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Keyframe_

find the next keyframe for the given time

#### Parameters

| Name   | Type                                            | Description |
| :----- | :---------------------------------------------- | :---------- |
| inTime | [_TickTime_](/ppro_reference/classes/ticktime/) | -           |

---

### findPreviousKeyframe

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Keyframe_

find the previous keyframe for the given time

#### Parameters

| Name   | Type                                            | Description |
| :----- | :---------------------------------------------- | :---------- |
| inTime | [_TickTime_](/ppro_reference/classes/ticktime/) | -           |

---

### getKeyframeListAsTickTimes

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_TickTime[]_

Get a list of tickTime for the keyframes of this component param

---

### getKeyframePtr

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Keyframe_

Get the Keyframe at the given tickTime postion

#### Parameters

| Name | Type                                            | Description |
| :--- | :---------------------------------------------- | :---------- |
| time | [_TickTime_](/ppro_reference/classes/ticktime/) | -           |

---

### getStartValue

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Keyframe_

Returned promise will be fullfilled with the start value (keyframe) of the component param

---

### getValueAtTime

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_number | string | boolean | PointF | Color_

Gets the value of component Param at the given time

#### Parameters

| Name | Type                                            | Description                                               |
| :--- | :---------------------------------------------- | :-------------------------------------------------------- |
| time | [_TickTime_](/ppro_reference/classes/ticktime/) | The time at which to get the value of the component param |

---

### isTimeVarying

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Returns true if the parameter value varies over time (for the duration of the item)

---
