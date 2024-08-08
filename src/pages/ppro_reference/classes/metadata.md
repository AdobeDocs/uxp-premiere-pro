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
  - Premiere Pro
---

# Metadata  

## Methods

### getProjectMetadata

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*string*
  
Get project metadata

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| projectItem | [*ProjectItem*](/ppro_reference/classes/projectitem/) | - |

___

### getXMPMetadata

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*string*
  
Get project XMP metadata

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| projectItem | [*ProjectItem*](/ppro_reference/classes/projectitem/) | - |

___

### createSetProjectMetadataAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*Action*
  
Get set project metadata action

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| projectItem | [*ProjectItem*](/ppro_reference/classes/projectitem/) | - |
| metadata | *string* | - |
| updatedFields | *Array* | - |

___

### createSetXMPMetadataAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*Action*
  
Get set project XMP metadata action

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| projectItem | [*ProjectItem*](/ppro_reference/classes/projectitem/) | - |
| metadata | *string* | - |

___

### addPropertyToProjectMetadataSchema

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*boolean*
  
Add name and label property to project metadata schema

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| name | *string* | - |
| label | *string* | - |
| type | *number* | - |

___

### getProjectColumnsMetadata

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*string*
  
Get project column metadata from project item

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| projectItem | [*ProjectItem*](/ppro_reference/classes/projectitem/) | - |

___

### getProjectPanelMetadata

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*string*
  
Get project panel metadata

___

### setProjectPanelMetadata

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">23.0</span>

*boolean*
  
Set project panel metadata

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| undefined | *string* | - |

___
