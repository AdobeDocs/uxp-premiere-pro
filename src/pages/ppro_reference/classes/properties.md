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
  - Premiere
---

# Properties

## Static Methods

### getProperties

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Properties_

Return Property Owner Object

#### Parameters

| Name                | Type                                                                                             | Description                                                 |
| :------------------ | :----------------------------------------------------------------------------------------------- | :---------------------------------------------------------- |
| propertyOwnerObject | [_Project_](/ppro_reference/classes/project/) or [_Sequence_](/ppro_reference/classes/sequence/) | This can also be object instance of Project, Sequence etc.. |

---

## Instance Methods

### createClearValueAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Create an action to clear the value with the given name. This method can fail if e.g. the underlying properties object does not support action based setting of properties.

#### Parameters

| Name | Type     | Description |
| :--- | :------- | :---------- |
| name | _string_ | -           |

---

### createSetValueAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Create an action to set a named value through scripting. The parameters are <name, value (number, boolean or string), persistence flag>. This method can fail if e.g. the underlying properties object does not support action based setting of properties.

#### Parameters

| Name            | Type                                                  | Description                                               |
| :-------------- | :---------------------------------------------------- | :-------------------------------------------------------- |
| name            | _string_                                              | property name                                             |
| value           | _boolean_ or _string_ or _number_                     | Value to set for the property key                         |
| persistenceFlag | [_Constants.PropertyType_](/ppro_reference/constants) | Indicates whether the property should be persisted or not |

---

### getValue

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_string_

Get named value in native string form

#### Parameters

| Name | Type     | Description |
| :--- | :------- | :---------- |
| name | _string_ | -           |

---

### getValueAsBool

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Get named value as boolean

#### Parameters

| Name | Type     | Description |
| :--- | :------- | :---------- |
| name | _string_ | -           |

---

### getValueAsFloat

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_number_

Get named value as float number

#### Parameters

| Name | Type     | Description |
| :--- | :------- | :---------- |
| name | _string_ | -           |

---

### getValueAsInt

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_number_

Get named value as integer number

#### Parameters

| Name | Type     | Description |
| :--- | :------- | :---------- |
| name | _string_ | -           |

---

### hasValue

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Check if a named value exists under this name.

#### Parameters

| Name | Type     | Description |
| :--- | :------- | :---------- |
| name | _string_ | -           |

---
