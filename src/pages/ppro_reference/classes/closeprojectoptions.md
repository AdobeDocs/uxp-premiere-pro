---
id: "closeprojectoptions"
title: "CloseProjectOptions"
sidebar_label: "CloseProjectOptions"
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
  - Premiere
---

# CloseProjectOptions

## Properties

| Name                     | Type      | Access | Min Version | Description                                                               |
| :----------------------- | :-------- | :----- | :---------- | :------------------------------------------------------------------------ |
| promptIfDirty            | _boolean_ | R      | 25.0        | Get whether a prompt is shown if a project is dirty on project open/close |
| showCancelButton         | _boolean_ | R      | 25.0        | Get whether the cancel button is shown on project open/close              |
| isAppBeingPreparedToQuit | _boolean_ | R      | 25.0        | Get whether the app is prepared to quit when open/closing a project       |
| saveWorkspace            | _boolean_ | R      | 25.0        | Get whether your workspaces are saved when opening/closing a project      |

## Instance Methods

### setIsAppBeingPreparedToQuit

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_CloseProjectOptions_

Set whether the app should be prepared to quit when open/closing a project

#### Parameters

| Name                     | Type      | Description |
| :----------------------- | :-------- | :---------- |
| isAppBeingPreparedToQuit | _boolean_ | -           |

---

### setPromptIfDirty

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_CloseProjectOptions_

Set whether to prompt if a project is dirty on project open/close

#### Parameters

| Name          | Type      | Description |
| :------------ | :-------- | :---------- |
| promptIfDirty | _boolean_ | -           |

---

### setSaveWorkspace

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_CloseProjectOptions_

Set whether to save your workspaces when opening/closing a project

#### Parameters

| Name                     | Type      | Description |
| :----------------------- | :-------- | :---------- |
| isAppBeingPreparedToQuit | _boolean_ | -           |

---

### setShowCancelButton

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_CloseProjectOptions_

Set whether to show the cancel button on project open/close

#### Parameters

| Name             | Type      | Description |
| :--------------- | :-------- | :---------- |
| showCancelButton | _boolean_ | -           |

---
