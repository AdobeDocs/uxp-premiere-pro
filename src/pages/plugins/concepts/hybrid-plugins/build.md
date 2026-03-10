---
title: Building Hybrid Plugins
description: Build, configure, debug, and distribute UXP Hybrid plugins with native C++ addons
keywords:
  - UXP Hybrid
  - Hybrid Plugins
  - C++
  - uxpaddon
  - building
  - manifest
  - debugging
  - packaging
contributors:
  - https://github.com/undavide
---

# Building Hybrid Plugins

A step-by-step guide to building, configuring, and shipping a UXP Hybrid plugin.

## Building a uxpaddon

### 1. Create a Native Library Project

- Create a new **Xcode** (macOS) or **Visual Studio** (Windows) project targeting a **dynamic library**.
- Add the UXP Hybrid Plugin SDK `src/api` path to your project's include paths.

### 2. Write Your C++ Logic

Include the main header and register your initialization and termination routines:

```cpp
#include "UxpAddon.h"

addon_value init(addon_env env, addon_value exports) {
    // Register functions and properties on 'exports'
    return exports;
}

void terminate() {
    // Cleanup logic
}

UXP_ADDON_INIT(init);
UXP_ADDON_TERMINATE(terminate);
```

Within your `init` function, use the addon APIs (defined in `UxpAddonShared.h` via `addon_apis`) to register native functions that will be callable from JavaScript. These APIs are invoked as `UxpAddonApis.uxp_addon_***()`.

### 3. Compile and Rename

Build the dynamic library (`.dylib` on macOS, `.dll` on Windows) and **rename the file extension** to `.uxpaddon`.

## Using a uxpaddon in JavaScript

Once compiled, the addon is loaded with `require()` and its exported functions are available immediately:

```js
const addon = require("sample-uxp-addon.uxpaddon");
let result = addon.first_function();
```

The addon behaves like any other JavaScript module—you can call functions, read properties, and pass data back and forth between JavaScript and C++.

## Manifest Configuration

Hybrid plugins require a few specific settings in the [`manifest.json`](../manifest/index.md):

