---
title: Changelog
description: What's New
keywords:
  - Changelog
  - Update
  - Release Notes
contributors:
  - https://github.com/undavide
---

# Changelog

## Premiere Pro v26.2.0

### UXP Hybrid Plugin Support

Premiere Pro now officially supports [UXP Hybrid Plugins](../plugins/hybrid-plugins/index.md), allowing developers to extend their UXP plugins with native C++ libraries. Hybrid plugins enable performance-critical workloads—such as audio/video processing, ML inference, and integration with native SDKs—to run as compiled code alongside the JavaScript-based plugin UI and logic.

- **UXP Hybrid Plugin SDK**: download from the [Adobe Developer Console](https://developer.adobe.com/console). The SDK provides C++ headers, utilities, and templates for building native addons (`.uxpaddon` files).
- **New documentation**: [Overview](../plugins/hybrid-plugins/index.md), [Building Hybrid Plugins](../plugins/hybrid-plugins/build.md), and [FAQ](../plugins/hybrid-plugins/faq.md).

## Premiere Pro v25.6.0

### Official Release of UXP extensibility in Premiere Pro

#### New Features

Premiere Pro's UXP APIs are approaching parity with what was previously possible, via CEP and ExtendScript. While the sample plugins don't (yet) exercise every call or listen to every message, the infrastructure is in place; we will continue to expand and improve the samples.

### Documentation update

- **Comprehensive overhaul** across the entire documentation site.
- **New distribution section** including guides covering Adobe Marketplace submission, enterprise and independent distribution, packaging, installation, listing creation, and review guidelines.
- **Expanded tutorials and recipes** featuring major new content on modal dialogs, panels, TypeScript support, filesystem operations, external processes, and inter-plugin communication.
- **Content reorganization** with streamlined navigation, consolidation, and complete rewrites.
- **New Premiere API Reference** updated to v25.6.

## Premiere Pro v25.2.0

### Initial Public Beta Release for UXP in Premiere Pro

**Release Date:** December 4, 2024

#### New Features

- **Unified Extensibility Platform (UXP) Integration:** Premiere Pro Beta now supports UXP, providing a modern and streamlined approach to developing plugins.
- **Enhanced Performance:** UXP integration aims to improve the performance and responsiveness of plugins within Premiere Pro.
- **Developer Tools:** APIs are available for developers to create and manage UXP-based plugins.

#### Known Issues

- **Limited Third-Party Support:** Initial beta release may have limited support for specific third-party development workflows. Full support is expected in future updates.
- Spectrum Web Component support in UXP is not yet fully supported for Premiere Pro
- Command Plugins do not yet work as a standalone plugin
- Unloading/Reloading a plugin from the UXP Developer Tool [UDT] while it's paused on a breakpoint doesn't work

#### Getting Started

- **Community Support:** Join the [Creative Cloud developer forums](https://forums.creativeclouddeveloper.com/) to share feedback, ask questions, and collaborate with other developers.
