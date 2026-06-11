---
description: Overview of ProjectUtils
id: projectutils
title: ProjectUtils
sidebar_label: ProjectUtils
repo: uxp-premierepro
product: premierepro
keywords: 
---

# ProjectUtils

Since: **25.6**

## Static Methods

### getProjectFromViewId

Get project based on input view guid

Since: **25.6**

Returns: Promise\<[*Project*](project.md)\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| guid | [*Guid*](guid.md) | - |

<HorizontalLine />

### getProjectViewIds

Get array of project view ids

Since: **25.6**

Returns: Promise\<[*Guid[]*](guid.md)\>

<HorizontalLine />

### getSelection

Get array of selected project items in project view

Since: **25.6**

Returns: Promise\<[*ProjectItemSelection*](projectitemselection.md)\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| project | [*Project*](project.md) | - |

<HorizontalLine />

### getSelectionFromViewId

Get array of selected projectItem based on input view guid

Since: **25.6**

Returns: Promise\<[*ProjectItemSelection*](projectitemselection.md)\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| guid | [*Guid*](guid.md) | - |

<HorizontalLine />
