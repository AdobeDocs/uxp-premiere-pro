---
description: Overview of CloseProjectOptions
id: closeprojectoptions
title: CloseProjectOptions
sidebar_label: CloseProjectOptions
repo: uxp-premierepro
product: premierepro
keywords: 
---

# CloseProjectOptions

Since: **25.6**

## Properties

| Name | Type | Access | Min Version | Description |
| :--- | :--- | :----- | :---------- | :---------- |
| promptIfDirty | *boolean* | R | 25.6 | Get whether a prompt is shown if a project is dirty on project open/close |
| showCancelButton | *boolean* | R | 25.6 | Get whether the cancel button is shown on project open/close |
| isAppBeingPreparedToQuit | *boolean* | R | 25.6 | Get whether the app is prepared to quit when open/closing a project |
| saveWorkspace | *boolean* | R | 25.6 | Get whether your workspaces are saved when opening/closing a project |

## Instance Methods

### setIsAppBeingPreparedToQuit

Set whether the app should be prepared to quit when open/closing a project

Since: **25.6**

Returns: [*CloseProjectOptions*](closeprojectoptions.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| isAppBeingPreparedToQuit | *boolean* | - |

<HorizontalLine />

### setPromptIfDirty

Set whether to prompt if a project is dirty on project open/close

Since: **25.6**

Returns: [*CloseProjectOptions*](closeprojectoptions.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| promptIfDirty | *boolean* | - |

<HorizontalLine />

### setSaveWorkspace

Set whether to save your workspaces when opening/closing a project

Since: **25.6**

Returns: [*CloseProjectOptions*](closeprojectoptions.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| isAppBeingPreparedToQuit | *boolean* | - |

<HorizontalLine />

### setShowCancelButton

Set whether to show the cancel button on project open/close

Since: **25.6**

Returns: [*CloseProjectOptions*](closeprojectoptions.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| showCancelButton | *boolean* | - |

<HorizontalLine />
