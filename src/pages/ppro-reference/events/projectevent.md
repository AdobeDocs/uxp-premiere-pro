---
description: Overview of ProjectEvent
id: projectevent
title: ProjectEvent
sidebar_label: ProjectEvent
repo: uxp-premierepro
product: premierepro
keywords: 
---

# ProjectEvent

Since: **25.6**

## Properties

| Name | Type | Access | Min Version | Description |
| :--- | :--- | :----- | :---------- | :---------- |
| id | *string* | R | 25.6 | The unique identifier of the project. |
| name | *string* | R | 25.6 | The project name. |
| path | *string* | R | 25.6 | The absolute file path to the project file. |
| project | [*Project*](project.md) | R | 25.6 | The project object. |

## Events

| Name | Version | Description |
| :--- | :------ | :---------- |
| EVENT_ACTIVATED | 25.6 | Event occurs when the active project has changed |
| EVENT_DIRTY | 25.6 | Event occurs when the project dirty state changed. |
| EVENT_OPENED | 25.6 | Event occurs when project was opened. |
