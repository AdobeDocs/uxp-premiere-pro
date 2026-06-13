---
title: require('uxp').storage.types
description: The entry kinds, file or folder, used when creating entries.
---

# require('uxp').storage.types

`types` describes the kind of entry to create. Pass one of these as the `type`
option to [createEntry](../../../modules/uxp/persistent-file-storage/folder.md#createentryname-options)
or [createEntryWithUrl](../../../modules/uxp/persistent-file-storage/file-system-provider.md#createentrywithurlurl-options).
The default is `types.file`.

**Example**

```js
const { types } = require('uxp').storage;
const catImages = await folder.createEntry("cats", { type: types.folder });
```

## types()

The namespace of entry kinds.

## file : `Symbol`

A file. This is the default when creating an entry.

## folder : `Symbol`

A folder.
