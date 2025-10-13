---
title: Premiere DOM APIs
description: Premiere DOM APIs and way to mount it.
keywords:
  - DOM Versions 
  - Premiere DOM
---

# Premiere Pro DOM APIs

Premiere Pro APIs (aka Document Object Model DOM or OMV) are used to create and modify the application document and content.

<InlineAlert variant="info" slots="text1, text2" />

Premiere DOM is available only as a JavaScript module and should be retrieved on a need basis using `require()`.

To access the Premiere DOM APIs, use

```js
const app = require("premierepro");
```

## DOM version

The minimum DOM version needed for UXP development is the same as the minimum required version of Premiere Pro that supports UXP development.
