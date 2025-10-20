---
title: Add Modal Dialogs
description: Create Modal Dialogs
keywords:
  - Modal Dialogs
  - panel entrypoints
  - lifecycle hooks
  - inter-panel communication
  - pluginManager
contributors:
  - https://github.com/undavide
---

# Add Modal Dialogs

Learn how to create a Modal Dialog as a user interface for Commands or as an additional UI for Panels

## Overview

Modal dialogs are temporary windows that appear on top of the main application interface, demanding user attention before they can continue working. Unlike panels, which can be docked alongside Premiere Pro's workspace, **modal dialogs block interaction with the host application until dismissed**—making them ideal for critical decisions, input forms, or alerts that require immediate user response.

In UXP, modal dialogs serve two primary purposes:

1. **Command UIs**: Provide an interface for command entrypoints that don't need a persistent panel but require user input or display information.
2. **Panel dialogs**: Launch additional interfaces from panels to gather input, show settings, or display detailed information without cluttering the main panel.

You'll learn how to:

- Create modal dialogs triggered by command entrypoints
- Display modal dialogs from panel entrypoints
- Control dialog size and behavior
- Handle user input and dialog results

## Key Concepts

Modal dialogs share the same HTML document as your plugin, similar to [multiple panels](../add-panels/index.md), but they **appear as floating windows** that must be closed before the user can interact with Premiere Pro again. This makes them perfect for workflows that require focused user attention—like configuration wizards, confirmation prompts, or data entry forms.

In their simplest form, modal dialogs are just a `<dialog>` element in the HTML document launched with a `uxpShowModal()` method.

![Modal Dialog](./img/add-modal-dialogs--simple-modal.png)

The code below shows a simple modal dialog triggered by a button from the main panel.

<CodeBlock slots="heading, code" repeat="2" languages="HTML, JavaScript" />

#### index.html

```html
<!DOCTYPE html>
<html>
<head>
  <script src="main.js"></script>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <!-- Panel content -->
  <sp-heading>Open Modal Dialog</sp-heading>
  <sp-button id="openDialogBtn">Click</sp-button>

  <!-- Modal dialog content (hidden by default) -->
  <dialog>
    <sp-heading>👋 Hello Modal Dialog!</sp-heading>
    <sp-divider size="L"></sp-divider>
    <sp-body>Modal body content</sp-body>
  </dialog>

</body>
</html>
```

#### main.js

```javascript
const openDialogBtn = document.getElementById("openDialogBtn");
openDialogBtn.addEventListener("click", () => {
  const dialog = document.querySelector("dialog");
  dialog.uxpShowModal({                      // 👈
    title: "Demo Modal Dialog",              // 👈
    resize: "none",                          // 👈
    size: { width: 300, height: 300 },       // 👈
  });                                        // 👈
});
```

### Modal Dialog creation properties

The `uxpShowModal()` method is **asynchronous**, it returns a Promise that resolves with the value passed to `dialog.close()`, and accepts an options object with the following properties.

| Property            | Type                                                   | Description                                    |
| :------------------ | :----------------------------------------------------- | :--------------------------------------------- |
| **title**           | string                                                 | The title of the dialog                        |
| **titleVisibility** | `"show"` \| `"none"`                                   | Whether to show the title                      |
| **resize**          | `"none"` \| `"both"` \| `"horizontal"` \| `"vertical"` | Whether to allow the user to resize the dialog |
| **size**            | `{ width: number; height: number; }`                   | The size of the dialog                         |
| **minSize**         | `{ width: number; height: number; }`                   | The minimum size of the dialog                 |
| **maxSize**         | `{ width: number; height: number; }`                   | The maximum size of the dialog                 |

### Multiple Modal Dialogs

Given how modal dialogs are implemented, nothing prevents you from **adding multiple `<dialog>` elements** in your HTML document, each with its own content; you can reference them by `id` and open them independently using the `uxpShowModal()` method.

![Multiple Modal Dialogs](./img/add-modal-dialogs--multiple-modals.png)

As they're originated from the same Panel and are modal (blocking) dialogs, only one can be open at a time.

<CodeBlock slots="heading, code" repeat="2" languages="HTML, JavaScript" />

#### index.html

