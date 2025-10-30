---
title: HTML Events and Listeners
description: Handle user interactions using event listeners in JavaScript or inline event handlers
keywords:
  - events
  - event listeners
  - click
  - addEventListener
contributors:
  - https://github.com/padmkris123
  - https://github.com/undavide
---

# HTML Events and Listeners

Handle user interactions using event listeners in JavaScript or inline event handlers

UXP supports standard HTML events for handling user interactions like clicks, input changes, and keyboard actions. You can attach event listeners in **JavaScript** (recommended) or use **inline event handlers** in HTML (requires additional permissions).

## Prerequisites

Before you begin, make sure your development environment uses the following versions:

- **Premiere Pro v25.6** or higher
- **UDT v2.2** or higher
- **Manifest version v5** or higher

## Example: JavaScript Event Listeners (Recommended)

The recommended approach is to attach event listeners in JavaScript using `addEventListener()` or by assigning event handler properties.

<CodeBlock slots="heading, code" repeat="2" languages="HTML, JavaScript" />

#### index.html

```html
<button id="firstButton">Click me</button>
<button id="secondButton">Click me too</button>
```

#### index.js

```js
// Method 1: addEventListener (recommended)
const firstButton = document.getElementById("firstButton");
firstButton.addEventListener("click", handleClick);

// Method 2: Event handler property
const secondButton = document.getElementById("secondButton");
secondButton.onclick = handleClick;

function handleClick(event) {
  console.log(`Button clicked: ${event.target.id}`);
}
```

<InlineAlert variant="info" slots="text"/>

Using `addEventListener()` is preferred because it allows multiple event listeners on the same element and provides better control over event handling.

## Example: Inline Event Handlers

You can define event handlers directly in HTML attributes, but this requires enabling a special permission.

<CodeBlock slots="heading, code" repeat="3" languages="HTML, JavaScript, JSON" />

#### index.html

```html
<button id="thirdButton" onclick="handleClick(event)">Click me</button>
```

#### index.js

```js
function handleClick(event) {
  console.log(`Button clicked: ${event.target.id}`);
}
```

#### manifest.json

```json
{
  // ...
  "requiredPermissions": {
    "allowCodeGenerationFromStrings": true
  }
  // ...
}
```

<InlineAlert variant="warning" slots="header, text"/>

Security consideration

The `allowCodeGenerationFromStrings` permission allows code execution from strings, which can introduce security risks. Only enable this if inline event handlers are essential to your plugin's architecture.

## Common Event Types

UXP supports standard HTML events:

| Event Type | Fires When                          | Common Use Cases                     |
| :--------- | :---------------------------------- | :----------------------------------- |
| `click`    | Element is clicked                  | Buttons, links, interactive elements |
| `input`    | Input value changes                 | Text fields, sliders, checkboxes     |
| `change`   | Input value changes and loses focus | Dropdowns, file inputs               |
| `submit`   | Form is submitted                   | Forms                                |
| `keydown`  | Key is pressed                      | Keyboard shortcuts                   |
| `keyup`    | Key is released                     | Text input validation                |
| `focus`    | Element receives focus              | Input fields                         |
| `blur`     | Element loses focus                 | Input validation                     |

## Working with Spectrum Components

Event listeners work the same way with Spectrum Web Components:

```js
// Spectrum button
const button = document.querySelector("sp-button");
button.addEventListener("click", () => {
  console.log("Spectrum button clicked");
});

// Spectrum slider
const slider = document.querySelector("sp-slider");
slider.addEventListener("input", (event) => {
  console.log(`Slider value: ${event.target.value}`);
});
```

## Reference Material

- [HTML Events](../../../uxp-api/reference-js/Global%20Members/HTML%20Events/): complete list of supported events.
- [Manifest Permissions](../../../plugins/concepts/manifest/index.md#permissionsdefinition): overview of all permissions.
