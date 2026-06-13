---
title: File
description: A file on a file system. Read its contents or write new data, as text or binary.
---

# File

A `File` is your handle to a single file on disk. You use it to read the file's
contents or to write new data. You do not create a `File` yourself. You get one
back from a
[FileSystemProvider](../../../modules/uxp/persistent-file-storage/file-system-provider.md)
(reached through `localFileSystem`), usually from a picker like
`getFileForOpening` or `getFileForSaving`, or from a folder's `getEntry`. The
`File` class needs no `require()`, but `localFileSystem` does.

**Example**

```js
const fs = require('uxp').storage.localFileSystem;
const file = await fs.getFileForOpening();
console.log(file.isFile); // true
```

## Permissions

Reading and writing files requires the `localFileSystem` permission in your
plugin's `manifest.json` (Manifest v5+). Use `"request"` for picker-based
access, `"plugin"` for the plugin's own storage, or `"fullAccess"` for
unrestricted access (the user consents at install time).

```json
{
  "requiredPermissions": {
    "localFileSystem": "request"
  }
}
```

## isFile

Indicates that this instance is a file. Always `true` on a `File`. Useful for
narrowing an [Entry](../../../modules/uxp/persistent-file-storage/entry.md) to
its concrete type.

**Example**

```js
if (anEntry.isFile) {
    await anEntry.read();
}
```

## mode : `Symbol`

Indicates whether this file is read-only or read-write. Compare against
[readOnly](../../../modules/uxp/persistent-file-storage/modes.md#readonly--symbol)
and [readWrite](../../../modules/uxp/persistent-file-storage/modes.md#readwrite--symbol).
A file opened through `getFileForOpening` is read-only; one from
`getFileForSaving` is read-write.

<InlineAlert variant="info" slots="text"/>

Only `File` exposes a `mode`. [Folder](../../../modules/uxp/persistent-file-storage/folder.md)
has no equivalent, so you cannot tell in advance whether a folder is writable.
The first write throws if it is not.

**Example**

```js
const { modes } = require('uxp').storage;
if (aFile.mode === modes.readOnly) {
    throw new Error("Can't write to a file opened as read-only.");
}
```

## read(options)

Reads data from the file and returns it. Specify the encoding with the `format`
option; without it, the file is read as UTF-8 text.

**Returns**: `Promise<string | ArrayBuffer>` - the contents of the file.

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| options | `any` |  |  |
| [options.format] | `Symbol` | `formats.utf8` | the format of the file; see [utf8](../../../modules/uxp/persistent-file-storage/formats.md#utf8--symbol) and [binary](../../../modules/uxp/persistent-file-storage/formats.md#binary--symbol). |

<InlineAlert variant="warning" slots="text"/>

Always wrap `read` and `write` in `try/catch`. In some async flows UXP can stop
on an internal file-system error without rejecting the returned `Promise`, so
relying on rejection alone can hide failures.

**Example**

```js
const text = await myNovel.read();
```

**Example**

```js
const { formats } = require('uxp').storage;
const data = await myNovel.read({ format: formats.binary });
```

## write(data, options)

Writes data to the file, appending if requested. The `format` option controls
the encoding and defaults to UTF-8.

**Returns**: `Promise<number>` - the number of bytes written.

**Throws**:

- `FileIsReadOnly` if writing to a read-only file
- `OutOfSpace` if the write would exceed the available space (or quota)

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| data | `string` \| `ArrayBuffer` |  | the data to write to the file |
| options | `any` |  |  |
| [options.format] | `Symbol` | `formats.utf8` | the format of the file; see [utf8](../../../modules/uxp/persistent-file-storage/formats.md#utf8--symbol) and [binary](../../../modules/uxp/persistent-file-storage/formats.md#binary--symbol). |
| [options.append] | `boolean` | `false` | if `true`, the data is appended to the end of the file |

**Example**

```js
await myNovel.write("It was a dark and stormy night.\n");
await myNovel.write("Cliches and tropes aside, it really was.", { append: true });
```

**Example**

```js
const { formats } = require('uxp').storage;
const data = new ArrayBuffer(8);
await aDataFile.write(data, { format: formats.binary });
```

## isFile(entry)

Static helper that determines whether an arbitrary value is a file. Safe to call
even if `entry` is `null` or `undefined`.

**Returns**: `boolean` - if `true`, the entry is a file.

| Param | Type | Description |
| --- | --- | --- |
| entry | `any` | the entry to check |

<InlineAlert variant="info" slots="text"/>

This page documents two different `isFile` members: the instance **property**
above (`aFile.isFile`) and this **static** helper (`File.isFile(value)`) that
takes any value. Use the property when you already have an `Entry`, and the
static helper when the value's type is unknown.

**Example**

```js
if (File.isFile(anEntry)) {
    await anEntry.read();
}
```
