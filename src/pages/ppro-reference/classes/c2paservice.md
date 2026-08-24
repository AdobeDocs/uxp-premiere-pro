---
description: Overview of C2PAService
id: c2paservice
title: C2PAService
sidebar_label: C2PAService
repo: uxp-premierepro
product: premierepro
keywords: 
---

# C2PAService

Since: **26.5**

## Static Methods

### getManifest

Returns an object with 'manifest' (JSON string) and 'manifestLocation' (number) indicating where the C2PA manifest was found. Location flags: NONE (0), EMBEDDED (1), SIDE_CAR (2), CLOUD (4). If withValidation is true, the file will be validated during processing.

Since: **26.5**

Returns: *\{ manifest: string, manifestLocation: [Constants.C2PAManifestLocation](../constants/index.md#c2pamanifestlocation) }*

#### Parameters

| Name | Type | Description |
| :----| :--- | :---------- |
| filePath | *string* | - |
| withValidation | *boolean* | - |

<HorizontalLine />
