---
title: Folder
description: A directory in UXP's sandboxed file system. List its contents, create files and subfolders, and rename entries.
---

# Folder

A `Folder` points to a directory inside UXP's sandboxed file system. You use it to
list what the directory contains, create new files and subfolders, and rename or
fetch entries. You do not construct a `Folder` yourself. You get one from
`localFileSystem`, usually through
[getTemporaryFolder](../../../modules/uxp/persistent-file-storage/storage.md#gettemporaryfolder),
[getFolder](../../../modules/uxp/persistent-file-storage/storage.md#getfolderoptions),
`getDataFolder`, or another folder's [getEntries](../../../modules/uxp/persistent-file-storage/folder.md#getentries).
Its methods are asynchronous and return promises.

**Example**

```js
// Get a Folder instance via localFileSystem
const fs = require('uxp').storage.localFileSystem;
const folder = await fs.getTemporaryFolder();
console.log(folder.isFolder); // true
```

## Permissions

Accessing the file system requires the `localFileSystem` permission in your
plugin's `manifest.json`. Use `"request"` for picker-based access, `"plugin"`
for the plugin's own data and temporary folders, or `"fullAccess"` for
unrestricted access (the user consents at install time).

```json
{
  "requiredPermissions": {
    "localFileSystem": "request"
  }
}
```

## isFolder

Indicates that this instance is a folder. Always `true` on a `Folder`. Useful
for type checking against an [Entry](../../../modules/uxp/persistent-file-storage/entry.md)
whose concrete type you don't yet know.

**Example**

```js
if (anEntry.isFolder) {
    const entries = await anEntry.getEntries();
}
```

## getEntries()

Returns an array of the immediate children of this folder.

**Returns**: `Promise<Array<Entry>>` - the entries within the folder, each a
[File](../../../modules/uxp/persistent-file-storage/file.md) or `Folder`.

**Example**

```js
const entries = await aFolder.getEntries();
const allFiles = entries.filter(entry => entry.isFile);
```

## createEntry(name, options)

Creates an entry within this folder and returns it. By default it creates a
file. Pass `types.folder` to create a folder instead.

**Returns**: `Promise<File | Folder>` - the created entry.

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| name | `string` |  | the name of the entry to create |
| options | `any` |  |  |
| [options.type] | `Symbol` | `types.file` | the kind of entry to create. Pass `types.folder` to create a folder. |
| [options.overwrite] | `boolean` | `false` | if `true`, overwrite an existing entry of the same name |

<InlineAlert variant="warning" slots="text"/>

When `type` is `types.file` (the default), this only creates the in-memory file
entry. The file is not written to disk until you call `write` on the returned
`File`. When `type` is `types.folder`, the folder is created on disk right away.

**Example**

```js
const myNovel = await aFolder.createEntry("mynovel.txt");
```

**Example**

```js
const { types } = require('uxp').storage;
const catImageCollection = await aFolder.createEntry("cats", { type: types.folder });
```

## createFile(name, options)

Creates a `File` entry within this folder and returns it. This only creates the
entry object, not the file on disk; the file is created when you first call
`write` on the returned entry.

**Returns**: `Promise<File>` - the created file entry.

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| name | `string` |  | the name of the file to create |
| options | `any` |  |  |
| [options.overwrite] | `boolean` | `false` | if `true`, overwrite an existing file |

**Example**

```js
const myNovelTxtFile = await aFolder.createFile("mynovel.txt");
await myNovelTxtFile.write("Chapter 1");
```

## createFolder(name)

Creates a folder within this folder and returns it.

**Returns**: `Promise<Folder>` - the created folder entry.

| Param | Type | Description |
| --- | --- | --- |
| name | `string` | the name of the folder to create |

<InlineAlert variant="warning" slots="text"/>

Unlike `createFile`, `createFolder` writes to disk immediately and has no
`overwrite` option. It fails if a folder with that name already exists.

**Example**

```js
const myCollectionsFolder = await aFolder.createFolder("collections");
```

## getEntry(filePath)

Gets an existing entry from within this folder by name or relative path, and
returns the appropriate instance. Inspect `isFile` / `isFolder` on the result
to disambiguate.

**Returns**: `Promise<File | Folder>` - the fetched entry.

| Param | Type | Description |
| --- | --- | --- |
| filePath | `string` | the name or relative path of the entry to fetch |

**Example**

```js
const myNovel = await aFolder.getEntry("mynovel.txt");
if (myNovel.isFile) {
    await myNovel.read();
}
```

## renameEntry(entry, newName, options)

Renames an entry within this folder to a new name.

**Returns**: `Promise<void>`

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| entry | `Entry` |  | the entry to rename |
| newName | `string` |  | the new name to assign |
| options | `any` |  |  |
| [options.overwrite] | `boolean` | `false` | if `true`, renaming can overwrite an existing entry at `newName` |

**Example**

```js
const myNovel = await aFolder.getEntry("mynovel.txt");
await aFolder.renameEntry(myNovel, "myFantasticNovel.txt");
```

## isFolder ⇒ `boolean`

Static helper that checks whether an arbitrary value is a folder. Safe to call
when the value might be `null` or `undefined`. Useful for type checking.

**Returns**: `boolean` - if `true`, the entry is a folder.

| Param | Type | Description |
| --- | --- | --- |
| entry | `any` | the entry to check |

**Example**

```js
if (Folder.isFolder(anEntry)) {
    await anEntry.getEntries();
}
```

## Known issues

<InlineAlert variant="info" slots="text"/>

The `create*` and `getEntry` methods behave differently on purpose, which is
easy to trip over. `createFile` does not write to disk. `createFolder` does, and
has no `overwrite`. `createEntry` does one or the other depending on `type`.
`getEntry` only reads. The behavior is stable, so design around it.

<InlineAlert variant="warning" slots="text"/>

On Windows, `getEntry` can fail when the base folder path ends with a trailing
backslash. Strip the trailing `\` from constructed paths before calling.

<InlineAlert variant="info" slots="text"/>

A `Folder` has no `mode` property, so you cannot detect a read-only folder before
writing. `getFolder` can return a read-only folder without any error, and the
write throws later. Wrap the first write in `try/catch` and surface a permission
error to the user.
