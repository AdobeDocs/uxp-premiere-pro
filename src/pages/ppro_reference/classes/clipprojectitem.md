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
  - Premiere
---

# ClipProjectItem

## Properties

| Name | Type     | Access | Min Version | Description                       |
| :--- | :------- | :----- | :---------- | :-------------------------------- |
| type | _number_ | R      | 25.0        | Get the type of the Project Item. |
| name | _string_ | R      | 25.0        | The name of this project item.    |

## Static Methods

### cast

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_ClipProjectItem_

Cast ProjectItem in to ClipProjectItem

#### Parameters

| Name        | Type                                                  | Description |
| :---------- | :---------------------------------------------------- | :---------- |
| projectItem | [_ProjectItem_](/ppro_reference/classes/projectitem/) | -           |

---

## Instance Methods

### attachProxy

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Attach proxy or high resolution footage to projectItem and returns true if successful. Not undoable.

#### Parameters

| Name                              | Type      | Description |
| :-------------------------------- | :-------- | :---------- |
| mediaPath                         | _string_  | -           |
| isHiRes                           | _boolean_ | -           |
| inMakeAlternateLinkInTeamProjects | _boolean_ | -           |

---

### canChangeMediaPath

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Returns true if Premiere can change the path associated with this project item; otherwise, returns false

---

### canProxy

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Indicates whether it is possible to attach a proxy to this project item.

---

### changeMediaFilePath

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Change media file path of projectItem and returns true if successful. Not undoable.

#### Parameters

| Name                       | Type      | Description |
| :------------------------- | :-------- | :---------- |
| newPath                    | _string_  | -           |
| overrideCompatibilityCheck | _boolean_ | -           |

---

### createClearInOutPointsAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Create Clear the in or out point of the Project item action

---

### createSetColorLabelAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Create an action for set color label to projectItem by index

#### Parameters

| Name              | Type     | Description |
| :---------------- | :------- | :---------- |
| inColorLabelIndex | _number_ | -           |

---

### createSetFootageInterpretationAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Set the footage interpretation object for project item

#### Parameters

| Name                  | Type                                                                      | Description |
| :-------------------- | :------------------------------------------------------------------------ | :---------- |
| footageInterpretation | [_FootageInterpretation_](/ppro_reference/classes/footageinterpretation/) | -           |

---

### createSetInOutPointsAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Set the in or out point of the Project item

#### Parameters

| Name     | Type                                            | Description |
| :------- | :---------------------------------------------- | :---------- |
| inPoint  | [_TickTime_](/ppro_reference/classes/ticktime/) | -           |
| outPoint | [_TickTime_](/ppro_reference/classes/ticktime/) | -           |

---

### createSetInPointAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Returns an action which Sets the in point of the Project item

#### Parameters

| Name     | Type                                            | Description |
| :------- | :---------------------------------------------- | :---------- |
| tickTime | [_TickTime_](/ppro_reference/classes/ticktime/) | -           |

---

### createSetInputLUTIDAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Create action for setting Guid of Input LUT on media. This applies for Video Clips only.

#### Parameters

| Name        | Type     | Description |
| :---------- | :------- | :---------- |
| stringLUTID | _string_ | -           |

---

### createSetNameAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Returns action that renames projectItem

#### Parameters

| Name   | Type     | Description |
| :----- | :------- | :---------- |
| inName | _string_ | -           |

---

### createSetOfflineAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Returns an action which sets the media offline

---

### createSetOutPointAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Returns an action which Sets the out point of the Project item

#### Parameters

| Name     | Type                                            | Description |
| :------- | :---------------------------------------------- | :---------- |
| tickTime | [_TickTime_](/ppro_reference/classes/ticktime/) | -           |

---

### createSetOverrideFrameRateAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Returns an action which sets the override frame rate

#### Parameters

| Name                       | Type     | Description |
| :------------------------- | :------- | :---------- |
| inOverriddenFrameRateValue | _number_ | -           |

---

### createSetOverridePixelAspectRatioAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Returns an action which sets Override pixel aspect ratio

#### Parameters

| Name          | Type     | Description |
| :------------ | :------- | :---------- |
| inNumerator   | _number_ | -           |
| inDenominator | _number_ | -           |

---

### createSetScaleToFrameSizeAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Returns an action which sets the scale to frame to true

---

### findItemsMatchingMediaPath

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_ProjectItem[]_

Returns array of project's items with media paths containing match string

#### Parameters

| Name           | Type      | Description |
| :------------- | :-------- | :---------- |
| matchString    | _string_  | -           |
| ignoreSubclips | _boolean_ | -           |

---

### getColorLabelIndex

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_number_

Get color label index of projectItem

---

### getComponentChain

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_string_

Gets the component chain associated with this project item.

#### Parameters

| Name      | Type                                               | Description                                    |
| :-------- | :------------------------------------------------- | :--------------------------------------------- |
| mediaType | [_Constants.MediaType_](/ppro_reference/constants) | Media type can be audio, video or data/caption |

---

### getContentType

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Constants.ContentType_

Get content type of the Project item

---

### getEmbeddedLUTID

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_string_

Get GUID of LUT embedded in media

---

### getFootageInterpretation

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_FootageInterpretation_

Get the footage interpretation object for project item

---

### getInPoint

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_TickTime_

Get the in point of the Project item

#### Parameters

| Name      | Type                                               | Description                                    |
| :-------- | :------------------------------------------------- | :--------------------------------------------- |
| mediaType | [_Constants.MediaType_](/ppro_reference/constants) | Media type can be audio, video or data/caption |

---

### getInputLUTID

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_string_

Get Guid of Input LUT overridden on media

---

### getMedia

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Media_

Return media associated with clipProjectItem

---

### getMediaFilePath

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_string_

Get the media file path of the Project item.

---

### getOutPoint

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_TickTime_

Get the out point of the Project item

#### Parameters

| Name      | Type                                               | Description                                    |
| :-------- | :------------------------------------------------- | :--------------------------------------------- |
| mediaType | [_Constants.MediaType_](/ppro_reference/constants) | Media type can be audio, video or data/caption |

---

### getProject

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Project_

Get the parent Project of this projectItem.

---

### getProxyPath

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_string_

Returns the proxy path if the project item has a proxy attached

---

### getSequence

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Sequence_

Get the sequence of the Project item

---

### hasProxy

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Indicates whether a proxy has already been attached to the project item.

---

### isMergedClip

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Returns true if the clip Project item is a merged clip

---

### isMulticamClip

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Returns true if the clip Project item is a multicam clip

---

### isOffline

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Returns true if the media is offline

---

### isSequence

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Returns true if the project item is a sequence

---

### refreshMedia

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Updates representation of the media associated with the project item

---
