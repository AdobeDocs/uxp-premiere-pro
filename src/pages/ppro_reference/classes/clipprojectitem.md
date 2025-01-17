---
id: "clipprojectitem"
title: "ClipProjectItem"
sidebar_label: "ClipProjectItem"
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

# ClipProjectItem  

## Properties

| Name | Type | Access | Min Version | Description |
| :------ | :------ | :------ | :------ | :------ |
| name | *string* | R | 25.0 | Get name of project item object |

## Static Methods

### cast

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*any*

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| projectItem | *any* | - |

___

## Instance Methods

### canChangeMediaPath

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Returns true if Premiere Pro can change the path, associated with this project item; otherwise, returns false

___

### canProxy

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Indicates whether it is possible to attach a proxy, to this project item.

___

### createClearInOutPointsAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Create Clear the in or out point of the Project item action

___

### createSetFootageInterpretationAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Set the footage interpretation object for project item

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| footageInterpretation | [*FootageInterpretation*](/ppro_reference/classes/footageinterpretation/) | - |

___

### createSetInOutPointsAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*any*
  
Set the in or out point of the Project item

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| inPoint | [*TickTime*](/ppro_reference/classes/ticktime/) | - |
| outPoint | [*TickTime*](/ppro_reference/classes/ticktime/) | - |

___

### createSetInPointAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Returns an action which Sets the in point of the Project item

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| tickTime | *any* | - |

___

### createSetInputLUTIDAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Create action for setting Guid of Input LUT on media. This applies for Video Clips only.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| stringLUTID | *string* | - |

___

### createSetOfflineAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Returns an action which sets the media offline

___

### createSetOutPointAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Returns an action which Sets the in point of the Project item

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| tickTime | *any* | - |

___

### createSetOverrideFrameRateAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Returns an action which sets the override frame rate

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| inOverriddenFrameRateValue | *any* | - |

___

### createSetOverridePixelAspectRatioAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Returns an action which sets Override pixel aspect ratio

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| inNumerator | *any* | - |
| inDenominator | *any* | - |

___

### createSetScaleToFrameSizeAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Action*
  
Returns an action which sets the scale to frame to true

___

### findItemsMatchingMediaPath

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Array*
  
Returns array of projects items with media paths containing match string

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| matchString | *string* | - |
| ignoreSubclips | *boolean* | - |

___

### getColorSpace

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*ColorSpace*
  
Get color space object of the project item

___

### getComponentChain

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*string*
  
Get the media file path of the Project item.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| mediaType | [*Constants.MediaType*](/ppro_reference/constants) | Media type can be audio, video or data/caption |

___

### getContentType

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*any*
  
Get content type of the Project item

___

### getEmbeddedLUTID

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*string*
  
Get GUID of LUT embedded in media

___

### getFootageInterpretation

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*FootageInterpretation*
  
Get the footage interpretation object for project item

___

### getInPoint

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*TickTime*
  
Get the in point of the Project item

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| mediaType | [*Constants.MediaType*](/ppro_reference/constants) | Media type can be audio, video or data/caption |

___

### getInputLUTID

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*string*
  
Get Guid of Input LUT overridden on media

___

### getMediaFilePath

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*string*
  
Get the media file path of the Project item.

___

### getOutPoint

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*TickTime*
  
Get the out point of the Project item

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| mediaType | [*Constants.MediaType*](/ppro_reference/constants) | Media type can be audio, video or data/caption |

___

### getOverrideColorSpaceList

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Array*
  
Get the override color space list

___

### getParent

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*ProjectItem*
  
Get the root item of the project which contains all items of the project on the lowest level

___

### getProject

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Project*
  
Get the root item of the project which contains all items of the project on the lowest level.

___

### getProxyPath

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*string*
  
Returns the proxy path if the project item has a proxy attached

___

### getSequence

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*Sequence*
  
Get the sequence of the Project item

___

### hasProxy

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Indicates whether a proxy has already been attached, to the project item.

___

### isMergedClip

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Returns true if the clip Project item is a merged clip

___

### isMulticamClip

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Returns true if the clip Project item is a multicam clip

___

### isOffline

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Returns true if the media is offline

___

### isSequence

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Returns true if the project item is sequence

___

### refreshMedia

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

*boolean*
  
Updates representation of the media associated with the project item

___
