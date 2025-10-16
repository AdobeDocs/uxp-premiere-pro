---
title: Filesystem operations
description: Learn how to read, write, and manage files & folders in UXP plugins
keywords:
  - localFileSystem
  - FS API
  - fullAccess
  - file permissions
  - sandbox
contributors:
  - https://github.com/padmkris123
  - https://github.com/undavide
---

# Filesystem operations

UXP provides powerful APIs for reading, writing, creating, and deleting files. This guide will walk you through the concepts, permissions, and practical examples you need to work with the file system in your plugins.

## Prerequisites

Before you begin, make sure your development environment uses the following versions:

- **Premiere Pro v25.2** or higher
- **UDT v2.1.0** or higher
- **Manifest version v5** or higher

## Understand File System Access

### The Sandbox Model

UXP uses a security model that restricts file system access by default. This protected area is called the **sandbox**—a set of safe locations your plugin can access without additional permissions.

**In plugins**, the sandbox includes:

- **Plugin folder**: Your plugin's installation directory (read-only)
- **Data folder**: Persistent storage for your plugin's data
- **Temporary folder**: Transitory storage that may be cleared automatically

<InlineAlert variant="info" slots="text"/>

The Temporary folder is _transitory_ and may be cleared automatically; the Data folder is _persistent_ across app upgrades, but will be removed on uninstall or if the user clears it. Always **provide users with options to back up critical data** to locations of their choice.

While the sandbox is sufficient for many use cases, you may need to access other locations—such as the user's Documents folder or a specific project directory. UXP supports this through a **permission-based system**.

### File System Permissions

To access the file system, you must declare the `localFileSystem` permission in your plugin's `manifest.json` file.

<InlineAlert variant="info" slots="header, text1, text2"/>

Before you proceed

