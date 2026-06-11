---
description: Overview of TickTime
id: ticktime
title: TickTime
sidebar_label: TickTime
repo: uxp-premierepro
product: premierepro
keywords: 
---

# TickTime

Since: **25.6**

## Properties

| Name | Type | Access | Min Version | Description |
| :--- | :--- | :----- | :---------- | :---------- |
| seconds | *number* | R | 25.6 | Get the TickTime in seconds |
| ticks | *string* | R | 25.6 | Get the TickTime in ticks as a string |
| ticksNumber | *number* | R | 25.6 | Get the TickTime in ticks as a number |

## Static Methods

### createWithFrameAndFrameRate

Constructs a TickTime object with a frame and a frame rate.

Since: **25.6**

Returns: [*TickTime*](ticktime.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| frameCount | *number* | - |
| frameRate | [*FrameRate*](framerate.md) | - |

<HorizontalLine />

### createWithSeconds

Constructs a TickTime object with seconds.

Since: **25.6**

Returns: [*TickTime*](ticktime.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| seconds | *number* | - |

<HorizontalLine />

### createWithTicks

Constructs a TickTime object with ticks as a string.

Since: **25.6**

Returns: [*TickTime*](ticktime.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| ticks | *string* | - |

<HorizontalLine />

## Instance Methods

### add

Add another TickTime to this one and return it. This TickTime is not modified.

Since: **25.6**

Returns: [*TickTime*](ticktime.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| tickTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### alignToFrame

alignToFrame will return a TickTime that is aligned to the nearest frame boundary less than the given time, for a given frame rate by rounding any fractional portion.

Since: **25.6**

Returns: [*TickTime*](ticktime.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| frameRate | [*FrameRate*](framerate.md) | - |

<HorizontalLine />

### alignToNearestFrame

AlignToNearestFrame will return a TickTime that is aligned to the nearest frame boundary greater than or less than the given time, for a given frame rate by rounding any fractional portion.

Since: **25.6**

Returns: [*TickTime*](ticktime.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| frameRate | [*FrameRate*](framerate.md) | - |

<HorizontalLine />

### divide

Divide this TickTime by a divisor and return it. In case of a division by zero, TIME_INVALID is returned. This TickTime is not modified.

Since: **25.6**

Returns: [*TickTime*](ticktime.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| divisor | *number* | - |

<HorizontalLine />

### equals

Returns true if the given TickTime is equal to the TickTime object

Since: **25.6**

Returns: *boolean*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| tickTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### multiply

Multiply this TickTime with a factor and return it. This TickTime is not modified.

Since: **25.6**

Returns: [*TickTime*](ticktime.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| factor | *number* | - |

<HorizontalLine />

### subtract

Subtract another TickTime from this one and return it. This TickTime is not modified.

Since: **25.6**

Returns: [*TickTime*](ticktime.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| tickTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />
