---
title: require('uxp').storage.domains
description: Well-known starting locations for file and folder pickers, such as the user's documents.
---

# require('uxp').storage.domains

`domains` lists common locations a picker can start in. Pass one as the
`initialDomain` option to [getFileForOpening](../../../modules/uxp/persistent-file-storage/file-system-provider.md#getfileforopeningoptions),
[getFileForSaving](../../../modules/uxp/persistent-file-storage/file-system-provider.md#getfileforsavingsuggestedname-options),
or [getFolder](../../../modules/uxp/persistent-file-storage/file-system-provider.md#getfolderoptions).
`initialDomain` sets the preferred starting location. When you omit it, the
picker opens at the most recently used domain. Not every provider supports every
domain, so check
[supportedDomains](../../../modules/uxp/persistent-file-storage/file-system-provider.md#supporteddomains--arraysymbol)
before relying on one.

**Example**

```js
const { localFileSystem: fs, domains } = require('uxp').storage;
const folder = await fs.getFolder({ initialDomain: domains.userDocuments });
if (!folder) {
    return; // picker was cancelled
}
```

## domains

The namespace of common picker locations.

## userDesktop : `Symbol`

The user's desktop folder.

## userDocuments : `Symbol`

The user's documents folder.

## userPictures : `Symbol`

The user's pictures folder or library.

## userVideos : `Symbol`

The user's videos or movies folder or library.

## userMusic : `Symbol`

The user's music folder or library.

## appLocalData : `Symbol`

The application's local data folder.

## appLocalLibrary : `Symbol`

The application's local library folder.

## appLocalCache : `Symbol`

The application's local cache folder.

Persistence is not guaranteed.

## appLocalShared : `Symbol`

The application's local shared-data folder.

## appLocalTemporary : `Symbol`

The application's local temporary folder.

## appRoamingData : `Symbol`

The application's roaming data folder.

## appRoamingLibrary : `Symbol`

The application's roaming library folder.
