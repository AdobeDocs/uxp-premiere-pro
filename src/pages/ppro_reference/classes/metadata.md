---
id: "metadata"
title: "Metadata"
sidebar_label: "Metadata"
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

# Metadata

## Static Methods

### addPropertyToProjectMetadataSchema

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Add name and label property to project metadata schema

#### Parameters

| Name  | Type     | Description |
| :---- | :------- | :---------- |
| name  | _string_ | -           |
| label | _string_ | -           |
| type  | _number_ | -           |

---

### createSetProjectMetadataAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Get set project metadata action

#### Parameters

| Name          | Type                                                  | Description |
| :------------ | :---------------------------------------------------- | :---------- |
| projectItem   | [_ProjectItem_](/ppro_reference/classes/projectitem/) | -           |
| metadata      | _string_                                              | -           |
| updatedFields | [_string[]_](/ppro_reference/classes/string[]/)       | -           |

---

### createSetXMPMetadataAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Get set project XMP metadata action

#### Parameters

| Name        | Type                                                  | Description |
| :---------- | :---------------------------------------------------- | :---------- |
| projectItem | [_ProjectItem_](/ppro_reference/classes/projectitem/) | -           |
| metadata    | _string_                                              | -           |

---

### getProjectColumnsMetadata

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_string_

Get project column metadata from project item

#### Parameters

| Name        | Type                                                  | Description |
| :---------- | :---------------------------------------------------- | :---------- |
| projectItem | [_ProjectItem_](/ppro_reference/classes/projectitem/) | -           |

---

### getProjectMetadata

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_string_

Get project metadata

#### Parameters

| Name        | Type                                                  | Description |
| :---------- | :---------------------------------------------------- | :---------- |
| projectItem | [_ProjectItem_](/ppro_reference/classes/projectitem/) | -           |

---

### getProjectPanelMetadata

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_string_

Get project panel metadata

---

### getXMPMetadata

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_string_

Get project XMP metadata

#### Parameters

| Name        | Type                                                  | Description |
| :---------- | :---------------------------------------------------- | :---------- |
| projectItem | [_ProjectItem_](/ppro_reference/classes/projectitem/) | -           |

---

### setProjectPanelMetadata

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Set project panel metadata

#### Parameters

| Name     | Type     | Description |
| :------- | :------- | :---------- |
| metadata | _string_ | -           |

---
