---
title: JavaScript Modules
description: Learn how to organize and import JavaScript modules in UXP plugins
keywords:
  - JavaScript modules
  - require statement
  - module.exports
  - code organization
contributors:
  - https://github.com/padmkris123
  - https://github.com/undavide
---

# JavaScript Modules

Learn how to organize your plugin code across multiple JavaScript files using modules

## Overview

UXP plugins support modular JavaScript development, allowing you to organize your code across multiple files for better maintainability and structure. This is particularly valuable for complex plugins where separating functionality into distinct modules improves code organization and reusability.

UXP uses the CommonJS module system with `require()` statements for importing modules and `module.exports` for exporting functionality.

## Implementation

### Exporting Modules

To make functions, objects, or variables available to other files, use `module.exports` in your module file:

<CodeBlock slots="heading, code" repeat="1" languages="JavaScript" />

#### utils.js

```js
// Export individual functions
function multiply(a, b) {
    return a * b;
}

function getAnswer() {
    return 42;
}

// Export an object containing all functions
module.exports = {
    multiply,
    getAnswer
};
```

### Importing Modules

Use the `require()` statement to import modules into your main file or other modules:

<CodeBlock slots="heading, code" repeat="1" languages="JavaScript" />

#### index.js

```js
// Import the entire module object
const utils = require("./utils.js");
const result = utils.multiply(3, 2); // returns 6

// Or use destructuring to import specific functions
const { multiply, getAnswer } = require("./utils.js");
const answer = getAnswer(); // returns 42
```

### Directory Structure

You can organize modules in subdirectories using relative paths:

```
my-plugin/
├── index.js
├── lib/
│   ├── calculations.js
│   └── helpers.js
└── components/
    └── ui-elements.js
```

<CodeBlock slots="heading, code" repeat="1" languages="JavaScript" />

#### index.js

```js
// Import from subdirectories
const { calculate } = require("./lib/calculations.js");
const { createButton } = require("./components/ui-elements.js");
```

<InlineAlert variant="info" slots="header, text" />

Path Requirements

The `require()` function in UXP uses relative paths and doesn't search global paths. Always specify the complete relative path from the current file to the target module, including the `.js` extension.

## Example

Here's a practical example of a plugin that uses multiple modules to organize different aspects of functionality:

<CodeBlock slots="heading, code" repeat="3" languages="JavaScript, JavaScript, JavaScript" />

#### index.js

```js
const { entrypoints } = require("uxp");
const { processVideo } = require("./lib/video-processor.js");
const { showNotification } = require("./lib/ui-helpers.js");

entrypoints.setup({
    commands: {
        processCommand: async () => {
            try {
                await processVideo();
                showNotification("Video processing completed!");
            } catch (error) {
                showNotification("Error: " + error.message);
            }
        }
    }
});
```

#### lib/video-processor.js

```js
async function processVideo() {
    // Video processing logic here
    console.log("Processing video...");
    // Simulate async operation
    return new Promise(resolve => setTimeout(resolve, 1000));
}

function getVideoInfo() {
    // Return video information
    return { duration: 120, format: "mp4" };
}

module.exports = {
    processVideo,
    getVideoInfo
};
```

#### lib/ui-helpers.js

```js
function showNotification(message) {
    console.log(`Notification: ${message}`);
    // Additional UI notification logic
}

function createProgressBar() {
    // Progress bar creation logic
    return document.createElement("progress");
}

module.exports = {
    showNotification,
    createProgressBar
};
```

## Summary

JavaScript modules in UXP plugins enable better code organization and maintainability by allowing you to split functionality across multiple files.

**Key Concepts:**

1. **Module exports**: Use `module.exports` to expose functions, objects, or variables from a module file.
2. **Module imports**: Use `require()` with relative paths to import modules into other files.
3. **Directory structure**: Organize modules in subdirectories using relative paths for better project structure.
4. **Path requirements**: Always specify complete relative paths including the `.js` extension—UXP doesn't search global paths.
