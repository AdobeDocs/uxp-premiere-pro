---
id: "projectevent"
title: "ProjectEvent"
sidebar_label: "ProjectEvent"
repo: "uxp-premierepro"
product: "premierepro"
keywords:
  - Creative Cloud
  - API Documentation
  - UXP
  - Plugins
  - JavaScript
  - ExtendScript
  - SDK
  - C++
  - Scripting
  - Premiere Pro
---

# ProjectEvent  ## Properties

| Name | Type | Access | Min Version | Description |
| :------ | :------ | :------ | :------ | :------ |
| name | *string* | R | 23.0 | The project name. |
| path | *string* | R | 23.0 | The absolute file path to the project file. |
| id | *string* | R | 23.0 | The unique identifier of the project. |
| project | *object* | R | 23.0 | The project object. |




## Events

| Name | Version | Description |
| :------ | :------ | :------ |
| EVENT_OPENED | 23.0 | Event occurs when project was opened. |
| EVENT_ACTIVATED | 23.0 | Event occurs when the active project has changed |
| EVENT_DIRTY | 23.0 | Event occurs when the project dirty state changed. |

