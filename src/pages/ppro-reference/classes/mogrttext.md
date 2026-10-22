---
description: Overview of MogrtText
id: mogrttext
title: MogrtText
sidebar_label: MogrtText
repo: uxp-premierepro
product: premierepro
keywords: 
---

# MogrtText

Since: **27.0**

## Constructor

Construct a MogrtText with a single empty text run.

Since: **27.0**

<HorizontalLine />

## Instance Methods

### getAllCaps

Get all caps. Throws if isUniformStyling() is false (mixed styling); check isUniformStyling() before calling.

Since: **27.0**

Returns: *boolean*

<HorizontalLine />

### getFauxBold

Get faux bold. Throws if isUniformStyling() is false (mixed styling); check isUniformStyling() before calling.

Since: **27.0**

Returns: *boolean*

<HorizontalLine />

### getFauxItalic

Get faux italic. Throws if isUniformStyling() is false (mixed styling); check isUniformStyling() before calling.

Since: **27.0**

Returns: *boolean*

<HorizontalLine />

### getFontName

Get font name. Throws if isUniformStyling() is false (mixed styling); check isUniformStyling() before calling.

Since: **27.0**

Returns: *string*

<HorizontalLine />

### getFontSize

Get font size. Throws if isUniformStyling() is false (mixed styling); check isUniformStyling() before calling.

Since: **27.0**

Returns: *number*

<HorizontalLine />

### getSmallCaps

Get small caps. Throws if isUniformStyling() is false (mixed styling); check isUniformStyling() before calling.

Since: **27.0**

Returns: *boolean*

<HorizontalLine />

### getText

Get the text content.

Since: **27.0**

Returns: *string*

<HorizontalLine />

### isFauxStylesEditable

Returns whether faux styles can be edited for this text parameter. Returns true for user-constructed instances (no author restrictions apply).

Since: **27.0**

Returns: *boolean*

<HorizontalLine />

### isFontNameEditable

Returns whether the font name can be edited for this text parameter. Returns true for user-constructed instances (no author restrictions apply).

Since: **27.0**

Returns: *boolean*

<HorizontalLine />

### isFontSizeEditable

Returns whether the font size can be edited for this text parameter. Returns true for user-constructed instances (no author restrictions apply).

Since: **27.0**

Returns: *boolean*

<HorizontalLine />

### isUniformStyling

Returns true when all text shares a single uniform style (exactly one text run).

Since: **27.0**

Returns: *boolean*

<HorizontalLine />

### setAllCaps

Set all caps across all runs. Throws if isFauxStylesEditable() is false.

Since: **27.0**

Returns: *boolean*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| inAllCaps | *boolean* | - |

<HorizontalLine />

### setFauxBold

Set faux bold across all runs. Throws if isFauxStylesEditable() is false.

Since: **27.0**

Returns: *boolean*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| inFauxBold | *boolean* | - |

<HorizontalLine />

### setFauxItalic

Set faux italic across all runs. Throws if isFauxStylesEditable() is false.

Since: **27.0**

Returns: *boolean*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| inFauxItalic | *boolean* | - |

<HorizontalLine />

### setFontName

Set font name across all runs. Throws if isFontNameEditable() is false.

Since: **27.0**

Returns: *boolean*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| inFontName | *string* | - |

<HorizontalLine />

### setFontSize

Set font size across all runs. Throws if isFontSizeEditable() is false.

Since: **27.0**

Returns: *boolean*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| inFontSize | *number* | - |

<HorizontalLine />

### setSmallCaps

Set small caps across all runs. Throws if isFauxStylesEditable() is false. 

Since: **27.0**

Returns: *boolean*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| inSmallCaps | *boolean* | - |

<HorizontalLine />

### setText

Set the text content. Collapses any multi-run styling to a single run.

Since: **27.0**

Returns: *boolean*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| inText | *string* | - |

<HorizontalLine />