```html
<!DOCTYPE html>
<html>
<head>
  <script src="main.js"></script>
  <link rel="stylesheet" href="style.css" />
</head>
<body>

  <sp-heading>Open Modal Dialog</sp-heading>
  <sp-button-group>
    <sp-button id="openFirstDialogBtn">Open First Dialog</sp-button>
    <sp-button id="openSecondDialogBtn">Open Second Dialog</sp-button>
  </sp-button-group>

  <!-- first modal -->
  <dialog id="modal1">
    <sp-heading>👋 Hello Modal Dialog!</sp-heading>
    <sp-divider size="L"></sp-divider>
    <sp-body>Modal body content 1</sp-body>
  </dialog>

  <!-- second modal -->
  <dialog id="modal2">
    <sp-heading>👋 Hello Another Modal Dialog!</sp-heading>
    <sp-divider size="L"></sp-divider>
    <sp-body>Modal body content 2</sp-body>
  </dialog>

</body>
</html>
```

#### main.js

```javascript
const modal1 = document.getElementById("modal1");
const modal2 = document.getElementById("modal2");

documwent.querySelector("#openFirstDialogBtn")
  .addEventListener("click", () => {
    modal1.uxpShowModal({ /* ... options ... */ });
  });

document.querySelector("#openSecondDialogBtn")
  .addEventListener("click", () => {
  modal2.uxpShowModal({ /* ... options ... */ });
});
```

Additionally, you can **chain modal dialogs** by opening a modal dialog from another modal dialog. Just add the relevant UI elements and event handlers to the modal dialog you want to open from. Being chained, both dialogs are open at the same time, but the first one will be blocked until the second is closed.

![](./img/add-modal-dialogs--chained-modals.png)

## Dialog Lifecycle and Event Handling

Modal dialogs can be programmatically closed by calling the `close()` method on the dialog element itself. This method takes an optional value that is returned to the code that called `uxpShowModal()` when the Promise resolves. You can use this value to pass data back to the caller or to signal how the dialog was dismissed.

### Example: Close a Modal Dialog and return a value

In this example, we’ll create a modal dialog with two buttons: **OK** and **Cancel**. When the user clicks either button, the dialog closes and returns the corresponding value—`"ok"` or `"cancel"`.

![Modal Dialog - close event](./img/add-modal-dialogs--close-event.png)

Please note that, in order to capture the returned value, you need to use the `await` keyword when calling `uxpShowModal()` and the "click" event handler on the buttons must be `async`.

<CodeBlock slots="heading, code" repeat="2" languages="HTML, JavaScript" />

#### index.html

```html
<!DOCTYPE html>
<html>
<head>
  <script src="main.js"></script>
  <link rel="stylesheet" href="style.css" />
</head>

<body>
  <sp-heading>Open Modal Dialog</sp-heading>
  <sp-button id="openDialogBtn">Click</sp-button>

  <dialog>
    <sp-heading>👋 Hello Modal Dialog!</sp-heading>
    <sp-divider size="L"></sp-divider>
    <sp-body>Modal body content</sp-body>
    <sp-button-group>
      <sp-button id="closeDialogBtn">OK</sp-button>
      <sp-button id="cancelDialogBtn">Cancel</sp-button>
    </sp-button-group>
  </dialog>

</body>
</html>
```

#### main.js

```javascript
// Modal Dialog reference
const mDialog = document.querySelector("dialog");

// Modal dialog buttons event handlers -----------------------
mDialog?.querySelector("#closeDialogBtn")
  ?.addEventListener("click", (evt) => {
    mDialog.close("ok");
  });
// Cancel button event handler on the modal dialog
mDialog?.querySelector("#cancelDialogBtn")
  ?.addEventListener("click", (evt) => {
    mDialog.close("cancel");
  });

// Open dialog button event handler -------------------------
document
  .querySelector("#openDialogBtn")
  ?.addEventListener("click", async () => {
    console.log("Opening dialog");
    const res = await mDialog?.uxpShowModal({
      title: "Demo Modal Dialog",
      resize: "none",
      size: { width: 300, height: 300 },
    });
    console.log("Dialog closed with:", res); // 👈 "ok", "cancel", or
                                             // 👈 "reasonCanceled"!
  });
```

<InlineAlert variant="warning" slots="header, text" />

Dialog dismissal

When users close the dialog by clicking the **red dot** (Mac) or **X** button (Windows) in the title bar, or by pressing the **Esc** key, the `close()` method is called with the value **`"reasonCanceled"`**. Make sure to handle this value in your code to provide a consistent user experience.

