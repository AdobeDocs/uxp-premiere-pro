---
description: Overview of VideoComponentChain
id: videocomponentchain
title: VideoComponentChain
sidebar_label: VideoComponentChain
repo: uxp-premierepro
product: premierepro
keywords: 
---

# VideoComponentChain  

## Instance Methods

### createAppendComponentAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Creates and returns an append component action

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| component | [*Component*](component.md) or [*VideoFilterComponent*](/ppro-reference/classes/videofiltercomponent/index.md) | Video filter component |

<HorizontalLine />

### createInsertComponentAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Creates and returns an insert component action

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| component | [*Component*](component.md) or [*VideoFilterComponent*](/ppro-reference/classes/videofiltercomponent/index.md) | Video filter component |
| componentInsertionIndex | *number* | Index which the component shall be inserted |

<HorizontalLine />

### createRemoveComponentAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Creates and returns an remove component action

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| component | [*Component*](component.md) or [*VideoFilterComponent*](/ppro-reference/classes/videofiltercomponent/index.md) | Video filter component |

<HorizontalLine />

### getComponentAtIndex

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Component*
  
Returns the component at the given index

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| componentIndex | *number* | - |

<HorizontalLine />

### getComponentCount

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*number*
  
Gets the number of components in the component chain

<HorizontalLine />
