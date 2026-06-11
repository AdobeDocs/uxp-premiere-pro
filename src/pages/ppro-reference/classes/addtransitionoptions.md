---
description: Overview of AddTransitionOptions
id: addtransitionoptions
title: AddTransitionOptions
sidebar_label: AddTransitionOptions
repo: uxp-premierepro
product: premierepro
keywords: 
---

# AddTransitionOptions

Since: **25.6**

## Properties

| Name | Type | Access | Min Version | Description |
| :--- | :--- | :----- | :---------- | :---------- |
| applyToStart | *boolean* | R | 25.6 | Get whether to apply transition to the start or end of trackitem |
| forceSingleSided | *boolean* | R | 25.6 | Get whether transition should be applied to one/both sides |
| transitionAlignment | *number* | R | 25.6 | Gets the transitionAlignment of transition |
| duration | [*TickTime*](ticktime.md) | R | 25.6 | Gets the duration of transition |

## Instance Methods

### setApplyToStart

Set whether to apply transition to the start or end of trackitem

Since: **25.6**

Returns: [*AddTransitionOptions*](addtransitionoptions.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| applyToStart | *boolean* | - |

<HorizontalLine />

### setDuration

Sets the duration of transition

Since: **25.6**

Returns: [*AddTransitionOptions*](addtransitionoptions.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| tickTime | [*TickTime*](ticktime.md) | Sets the duration of transition in TickTime |

<HorizontalLine />

### setForceSingleSided

Set whether transition should be applied to one/both sides

Since: **25.6**

Returns: [*AddTransitionOptions*](addtransitionoptions.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| forceSingleSided | *boolean* | - |

<HorizontalLine />

### setTransitionAlignment

Sets the transitionAlignment of the transition

Since: **25.6**

Returns: [*AddTransitionOptions*](addtransitionoptions.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| transitionAlignment | *number* | - |

<HorizontalLine />