Make sure you understand how [Manifest permissions](../../../plugins/concepts/manifest/index.md#permissionsdefinition) work before implementing file operations in your plugin.

The detailed [`PermissionsDefinition` reference](../../../plugins/concepts/manifest/index.md#permissionsdefinition) explains all available permission options and their security implications.

The `localFileSystem` permission accepts three values:

- **`"plugin"`** (default): Provides access only to the sandbox locations
- **`"request"`**: Allows your plugin to request user permission via file picker dialogs
- **`"fullAccess"`**: Grants unrestricted access to the user's file system

Here's how to declare this permission in `manifest.json`:

```json
{
  // ...
  "requiredPermissions": {
    "localFileSystem": "plugin"
  }
}
```

<InlineAlert variant="info" slots="header, text1, text2"/>

Best practices for permissions

Choose the _most accurate_ permission level for your use case. In the future, users will be asked to provide explicit consent based on the permissions you request.

While `"fullAccess"` might seem like the easiest option, users may be uncomfortable granting full file system access unless it's absolutely necessary—and they might deny installation of your plugin altogether. Use `"request"` when you need access to user-specified files, and `"plugin"` when sandbox access is sufficient.

### URL Schemes

UXP provides convenient URL schemes as shortcuts to specific file system locations:

| Scheme          | Description                                | Permission Required |
| :-------------- | :----------------------------------------- | :------------------ |
| `plugin:/`      | Plugin installation folder (read-only)     | `"plugin"`          |
| `plugin-data:/` | Plugin data folder (read-write)            | `"plugin"`          |
| `plugin-temp:/` | Plugin temporary folder (read-write)       | `"plugin"`          |
| `file:/`        | Arbitrary file system location (full path) | `"fullAccess"`      |

You can use these schemes in both HTML and JavaScript:

```html
<img src="plugin:/icons/logo.png" />
<img src="file:/Users/user/Downloads/sample.png" /> <!-- update the path based on your system -->
```

```javascript
const dataFile = await localFileSystem.getEntryWithUrl("plugin-data:/settings.json");
```

## Choosing the Right API

UXP provides two APIs for file system operations, each suited to different use cases:

| API                 | Best For                             | Access Pattern    |
| :------------------ | :----------------------------------- | :---------------- |
| **LocalFileSystem** | Multiple operations on the same file | Object references |
| **FS Module**       | Single, direct file operations       | Path-based        |

### The `LocalFileSystem` API

The `LocalFileSystem` API is object-oriented and works with **Entry references**—objects that represent files and folders. This approach is ideal when you need to perform multiple operations on the same file or traverse directory structures.

**Access the API:**

```javascript
const { localFileSystem, types } = require('uxp').storage;
```

#### Understanding Entries

The file system contains two types of items: files and folders. UXP represents these with the `File` and `Folder` classes, both of which extend a base class called `Entry`.

Some methods return an `Entry` because the type can only be determined at runtime. You should check the entry type before performing type-specific operations:

```javascript
const { localFileSystem, types } = require('uxp').storage;

async function createFileInFolder() {
    try {
        // Create a folder entry
        const folderEntry = await localFileSystem.createEntryWithUrl(
            "plugin-temp:/myFolder",
            { type: types.folder }
        );

        // Verify it's a folder before using folder-specific methods
        if (folderEntry.isFolder) {
            const newFile = await folderEntry.createFile("data.txt", { overwrite: true });
            await newFile.write("This is sample content.");
            console.log(`File created at: ${newFile.nativePath}`);
        }
    } catch (e) {
        console.error("Failed to create file:", e);
    }
}
```

### The `fs` module

The `fs` module provides a path-based API similar to [Node.js file system operations](https://nodejs.org/api/fs.html). It's ideal for straightforward, single-operation tasks like reading a configuration file or writing output.

**Access the API:**

```javascript
const fs = require("fs");
```

Now let's explore practical examples for different permission levels.

## Working with LocalFileSystem

### Example 1: Accessing the Sandbox

When your plugin only needs to work with files in its own sandbox, use the `"plugin"` permission level.

<CodeBlock slots="heading, code" repeat="2" languages="JavaScript, JSON" />

#### index.js

```js
const { localFileSystem } = require('uxp').storage;

async function accessPluginDataFolder() {
    // Access the plugin's data folder
    try {
        const dataFolder = await localFileSystem.getEntryWithUrl("plugin-data:/");
        console.log(`Data folder path: ${dataFolder.nativePath}`);

        // List all files in the data folder
        const entries = await dataFolder.getEntries();
        console.log(`Found ${entries.length} items in data folder`);

        for (const entry of entries) {
            console.log(`- ${entry.name} (${entry.isFile ? 'file' : 'folder'})`);
        }
    } catch (e) {
        console.error("Failed to access data folder:", e);
    }
}
```

#### manifest.json

```json
{
  "manifestVersion": 5,
  // ...
  "requiredPermissions": {
    "localFileSystem": "plugin"
  }
  // ...
}
```

### Example 2: Accessing Arbitrary Locations

When your plugin needs unrestricted access to the file system, use the `"fullAccess"` permission level. This requires you to specify absolute file paths using the `file:/` scheme.

<CodeBlock slots="heading, code" repeat="2" languages="JavaScript, JSON" />

#### index.js

```js
const { localFileSystem } = require('uxp').storage;

async function accessUserDocuments() {
    // Access a specific location outside the sandbox
    try {
        // For macOS
        const documentsFolder = await localFileSystem.getEntryWithUrl("file:/Users/user/Documents");
        // For Windows, use: "file:/C:/Users/user/Documents"

        console.log(`Documents folder path: ${documentsFolder.nativePath}`);

        // Read a specific file
        const configFile = await localFileSystem.getEntryWithUrl("file:/Users/user/Documents/config.json");
        if (configFile.isFile) {
            const content = await configFile.read();
            console.log("Config file content:", content);
        }
    } catch (e) {
        console.error("Failed to access documents folder:", e);
    }
}
```

#### manifest.json

```json
{
  "manifestVersion": 5,
  // ...
  "requiredPermissions": {
    "localFileSystem": "fullAccess"
  }
  // ...
}
```

<InlineAlert variant="warning" slots="text"/>

Remember that users may be hesitant to install plugins requesting `"fullAccess"`. Only use this permission level when absolutely necessary. Consider using `"request"` instead to let users choose specific files or folders.

### Example 3: User-Selected Locations

The most user-friendly approach is to let users choose which files or folders your plugin can access. Use the `"request"` permission level with file picker dialogs.

<CodeBlock slots="heading, code" repeat="2" languages="JavaScript, JSON" />

#### index.js

```js
const { localFileSystem, domains, fileTypes } = require('uxp').storage;

async function openUserSelectedFile() {
    // Present a file picker starting at the user's Desktop
    try {
        const file = await localFileSystem.getFileForOpening({
            initialDomain: domains.userDesktop,
            types: fileTypes.text
        });

        if (!file) {
            console.log("User cancelled file selection");
            return;
        }

        // Read the selected file
        const content = await file.read();
        console.log(`File content:\n${content}`);
        console.log(`File path: ${file.nativePath}`);
    } catch (err) {
        console.error("Failed to open file:", err);
    }
}

async function saveToUserSelectedLocation() {
    // Present a save dialog to let the user choose where to save
    try {
        const file = await localFileSystem.getFileForSaving("export.txt", {
            types: ["txt"]
        });

        if (!file) {
            console.log("User cancelled save operation");
            return;
        }

        // Write content to the selected location
        await file.write("This content was exported from the plugin.");
        console.log(`File saved to: ${file.nativePath}`);
    } catch (err) {
        console.error("Failed to save file:", err);
    }
}

async function selectFolderForExport() {
    // Let the user select a folder for batch export
    try {
        const folder = await localFileSystem.getFolder({
            initialDomain: domains.userDocuments
        });

        if (!folder) {
            console.log("User cancelled folder selection");
            return;
        }

        // Create multiple files in the selected folder
        for (let i = 1; i <= 3; i++) {
            const file = await folder.createFile(`export_${i}.txt`, { overwrite: true });
            await file.write(`Content for file ${i}`);
        }

        console.log(`Created 3 files in: ${folder.nativePath}`);
    } catch (err) {
        console.error("Failed to export files:", err);
    }
}
```

#### manifest.json

```json
{
  "manifestVersion": 5,
  // ...
  "requiredPermissions": {
    "localFileSystem": "request"
  }
  // ...
}
```

### Example 4: Remembering User Selections with Tokens

When users grant access to files or folders, you can create tokens to remember those locations across sessions—saving users from repeatedly selecting the same files.

UXP provides two types of tokens:

- [**Session tokens**](../../../uxp-api/reference-js/Modules/uxp/Persistent%20File%20Storage/FileSystemProvider.md): Last until the plugin is unloaded or the application closes
- [**Persistent tokens**](../../../uxp-api/reference-js/Modules/uxp/Persistent%20File%20Storage/FileSystemProvider.md): Survive across sessions until the plugin is uninstalled

```javascript
const { localFileSystem, domains, fileTypes } = require('uxp').storage;

async function selectAndRememberFile() {
    try {
        // Let the user select a file
        const file = await localFileSystem.getFileForOpening({
            initialDomain: domains.userDesktop,
            types: fileTypes.text
        });

        if (!file) {
            console.log("User cancelled file selection");
            return;
        }

        // Create a persistent token for this file
        const token = await localFileSystem.createPersistentToken(file);

        // Store the token for future use (e.g., in localStorage)
        localStorage.setItem("selectedFileToken", token);

        console.log(`File selected and token saved: ${file.nativePath}`);
    } catch (err) {
        console.error("Failed to create token:", err);
    }
}

async function readPreviouslySelectedFile() {
    try {
        // Retrieve the token from storage
        const token = localStorage.getItem("selectedFileToken");

        if (!token) {
            console.log("No previously selected file found");
            return;
        }

        // Access the file using the token
        const file = await localFileSystem.getEntryForPersistentToken(token);

        // Read the file content
        const content = await file.read();
        console.log(`File content:\n${content}`);
    } catch (err) {
        console.error("Failed to read file using token:", err);
        // Token may be invalid if file was deleted or moved
        localStorage.removeItem("selectedFileToken");
    }
}
```

<InlineAlert variant="info" slots="header, text"/>

Token Storage

Store tokens in [`localStorage`](../../../uxp-api/reference-js/Global%20Members/Data%20Storage/LocalStorage.md) or your plugin's data folder so they persist between plugin sessions. Always handle cases where tokens become invalid (e.g., if the user deletes or moves the file).

### `LocalFileSystem` API Reference

For complete API documentation, see:

- [FileSystemProvider](../../../uxp-api/reference-js/Modules/uxp/Persistent%20File%20Storage/FileSystemProvider.md): main interface for file system operations.
- [Entry](../../../uxp-api/reference-js/Modules/uxp/Persistent%20File%20Storage/Entry.md): base class for files and folders.
- [File](../../../uxp-api/reference-js/Modules/uxp/Persistent%20File%20Storage/File.md): file-specific operations.
- [Folder](../../../uxp-api/reference-js/Modules/uxp/Persistent%20File%20Storage/Folder.md): folder-specific operations.
- [EntryMetadata](../../../uxp-api/reference-js/Modules/uxp/Persistent%20File%20Storage/EntryMetadata.md): file and folder metadata.
- [Path](../../../uxp-api/reference-js/Global%20Members/Path.md): path manipulation utilities.

## Working with the `fs` module

The `fs` module offers a simpler, path-based approach similar to [Node.js](https://nodejs.org/api/fs.html). It's ideal for quick, single-operation tasks.

### Example 5: Reading from the Sandbox

Read a file directly from the sandbox using a URL scheme:

<CodeBlock slots="heading, code" repeat="2" languages="JavaScript, JSON" />

#### index.js

```js
const fs = require("fs");

async function readConfigFile() {
    // Read a configuration file from the plugin folder
    try {
        const content = await fs.readFile("plugin:/config.json", "utf8");
        const config = JSON.parse(content);
        console.log("Configuration loaded:", config);
    } catch (e) {
        console.error("Failed to read config file:", e);
    }
}

async function writeToDataFolder() {
    // Write data to the plugin's data folder
    try {
        const data = {
            lastRun: new Date().toISOString(),
            version: "1.0.0"
        };

        await fs.writeFile(
            "plugin-data:/state.json",
            JSON.stringify(data, null, 2),
            "utf-8"
        );

        console.log("State saved successfully");
    } catch (e) {
        console.error("Failed to save state:", e);
    }
}
```

#### manifest.json

```json
{
  "manifestVersion": 5,
  // ...
  "requiredPermissions": {
    "localFileSystem": "plugin"
  }
  // ...
}
```

### Example 6: Writing to Arbitrary Locations

Write files to any location on the file system using absolute paths:

<CodeBlock slots="heading, code" repeat="2" languages="JavaScript, JSON" />

#### index.js

```js
const fs = require("fs");

async function exportToDesktop() {
    // Export data to the user's Desktop
    try {
        const exportData = "Exported data from plugin";

        // For macOS
        await fs.writeFile(
            "/Users/user/Desktop/export.txt",
            exportData,
            { encoding: "utf-8" }
        );
        // For Windows, use: "C:/Users/user/Desktop/export.txt"

        console.log("File exported to Desktop");
    } catch (e) {
        console.error("Failed to export file:", e);
    }
}

async function readFromDocuments() {
    // Read a file from the user's Documents folder
    try {
        // For macOS
        const content = await fs.readFile(
            "/Users/user/Documents/input.txt",
            "utf8"
        );
        // For Windows, use: "C:/Users/user/Documents/input.txt"

        console.log("File content:", content);
    } catch (e) {
        console.error("Failed to read file:", e);
    }
}
```

#### manifest.json

```json
{
  "manifestVersion": 5,
  // ...
  "requiredPermissions": {
    "localFileSystem": "fullAccess"
  }
  // ...
}
```

### `fs` module API Reference

For complete API documentation, see:

- [`fs` module](../../../uxp-api/reference-js/Modules/fs/): complete file system API reference.
- [`path`](../../../uxp-api/reference-js/Global%20Members/Path.md): path manipulation utilities.

## Additional Considerations

### Operating System Limitations

Even with `"fullAccess"` permission, certain system locations may be restricted by the operating system:

- **macOS and Windows**: Generally allow access to most user-accessible locations
- **UWP (Windows Store apps)**: System folders are prohibited and cannot be accessed

<InlineAlert variant="info" slots="text"/>

Always handle file system errors gracefully and inform users when access is denied. Operating system security policies may prevent access to certain locations even when your plugin has the correct permissions.

### Best Practices

1. **Choose the right permission level**: start with `"plugin"`, upgrade to `"request"`, and only use `"fullAccess"` when absolutely necessary.
2. **Handle errors gracefully**: always wrap file operations in try-catch blocks.
3. **Validate file paths**: check that files exist before attempting to read them.
4. **Use appropriate encoding**: specify `"utf-8"` for text files to ensure proper character handling.
5. **Provide user feedback**: show progress indicators for long-running file operations.
6. **Clean up temporary files**: delete temporary files when they're no longer needed.

### When to Use Each API

| Use Case                             | Recommended API |
| :----------------------------------- | :-------------- |
| Multiple operations on the same file | LocalFileSystem |
| Traversing directory structures      | LocalFileSystem |
| Working with file metadata           | LocalFileSystem |
| Creating persistent tokens           | LocalFileSystem |
| Quick read/write operations          | FS Module       |
| Simple path-based operations         | FS Module       |
| Familiarity with Node.js fs API      | FS Module       |

## Reference Material

- [FileSystemProvider](../../../uxp-api/reference-js/Modules/uxp/Persistent%20File%20Storage/FileSystemProvider.md): main interface for file system operations.
- [Entry](../../../uxp-api/reference-js/Modules/uxp/Persistent%20File%20Storage/Entry.md): base class for files and folders.
- [File](../../../uxp-api/reference-js/Modules/uxp/Persistent%20File%20Storage/File.md): file-specific operations.
- [Folder](../../../uxp-api/reference-js/Modules/uxp/Persistent%20File%20Storage/Folder.md): folder-specific operations.
- [EntryMetadata](../../../uxp-api/reference-js/Modules/uxp/Persistent%20File%20Storage/EntryMetadata.md): file and folder metadata.
- [`fs` module](../../../uxp-api/reference-js/Modules/fs/): complete file system API reference.
- [Path](../../../uxp-api/reference-js/Global%20Members/Path.md): path manipulation utilities.
- [LocalStorage](../../../uxp-api/reference-js/Global%20Members/Data%20Storage/LocalStorage.md): persistent data storage for tokens.
- [Manifest Permissions](../../../plugins/concepts/manifest/index.md#permissionsdefinition): overview of all permissions.
- [Local File System Permission](../../../plugins/concepts/manifest/index.md#localfilesystem): detailed permission documentation.

## Summary

1. **The Sandbox Model**: By default, plugins can only access safe locations (plugin folder, data folder, and temporary folder) without additional permissions. The plugin folder is read-only, while data and temporary folders are read-write but may be cleared automatically.

2. **File System Permissions**: Declare the `localFileSystem` permission in your `manifest.json` with three possible values:

   - `"plugin"`: Access only sandbox locations (default, most secure)
   - `"request"`: Present file picker dialogs for user-selected files and folders (recommended for user data)
   - `"fullAccess"`: Unrestricted file system access (use sparingly, may deter users from installing)

3. **URL Schemes**: UXP provides convenient shortcuts to file system locations:

   - `plugin:/` for the plugin folder (read-only)
   - `plugin-data:/` for persistent plugin data
   - `plugin-temp:/` for temporary storage
   - `file:/` for absolute paths (requires `"fullAccess"`)

4. **Two File System APIs**: Choose based on your use case:

   - **LocalFileSystem API**: Object-oriented, uses Entry references (File and Folder objects), ideal for multiple operations, directory traversal, and working with metadata
   - **fs module**: Path-based like Node.js, ideal for quick single operations and simple read/write tasks

5. **Persistent Access with Tokens**: When users grant access to files or folders via `"request"` permission, create session tokens (temporary) or persistent tokens (survive across sessions) to remember these locations without repeatedly prompting users.

6. **Common Patterns**:

   - For configuration files in your plugin folder: Use `fs.readFile("plugin:/config.json")`
   - For saving plugin state: Use `fs.writeFile("plugin-data:/state.json")`
   - For user-selected files: Use `localFileSystem.getFileForOpening()` with `"request"` permission
   - For batch operations: Use `LocalFileSystem` API with folder traversal
   - For remembering user selections: Create persistent tokens and store them in `localStorage`
