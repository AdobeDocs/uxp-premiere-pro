---
description: Overview of AudioComponentChain
id: audiocomponentchain
title: AudioComponentChain
sidebar_label: AudioComponentChain
repo: uxp-premierepro
product: premierepro
keywords: 
---

# AudioComponentChain

Since: **25.6**

## Instance Methods

### createAppendComponentAction

Creates and returns an append component action

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| component | [*Component*](component.md) or [*AudioFilterComponent*](audiofiltercomponent.md) | Audio filter component |

<HorizontalLine />

### createInsertComponentAction

Creates and returns an insert component action

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| component | [*Component*](component.md) or [*AudioFilterComponent*](audiofiltercomponent.md) | Audio filter component |
| componentInsertionIndex | *number* | Index which the component shall be inserted |

<HorizontalLine />

### createRemoveComponentAction

Creates and returns an remove component action

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| component | [*Component*](component.md) or [*AudioFilterComponent*](audiofiltercomponent.md) | Audio filter component |

<HorizontalLine />

### getComponentAtIndex

Returns the component at the given index

Since: **25.6**

Returns: [*Component*](component.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| componentIndex | *number* | - |

<HorizontalLine />

### getComponentCount

Gets the number of components in the component chain

Since: **25.6**

Returns: *number*

<HorizontalLine />
