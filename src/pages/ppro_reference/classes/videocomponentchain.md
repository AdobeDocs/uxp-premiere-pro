---
id: "videocomponentchain"
title: "VideoComponentChain"
sidebar_label: "VideoComponentChain"
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

# VideoComponentChain

## Instance Methods

### createAppendComponentAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Creates and returns an append component action

#### Parameters

| Name      | Type                                                                                                                         | Description            |
| :-------- | :--------------------------------------------------------------------------------------------------------------------------- | :--------------------- |
| component | [_Component_](/ppro_reference/classes/component/) or [_VideoFilterComponent_](/ppro_reference/classes/videofiltercomponent/) | Video filter component |

---

### createInsertComponentAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Creates and returns an insert component action

#### Parameters

| Name                    | Type                                                                                                                         | Description                                 |
| :---------------------- | :--------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------ |
| component               | [_Component_](/ppro_reference/classes/component/) or [_VideoFilterComponent_](/ppro_reference/classes/videofiltercomponent/) | Video filter component                      |
| componentInsertionIndex | _number_                                                                                                                     | Index which the component shall be inserted |

---

### createRemoveComponentAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Creates and returns an remove component action

#### Parameters

| Name      | Type                                                                                                                         | Description            |
| :-------- | :--------------------------------------------------------------------------------------------------------------------------- | :--------------------- |
| component | [_Component_](/ppro_reference/classes/component/) or [_VideoFilterComponent_](/ppro_reference/classes/videofiltercomponent/) | Video filter component |

---

### getComponentAtIndex

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Component_

Returns the component at the given index

#### Parameters

| Name           | Type     | Description |
| :------------- | :------- | :---------- |
| componentIndex | _number_ | -           |

---

### getComponentCount

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_number_

Gets the number of components in the component chain

---
