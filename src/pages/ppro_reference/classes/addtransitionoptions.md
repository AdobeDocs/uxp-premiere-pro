---
id: "addtransitionoptions"
title: "AddTransitionOptions"
sidebar_label: "AddTransitionOptions"
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

# AddTransitionOptions

## Properties

| Name                | Type       | Access | Min Version | Description                                                      |
| :------------------ | :--------- | :----- | :---------- | :--------------------------------------------------------------- |
| applyToStart        | _boolean_  | R      | 25.0        | Get whether to apply transition to the start or end of trackitem |
| forceSingleSided    | _boolean_  | R      | 25.0        | Get whether transition should be applied to one/both sides       |
| transitionAlignment | _number_   | R      | 25.0        | Gets the transitionAlignment of transition                       |
| duration            | _TickTime_ | R      | 25.0        | Gets the duration of transition                                  |

## Instance Methods

### setApplyToStart

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_AddTransitionOptions_

Set whether to apply transition to the start or end of trackitem

#### Parameters

| Name         | Type      | Description |
| :----------- | :-------- | :---------- |
| applyToStart | _boolean_ | -           |

---

### setDuration

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_AddTransitionOptions_

Sets the duration of transition

#### Parameters

| Name     | Type                                            | Description                                 |
| :------- | :---------------------------------------------- | :------------------------------------------ |
| tickTime | [_TickTime_](/ppro_reference/classes/ticktime/) | Sets the duration of transition in TickTime |

---

### setForceSingleSided

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_AddTransitionOptions_

Set whether transition should be applied to one/both sides

#### Parameters

| Name             | Type      | Description |
| :--------------- | :-------- | :---------- |
| forceSingleSided | _boolean_ | -           |

---

### setTransitionAlignment

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_AddTransitionOptions_

Sets the transitionAlignment of the transition

#### Parameters

| Name                | Type     | Description |
| :------------------ | :------- | :---------- |
| transitionAlignment | _number_ | -           |

---