- **Manifest version** 6 or above.
- The [`addon`](../manifest/index.md#addon) field with the name of your uxpaddon.
- The [`enableAddon`](../manifest/index.md#enableaddon) permission.

```json
{
  "manifestVersion": 6,
  "host": {
    "app": "premierepro",
    "minVersion": "25.6.0",
  },
  "addon": {
    "name": "sample-uxp-addon.uxpaddon"
  },
  "requiredPermissions": {
    "enableAddon": true
  }
}
```

## Plugin Structure

The uxpaddon binaries must be placed in a specific directory layout within your plugin bundle, organized by platform and architecture:

```txt
my-hybrid-plugin/
├── manifest.json
├── index.html
├── index.js
└── addons/
    ├── mac/
    │   ├── arm64/
    │   │   └── sample-uxp-addon.uxpaddon
    │   └── x64/
    │       └── sample-uxp-addon.uxpaddon
    └── win/
        └── x64/
            └── sample-uxp-addon.uxpaddon
```

If the directory structure is incorrect, the plugin will fail to load with a _"Plugin Manifest Validation Failed"_ error in the UDT logs.

<InlineAlert variant="info" slots="text" />

You can try the pre-compiled `template-plugin` included in the SDK to quickly verify your setup. Load it via UDT and find it under the **Window** > **UXP Plugins** menu.

## Asynchronous Operations

It is important to understand the threading model when working with uxpaddons:

- **Initialization and termination** routines run on the **main thread** of the host application.
- **JavaScript calls** to addon functions run on a **dedicated scripting thread** (never the main thread).

When your addon needs to perform work on the main thread (e.g., interacting with host-specific APIs) and return results to JavaScript, you must use the asynchronous scheduling APIs. These operations are exposed to JavaScript as **Promises**.

The pattern involves three steps:

1. **From the scripting thread**: create a deferred promise and schedule work on the main thread.
2. **On the main thread**: perform the task, then schedule the result back to the scripting thread.
3. **Back on the scripting thread**: resolve or reject the promise.

```cpp
addon_value MyAsyncOperation(addon_env env, addon_callback_info info) {
    // Extract and convert arguments to standard C++ types
    // (addon_value is transient and cannot be used after this function returns)
    std::string myArg = ExtractString(env, argValue);

    // Create a promise for the JavaScript caller
    addon_deferred promiseValue = nullptr;
    addon_value deferred = nullptr;
    apis.uxp_addon_create_promise(env, &deferred, &promiseValue);

    // Schedule work on the main thread
    apis.uxp_addon_schedule_on_main_queue(env, MainThreadTask, ...);
    return deferred;
}

void MainThreadTask(...) {
    // Perform the task on the main thread...

    // When done, schedule the result back to the scripting thread
    apis.uxp_addon_schedule_on_javascript_queue(env, ScriptThreadTask, ...);
}

void ScriptThreadTask(...) {
    apis.uxp_addon_open_handle_scope(env, &scope);

    // Resolve (or reject) the JavaScript promise
    addon_value resultValue = nullptr;
    apis.uxp_addon_resolve_deferred(env, deferred, resultValue);
    apis.uxp_addon_close_handle_scope(env, scope);
}
```

The `template-dev` project in the SDK includes a working implementation of this pattern (see `MyAsyncEcho` in `module.cpp`).

## File System Access

Hybrid plugins benefit from relaxed UXP sandbox restrictions. You can access the file system using direct paths:

```js
let entry = '/path/to/file.txt';
```

This is unlike standard UXP plugins, which must use `require('uxp').storage.localFileSystem` to access files outside the sandbox. See the [Filesystem Operations recipe](../../../resources/recipes/filesystem-operations/index.md) for more details on standard file system access.

## Debugging

Hybrid plugins have both a JavaScript and a C++ layer, each requiring its own debugging approach:

- **JavaScript**: use the UDT Debug tool to set breakpoints and inspect variables.
- **C++**: attach your IDE's debugger to the running Premiere process. In most IDEs this is found under **Debug** > **Attach to Process**.

<InlineAlert variant="info" slots="text" />

On macOS, you may need to perform an additional setup step before you can attach a debugger. Follow [this guide](https://helpx.adobe.com/ca/photoshop/kb/debug-plugins-in-photoshop-bigsur.html) for details.

## Packaging and Distribution

Package your Hybrid plugin the same way as a standard UXP plugin using the [UXP Developer Tool](../../distribution/package/index.md). Additionally:

1. Follow the directory structure described in [Plugin Structure](#plugin-structure) for the uxpaddon binaries.
2. **Sign and notarize** the macOS executables with a valid Apple Developer ID certificate (self-signed/test certificates are not accepted). The certificate must be valid for at least one year.
3. If you support them, ensure the plugin works on **all three architectures**: macOS arm64, macOS x64, and Windows x64.

Since Hybrid plugins include native code, users will be prompted to enter their OS administrator credentials during installation and updates.

For full distribution details, see the [Share & Distribute](../../distribution/overview/index.md) section.

## FAQ

#### Do I need to code sign the entire plugin bundle?

No. Only the macOS `.uxpaddon` executables need to be signed and notarized with a valid Apple Developer ID certificate. The rest of the plugin bundle (JavaScript, HTML, CSS, manifest) does not require code signing.

#### Do I need an Apple Developer ID?

Yes. macOS requires a Developer ID-signed certificate for notarized executables. See [Apple's code signing guide](https://support.apple.com/guide/security/app-code-signing-process-sec3ad8e6e53/web) for details.

#### How do I prepare binaries for all architectures?

You need binaries for macOS arm64, macOS x64, and Windows x64. For the platform not natively available to you, consider using a virtual machine (e.g., VMware Fusion). For building universal macOS binaries, refer to [Apple's guide to building universal binaries](https://developer.apple.com/documentation/apple-silicon/building-a-universal-macos-binary).

#### Are Hybrid plugins forward-compatible?

Yes. A plugin built with an older version of the SDK will continue to work with newer versions of Premiere. However, updating to a new SDK version requires recompiling and republishing your plugin.

#### Why can't I see the plugin in Premiere after loading it?

While loading via UDT, the plugin may not appear automatically. Try unchecking and re-checking the plugin name from the **Window** > **UXP Plugins** menu. This issue is expected to be resolved in a future release.

#### The macOS binaries trigger security warnings. What should I do?

The binaries in the SDK's `template-plugin` are not code signed. On macOS, go to **System Settings** > **Privacy & Security** to allow them to load. For production builds, always sign and notarize your binaries with a valid Apple Developer ID.
