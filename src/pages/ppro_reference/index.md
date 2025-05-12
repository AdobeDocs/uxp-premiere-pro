---
id: "premierepro-api"
title: Premiere Pro API—UXP for Adobe Premiere Pro
description: Learn about the Premiere Pro API that is exposed through UXP for developers of plugins and scripts.
---

# Premiere Pro API

## Overview

The following line allows you access to the Premiere Pro DOM via UXP.

```javascript
const app = require('premierepro');
```

From here, you can open documents, modify them, run menu items, and more.

### Minimum Version

You will now find minimum version information on properties and methods.  This version tag corresponds to the version of Premiere Pro where the member was introduced or last updated significantly.
For properties, you will find a column "MIN VERSION".  For methods, the version number appears as a tag to the right of the name.

## Synchronous vs Asynchronous

An important difference between ExtendScript (and CEP) and UXP in Premiere Pro is that all ExtendScript calls to Premiere Pro were synchronous. This means they blocked the Premiere Pro UI while they were executing. In UXP, a method call is *asynchronous*, and does not block the UI thread.

For a smooth transition between the ExtendScript DOM and the UXP DOM, all properties (get and set) in the API were designed to be *synchronous* and do not need to be awaited. It is worth noting that they are, in the background, asynchronous in nature.

## Working with Premiere Pro Objects

### Premiere Pro Application

Through the [`app`](#overview) object, you can access the rest of Premiere Pro's objects and methods.

The currently-active project is obtained like this:

```javascript
const project = await app.Project.getActiveProject();
```

And you can get the active sequence from the project like this:

```javascript
const sequence = await project.getActiveSequence();
```

## UXP Scripting

UXP is not just for plugins anymore.  Individual JavaScript files may be developed and executed as detailed in the [UXP Scripting section](../uxp-api/).

## Useful links

 - [Typescript Definition File](./types.d.ts)