## Modal Dialogs as Command UIs

Modal dialogs are perfect to show a simple interface for a command, when the built-in [`alert()`](../../../uxp-api/reference-js/Global%20Members/HTML%20DOM/alert.md), [`prompt()`](../../../uxp-api/reference-js/Global%20Members/HTML%20DOM/prompt.md) and [`confirm()`](../../../uxp-api/reference-js/Global%20Members/HTML%20DOM/confirm.md) methods are not enough. The example below shows how to create a dialog for an About command.

![Modal Dialog - About dialog](./img/add-modal-dialogs--command-modal.png)

These are often very simple UIs, used to show information about the plugin or copyright data.

### Example: About dialog

<CodeBlock slots="heading, code" repeat="2" languages="JavaScript, json" />

#### main.js

```javascript
const { entrypoints, host, versions } = require("uxp");
const manifest = require("./manifest.json");
const os = require("os");

entrypoints.setup({
  commands: {
    "about-command": async () => {
      // Create the dialog dynamically (or load from an HTML file)
      const dialog = document.createElement("dialog");
      dialog.innerHTML = `
        <sp-heading>Clip Mixer</sp-heading>
        <sp-divider size="L"></sp-divider>
        <sp-body>🙌 Thanks for using Clip Mixer v${manifest.version}!</sp-body>
        <sp-body><b>Application:</b> ${host.name} v${
        host.version
      } (${os.platform()})</sp-body>
        <sp-body><b>UXP Runtime:</b> ${versions.uxp} - <b>Plugin Version:</b> ${
        versions.plugin
      }</sp-body>
      `.trim();
      // ☝ trim is a safety measure to avoid whitespace issues

      document.body.appendChild(dialog);

      // Add styles programmatically using element.style
      dialog.style.color = "white";
      dialog.style.padding = "16px";
      dialog.querySelector("sp-divider").style.margin = "0 0 16px 0";
      dialog.querySelector("sp-heading").style.margin = "0 0 16px 0";

      // Show modal
      await dialog.uxpShowModal({
        title: "Command Modal Dialog",
        resize: "none",
        size: { width: 300, height: 200 },
      });
    },
  },
});
```

#### manifest.json

```json
{
  "id": "Test-modaldialog",
  "name": "Test-modaldialog",
  "version": "1.0.0",
  "main": "main.js",
  "host": { "app": "premierepro", "minVersion": "25.6.0" },
  "manifestVersion": 5,
  "entrypoints": [
    {
      "id": "about-command",
      "type": "command",
      "label": "About..."
    }
  ],
  "icons": [ /* ... icons ... */ ],
}
```

