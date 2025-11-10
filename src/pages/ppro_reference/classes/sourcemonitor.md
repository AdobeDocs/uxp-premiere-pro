---
id: "sourcemonitor"
title: "SourceMonitor"
sidebar_label: "SourceMonitor"
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

# SourceMonitor

## Static Methods

### closeAllClips

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Close all clips on Source Monitor

---

### closeClip

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Close clip on Source Monitor

---

### getPosition

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_TickTime_

Get position of source monitor in time

---

### getProjectItem

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_ProjectItem_

Get projectItem at source monitor

---

### openFilePath

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Open the item at the specified path and send to the Source Monitor for preview

#### Parameters

| Name     | Type     | Description |
| :------- | :------- | :---------- |
| filePath | _string_ | -           |

---

### openProjectItem

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Open input projectItem on Source Monitor

#### Parameters

| Name        | Type                                                  | Description |
| :---------- | :---------------------------------------------------- | :---------- |
| projectItem | [_ProjectItem_](/ppro_reference/classes/projectitem/) | -           |

---

### play

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Play clip at source monitor with input speed

#### Parameters

| Name  | Type     | Description |
| :---- | :------- | :---------- |
| speed | _number_ | -           |

---
