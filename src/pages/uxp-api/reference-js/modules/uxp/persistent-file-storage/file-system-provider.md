---
title: require('uxp').storage.localFileSystem
description: The entry point to the file system. Open pickers, reach plugin storage, and turn entries into tokens for host APIs.
---

# require('uxp').storage.localFileSystem

`localFileSystem` is the single `FileSystemProvider` that UXP gives every plugin.
It is how you reach the file system: show open and save pickers, get the plugin's
own data and temporary folders, resolve URLs to entries, and create tokens that
host applications understand. You do not construct it. Require it and use the
instance UXP already created for you.

These APIs require UXP Manifest version v5 or later.

```js
const fs = require('uxp').storage.localFileSystem;
```

## Permissions

File system access requires the `localFileSystem` permission in your plugin's
`manifest.json`. Use `"request"` to open pickers, `"plugin"` to reach only the
plugin's own storage, or `"fullAccess"` for broad access that the user consents
to at install time.

```json
{
  "requiredPermissions": {
    "localFileSystem": "request"
  }
}
```

## isFileSystemProvider : `boolean`

Indicates that this object is a `FileSystemProvider`. Always `true` on
`localFileSystem`. Useful for type checking.

## supportedDomains : `Array<Symbol>`

The [domains](../../../modules/uxp/persistent-file-storage/domains.md) this
provider can open a picker to. For example, if the provider can show a picker in
the user's documents folder, [userDocuments](../../../modules/uxp/persistent-file-storage/domains.md#module-storage-domains-userdocuments)
appears in this list.

**Example**

```js
const { domains } = require('uxp').storage;
if (fs.supportedDomains.includes(domains.userDocuments)) {
    console.log("We can open a picker to the user's documents.");
}
```

## getFileForOpening(options)

Shows an open picker and returns the selected file or files. Files returned this
way are read-only. Set `allowMultiple` to `true` to return an array.

**Returns**: `Promise<File | Array<File>>` - the selected file, or an array when
`allowMultiple` is `true`. Resolves empty when the user selects nothing.

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| options | `*` |  |  |
| [options.initialDomain] | `Symbol` |  | the preferred starting location of the picker. Defaults to the most recently used domain. |
| [options.types] | `Array<string>` | `['.*']` | the file types the picker shows. |
| [options.initialLocation] | `File` \| `Folder` |  | a file or folder to start the picker at. A file starts the picker in its parent folder. Overrides `initialDomain`. |
| [options.allowMultiple] | `boolean` | `false` | if `true`, the user can select multiple files. |

**Example**

```js
const { domains } = require('uxp').storage;
const folder = await fs.getFolder({ initialDomain: domains.userDocuments });
const file = await fs.getFileForOpening({ initialLocation: folder });
if (!file) {
    return; // no file selected
}
const text = await file.read();
```

**Example**

```js
const { fileTypes } = require('uxp').storage;
const files = await fs.getFileForOpening({ allowMultiple: true, types: fileTypes.images });
if (files.length === 0) {
    return; // no files selected
}
```

## getFileForSaving(suggestedName, options)

Shows a save picker and returns a read-write file at the chosen location. If
saving would overwrite an existing file, the picker asks the user to confirm
before returning.

**Returns**: `Promise<File>` - the selected file, or `null` if the user cancels.

| Param | Type | Description |
| --- | --- | --- |
| suggestedName | `string` | the default file name. Required when `options.types` is not set. |
| options | `Object` |  |
| [options.initialDomain] | `Symbol` | the preferred starting location of the picker. Defaults to the most recently used domain. |
| [options.types] | `Array<string>` | allowed file extensions, with no leading dot. |

**Example**

```js
const file = await fs.getFileForSaving("output.txt", { types: ["txt"] });
if (!file) {
    return; // picker was cancelled
}
await file.write("It was a dark and stormy night.");
```

## getFolder(options)

