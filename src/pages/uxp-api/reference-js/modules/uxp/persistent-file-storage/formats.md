---
title: require('uxp').storage.formats
description: The content formats, UTF-8 text or binary, used by File read and write.
---

# require('uxp').storage.formats

`formats` describes how file content is encoded. Pass one of these as the
`format` option to [File.read](../../../modules/uxp/persistent-file-storage/file.md#readoptions)
or [File.write](../../../modules/uxp/persistent-file-storage/file.md#writedata-options).
The default is `formats.utf8`, so you only need to set it for binary data.

**Example**

```js
const { formats } = require('uxp').storage;
const bytes = await file.read({ format: formats.binary });
```

## formats()

The namespace of content formats.

## utf8 : `Symbol`

UTF-8 text encoding. This is the default.

## binary : `Symbol`

Binary encoding. Use it to read or write an `ArrayBuffer`.
