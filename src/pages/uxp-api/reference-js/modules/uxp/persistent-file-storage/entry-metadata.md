---
title: EntryMetadata
description: Read-only details about an Entry, such as its size, name, and created and modified dates.
---

# EntryMetadata

`EntryMetadata` holds read-only details about an [Entry](../../../modules/uxp/persistent-file-storage/entry.md):

* `size` of the file (zero for a folder)
* `dateCreated`
* `dateModified`
* `name`
* whether the entry is a file or a folder

You do not construct `EntryMetadata`. Call [getMetadata](../../../modules/uxp/persistent-file-storage/entry.md#module-storage-entry-getmetadata)
on a `File` or `Folder` to get it.

**Example**

```js
const fs = require('uxp').storage.localFileSystem;
const folder = await fs.getPluginFolder();
const metadata = await folder.getMetadata();
console.log(metadata.name, metadata.dateModified);
```

## name : `string`

The name of the entry.

## size : `number`

The size of the entry in bytes if it is a file. Zero for a folder.

## dateCreated : `Date`

The date the entry was created.

## dateModified : `Date`

The date the entry was last modified.

## isFile : `boolean`

Indicates whether the entry is a file.

## isFolder : `boolean`

Indicates whether the entry is a folder.
