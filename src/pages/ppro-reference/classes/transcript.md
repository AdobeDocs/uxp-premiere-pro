---
description: Overview of Transcript
id: transcript
title: Transcript
sidebar_label: Transcript
repo: uxp-premierepro
product: premierepro
keywords: 
---

# Transcript

Since: **25.6**

## Static Methods

### createImportTextSegmentsAction

Create action that import external transcripts to ClipProjectItem

Since: **25.6**

Returns: [*Action*](action.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| textSegments | [*TextSegments*](textsegments.md) | - |
| clipProjectItem | [*ClipProjectItem*](clipprojectitem.md) | - |

<HorizontalLine />

### exportToJSON

Export transcripts inside of clipProjectItem as JSON string if transcript exist

Since: **25.6**

Returns: Promise\<*string*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| clipProjectItem | [*ClipProjectItem*](clipprojectitem.md) | - |

<HorizontalLine />

### hasTranscript

Returns true if the ClipProjectItem has an existing transcript

Since: **26.3**

Returns: *boolean*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| clipProjectItem | [*ClipProjectItem*](clipprojectitem.md) | - |

<HorizontalLine />

### importFromJSON

Returns TextSegments object initialized from jsonString

Since: **25.6**

Returns: [*TextSegments*](textsegments.md)

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| jsonString | *string* | - |

<HorizontalLine />

### querySupportedLanguages

Returns the list of language services available for transcription

Since: **26.3**

Returns: *Array\<\{displayString: string, languageCode: string, locale: string}\>*

<HorizontalLine />
