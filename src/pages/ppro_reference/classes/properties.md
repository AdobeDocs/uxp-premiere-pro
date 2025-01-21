---
id: "properties"
title: "Properties"
sidebar_label: "Properties"
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

# Properties  

## Instance Methods

### createClearValueAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*object*
  
Create an action to clear the value with the given name. This method can fail if e.g. the underlying properties object does not support action based setting of properties.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| name | *string* | - |

___

### createSetValueAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*object*
  
Create an action to set a named value through scripting. The parameters are <name, value (number, boolean or string), persistence flag>. This method can fail if e.g. the underlying properties object does not support action based setting of properties.

___

### getValue

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*string*
  
Get named value in native string form

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| name | *string* | - |

___

### getValueAsBool

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Get named value as boolean

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| name | *string* | - |

___

### getValueAsFloat

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*number*
  
Get named value as float number

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| name | *string* | - |

___

### getValueAsInt

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*number*
  
Get named value as integer number

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| name | *string* | - |

___

### hasValue

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Check if a named value exists under this name.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| name | *string* | - |

___
