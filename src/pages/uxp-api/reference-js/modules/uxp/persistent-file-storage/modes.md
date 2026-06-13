---
title: require('uxp').storage.modes
description: The file open modes, read-only or read-write, reported by File.mode.
---

# require('uxp').storage.modes

`modes` describes how a file was opened: read-only or read-write. A
[File](../../../modules/uxp/persistent-file-storage/file.md) reports its mode
through its [mode](../../../modules/uxp/persistent-file-storage/file.md#mode--symbol)
property. A file from `getFileForOpening` is read-only; a file from
`getFileForSaving` is read-write.

**Example**

```js
const { modes } = require('uxp').storage;
const file = await fs.getFileForOpening();
if (file.mode === modes.readOnly) {
    throw new Error("Can't write to a file opened as read-only.");
}
```

## modes()

The namespace of file open modes.

## readOnly : `Symbol`

The file is read-only. Attempts to write fail.

## readWrite : `Symbol`

The file is read-write.
