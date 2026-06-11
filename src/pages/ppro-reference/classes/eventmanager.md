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

Since: **25.6**

## Static Methods

### addGlobalEventListener

add global event listener

Since: **25.6**

Returns: *void*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| eventName | *string* or [*Constants.SnapEvent*](../constants/index.md#snapevent) or [*Constants.ProjectEvent*](../constants/index.md#projectevent) or [*Constants.SequenceEvent*](../constants/index.md#sequenceevent) or [*Constants.OperationCompleteEvent*](../constants/index.md#operationcompleteevent) | - |
| eventHandler | *(event?: object) =\> void* | - |
| inCapturePhase | *boolean* | - |

<HorizontalLine />

### removeGlobalEventListener

remove global event listener

Since: **25.6**

Returns: *void*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| eventName | *string* or [*Constants.SnapEvent*](../constants/index.md#snapevent) or [*Constants.ProjectEvent*](../constants/index.md#projectevent) or [*Constants.SequenceEvent*](../constants/index.md#sequenceevent) or [*Constants.OperationCompleteEvent*](../constants/index.md#operationcompleteevent) | - |
| eventHandler | *(event?: object) =\> void* | - |

<HorizontalLine />
