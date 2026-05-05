---
description: Overview of Metadata
id: metadata
title: Metadata
sidebar_label: Metadata
repo: uxp-premierepro
product: premierepro
keywords: 
---

# Metadata  

## Static Methods

### addPropertyToProjectMetadataSchema

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Add name and label property to project metadata schema

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| name | *string* | - |
| label | *string* | - |
| type | *number* | - |

___

### createSetProjectMetadataAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Get set project metadata action

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| projectItem | [*ProjectItem*](projectitem.md) | - |
| metadata | *string* | - |
| updatedFields | [*string[]*](/ppro-reference/classes/string[]/) | - |

___

### createSetXMPMetadataAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Get set project XMP metadata action

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| projectItem | [*ProjectItem*](projectitem.md) | - |
| metadata | *string* | - |

___

### getProjectColumnsMetadata

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*string*
  
Get project column metadata from project item

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| projectItem | [*ProjectItem*](projectitem.md) | - |

___

### getProjectMetadata

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*string*
  
Get project metadata

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| projectItem | [*ProjectItem*](projectitem.md) | - |

___

### getProjectPanelMetadata

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*string*
  
Get project panel metadata

___

### getXMPMetadata

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*string*
  
Get project XMP metadata

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| projectItem | [*ProjectItem*](projectitem.md) | - |

___

### setProjectPanelMetadata

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Set project panel metadata

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| metadata | *string* | - |

___
