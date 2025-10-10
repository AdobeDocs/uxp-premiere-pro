---
title: Plugin concepts
description: Core ideas behind the UXP plugin architecture in Premiere Pro
keywords:
  - UXP plugin concepts
  - plugin architecture
  - plugin manifest
  - plugin entrypoints
contributors:
  - https://github.com/padmkris123
  - https://github.com/undavide
---

# Concepts

Before diving into plugin development, it helps to understand how UXP Plugins are structured and how they connect to Premiere Pro

Every UXP plugin is built around two fundamental concepts:

- **The Manifest** — a JSON file that defines your plugin's identity, capabilities, permissions, and entrypoints.
- **Entrypoints** — the executable touchpoints (commands and panels) that expose your plugin's functionality inside Premiere Pro.

Together, these define how your plugin is discovered, loaded, and interacted with by users and the host application.  
Understanding these concepts will help you plan your plugin's architecture, manage lifecycle events, and integrate seamlessly with the UXP environment.

Explore the following guides to learn more:

- [**Entrypoints**](./entrypoints/index.md): Declaring, wiring, and handling your plugin's panels and commands.
- [**Manifest**](./manifest/index.md): Structure and configuration of the `manifest.json` file.
