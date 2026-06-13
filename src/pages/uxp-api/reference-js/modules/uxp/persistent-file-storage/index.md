---
title: Persistent File Storage
description: Read and write files and folders from a UXP plugin, through pickers or the plugin's own storage.
---

# Persistent File Storage

Persistent File Storage is how a UXP plugin reads and writes files. You reach the
file system through `localFileSystem`, get files and folders from a picker or from
the plugin's own storage, and work with them through `File` and `Folder` entries.
All access requires the `localFileSystem` permission in your manifest.

## Classes

* [localFileSystem](../../../modules/uxp/persistent-file-storage/local-file-system.md). The entry point. Opens pickers, reaches plugin storage, and creates tokens for host APIs.
* [FileSystemProvider](../../../modules/uxp/persistent-file-storage/file-system-provider.md). The full method reference behind `localFileSystem`.
* [Entry](../../../modules/uxp/persistent-file-storage/entry.md). The base class shared by `File` and `Folder`.
* [EntryMetadata](../../../modules/uxp/persistent-file-storage/entry-metadata.md). Size, dates, and type for an entry.
* [File](../../../modules/uxp/persistent-file-storage/file.md). Reads from and writes to a file.
* [Folder](../../../modules/uxp/persistent-file-storage/folder.md). Lists, creates, and renames entries in a directory.

## Constants

* [domains](../../../modules/uxp/persistent-file-storage/domains.md). Well-known picker locations, such as the user's documents.
* [types](../../../modules/uxp/persistent-file-storage/types.md). File or folder, used by create calls.
* [formats](../../../modules/uxp/persistent-file-storage/formats.md). Text or binary, used by read and write.
* [modes](../../../modules/uxp/persistent-file-storage/modes.md). Read-only or read-write.
* [fileTypes](../../../modules/uxp/persistent-file-storage/file-types.md). Common file-extension groups for pickers.
* [errors](../../../modules/uxp/persistent-file-storage/errors.md). The error types thrown by file operations.