In the example above, the `about-command` is defined in the `entrypoints` array of the `manifest.json` file and implemented via `entrypoints.setup()` in the `main.js` file—see [this guide](../../concepts/entrypoints/index.md#commands-and-panels) if you need a refresher on Commands concepts, and [this tutorial](../add-commands/index.md) for implementation examples.

Also note that the entire UI is created with a mix of JavaScript methods (for the parent `<dialog>` element and the styling), and Template Literals for easier readability.

<InlineAlert variant="info" slots="header, text" />

Trim Template Literals

When using Template Literals for the `dialog.innerHTML` property, it's a good practice to use the `trim()` method to remove any whitespace from the beginning and end of the string, which would otherwise create problems.

## Load external HTML files

To keep your code organized, you can load the HTML content from an external file. In UXP, it is extremely easy to do so using the `fetch()` method; just make sure to handle the response as a text string and remember that the methods are asynchronous. Using the same structure from the previous example, we can load the HTML content from an external file and use it to fill the `dialog.innerHTML` property.

<CodeBlock slots="heading, code" repeat="3" languages="JavaScript, html, json" />

#### main.js

```javascript
const { entrypoints, host, versions } = require("uxp");
const manifest = require("./manifest.json");
const os = require("os");

entrypoints.setup({
  commands: {
    "about-command": async () => {
      // Load the HTML content from an external file
      // In this case, the _dialog.html file is located in the
      // same directory as the main.js file
      const dialogHtml = await fetch("./_dialog.html") // 👈
        .then((res) => res.text())    // 👈 handle the response as text
      console.log("About command");
      const dialog = document.createElement("dialog");
      dialog.innerHTML = dialogHtml.trim();
      // ...
      // Replace the placeholders with the actual values. It is the
      // equivalent of using Template Literals in the previous example
      dialog.querySelector("#version").textContent = manifest.version;
      dialog.querySelector("#app-name").textContent = host.name;
      dialog.querySelector("#app-version").textContent = host.version;
      dialog.querySelector("#platform").textContent = os.platform();
      dialog.querySelector("#uxp-version").textContent = versions.uxp;
      dialog.querySelector("#plugin-version").textContent = versions.plugin;
      // ...
      document.body.appendChild(dialog);
      // ...
      const result = await dialog.uxpShowModal({ /* ... */ });
    }
  }
});
```

#### \_dialog.html

```html
<sp-heading>Clip Mixer</sp-heading>
<sp-divider size="L"></sp-divider>
<sp-body>🙌 Thanks for using Clip Mixer v<span id="version"></span>!</sp-body>
<sp-body><b>Application:</b> <span id="app-name"></span> v<span id="app-version"></span> (<span id="platform"></span>)</sp-body>
<sp-body><b>UXP Runtime:</b> <span id="uxp-version"></span> - <b>Plugin Version:</b> <span id="plugin-version"></span></sp-body>
```

#### manifest.json

```json
{
  "id": "Test-modaldialog",
  "name": "Test-modaldialog",
  "version": "1.0.0",
  "main": "main.js",
  "host": { "app": "premierepro", "minVersion": "25.6.0" },
  "manifestVersion": 5,
  "entrypoints": [
    {
      "id": "about-command",
      "type": "command",
      "label": "About..."
    }
  ],
  "icons": [ /* ... icons ... */ ],
}
```

Compared to the [previous example](#example-about-dialog), in this one it is slightly more tedious to fill the dialog with values: with Template Literals you can use the `${}` syntax to insert the values directly into the string, but with external HTML files you need to use the `querySelector()` method to select the `<span>` elements and set the values programmatically.

Please note that the `"main"` property in the `manifest.json` file is still set to `"main.js"`, a JavaScript file—even if we are loading the dialog content from an external `.html` file.

<InlineAlert variant="info" slots="header, text, text2" />

Use `fetch()` and `require()` with external files

In the [original About dialog example](#example-about-dialog), we used `require()` to import the `manifest.json` file and extract the plugin version. This is a handy trick to access the plugin's metadata from the `main.js` file; in general, `require()` works for any `.js` and `.json` files that are local to the plugin.

For all other file formats, you may use the `fetch()` or the `fs` methods illustrated in the [Working with the file system](../../../resources/recipes/filesystem-operations/index.md#the-fs-module) tutorial.

## Class pattern for Modal Dialogs

For complex dialogs, we recommend using a Class pattern to encapsulate the dialog logic and UI. This approach allows you to separate the dialog creation, initialization, and running logic in an efficient and maintainable way. The skeleton of the Class is as follows.

```javascript
class ModalDialog {
  // Private property to store the dialog element
  #dialog;

  // Use it to inject libraries if needed
  constructor() {}

  // Create the dialog's User Interface
  // Assign to #dialog
  createDialog() { /* ... */ }

  // Populate with default values
  // Attach event listeners
  initDialog() { /* ... */ }

  // Run the dialog (return a Promise)
  async runDialog() {}

  // Private member
  // Run the Host App DOM code if needed
  async #runRoutine() {}
}

// Example usage
try {
  const modalDialog = new ModalDialog();
  modalDialog.createDialog();
  modalDialog.initDialog();
  const res = await modalDialog.runDialog();
  res;
} catch (error) {
  console.error("Argh!", error);
}
```

A brief explanation of the properties and methods is as follows.

- `#dialog`: a private property that stores the dialog element. Used internally to access the `close()` method.
- `constructor()`: optional; can be used to inject dependencies or external libraries.
- `createDialog()`: builds the dialog's user interface and assigns the resulting element to the `#dialog` property.
- `initDialog()`: initializes the dialog by setting default values and attaching event listeners (e.g., button clicks, form changes, focus/blur events, etc.).
- `runDialog()`: displays the dialog and returns a Promise that resolves with the value provided to the `close()` method. Internally calls `#runRoutine()` to execute Host App DOM logic, passing dialog data as needed.
- `#runRoutine()`: a private method that runs Host App DOM code when required.

### Example

WIP
