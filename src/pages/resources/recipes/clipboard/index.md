---
title: Clipboard Operations
description: Integrate your plugin with the system clipboard to seamlessly read and write text data—enabling users to copy, paste, and share content between your plugin and other applications.
keywords:
  - clipboard
  - copy
  - paste
  - read write
  - permissions
contributors:
  - https://github.com/padmkris123
  - https://github.com/undavide
---

# Clipboard Operations

Integrate your plugin with the system clipboard to read and write text data

UXP provides clipboard APIs that let your plugin **read from** and **write to** the system clipboard—enabling users to copy, paste, and share content between your plugin and other applications. This guide covers how to use the [`Clipboard` API](../../../uxp-api/reference-js/Global%20Members/Data%20Transfers/Clipboard.md), declare the necessary permissions, and handle common use cases.

## System requirements

Please make make sure your development environment uses the following **minimum versions** to avoid compatibility issues:

- **Premiere Pro v25.6**
- **UDT v2.2**
- **Manifest v5**

## Clipboard Security

By default, UXP plugins can't access the system clipboard; this protects users from unwanted data access. If your plugin needs to read or write clipboard content, **you must declare** the right [clipboard permission](../../../plugins/concepts/manifest/index.md#permissionsdefinition) in your `manifest.json`.

Choose the most appropriate permission level:

| Permission       | Access Level          | Use When                                     |
| :--------------- | :-------------------- | :------------------------------------------- |
| `"read"`         | Read-only             | Your plugin only needs to paste or read data |
| `"readAndWrite"` | Read and write access | Your plugin needs to copy and paste data     |

<InlineAlert variant="info" slots="header, text"/>

Pick the least-permissive option that meets your needs

In future versions, users may be asked to grant consent for clipboard access, and they'll be more comfortable approving read-only access unless your plugin clearly needs to write data.

## Using the Clipboard API

The clipboard is accessed through `navigator.clipboard`, which provides two main methods:

- **`setContent()`**: Write data to the clipboard.
- **`getContent()`**: Read data from the clipboard.

Both methods work with MIME type objects, where keys represent data formats (like `"text/plain"`) and values contain the actual content.

### Example: Writing to the Clipboard

Here's how to copy text to the system clipboard.

<CodeBlock slots="heading, code" repeat="2" languages="JavaScript, JSON" />

#### index.js

```js
// Copy formatted text to the clipboard ✂️
async function copyToClipboard(text) {
  try {
    await navigator.clipboard.setContent({
      "text/plain": text
    });
    console.log("✅ Text copied to clipboard");

  } catch (err) {
    console.error("❌ Failed to copy to clipboard:", err);
  }
}

// Example usage
copyToClipboard("Welcome to UXP for Premiere Pro!");
```

#### manifest.json

```json
{
  // ...
  "requiredPermissions": {
    "clipboard": "readAndWrite"
  }
  // ...
}
```

### Example: Reading from the Clipboard

You can also read content that users have copied from other applications.

<CodeBlock slots="heading, code" repeat="2" languages="JavaScript, JSON" />

#### index.js

```js
// Paste text from the clipboard 📋
async function pasteFromClipboard() {
  try {
    const clipboardData = await navigator.clipboard.getContent();

    if (clipboardData["text/plain"]) {
      console.log(`Pasted text: ${clipboardData["text/plain"]}`);
      return clipboardData["text/plain"];
    } else {
      console.log("⚠️ No text data found on clipboard");
      return null;
    }

  } catch (err) {
    console.error("❌ Failed to read from clipboard:", err);
  }
}
```

#### manifest.json

```json
{
  // ...
  "requiredPermissions": {
    "clipboard": "read"
  }
  // ...
}
```

<InlineAlert variant="info" slots="text"/>

Notice how this example uses `"read"` permission since it only needs to **read** from the clipboard, not write to it. Always choose the minimum permission level your plugin requires.

### Example: Copy and Paste Together

In many workflows, you'll want to both read and write clipboard data—for example, transforming text or syncing data between your plugin and external tools.

```js
// Transform clipboard text to uppercase
async function transformClipboardText() {
  try {
    // Read current clipboard content
    const data = await navigator.clipboard.getContent();

    if (data["text/plain"]) {
      const originalText = data["text/plain"];
      const transformedText = originalText.toUpperCase();

      // Write the transformed text back
      await navigator.clipboard.setContent({
        "text/plain": transformedText
      });

      console.log(`✅ Transformed: "${originalText}" → "${transformedText}"`);
    } else {
      console.log("⚠️ No text found on clipboard");
    }

  } catch (err) {
    console.error("Failed to transform clipboard text:", err);
  }
}
```

For this use case, your manifest would need `"readAndWrite"` permission.

## Reference Material

- [`Clipboard`](../../../uxp-api/reference-js/Global%20Members/Data%20Transfers/Clipboard.md) API Reference.
- [Manifest Permissions](../../../plugins/concepts/manifest/index.md#permissionsdefinition).

## Summary

1. **Clipboard Security**: By default, plugins cannot access the system clipboard. You must explicitly declare clipboard permissions in `manifest.json`:
   - Use `"read"` for read-only access (pasting content).
   - Use `"readAndWrite"` when you need to both copy and paste.
   - Choose the least-permissive option to avoid installation friction.
2. **Using the API**: Access the clipboard via `navigator.clipboard`:
   - **`setContent()`**: Writes data to the clipboard using MIME type objects (e.g., `{ "text/plain": "text" }`).
   - **`getContent()`**: Reads data from the clipboard, returning an object keyed by MIME types.
   - Always wrap clipboard operations in `try...catch` blocks and use `await` for proper error handling.
