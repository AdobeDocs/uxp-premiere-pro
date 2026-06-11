---
description: Overview of VideoFilterFactory
id: videofilterfactory
title: VideoFilterFactory
sidebar_label: VideoFilterFactory
repo: uxp-premierepro
product: premierepro
keywords: 
---

# VideoFilterFactory

Since: **25.6**

## Static Methods

### createComponent

Creates a new video filter component based on the input matchName

Since: **25.6**

Returns: Promise\<[*VideoFilterComponent*](videofiltercomponent.md)\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| matchName | *string* | The match name of the component to create, example 'PR.ADBE Solarize', 'AE.ADBE Mosaic' etc.. |

<HorizontalLine />

### getDisplayNames

Returns an array of video filter display names

Since: **25.6**

Returns: Promise\<*string[]*\>

<HorizontalLine />

### getMatchNames

Returns an array of video filter matchNames

Since: **25.6**

Returns: Promise\<*string[]*\>

<HorizontalLine />
