---
title: Hybrid Plugins FAQ
description: Frequently asked questions about UXP Hybrid Plugins for Premiere
keywords:
  - UXP Hybrid
  - Hybrid Plugins FAQ
  - C++
  - uxpaddon
  - code signing
  - architectures
contributors:
  - https://github.com/undavide
---

# Hybrid Plugins FAQ

Frequently asked questions about Hybrid Plugins.

## Questions

- [Do I need to code sign the entire plugin bundle?](#do-i-need-to-code-sign-the-entire-plugin-bundle)
- [Do I need an Apple Developer ID?](#do-i-need-an-apple-developer-id)
- [How do I prepare and test binaries for all architectures?](#how-do-i-prepare-and-test-binaries-for-all-architectures)
- [Are Hybrid plugins forward-compatible?](#are-hybrid-plugins-forward-compatible)
- [Why can't I see the plugin in Premiere after loading it?](#why-cant-i-see-the-plugin-in-premiere-after-loading-it)
- [The macOS binaries trigger security warnings. What should I do?](#the-macos-binaries-trigger-security-warnings-what-should-i-do)
- [Why do I get "Failed to load Addon" with "The specified module could not be found" on Windows?](#why-do-i-get-failed-to-load-addon-with-the-specified-module-could-not-be-found-on-windows)

## Answers

#### Do I need to code sign the entire plugin bundle?

No. Only the macOS `.uxpaddon` executables need to be signed and notarized with a valid Apple Developer ID certificate. The rest of the plugin bundle (JavaScript, HTML, CSS, manifest) does not require code signing.

#### Do I need an Apple Developer ID?

Yes. macOS requires a Developer ID-signed certificate for notarized executables. See [Apple's code signing guide](https://support.apple.com/guide/security/app-code-signing-process-sec3ad8e6e53/web) for details.

#### How do I prepare and test binaries for all architectures?

You need to build and test binaries for macOS arm64, macOS x64, and Windows x64. For building universal macOS binaries, refer to [Apple's guide to building universal binaries](https://developer.apple.com/documentation/apple-silicon/building-a-universal-macos-binary). For platforms not natively available to you, consider using a virtual machine (e.g., VMware Fusion or Parallels). Keep in mind that Apple Silicon Macs cannot virtualize Windows x64—only Intel Macs can. Dedicated hardware may be required to build and test on all three architectures.

#### Are Hybrid plugins forward-compatible?

Yes. A plugin built with an older version of the SDK will continue to work with newer versions of Premiere. However, updating to a new SDK version requires recompiling and republishing your plugin.

#### Why can't I see the plugin in Premiere after loading it?

While loading via UDT, the plugin may not appear automatically. Try unchecking and re-checking the plugin name from the **Window** > **UXP Plugins** menu. This issue is expected to be resolved in a future release.

#### The macOS binaries trigger security warnings. What should I do?

The binaries in the SDK's `template-plugin` are not code signed. On macOS, go to **System Settings** > **Privacy & Security** to allow them to load. For production builds, always sign and notarize your binaries with a valid Apple Developer ID.

#### Why do I get "Failed to load Addon" with "The specified module could not be found" on Windows?

This usually means your `.uxpaddon` was built in Debug mode, which depends on Visual Studio debug runtimes that are not present on end-user systems. It may work on development machines but fail on clean Windows installs. Rebuild the addon in Release mode (and ensure correct project settings, such as `.uxpaddon` output and no debug dependencies) and redistribute it.
