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
  - Premiere Pro
---

# SourceMonitor  

## Static Methods

### closeAllClips

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Close all clips on Source Monitor

___

### closeClip

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Close clip on Source Monitor

___

### getPosition

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*TickTime*
  
Get position of source monitor in time

___

### getProjectItem

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*ProjectItem*
  
Get projectItem at source monitor

___

### openFilePath

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Open the item at the specified path and send to the Source Monitor for preview

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| filePath | *string* | - |

___

### openProjectItem

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Open input projectItem on Source Monitor

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| projectItem | [*ProjectItem*](/ppro_reference/classes/projectitem/) | - |

___

### play

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Play clip at source monitor with input speed

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| speed | *number* | - |

___
