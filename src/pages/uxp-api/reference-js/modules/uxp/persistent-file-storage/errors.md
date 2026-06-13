---
title: require('uxp').storage.errors
description: The error types thrown by file system operations, and what each one means.
---

# require('uxp').storage.errors

`errors` lists the error types that file system operations can throw. Wrap file
calls in `try/catch` and check the error to recover or to show the user a clear
message. The most common ones in day-to-day plugin code are
`PermissionDeniedError`, `EntryExistsError`, `FileIsReadOnlyError`, and
`OutOfSpaceError`.

**Example**

```js
const { errors } = require('uxp').storage;
try {
    await folder.createFile("report.txt");
} catch (err) {
    if (err instanceof errors.EntryExistsError) {
        // file already exists; retry with overwrite or pick a new name
    } else {
        throw err;
    }
}
```

## AbstractMethodInvocationError

An abstract method was invoked.

## ProviderMismatchError

An operation required every entry to belong to the same provider, but they did
not.

## EntryIsNotAnEntryError

The value passed as an entry is not an `Entry`.

## EntryIsNotAFolderError

The entry was expected to be a folder, but is not.

## EntryIsNotAFileError

The entry was expected to be a file, but is not.

## NotAFileSystemError

The value was expected to be a file system, but is not.

## OutOfSpaceError

The file system is out of space, or the quota has been exceeded.

## PermissionDeniedError

The file system denied permission to complete the action.

## EntryExistsError

An entry would be overwritten, but `overwrite: true` was not set.

## FileIsReadOnlyError

An attempt was made to write to a file that was opened read-only.

## DomainNotSupportedError

The domain is not supported by the current provider.

## InvalidFileNameError

The file name contains invalid characters.

## InvalidFileFormatError

The format type is not supported.

## DataFileFormatMismatchError

The data does not match the requested format.
