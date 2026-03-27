---
title: Hybrid Plugins
description: Extend UXP plugins with high-performance C++ native libraries
keywords:
  - UXP Hybrid
  - Hybrid Plugins
  - C++
  - uxpaddon
  - native libraries
  - Node API
  - performance
contributors:
  - https://github.com/undavide
---

# Hybrid Plugins

Extend your UXP plugins with the power of C++ native libraries.

## Overview

A UXP plugin can provide extensive functionality using JavaScript, HTML, and CSS. However, situations can arise where the UXP runtime cannot address specific programming needs—for instance, performance-critical computation or integration with existing native codebases. For these scenarios, UXP offers **Hybrid Plugins**.

A **UXP Hybrid plugin** is a standard UXP plugin that can load dynamically-linked shared objects written in C++. The concept is similar to [C++ addons](https://nodejs.org/api/addons.html) in Node.js: compiled native libraries are loaded at runtime via the `require()` function, just like any other JavaScript module.

```js
const addon = require("sample.uxpaddon");
```

The loaded addon exposes C++ functions and properties directly to your JavaScript code, enabling seamless two-way communication between the two environments.

<InlineAlert variant="info" slots="header, text" />

#### Advanced Topic

Building Hybrid plugins requires proficiency in C++. Make sure you also have experience [writing UXP plugins](../../plugins/index.md) and are comfortable using the [UXP Developer Tool](../../introduction/essentials/dev-tools/index.md#uxp-developer-tool-udt) before diving in.

## Use Cases

- **Performance-intensive audio/video processing**: offload computationally expensive operations (custom waveform analysis, frame-level pixel manipulation, audio DSP algorithms) to native code while keeping the UI and orchestration logic in JavaScript.
- **Integration with C++ libraries**: leverage established native libraries such as OpenCV, TensorFlow Lite, or custom in-house codecs directly from your plugin.
- **Metadata processing at scale**: perform batch XMP operations or custom metadata schema transformations that would be too slow in pure JavaScript.
- **Bridging to external native pipelines**: connect to hardware SDKs, proprietary encoding pipelines, or platform-specific system APIs that are only available via C/C++.

## Minimum Requirements

| Component                    | Minimum Version |
| :--------------------------- | :-------------- |
| **Premiere**                 | 26.2            |
| **UXP Developer Tool (UDT)** | 2.2             |
| **Creative Cloud Desktop**   | 5.10            |

## The UXP Hybrid Plugin SDK

### Download

Download the UXP Hybrid Plugin SDK from the [Adobe Developer Console](https://developer.adobe.com/console) (if you get "Access Denied", see [this FAQ](https://developer.adobe.com/developer-distribution/creative-cloud/docs/guides/faq/#what-do-i-do-when-i-get-access-denied-upon-login)). Unpack the contents and read the included `README.md` for platform-specific build instructions.

### SDK Contents

The SDK provides C++ headers, utilities, and templates for building native addons (called **uxpaddons**). Its API surface is intentionally similar to [Node-API](https://nodejs.org/api/n-api.html)—if you're familiar with Node.js native addons, you'll feel right at home.

| Folder                     | Contents                                                                                                                                                                      |
| :------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `src/api`                  | **UxpAddonTypes.h** — fundamental data types (opaque abstractions consumed by the SDK APIs). **UxpAddonShared.h** — the full addon API surface, closely mirroring Node-API.   |
| `src/utilities`            | Utility classes with common helpers. **UxpAddon.h** — provides the `UXP_ADDON_INIT` and `UXP_ADDON_TERMINATE` macros for registering initialization and termination routines. |
| `template/template-dev`    | Source code for a minimal addon example—use it as a starting point for your own plugin.                                                                                       |
| `template/template-plugin` | A pre-compiled Hybrid plugin ready to load in UDT.                                                                                                                            |

### Releases

The SDK is versioned independently from the host application (it is labeled with a UXP version, since Hybrid plugins are designed to be app-independent). Announcements of new SDK releases are made in the [Changelog](../../changelog/index.md). Updating to a new SDK version requires recompiling and republishing your plugin; however, plugins built with an older SDK remain forward-compatible with newer host application versions.

## Next Steps

Ready to build? Head over to [Building Hybrid Plugins](./build.md) for the complete development guide—from compiling your first uxpaddon to packaging and distributing the finished plugin.
