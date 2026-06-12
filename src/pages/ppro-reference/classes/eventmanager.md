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

### addEventListener

add event listener to target object

Since: **25.6**

Returns: *void*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| target | [*Project*](project.md) or [*Sequence*](sequence.md) or [*VideoTrack*](videotrack.md) or [*AudioTrack*](audiotrack.md) or [*EncoderManager*](encodermanager.md) | - |
| eventName | *string* or [*Constants.SnapEvent*](../constants/index.md#snapevent) or [*Constants.ProjectEvent*](../constants/index.md#projectevent) or [*Constants.SequenceEvent*](../constants/index.md#sequenceevent) or [*Constants.OperationCompleteEvent*](../constants/index.md#operationcompleteevent) | - |
| eventHandler | *(event?: object) =\> void* | - |
| inCapturePhase | *boolean* | - |

<HorizontalLine />

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

### removeEventListener

remove event listener from target object

Since: **25.6**

Returns: *void*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| target | [*Project*](project.md) or [*Sequence*](sequence.md) or [*VideoTrack*](videotrack.md) or [*AudioTrack*](audiotrack.md) or [*EncoderManager*](encodermanager.md) | - |
| eventName | *string* or [*Constants.SnapEvent*](../constants/index.md#snapevent) or [*Constants.ProjectEvent*](../constants/index.md#projectevent) or [*Constants.SequenceEvent*](../constants/index.md#sequenceevent) or [*Constants.OperationCompleteEvent*](../constants/index.md#operationcompleteevent) | - |
| eventHandler | *(event?: object) =\> void* | - |

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
