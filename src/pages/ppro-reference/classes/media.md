---
description: Overview of Media
id: media
title: Media
sidebar_label: Media
repo: uxp-premierepro
product: premierepro
keywords: 
---

# Media

Since: **25.6**

## Properties

| Name | Type | Access | Min Version | Description |
| :--- | :--- | :----- | :---------- | :---------- |
| duration | Promise\<[*TickTime*](ticktime.md)\> | R | 26.5 | Get the media duration - Deprecated: Use getDuration() instead. |
| start | Promise\<[*TickTime*](ticktime.md)\> | R | 26.5 | Get the media start time - Deprecated: Use getStart() instead. |

## Instance Methods

### createSetStartAction

Returns action that set start of media

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| time | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### getDuration

Get the media duration.

Since: **26.5**

Returns: [*TickTime*](ticktime.md)

<HorizontalLine />

### getStart

Get the media start time.

Since: **26.5**

Returns: [*TickTime*](ticktime.md)

<HorizontalLine />
