---
title: Debugging
description: Simple ways to debug in UXP
keywords:
  - console
  - alerts
contributors:
  - https://github.com/padmkris123
---

# Debugging

While writing complex logic, you might be in the cycle of testing/debugging your code. Although UDT -> Debug lets you set breakpoints and debug your code using Chrome Debug Tool, these couple of techniques may also prove handy.

## System requirements

Please make sure your local environment uses the following application versions before proceeding.

- Premiere Pro v25.1 or higher
- UDT v2.1.0 or higher
- Manifest version v5 or higher

## Console logs

<CodeBlock slots="heading, code" repeat="1" languages="JavaScript" />

#### JavaScript

```js
async function foo() {
    console.log("foo"); // writes "foo" to the UXP Developer Tool console.
    console.error("foo error"); // does the same thing, but the text is shown in red so errors are more easily seen.
}
```

## Alerts

Use [alert()](../../../uxp-api/reference-js/Global%20Members/HTML%20DOM/alert.md), [prompt()](../../../uxp-api/reference-js/Global%20Members/HTML%20DOM/prompt.md) and [confirm()](../../../uxp-api/reference-js/Global%20Members/HTML%20DOM/confirm.md)in UXP
