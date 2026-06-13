---
title: require('uxp').storage.localFileSystem
description: The file system entry point for plugins. Use pickers, plugin storage, and tokens for host APIs.
---

# require('uxp').storage.localFileSystem

`localFileSystem` is the object a plugin uses to read and write files. It is the
one [FileSystemProvider](../../../modules/uxp/persistent-file-storage/file-system-provider.md)
instance that UXP creates for you. Require it once and reuse it.

```js
const fs = require('uxp').storage.localFileSystem;
```

There are two ways to reach files. Plugin storage needs no user interaction, and
user storage goes through a picker so the user grants access.

- **Plugin storage:** `getDataFolder`, `getTemporaryFolder`, and
  `getPluginFolder` return folders the plugin owns.
- **User storage:** `getFileForOpening`, `getFileForSaving`, and `getFolder`
  return entries the user picks.

To keep access to a user-picked entry across sessions, store a persistent token
from `createPersistentToken` and resolve it later with
`getEntryForPersistentToken`.

For the full list of methods and properties, see
[FileSystemProvider](../../../modules/uxp/persistent-file-storage/file-system-provider.md).

## Permissions

File system access requires the `localFileSystem` permission in your plugin's
`manifest.json` (Manifest v5 or later). Use `"request"` to open pickers,
`"plugin"` to reach only the plugin's own storage, or `"fullAccess"` for broad
access that the user consents to at install time.

```json
{
  "requiredPermissions": {
    "localFileSystem": "request"
  }
}
```

## Quick start

```js
const fs = require('uxp').storage.localFileSystem;

// Plugin-owned storage, no picker needed
const dataFolder = await fs.getDataFolder();
const settings = await dataFolder.createFile("settings.json", { overwrite: true });
await settings.write(JSON.stringify({ ready: true }));

// User storage, through a picker
const file = await fs.getFileForOpening();
if (file) {
    const text = await file.read();
}
```
