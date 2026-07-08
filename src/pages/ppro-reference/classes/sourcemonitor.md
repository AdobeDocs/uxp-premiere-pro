---
description: Overview of SourceMonitor
id: sourcemonitor
title: SourceMonitor
sidebar_label: SourceMonitor
repo: uxp-premierepro
product: premierepro
keywords: 
---

# SourceMonitor

Since: **25.6**

## Static Methods

### closeAllClips

Close all clips on Source Monitor

Since: **25.6**

Returns: Promise\<*boolean*\>

<HorizontalLine />

### closeClip

Close clip on Source Monitor

Since: **25.6**

Returns: Promise\<*boolean*\>

<HorizontalLine />

### getPosition

Get position of source monitor in time

Since: **25.6**

Returns: Promise\<[*TickTime*](ticktime.md)\>

<HorizontalLine />

### getProjectItem

Get projectItem at source monitor

Since: **25.6**

Returns: Promise\<[*ProjectItem*](projectitem.md)\>

<HorizontalLine />

### openFilePath

Open the item at the specified path and send to the Source Monitor for preview

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| filePath | *string* | - |

<HorizontalLine />

### openProjectItem

Open input projectItem on Source Monitor

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| projectItem | [*ProjectItem*](projectitem.md) | - |

<HorizontalLine />

### play

Play clip at source monitor with input speed

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| speed | *number* | - |

<HorizontalLine />

### setPosition

Set position of source monitor to the given TickTime

Since: **26.3**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| position | [*TickTime*](ticktime.md) | - |

<HorizontalLine />
