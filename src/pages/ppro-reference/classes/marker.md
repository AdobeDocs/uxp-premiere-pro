---
description: Overview of Marker
id: marker
title: Marker
sidebar_label: Marker
repo: uxp-premierepro
product: premierepro
keywords: 
---

# Marker

Since: **25.6**

## Properties

| Name | Type | Access | Min Version | Description |
| :--- | :--- | :----- | :---------- | :---------- |
| guid | [*Guid*](guid.md) | R | 26.3 | The unique identifier of the marker. |

## Instance Methods

### createSetColorByIndexAction

Return an action to set the color of the marker by the color index

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| colorIndex | *number* | - |

<HorizontalLine />

### createSetCommentsAction

Return an action to set the comments of the marker.

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| comments | *string* | - |

<HorizontalLine />

### createSetDurationAction

Return an action to set the duration of the marker.

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| tickTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### createSetNameAction

Return an action to set the name of the marker.

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| name | *string* | - |

<HorizontalLine />

### createSetTypeAction

Return an action to set the type of the marker.

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| markerType | *string* | Can be set to "Comment", "Chapter", "Segmentation", or "WebLink" |

<HorizontalLine />

### getColor

Get color code of the marker.

Since: **25.6**

Returns: [*Color*](color.md)

<HorizontalLine />

### getColorIndex

Get color index of the marker.

Since: **25.6**

Returns: *number*

<HorizontalLine />

### getComments

Get comments of the marker.

Since: **25.6**

Returns: *string*

<HorizontalLine />

### getDuration

Get duration time of the marker.

Since: **25.6**

Returns: [*TickTime*](ticktime.md)

<HorizontalLine />

### getName

Get name of the marker.

Since: **25.6**

Returns: *string*

<HorizontalLine />

### getStart

Get start time of the marker.

Since: **25.6**

Returns: [*TickTime*](ticktime.md)

<HorizontalLine />

### getTarget

Get target of the marker. Used together with url for web targets.

Since: **25.6**

Returns: *string*

<HorizontalLine />

### getType

Get type of the marker. e.g. Cue / Track / Subclip / Cart

Since: **25.6**

Returns: *string*

<HorizontalLine />

### getUrl

Get url of the marker.

Since: **25.6**

Returns: *string*

<HorizontalLine />
