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

Since: **25.6**

## Properties

| Name | Type | Access | Min Version | Description |
| :--- | :--- | :----- | :---------- | :---------- |
| name | *string* | R | 25.6 | The name of this project item. |
| type | *number* | R | 25.6 | Get the type of the Project Item. |

## Static Methods

### cast

Cast ProjectItem in to ClipProjectItem

Since: **25.6**

Returns: [*ClipProjectItem*](clipprojectitem.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| projectItem | [*ProjectItem*](projectitem.md) | - |

<HorizontalLine />

## Instance Methods

### attachProxy

Attach proxy or high resolution footage to projectItem and returns true if successful. Not undoable.

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| mediaPath | *string* | - |
| isHiRes | *boolean* | - |
| inMakeAlternateLinkInTeamProjects | *boolean* | - |

<HorizontalLine />

### canChangeMediaPath

Returns true if Premiere Pro can change the path associated with this project item; otherwise, returns false

Since: **25.6**

Returns: Promise\<*boolean*\>

<HorizontalLine />

### canProxy

Indicates whether it is possible to attach a proxy to this project item.

Since: **25.6**

Returns: Promise\<*boolean*\>

<HorizontalLine />

### changeMediaFilePath

Change media file path of projectItem and returns true if successful. Not undoable.

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| newPath | *string* | - |
| overrideCompatibilityCheck | *boolean* | - |

<HorizontalLine />

### createClearInOutPointsAction

Create Clear the in or out point of the Project item action

Since: **25.6**

Returns: [*Action*](action.md)

<HorizontalLine />

### createSetColorLabelAction

Create an action for set color label to projectItem by index

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| inColorLabelIndex | *number* | - |

<HorizontalLine />

### createSetFootageInterpretationAction

Set the footage interpretation object for project item

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| footageInterpretation | [*FootageInterpretation*](footageinterpretation.md) | - |

<HorizontalLine />

### createSetInOutPointsAction

Set the in or out point of the Project item

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| inPoint | [*TickTime*](ticktime.md) | - |
| outPoint | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### createSetInPointAction

Returns an action which Sets the in point of the Project item

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| tickTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### createSetInputLUTIDAction

Create action for setting Guid of Input LUT on media. This applies for Video Clips only.

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| stringLUTID | *string* | - |

<HorizontalLine />

### createSetNameAction

Returns action that renames projectItem

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| inName | *string* | - |

<HorizontalLine />

### createSetOfflineAction

Returns an action which sets the media offline

Since: **25.6**

Returns: [*Action*](action.md)

<HorizontalLine />

### createSetOutPointAction

Returns an action which Sets the in point of the Project item

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| tickTime | [*TickTime*](ticktime.md) | - |

<HorizontalLine />

### createSetOverrideFrameRateAction

Returns an action which sets the override frame rate

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| overriddenFrameRateValue | *number* | - |

<HorizontalLine />

### createSetOverridePixelAspectRatioAction

Returns an action which sets Override pixel aspect ratio

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| numerator | *number* | - |
| denominator | *number* | - |

<HorizontalLine />

### createSetScaleToFrameSizeAction

Returns an action which sets the scale to frame to true

Since: **25.6**

Returns: [*Action*](action.md)

<HorizontalLine />

### createSubClipAction

Returns a deferred Action that creates a subclip when committed inside a transaction. hasHardBoundaries: if true, prevents trimming beyond the subclip boundaries. Takes additional options (defaulting to true).

Since: **26.3**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| name | *string* | - |
| startTime | [*TickTime*](ticktime.md) | - |
| endTime | [*TickTime*](ticktime.md) | - |
| hasHardBoundaries | *boolean* | - |
| options | *\{ takeVideo?: boolean, takeAudio?: boolean }* | - |

<HorizontalLine />

### findItemsMatchingMediaPath

Returns array of project's items with media paths containing match string

Since: **25.6**

Returns: Promise\<[*ProjectItem[]*](projectitem.md)\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| matchString | *string* | - |
| ignoreSubclips | *boolean* | - |

<HorizontalLine />

### getColorLabelIndex

Get color label index of projectItem

Since: **25.6**

Returns: Promise\<*number*\>

<HorizontalLine />

### getComponentChain

Get the component chain of the Project item for the given media type.

Since: **25.6**

Returns: Promise\<[*AudioComponentChain*](audiocomponentchain.md) | [*VideoComponentChain*](videocomponentchain.md) | null\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| mediaType | [*Constants.MediaType*](../constants/index.md#mediatype) | Media type can be audio or video |

<HorizontalLine />

### getContentType

Get content type of the Project item

Since: **25.6**

Returns: Promise\<[*Constants.ContentType*](../constants/index.md#contenttype)\>

<HorizontalLine />

### getEmbeddedLUTID

Get GUID of LUT embedded in media

Since: **25.6**

Returns: Promise\<*string*\>

<HorizontalLine />

### getFootageInterpretation

Get the footage interpretation object for project item

Since: **25.6**

Returns: Promise\<[*FootageInterpretation*](footageinterpretation.md)\>

<HorizontalLine />

### getInPoint

Get the in point of the Project item

Since: **25.6**

Returns: Promise\<[*TickTime*](ticktime.md)\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| mediaType | [*Constants.MediaType*](../constants/index.md#mediatype) | Media type can be audio, video or data/caption |

<HorizontalLine />

### getInputLUTID

Get Guid of Input LUT overridden on media

Since: **25.6**

Returns: Promise\<*string*\>

<HorizontalLine />

### getMedia

Return media associated with clipProjectItem

Since: **25.6**

Returns: Promise\<[*Media*](media.md)\>

<HorizontalLine />

### getMediaFilePath

Get the media file path of the Project item.

Since: **25.6**

Returns: Promise\<*string*\>

<HorizontalLine />

### getOriginatingProjectPath

Return originating project path associated with clipProjectItem

Since: **26.2**

Returns: Promise\<*string*\>

<HorizontalLine />

### getOutPoint

Get the out point of the Project item

Since: **25.6**

Returns: Promise\<[*TickTime*](ticktime.md)\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| mediaType | [*Constants.MediaType*](../constants/index.md#mediatype) | Media type can be audio, video or data/caption |

<HorizontalLine />

### getProject

Get the parent Project of this projectItem.

Since: **25.6**

Returns: Promise\<[*Project*](project.md)\>

<HorizontalLine />

### getProxyPath

Returns the proxy path if the project item has a proxy attached

Since: **25.6**

Returns: Promise\<*string*\>

<HorizontalLine />

### getSequence

Get the sequence of the Project item

Since: **25.6**

Returns: Promise\<[*Sequence*](sequence.md)\>

<HorizontalLine />

### hasProxy

Indicates whether a proxy has already been attached to the project item.

Since: **25.6**

Returns: Promise\<*boolean*\>

<HorizontalLine />

### isMergedClip

Returns true if the clip Project item is a merged clip

Since: **25.6**

Returns: Promise\<*boolean*\>

<HorizontalLine />

### isMulticamClip

Returns true if the clip Project item is a multicam clip

Since: **25.6**

Returns: Promise\<*boolean*\>

<HorizontalLine />

### isOffline

Returns true if the media is offline

Since: **25.6**

Returns: Promise\<*boolean*\>

<HorizontalLine />

### isSequence

Returns true if the project item is a sequence

Since: **25.6**

Returns: Promise\<*boolean*\>

<HorizontalLine />

### refreshMedia

Updates representation of the media associated with the project item

Since: **25.6**

Returns: Promise\<*boolean*\>

<HorizontalLine />
