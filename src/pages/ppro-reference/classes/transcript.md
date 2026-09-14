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

### isLanguagePackAvailable

Returns true if the language pack for the given language code is available ex:isLanguagePackAvailable('en-US')

Since: **25.6**

Returns: *boolean*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| language | *string* | - |

<HorizontalLine />

### querySupportedLanguages

Returns the list of language services available for transcription

Since: **26.3**

Returns: *Array\<\{displayString: string, languageCode: string, locale: string}\>*

<HorizontalLine />

### transcribeClipProjectItem

Transcribes the clip audio associated with the given ClipProjectItem

Since: **25.6**

Returns: Promise\<*boolean*\>

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| clipProjectItem | [*ClipProjectItem*](clipprojectitem.md) | - |
| options? | *\{language?: string}* | optional transcription options. `language` is a language code (ISO 639-1 language + ISO 3166-1 region, e.g. "en-US") and must be one of the languageCode values returned by `querySupportedLanguages()`; an unsupported code throws. If language is omitted, the default language from the user's transcription preferences is used. Note: if the "auto-detect language" transcription preference is enabled, the spoken language is detected automatically and overrides the language provided here. |

<HorizontalLine />
