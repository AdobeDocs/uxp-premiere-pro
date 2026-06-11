---
description: Overview of Markers
id: markers
title: Markers
sidebar_label: Markers
repo: uxp-premierepro
product: premierepro
keywords: 
---

# Markers

Since: **25.6**

## Static Methods

### getMarkers

Returns the Markers object for Sequence Or ProjectItem

Since: **25.6**

Returns: Promise\<[*Markers*](markers.md)\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| markerOwnerObject | [*Sequence*](sequence.md) or [*ClipProjectItem*](clipprojectitem.md) | - |

<HorizontalLine />

## Instance Methods

### createAddMarkerAction

Add a new marker

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| Name | *string* | - |
| markerType | *string* | - |
| startTime | [*TickTime*](ticktime.md) | - |
| duration | [*TickTime*](ticktime.md) | - |
| comments | *string* | - |

<HorizontalLine />

### createMoveMarkerAction

Move the given marker at new time value

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| marker | [*Marker*](marker.md) | - |
| tickTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### createRemoveMarkerAction

Remove the given marker

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| marker | [*Marker*](marker.md) | - |

<HorizontalLine />

### getMarkers

Get all markers

Since: **25.6**

Returns: [*Marker[]*](marker.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| filters | *string[]* | Marker Type Filter (Optional) |

<HorizontalLine />
