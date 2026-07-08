---
id: "premierepro-api"
title: Premiere API—UXP for Adobe Premiere
description: Learn about the Premiere API that is exposed through UXP for developers of plugins and scripts.
---

# Premiere API

## Overview

The following line allows you access to the Premiere DOM via UXP.

```javascript
const app = require('premierepro');
```

From here, you can open documents, modify them, run menu items, and more.

### Minimum Version

You will now find minimum version information on properties and methods. This version tag corresponds to the version of Premiere where the member was introduced or last updated significantly.
For properties, you will find a column "MIN VERSION". For methods, the version number appears alongside the documentation for the method.

## Synchronous vs Asynchronous

An important difference between ExtendScript (and CEP) and UXP in Premiere is that all ExtendScript calls to Premiere were synchronous. This means they blocked the Premiere UI while they were executing. In UXP, a method call is *asynchronous*, and does not block the UI thread.

For a smooth transition between the ExtendScript DOM and the UXP DOM, all properties (get and set) in the API were designed to be *synchronous* and do not need to be awaited. It is worth noting that they are, in the background, asynchronous in nature.

## Working with Premiere Objects

### Premiere Application

Through the `app` object, you can access the rest of Premiere's objects and methods.

The currently-active project is obtained like this:

```javascript
const project = await app.Project.getActiveProject();
```

And you can get the active sequence from the project like this:

```javascript
const sequence = await project.getActiveSequence();
```

You can find more details about the available [classes](classes/index.md) and [constants](constants/index.md) of the `app` object, as well as the various [events](events/index.md) that can be listened for, at their respective subpages.

## Useful links

 - [TypeScript Declarations](https://github.com/adobe/premierepro-types)
