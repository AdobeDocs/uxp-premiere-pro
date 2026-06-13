---
title: require('uxp').storage.fileTypes
description: Ready-made file-extension groups for the types option of open and save pickers.
---

# require('uxp').storage.fileTypes

`fileTypes` provides ready-made groups of file extensions for picker methods.
Pass one as the `types` option to
[getFileForOpening](../../../modules/uxp/persistent-file-storage/file-system-provider.md#getfileforopeningoptions)
to limit what the user can select.

**Example**

```js
const { fileTypes } = require('uxp').storage;
const files = await fs.getFileForOpening({ allowMultiple: true, types: fileTypes.images });
```

## fileTypes()

The namespace of file-extension groups.

## text : `Array<string>`

Common text file extensions.

## images : `Array<string>`

Common image file extensions.

## all : `Array<string>`

All file types. This is the default when no `types` option is given.
