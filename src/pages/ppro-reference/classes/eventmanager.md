---
description: Overview of EventManager
id: eventmanager
title: EventManager
sidebar_label: EventManager
repo: uxp-premierepro
product: premierepro
keywords: 
---

# EventManager  

## Static Methods

### addGlobalEventListener

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*void*
  
add global event listener

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| eventName | *string* or [*Constants.SnapEvent*](../constants/index.md) or [*Constants.ProjectEvent*](../constants/index.md) or [*Constants.SequenceEvent*](../constants/index.md) or [*Constants.OperationCompleteEvent*](../constants/index.md) | - |
| eventHandler | *(event?: object) => void* | - |
| inCapturePhase? | *boolean* | - |

<HorizontalLine />

### removeGlobalEventListener

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*void*
  
remove global event listener

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| eventName | *string* or [*Constants.SnapEvent*](../constants/index.md) or [*Constants.ProjectEvent*](../constants/index.md) or [*Constants.SequenceEvent*](../constants/index.md) or [*Constants.OperationCompleteEvent*](../constants/index.md) | - |
| eventHandler | *(event?: object) => void* | - |

<HorizontalLine />
