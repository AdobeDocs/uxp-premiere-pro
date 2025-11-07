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
  - Premiere Pro
---

# EventManager  

## Static Methods

### addGlobalEventListener

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*void*
  
add global event listener

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| eventName | *string* or [*Constants.SnapEvent*](/ppro_reference/constants) or [*Constants.ProjectEvent*](/ppro_reference/constants) or [*Constants.SequenceEvent*](/ppro_reference/constants) or [*Constants.OperationCompleteEvent*](/ppro_reference/constants) | - |
| eventHandler | *(event?: Object) => void* | - |
| inCapturePhase? | *boolean* | - |

___

### removeGlobalEventListener

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*void*
  
remove global event listener

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| eventName | *string* or [*Constants.SnapEvent*](/ppro_reference/constants) or [*Constants.ProjectEvent*](/ppro_reference/constants) or [*Constants.SequenceEvent*](/ppro_reference/constants) or [*Constants.OperationCompleteEvent*](/ppro_reference/constants) | - |
| eventHandler | *(event?: Object) => void* | - |

___
