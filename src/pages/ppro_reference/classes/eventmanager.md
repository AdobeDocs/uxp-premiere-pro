---
id: "eventmanager"
title: "EventManager"
sidebar_label: "EventManager"
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

# EventManager

## Static Methods

### addGlobalEventListener

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_void_

add global event listener

#### Parameters

| Name            | Type                                                                                                                                                                                                                                                 | Description |
| :-------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------- |
| eventName       | _string_ or [_Constants.SnapEvent_](/ppro_reference/constants) or [_Constants.ProjectEvent_](/ppro_reference/constants) or [_Constants.SequenceEvent_](/ppro_reference/constants) or [_Constants.OperationCompleteEvent_](/ppro_reference/constants) | -           |
| eventHandler    | _(event?: Object) => void_                                                                                                                                                                                                                           | -           |
| inCapturePhase? | _boolean_                                                                                                                                                                                                                                            | -           |

---

### removeGlobalEventListener

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_void_

remove global event listener

#### Parameters

| Name         | Type                                                                                                                                                                                                                                                 | Description |
| :----------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------- |
| eventName    | _string_ or [_Constants.SnapEvent_](/ppro_reference/constants) or [_Constants.ProjectEvent_](/ppro_reference/constants) or [_Constants.SequenceEvent_](/ppro_reference/constants) or [_Constants.OperationCompleteEvent_](/ppro_reference/constants) | -           |
| eventHandler | _(event?: Object) => void_                                                                                                                                                                                                                           | -           |

---
