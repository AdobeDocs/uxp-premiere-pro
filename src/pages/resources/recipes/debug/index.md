---
title: Debugging Techniques
description: Use console logs and dialog methods to debug your UXP plugin quickly
keywords:
  - debugging
  - console
  - alerts
  - developer tools
contributors:
  - https://github.com/padmkris123
  - https://github.com/undavide
---

# Debugging Techniques

Use console logs and dialog methods to debug your plugin quickly

While the [UXP Developer Tool](../../../plugins/tutorials/udt-deep-dive/index.md) offers a full debugging experience with breakpoints and the Chrome DevTools, these simple techniques can help you quickly troubleshoot issues during development.

## Prerequisites

Before you begin, make sure your development environment uses the following versions:

- **Premiere Pro v25.6** or higher
- **UDT v2.2** or higher
- **Manifest version v5** or higher

## Console Logging

The simplest way to debug is to log values to the console. Open the UXP Developer Tool console to view output.

```js
// Basic logging
console.log("Plugin initialized");          // 💡 General information
console.warn("This feature is deprecated"); // ⚠️ Warnings (yellow)
console.error("Failed to load data");       // ❌ Errors (red)

// Log variables and objects
const user = { name: "Jane", role: "Editor" };
console.log("User data:", user);
// Logs: User data: { name: "Jane", role: "Editor" }

// Log multiple values using template literals
const width = 1920;
const height = 1080;
console.log(`Resolution: ${width}x${height}`); // Template literals for formatting
```

## Dialog-based Debugging

For quick checks without switching to the console, use dialog methods to display information or input values directly in the UI.

<InlineAlert variant="error" slots="text"/>

The `alert()`, `confirm()`, and `prompt()` methods are not fully supported in Premiere Pro; they will be fixed in a future release.

<InlineAlert variant="info" slots="header, text"/>

Requires Manifest configuration

To use [`alert()`](../../../uxp-api/reference-js/Global%20Members/HTML%20DOM/alert.md), [`confirm()`](../../../uxp-api/reference-js/Global%20Members/HTML%20DOM/confirm.md), and [`prompt()`](../../../uxp-api/reference-js/Global%20Members/HTML%20DOM/prompt.md), you must enable the `enableAlerts` feature flag in your [`manifest.json`](../../../plugins/concepts/manifest/index.md#enablealerts).

<CodeBlock slots="heading, code" repeat="2" languages="JavaScript, JSON" />

#### index.js

```js
// Simple alert dialog
alert("Plugin loaded successfully");

// Confirmation dialog
const confirmed = confirm("Do you want to continue?");
if (confirmed) {
  console.log("User clicked OK");
} else {
  console.log("User clicked Cancel");
}

// Prompt dialog for user input
const userName = prompt("Enter your name:", "Default Name");
console.log(`User entered: ${userName}`);
```

#### manifest.json

```json
{
  "manifestVersion": 5,
  // ...
  "featureFlags": {
    "enableAlerts": true
  }
  // ...
}
```

## Using UXP Developer Tool

For comprehensive debugging using the UXP Developer Tool, please refer to the [Plugin Workflows](../../../plugins/tutorials/udt-deep-dive/plugin-workflows.md#debug-your-plugin) documentation.

## Reference Material

- [`alert()`](../../../uxp-api/reference-js/Global%20Members/HTML%20DOM/alert.md): display simple alert dialogs.
- [`confirm()`](../../../uxp-api/reference-js/Global%20Members/HTML%20DOM/confirm.md): display confirmation dialogs.
- [`prompt()`](../../../uxp-api/reference-js/Global%20Members/HTML%20DOM/prompt.md): prompt users for input.
