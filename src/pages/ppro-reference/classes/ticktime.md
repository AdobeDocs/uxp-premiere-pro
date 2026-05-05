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

## Properties

| Name | Type | Access | Min Version | Description |
| :------ | :------ | :------ | :------ | :------ |
| seconds | *number* | R | 25.0 | Get the TickTime in seconds |
| ticks | *string* | R | 25.0 | Get the TickTime in ticks as a string |
| ticksNumber | *number* | R | 25.0 | Get the TickTime in ticks as a number |

## Static Methods

### createWithFrameAndFrameRate

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*TickTime*
  
Constructs a TickTime object with a frame and a frame rate.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| frameCount | *number* | - |
| frameRate | [*FrameRate*](framerate.md) | - |

<HorizontalLine />

### createWithSeconds

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*TickTime*
  
Constructs a TickTime object with seconds.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| seconds | *number* | - |

<HorizontalLine />

### createWithTicks

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*TickTime*
  
Constructs a TickTime object with ticks as a string.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| ticks | *string* | - |

<HorizontalLine />

## Instance Methods

### add

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*TickTime*
  
Add another TickTime to this one and return it. This TickTime is not modified.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| tickTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### alignToFrame

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*TickTime*
  
alignToFrame will return a TickTime that is aligned to the nearest frame boundary less than the given time, for a given frame rate by rounding any fractional portion.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| frameRate | [*FrameRate*](framerate.md) | - |

<HorizontalLine />

### alignToNearestFrame

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*TickTime*
  
AlignToNearestFrame will return a TickTime that is aligned to the nearest frame boundary greater than or less than the given time, for a given frame rate by rounding any fractional portion.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| frameRate | [*FrameRate*](framerate.md) | - |

<HorizontalLine />

### divide

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*TickTime*
  
Divide this TickTime by a divisor and return it. In case of a division by zero, TIME_INVALID is returned. This TickTime is not modified.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| divisor | *number* | - |

<HorizontalLine />

### equals

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Returns true if the given TickTime is equal to the TickTime object

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| tickTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### multiply

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*TickTime*
  
Multiply this TickTime with a factor and return it. This TickTime is not modified.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| factor | *number* | - |

<HorizontalLine />

### subtract

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*TickTime*
  
Subtract another TickTime from this one and return it. This TickTime is not modified.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| tickTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />
