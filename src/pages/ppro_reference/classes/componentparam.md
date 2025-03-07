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
  - Premiere Pro
---

# ComponentParam  

## Properties

| Name | Type | Access | Min Version | Description |
| :------ | :------ | :------ | :------ | :------ |
| displayName | *string* | R | 25.0 | Returns the display name of the component param |


## Instance Methods

### areKeyframesSupported

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Returns bool whether keyframes are supported for this component parameter

___

### createAddKeyframeAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Creates and returns an action object which can be used to add a keyframe component

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| Keyframe | *object* | - |

___

### createKeyframe

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*object*
  
Creates and returns a keyframe initialised with the ComponentParam's type and passed in value. This throws if the passed in value is not compatible with the component param type

___

### createRemoveKeyframeAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Returns an action which removes keyframe at specific time

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| TickTime | *object* | - |
| UpdateUI | *boolean* | - |

___

### createRemoveKeyframeRangeAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Returns an action which removes keyframe at specific time range

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| TickTime | *object* | - |
| TickTime | *object* | - |
| UpdateUI | *boolean* | - |

___

### createSetInterpolationAtKeyframeAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Returns an action which sets the interpolation mode of keyframe at the given time

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| TickTime | *object* | - |
| InterpolationMode | *number* | - |
| UpdateUI | *boolean* | - |

___

### createSetTimeVaryingAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Creates and returns an action object to set the component to be time varying

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| inTimeVarying | *boolean* | - |

___

### createSetValueAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Creates and returns an action object which can be used to set the value of a non-time varying component

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| Keyframe | *object* | - |
| inSafeForPlayback | *boolean* | - |

___

### findNearestKeyframe

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Keyframe*
  
Find sthe nearest key for the given time

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| TickTime | *object* | - |
| TickTime | *object* | - |

___

### findNextKeyframe

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Keyframe*
  
find the next keyframe for the given time

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| TickTime | *object* | - |

___

### findPreviousKeyframe

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Keyframe*
  
find the previous keyframe for the given time

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| TickTime | *object* | - |

___

### getKeyframeListAsTickTimes

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Array*
  
Get a list of tickTime for the keyframes of this component param

___

### getKeyframePtr

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Keyframe*
  
Get the Keyframe at the given tickTime postion

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| time | [*TickTime*](/ppro_reference/classes/ticktime/) | - |

___

### getStartValue

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Keyframe*
  
Returned promise will be fullfilled with the start value (keyframe) of the component param

___

### getValueAtTime

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*object*
  
Gets the value of component Param at the given time

___

### isTimeVarying

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Returns true if the parameter value varies over time (for the duration of the item)

___
