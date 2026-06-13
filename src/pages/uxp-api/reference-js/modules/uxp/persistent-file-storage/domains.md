---
title: require('uxp').storage.domains
description: Well-known starting locations for file and folder pickers, such as the user's documents.
---

# require('uxp').storage.domains

`domains` lists common locations a picker can start in. Pass one as the
`initialDomain` option to [getFileForOpening](../../../modules/uxp/persistent-file-storage/file-system-provider.md#getfileforopeningoptions),
[getFileForSaving](../../../modules/uxp/persistent-file-storage/file-system-provider.md#getfileforsavingsuggestedname-options),
or [getFolder](../../../modules/uxp/persistent-file-storage/file-system-provider.md#getfolderoptions).
Not every provider supports every domain; check
[supportedDomains](../../../modules/uxp/persistent-file-storage/file-system-provider.md#supporteddomains--arraysymbol)
before relying on one.

**Example**

```js
const { domains } = require('uxp').storage;
const folder = await fs.getFolder({ initialDomain: domains.userDocuments });
```

## domains()

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

Local application data.

## appLocalLibrary : `Symbol`

Local application library.

## appLocalCache : `Symbol`

Local application cache directory. Persistence is not guaranteed.

## appLocalShared : `Symbol`

Local application shared data folder.

## appLocalTemporary : `Symbol`

Local temporary directory.

## appRoamingData : `Symbol`

Roaming application data.

## appRoamingLibrary : `Symbol`

Roaming application library data.
