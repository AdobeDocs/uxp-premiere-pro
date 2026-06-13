---
title: Entry
description: The base class for File and Folder. Defines the shared name, path, copy, move, and delete behavior.
---

# Entry

`Entry` is the base class that [File](../../../modules/uxp/persistent-file-storage/file.md)
and [Folder](../../../modules/uxp/persistent-file-storage/folder.md) share. Any
entry you work with is really a `File` or a `Folder`. `Entry` is where their
common members live: the name, the path, and operations like copy, move, and
delete. You get entries from `localFileSystem`, for example through a folder's
`getEntry`.

**Example**

```js
// Entry can't be constructed directly; obtain a File or Folder, which IS an Entry
const fs = require('uxp').storage.localFileSystem;
const folder = await fs.getPluginFolder(); // a Folder, which is an Entry
const entry = await folder.getEntry("entryName.txt");
console.log(entry.isEntry); // true
```

## Permissions

Accessing the file system requires the `localFileSystem` permission in your
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

## isEntry : `boolean`

Indicates that this instance is an `Entry`. Always `true`. Useful for type
checking.

**Example**

```js
if (something.isEntry) {
    return something.getMetadata();
}
```

## isFile : `boolean`

**Read only.** Indicates whether this instance is a [File](../../../modules/uxp/persistent-file-storage/file.md).
Useful for narrowing an `Entry` to its concrete type.

**Example**

```js
if (anEntry.isFile) {
    const contents = await anEntry.read();
}
```

## isFolder : `boolean`

**Read only.** Indicates whether this instance is a [Folder](../../../modules/uxp/persistent-file-storage/folder.md).
Useful for narrowing an `Entry` to its concrete type.

**Example**

```js
if (anEntry.isFolder) {
    const entries = await anEntry.getEntries();
}
```

## name : `string`

**Read only.** The name of this entry.

**Example**

```js
console.log(anEntry.name);
```

## provider : `FileSystemProvider`

**Read only.** The [FileSystemProvider](../../../modules/uxp/persistent-file-storage/file-system-provider.md)
that services this entry.

**Example**

```js
if (entryOne.provider !== entryTwo.provider) {
    throw new Error("Providers are not the same");
}
```

## url : `string`

**Read only.** The URL of this entry. You can pass this URL to other parts of
the extension system. For example, use it as the `src` of an image widget in
your UI.

**Example**

```js
console.log(anEntry.url);
```

## nativePath : `string`

**Read only.** The platform-native file-system path of this entry.

<InlineAlert variant="warning" slots="text"/>

`nativePath` is not safe to compare or concatenate across platforms. macOS and
Windows differ in slash direction (`/` vs `\`) and in whether a trailing slash
is present, and the result can even differ between `getFolder`, `createFolder`,
and `getEntry` on the same OS. Normalize paths before comparing, and prefer the
`Entry` APIs over string path manipulation.

**Example**

```js
console.log(anEntry.nativePath);
```

## toString()

Returns the entry's details (name, type, and native path) as a readable string.

**Returns**: `string`

**Example**

```js
console.log(anEntry.toString());
```

## copyTo(folder, options)

Copies this entry to the specified `folder`.

**Returns**: `Promise<File | Folder>`

**Throws**:

- `EntryExists` if the attempt would overwrite an entry and `overwrite` is `false`
- `PermissionDenied` if the underlying file system rejects the attempt
- `OutOfSpace` if the file system is out of storage space

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| folder | `Folder` |  | the folder to which to copy this entry |
| options | `*` |  |  |
| [options.overwrite] | `boolean` | `false` | if `true`, allows overwriting existing entries |
| [options.allowFolderCopy] | `boolean` | `false` | if `true`, allows copying a folder (and its contents) |

<InlineAlert variant="warning" slots="text"/>

Copying a folder requires `allowFolderCopy: true`. Without it, a folder copy
fails even when `overwrite` is set.

**Example**

```js
await someFile.copyTo(someFolder);
```

**Example**

```js
await someFile.copyTo(someFolder, { overwrite: true });
```

**Example**

```js
await someFolder.copyTo(anotherFolder, { overwrite: true, allowFolderCopy: true });
```

## moveTo(folder, options)

Moves this entry to the target folder, optionally renaming it.

**Returns**: `Promise<void>`

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| folder | `Folder` |  | the folder to which to move this entry |
| options | `*` |  |  |
| [options.overwrite] | `boolean` | `false` | if `true`, allows the move to overwrite existing entries |
| [options.newName] | `string` |  | if specified, the entry is renamed to this name |

**Example**

```js
await someFile.moveTo(someFolder);
```

**Example**

```js
await someFile.moveTo(someFolder, { overwrite: true });
```

**Example**

```js
await someFile.moveTo(someFolder, { newName: 'masterpiece.txt' });
```

**Example**

```js
await someFile.moveTo(someFolder, { newName: 'novel.txt', overwrite: true });
```

## delete()

Removes this entry from the file system. A folder must be empty before it can be
deleted.

**Returns**: `Promise<number>` - `0` on success; otherwise an error is thrown.

<InlineAlert variant="warning" slots="text"/>

Deleting a folder that was selected from a storage picker or added via
drag-and-drop currently fails with a permission-denied error. Delete such
content via its contents rather than the picked folder itself.

**Example**

```js
await aFile.delete();
```

## getMetadata()

Returns this entry's metadata.

**Returns**: `Promise<EntryMetadata>` - see [EntryMetadata](../../../modules/uxp/persistent-file-storage/entry-metadata.md).

**Example**

```js
const metadata = await aFile.getMetadata();
console.log(metadata.size);
```
