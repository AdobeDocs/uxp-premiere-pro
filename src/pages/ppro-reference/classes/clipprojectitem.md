---
description: Overview of ClipProjectItem
id: clipprojectitem
title: ClipProjectItem
sidebar_label: ClipProjectItem
repo: uxp-premierepro
product: premierepro
keywords: 
---

# ClipProjectItem  

## Properties

| Name | Type | Access | Min Version | Description |
| :------ | :------ | :------ | :------ | :------ |
| type | *number* | R | 25.0 | Get the type of the Project Item. |
| name | *string* | R | 25.0 | The name of this project item. |

## Static Methods

### cast

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*ClipProjectItem*
  
Cast ProjectItem in to ClipProjectItem

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| projectItem | [*ProjectItem*](projectitem.md) | - |

<HorizontalLine />

## Instance Methods

### attachProxy

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Attach proxy or high resolution footage to projectItem and returns true if successful. Not undoable.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| mediaPath | *string* | - |
| isHiRes | *boolean* | - |
| inMakeAlternateLinkInTeamProjects | *boolean* | - |

<HorizontalLine />

### canChangeMediaPath

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Returns true if Premiere Pro can change the path associated with this project item; otherwise, returns false

<HorizontalLine />

### canProxy

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Indicates whether it is possible to attach a proxy to this project item.

<HorizontalLine />

### changeMediaFilePath

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Change media file path of projectItem and returns true if successful. Not undoable.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| newPath | *string* | - |
| overrideCompatibilityCheck | *boolean* | - |

<HorizontalLine />

### createClearInOutPointsAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Create Clear the in or out point of the Project item action

<HorizontalLine />

### createSetColorLabelAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Create an action for set color label to projectItem by index

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| inColorLabelIndex | *number* | - |

<HorizontalLine />

### createSetFootageInterpretationAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Set the footage interpretation object for project item

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| footageInterpretation | [*FootageInterpretation*](footageinterpretation.md) | - |

<HorizontalLine />

### createSetInOutPointsAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Set the in or out point of the Project item

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| inPoint | [*TickTime*](ticktime.md) | - |
| outPoint | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### createSetInPointAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Returns an action which Sets the in point of the Project item

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| tickTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### createSetInputLUTIDAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Create action for setting Guid of Input LUT on media. This applies for Video Clips only.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| stringLUTID | *string* | - |

<HorizontalLine />

### createSetNameAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Returns action that renames projectItem

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| inName | *string* | - |

<HorizontalLine />

### createSetOfflineAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Returns an action which sets the media offline

<HorizontalLine />

### createSetOutPointAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*

Returns an action which Sets the out point of the Project item

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| tickTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### createSetOverrideFrameRateAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Returns an action which sets the override frame rate

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| inOverriddenFrameRateValue | *number* | - |

<HorizontalLine />

### createSetOverridePixelAspectRatioAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Returns an action which sets Override pixel aspect ratio

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| inNumerator | *number* | - |
| inDenominator | *number* | - |

<HorizontalLine />

### createSetScaleToFrameSizeAction

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Action*
  
Returns an action which sets the scale to frame to true

<HorizontalLine />

### findItemsMatchingMediaPath

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*ProjectItem[]*
  
Returns array of project's items with media paths containing match string

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| matchString | *string* | - |
| ignoreSubclips | *boolean* | - |

<HorizontalLine />

### getColorLabelIndex

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*number*
  
Get color label index of projectItem

<HorizontalLine />

### getComponentChain

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*string*

Gets the component chain associated with this project item.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| mediaType | [*Constants.MediaType*](../constants/index.md) | Media type can be audio, video or data/caption |

<HorizontalLine />

### getContentType

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Constants.ContentType*
  
Get content type of the Project item

<HorizontalLine />

### getEmbeddedLUTID

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*string*
  
Get GUID of LUT embedded in media

<HorizontalLine />

### getFootageInterpretation

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*FootageInterpretation*
  
Get the footage interpretation object for project item

<HorizontalLine />

### getInPoint

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*TickTime*
  
Get the in point of the Project item

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| mediaType | [*Constants.MediaType*](../constants/index.md) | Media type can be audio, video or data/caption |

<HorizontalLine />

### getInputLUTID

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*string*
  
Get Guid of Input LUT overridden on media

<HorizontalLine />

### getMedia

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Media*
  
Return media associated with clipProjectItem

<HorizontalLine />

### getMediaFilePath

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*string*
  
Get the media file path of the Project item.

<HorizontalLine />

### getOriginatingProjectPath

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*string*
  
Return originating project path associated with clipProjectItem

<HorizontalLine />

### getOutPoint

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*TickTime*
  
Get the out point of the Project item

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| mediaType | [*Constants.MediaType*](../constants/index.md) | Media type can be audio, video or data/caption |

<HorizontalLine />

### getProject

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Project*
  
Get the parent Project of this projectItem.

<HorizontalLine />

### getProxyPath

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*string*
  
Returns the proxy path if the project item has a proxy attached

<HorizontalLine />

### getSequence

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*Sequence*
  
Get the sequence of the Project item

<HorizontalLine />

### hasProxy

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Indicates whether a proxy has already been attached to the project item.

<HorizontalLine />

### isMergedClip

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Returns true if the clip Project item is a merged clip

<HorizontalLine />

### isMulticamClip

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Returns true if the clip Project item is a multicam clip

<HorizontalLine />

### isOffline

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Returns true if the media is offline

<HorizontalLine />

### isSequence

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Returns true if the project item is a sequence

<HorizontalLine />

### refreshMedia

\<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;"\>25.0\</span\>

*boolean*
  
Updates representation of the media associated with the project item

<HorizontalLine />
