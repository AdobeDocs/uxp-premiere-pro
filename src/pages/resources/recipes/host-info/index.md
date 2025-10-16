---
title: Host Environment Information
description: Detect the user's operating system, application version, and UXP runtime
keywords:
  - host information
  - platform detection
  - version checking
  - os detection
  - locale
  - environment
contributors:
  - https://github.com/padmkris123
  - https://github.com/undavide
---

# Host Environment Information

Detect the user's operating system, application version, and UXP runtime

UXP provides APIs to inspect the **host environment** where your plugin runs—including the operating system, application version, UXP runtime version, and user locale. This information is essential for building plugins that adapt to different platforms, check feature compatibility, or implement platform-specific logic.

## Prerequisites

Before you begin, make sure your development environment uses the following versions:

- **Premiere Pro v25.6** or higher
- **UDT v2.2** or higher
- **Manifest version v5** or higher

## Available APIs

UXP provides three main modules for host environment detection:

| Module                                                                         | Purpose                        | Key Properties                                                                        |
| :----------------------------------------------------------------------------- | :----------------------------- | :------------------------------------------------------------------------------------ |
| [`host`](../../../uxp-api/reference-js/Modules/uxp/Host%20Information/Host.md) | Application and UI information | `name`, `version`, `uiLocale`                                                         |
| [`versions`](../../../uxp-api/reference-js/Modules/uxp/Versions/Versions.md)   | UXP runtime and plugin version | `uxp`, `plugin`                                                                       |
| [`os`](../../../uxp-api/reference-js/Modules/os/OS.md)                         | Operating system information   | `platform()`, `release()`, `arch()`, `cpus()`, `totalmem()`, `freemem()`, `homedir()` |

### Example: Basic Host Detection

Here's a simple example that logs environment information to the console.

<CodeBlock slots="heading, code" repeat="2" languages="JavaScript, text" />

#### index.js

```js
const { host, versions } = require("uxp");
const os = require("os");

// Log host environment information 💻
function logHostInfo() {
  console.log("=== Host Environment ===");
  console.log(`OS: ${os.platform()} ${os.release()}`);
  console.log(`Application: ${host.name} v${host.version}`);
  console.log(`UXP Runtime: v${versions.uxp}`);
  console.log(`Plugin Version: v${versions.plugin}`);
  console.log(`UI Locale: ${host.uiLocale}`);
}
logHostInfo();
```

#### Console Output

```text
=== Host Environment ===
OS: darwin 24.6.0
Application: premierepro v25.6.0
UXP Runtime: vuxp-8.1.0-local
Plugin Version: v1.0.0
UI Locale: en_US
```

<InlineAlert variant="info" slots="text"/>

The `os.platform()` method returns `"darwin"` for macOS and `"win32"` for Windows. Use this to detect the user's operating system reliably.

### Example: Platform-Specific Logic

In real-world plugins, you'll often need to adjust behavior based on the user's platform—for example, using different file paths, keyboard shortcuts, or native features.

```js
const { host, shell } = require("uxp");
const os = require("os");

// Use platform-appropriate URL scheme 🗺️
async function openMapsLocation(address) {
  const IS_MAC = os.platform() === "darwin";
  let url;
  if (IS_MAC) {
    // Use Apple Maps on macOS
    url = `maps://?address=${encodeURIComponent(address)}`;
  } else {
    // Use Bing Maps on Windows
    url = `bingmaps:?q=${encodeURIComponent(address)}`;
  }

  try {
    await shell.openExternal(url, "Opening maps application");
    console.log(`✅ Opened maps for: ${address}`);
  } catch (err) {
    console.error("Failed to open maps:", err);
  }
}

// Example usage
openMapsLocation("345 Park Ave, San Jose");
```

### Example: Version-based Feature Detection

Check application or UXP versions to enable features conditionally and avoid errors on older installations.

```js
const { host, versions } = require("uxp");

// Check if UXP version supports a feature 🔍
function supportsAdvancedFeatures() {
  const uxpVersion = versions.uxp;

  // Parse version string (e.g., "8.1.0" -> 8.1)
  const majorMinor = parseFloat(
    uxpVersion.split(".").slice(0, 2).join(".")
  );

  // Check if UXP is version 8.1 or higher
  return majorMinor >= 8.1;
}

// Conditionally enable features based on version
function initializePlugin() {
  console.log("Initializing plugin...");

  if (supportsAdvancedFeatures()) {
    console.log("✅ Advanced features enabled (UXP 8.1+)");
    // Enable newer API usage
  } else {
    console.log("⚠️ Using legacy mode (UXP < 8.1)");
    // Provide fallback behavior
  }
}
```

## Reference Material

- [`host` module](../../../uxp-api/reference-js/Modules/uxp/Host%20Information/Host.md): application and UI information.
- [`versions` module](../../../uxp-api/reference-js/Modules/uxp/Versions/Versions.md): UXP and plugin version information.
- [`os` module](../../../uxp-api/reference-js/Modules/os/OS.md): operating system information.

## Summary

1. **Three Information Sources**: UXP provides three modules for host environment detection:

   - **`host`**: Application name, version, and locale information (`host.name`, `host.version`, `host.uiLocale`).
   - **`versions`**: UXP runtime and plugin version (`versions.uxp`, `versions.plugin`).
   - **`os`**: Operating system information (`platform()`, `release()`, `arch()`, `cpus()`, `totalmem()`, `freemem()`, `homedir()`).

2. **Platform Detection**: Use `os.platform()` to detect the operating system:

   - Returns `"darwin"` for macOS and `"win32"` for Windows.
   - Use this for platform-specific file paths, keyboard shortcuts, URL schemes, and UI conventions.
   - Cache the result in a constant for better performance.

3. **Version Checking**: Parse version strings to implement feature detection:

   - Check UXP version for API compatibility (`versions.uxp`).
   - Check application version for feature availability (`host.version`).
   - Always provide fallbacks or clear error messages for unsupported versions.
