---
id: "audiocomponentchain"
title: "AudioComponentChain"
sidebar_label: "AudioComponentChain"
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

# AudioComponentChain  

## Methods

### createInsertComponentAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*Action*
  
Creates and returns an insert component action

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| component | *object* | - |
| componentInsertionIndex | *number* | - |

___

### createAppendComponentAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*Action*
  
Creates and returns an append component action

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| component | *object* | - |

___

### createRemoveComponentAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*Action*
  
Creates and returns an remove component action

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| component | *object* | - |

___

### getComponentAtIndex

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*VideoComponentChain*
  
Returns the component at the given index

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| componentIndex | *number* | - |

___

### getComponentCount

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*number*
  
Gets the number of components in the component chain

___