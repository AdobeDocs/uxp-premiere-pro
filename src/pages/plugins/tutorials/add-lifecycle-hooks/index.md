---
title: Plugin Lifecycle Hooks
description: Use plugin life cycle events to carry out load/unload routines
keywords:
  - plugin hooks
  - lifecycle
contributors:
  - https://github.com/padmkris123
  - https://github.com/undavide
---

# Add Lifecycle Hooks

Learn how to respond to plugin and panel events

## Overview

As we have seen in the [Entrypoints concept guide](../../concepts/entrypoints/index.md#plugin-lifecycle-hooks), lifecycle hooks are callback functions that are automatically invoked when specific events occur during the lifecycle of a Plugin or a Panel. They are optional and can be used to perform, for example, any setup or teardown logic.

<InlineAlert variant="info" slots="text"/>

This guide is only **applicable to Plugins with at least one Panel**; there are no hooks related to Commands. Read [here](../../concepts/panels-and-commands/index.md#key-differences) if you need a refresher on the difference between a Command and a Panel.

## Hook Types

UXP provides two kinds of lifecycle hooks:

- At a **Plugin level**, respectively invoked when the plugin container itself is created and destroyed: `create()` and `destroy()`.
- At a **Panel level**, respectively invoked when the panel is created, shown, hidden, and destroyed: `create()`, `show()`, `hide()`, and `destroy()`.

More details on the types of hooks can be found in the [Entrypoints concept guide](../../concepts/entrypoints/index.md#plugin-lifecycle-hooks).

<InlineAlert variant="error" slots="header, text, text2" />

Current limitations

The `hide()` and `destroy()` hooks are **not working as expected yet** in Premiere Pro; this will be fixed in a future update.

For plugins with multiple panels, **lifecycle hooks currently fire for all panels** without distinguishing between them

## Implementation

Hooks are implemented in the `entrypoints.setup()` method, which accepts an object with the following properties:

- `plugin`: An object with the plugin lifecycle hooks.
- `panels`: An object with one property for each `"panel"` entrypoint declared in the `manifest.json`—using the panel IDs as property names, and objects with the panel lifecycle hooks as values.

Promises are allowed for most callbacks, as demonstrated in the following example. Panel hooks receive a `rootNode` parameter; it's the HTML document root node, which can be used to programmatically append or remove an appropriate container element in a multiple panels scenario.

### Example

<CodeBlock slots="heading, code" repeat="2" languages="JavaScript, JSON" />

#### index.js

```js
const { entrypoints } = require("uxp");
entrypoints.setup({
  plugin: {
    create() {
      console.log("Plugin create hook");
    },
    destroy() {
      return new Promise(function (resolve, reject) {
        console.log("Plugin destroy hook");
        resolve();
      });
    },
  },
  panels: {
    firstPanel: { // 👈 matches the panel ID from manifest.json
      create(rootNode) {
        return new Promise(function (resolve, reject) {
          console.log("Panel create hook", rootNode);
          resolve();
        });
      },
      show(rootNode, data) {
        return new Promise(function (resolve, reject) {
          console.log("Panel show hook", data);
          resolve();
        });
      },
      hide(rootNode, data) {
        return new Promise(function (resolve, reject) {
          console.log("Panel hide hook", data);
          resolve();
        });
      },
      destroy(rootNode) {
        return new Promise(function (resolve, reject) {
          console.log("Panel destroy hook", rootNode);
          resolve();
        });
      },
    },
  },
});

```

#### manifest.json

```json
{
  // ...
  "entrypoints": [
    {
      "type": "panel",
      "id": "firstPanel",
      "label": "My plugin",
      "minimumSize": { "width": 400, "height": 400 },
      "maximumSize": { "width": 800, "height": 800 },
      "preferredDockedSize": { "width": 400, "height": 400 },
      "preferredFloatingSize": { "width": 600, "height": 600 }
    }
  ],
  // ...
}
```

## Summary

Lifecycle hooks are callback functions that automatically execute during specific plugin and panel events, enabling setup and teardown logic for UXP plugins in Adobe Premiere Pro.

**Key Concepts:**

1. **Plugin-level hooks**: `create()` and `destroy()` are triggered when the plugin container is created/destroyed.
2. **Panel-level hooks**: `create()`, `show()`, `hide()`, and `destroy()` are triggered during panel lifecycle events.
3. **Implementation**: Use `entrypoints.setup()` with `plugin` and `panels` objects to define hooks. Promises are allowed for most callbacks.
4. **Known limitations**: `hide()` and `destroy()` hooks are not working as expected in Premiere Pro (will be fixed in future updates). For multi-panel plugins, lifecycle hooks currently fire for all panels without distinction.