Shows a folder picker and returns the chosen folder. Its contents are read-write
and can be listed with [Folder.getEntries](../../../modules/uxp/persistent-file-storage/folder.md#getentries).
Returns `null` if the user dismisses the picker.

**Returns**: `Promise<Folder | null>` - the selected folder, or `null`.

| Param | Type | Description |
| --- | --- | --- |
| options | `any` |  |
| [options.initialDomain] | `Symbol` | the preferred starting location of the picker. Defaults to the most recently used domain. |

**Example**

```js
const folder = await fs.getFolder();
if (!folder) {
    return; // picker was cancelled
}
const entries = await folder.getEntries();
const myNovel = entries.find(entry => entry.name.includes("novel"));
const text = await myNovel.read();
```

## getTemporaryFolder()

Returns a temporary folder for the plugin. UXP clears its contents when the
plugin is disposed, so do not use it for anything you need to keep.

**Returns**: `Promise<Folder>`

**Example**

```js
const temp = await fs.getTemporaryFolder();
```

## getDataFolder()

Returns the plugin's persistent data folder. No user interaction is needed, and
the folder survives host-app version upgrades. This is the right place for
settings and other data the plugin owns.

**Returns**: `Promise<Folder>`

**Example**

```js
const dataFolder = await fs.getDataFolder();
```

## getPluginFolder()

Returns the plugin's own packaged folder. This folder and everything in it are
read-only, and contain the assets you shipped with the plugin.

**Returns**: `Promise<Folder>`

**Example**

```js
const pluginFolder = await fs.getPluginFolder();
```

## createEntryWithUrl(url, options)

Creates an entry at the given URL and returns it. Use a `plugin-temp:`,
`plugin-data:`, or `file:` URL. By default it creates a file. Pass
`types.folder` to create a folder.

**Returns**: `Promise<File | Folder>` - the created file or folder.

**Throws**:

- `Error` if the URL format or value is invalid
- `Error` if the parent folder does not exist
- `Error` if a folder already exists at the URL
- `Error` if a file exists at the URL and a folder was requested
- `Error` if a file exists at the URL and `overwrite` is not `true`

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| url | `string` |  | the URL to create an entry for. The `file:` scheme has limited support on Windows (UWP) due to strict [file access permissions](https://learn.microsoft.com/en-us/windows/uwp/files/file-access-permissions). |
| options | `*` |  |  |
| [options.type] | `Symbol` | `types.file` | the kind of entry to create. Pass `types.folder` to create a folder. A file entry is not written to disk until you call `write` on it. |
| [options.overwrite] | `Boolean` | `false` | if `true`, the create attempt can overwrite an existing file. |

**Example**

```js
const { types } = require('uxp').storage;
const newImgFolder = await fs.createEntryWithUrl("plugin-temp:/img", { type: types.folder });
```

**Example**

```js
const newDatFile = await fs.createEntryWithUrl("plugin-temp:/tmp/test.dat", { overwrite: true });
```

## getEntryWithUrl(url)

Resolves an existing entry at the given URL and returns it.

**Returns**: `Promise<File | Folder>` - the file or folder at the URL.

**Throws**:

- `Error` if the URL format or value is invalid
- `Error` if no file or folder exists at the URL

| Param | Type | Description |
| --- | --- | --- |
| url | `string` | the URL to resolve. The `file:` scheme has limited support on Windows (UWP) due to strict [file access permissions](https://learn.microsoft.com/en-us/windows/uwp/files/file-access-permissions). |

<InlineAlert variant="warning" slots="text"/>

On Windows, resolving a path that ends with a trailing backslash can fail. Strip
the trailing `\` from a path before you build the URL.

**Example**

```js
const tmpFolder = await fs.getEntryWithUrl("plugin-temp:/tmp");
const tmpFile = await fs.getEntryWithUrl("plugin-temp:/tmp/test.dat");
```

## getFsUrl(entry)

Returns the file system URL for an entry.

**Returns**: `string` - the `fs` URL of the entry.

| Param | Type |
| --- | --- |
| entry | `Entry` |

## getNativePath(entry)

Returns the platform-native file system path for an entry.

**Returns**: `string` - the native path of the entry.

| Param | Type |
| --- | --- |
| entry | `Entry` |

## createSessionToken(entry)

Returns a token for an entry that some host APIs accept in place of a path, such
as Photoshop's `batchPlay`. The token is valid only for the current plugin
session, so do not store it. A stored session token is useless on the next run.

**Returns**: `string` - the session token for the entry.

| Param | Type |
| --- | --- |
| entry | `Entry` |

<InlineAlert variant="info" slots="text"/>

When you call the Photoshop DOM API, pass the file entry itself, not a session
token. Photoshop converts the entry to a token for you.

**Example (Photoshop host)**

```js
const fs = require('uxp').storage.localFileSystem;
const entry = await fs.getFileForOpening();
const token = fs.createSessionToken(entry);
await require('photoshop').action.batchPlay([{
    _obj: "open",
    target: {
        _path: token, // a session token, not a system path
        _kind: "local",
    },
}], {});
```

## getEntryForSessionToken(token)

Returns the entry for a session token created with `createSessionToken`. Throws a
`ReferenceError` if no entry matches the token.

**Returns**: `Entry` - the entry for the token.

| Param | Type |
| --- | --- |
| token | `string` |

## createPersistentToken(entry)

Returns a token you can store to keep access to an entry across sessions. This
lets you ask for permission once and reuse the entry later. A persistent token is
not guaranteed to last forever. Moving the file, changing permissions, or
OS-specific limits can invalidate it, and you find out when you try to use it.

**Returns**: `Promise<string>` - the persistent token for the entry.

| Param | Type |
| --- | --- |
| entry | `Entry` |

**Example**

```js
const fs = require('uxp').storage.localFileSystem;
const entry = await fs.getFileForOpening();
const token = await fs.createPersistentToken(entry);
localStorage.setItem("persistent-file", token);
```

## getEntryForPersistentToken(token)

Returns the entry for a persistent token created with `createPersistentToken`.
Throws a `ReferenceError` if no entry matches the token.

**Returns**: `Promise<Entry>` - the entry for the token.

| Param | Type |
| --- | --- |
| token | `string` |

<InlineAlert variant="warning" slots="text"/>

A persistent token can resolve to an entry that no longer works. The file may be
gone, or its permissions may have changed. Handle the error, then ask the user to
pick the entry again and store the new token.

**Example**

```js
const fs = require('uxp').storage.localFileSystem;
let entry, contents, tries = 3, success = false;
while (tries > 0) {
    try {
        entry = await fs.getEntryForPersistentToken(localStorage.getItem("persistent-file"));
        contents = await entry.read();
        tries = 0;
        success = true;
    } catch (err) {
        entry = await fs.getFileForOpening();
        localStorage.setItem("persistent-file", await fs.createPersistentToken(entry));
        tries--;
    }
}
if (!success) {
    // fail gracefully
}
```

## isFileSystemProvider(fs)

Static helper that checks whether a value is a `FileSystemProvider`. Safe to call
even if the value is `null` or `undefined`. Useful for type checking.

**Returns**: `boolean` - if `true`, the value is a file system provider.

| Param | Type | Description |
| --- | --- | --- |
| fs | `any` | the value to check |
