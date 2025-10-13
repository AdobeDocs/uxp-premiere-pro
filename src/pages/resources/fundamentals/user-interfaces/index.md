---
keywords:
  - Spectrum UXP Reference
  - Spectrum Web Components
  - SWC
  - Web Components
  - Spectrum differences
  - Spectrum in UXP
  - UI
  - User interface
title: Building User Interfaces in UXP
description: Learn about the three ways to create user interfaces in UXP plugins
contributors:
  - https://github.com/padmkris123
  - https://github.com/undavide
---

# User Interfaces

Learn how to create beautiful and functional user interfaces for your UXP plugins

## Overview

Every UXP plugin with a visual component needs a user interface. Whether you're building a simple dialog or a complex panel, UXP gives you multiple ways to create UI that looks and feels like a native part of Premiere Pro.

UXP provides three approaches for building user interfaces:

1. [**Standard HTML Elements**](#standard-html-elements): familiar web technologies with custom styling.
2. [**Spectrum UXP Widgets**](#spectrum-uxp-widgets): built-in, Adobe-styled components that work out of the box.
3. [**Spectrum Web Components (SWC)**](#spectrum-web-components-swc): modern Web Component library with Adobe's design system.

Each approach has its strengths and you can mix and match them in the same plugin—although we recommend using Spectrum Web Components going forward for the most complete feature set and future support. Let's explore each option to help you choose the right tools for your project.

## Understand the Options

Before diving into the technical details, it's helpful to understand some key terminology:

- [**Spectrum**](https://spectrum.adobe.com/): Adobe's open-source design language[^1] and guidelines that ensure consistency across applications.
- [**Web Components**](https://developer.mozilla.org/en-US/docs/Web/API/Web_components): A set of HTML5 technologies that let you create custom, reusable HTML elements.
- [**Adobe Spectrum Web Components**](https://opensource.adobe.com/spectrum-web-components/) (SWC): An open-source library of pre-built Web Components styled according to Spectrum design guidelines.

[^1]: Adobe is working on the second iteration of the Spectrum design system; more information can be found [here](https://s2.spectrum.adobe.com/).

### Standard HTML Elements

These are the familiar HTML elements you've likely used before: `<div>`, `<button>`, `<input>`, `<img>`, `<dialog>`, and more. They follow web standards and give you complete control over styling through CSS.

```html
<div class="container">
  <button class="primary-button">Click me</button>
  <input type="text" placeholder="Enter text" />
</div>
```

**Best for**: Developers who prefer full control over styling, or when building highly custom interfaces.

<InlineAlert variant="warning" slots="header, text" />

UXP is not a browser

While UXP supports modern web technologies, it's not a full browser environment. Not all HTML elements, CSS properties, or JavaScript APIs available in browsers will work in UXP. Check the list of [unsupported HTML elements](../../../uxp-api/reference-html/General/Unsupported%20Elements.md) and [unsupported attributes](../../../uxp-api/reference-html/General/Unsupported%20Attributes.md) for details.

### Spectrum UXP Widgets

Spectrum UXP Widgets are built directly into the UXP platform. They provide ready-to-use, Adobe-styled components that automatically match Premiere Pro's look and feel, including dark and light theme support.

```html
<sp-button variant="primary">I'm a Spectrum button</sp-button>
<sp-textfield placeholder="Enter your name"></sp-textfield>
<sp-checkbox>Enable feature</sp-checkbox>
```

These widgets are immediately available—no installation or imports required. Just use them like any other HTML tag.

**Best for**: Quick prototyping, getting started with UXP, or when you want Premiere Pro's native look without extra setup.

**Trade-offs**: Since these components are built into UXP, they're somewhat of a "black box." You can't easily inspect their internal structure or deeply customize their behavior beyond the provided API.

### Spectrum Web Components (SWC)

[Spectrum Web Components](https://opensource.adobe.com/spectrum-web-components/) are Adobe's official implementation of the Spectrum Design System using modern [Web Component standards](https://developer.mozilla.org/en-US/docs/Web/API/Web_components). They offer the most complete feature set and the closest adherence to Spectrum guidelines.

To use SWCs, you need to [install each component](https://opensource.adobe.com/spectrum-web-components/getting-started/) individually via `npm` or `yarn` and import it in your code:

```bash
npm install @spectrum-web-components/button@0.37.0
npm install @spectrum-web-components/textfield@0.37.0
```

Then import and use them in your JavaScript:

```javascript
import '@spectrum-web-components/button/sp-button.js';
import '@spectrum-web-components/textfield/sp-textfield.js';
```

```html
<sp-button variant="primary">I'm a SWC button</sp-button>
<sp-textfield placeholder="Enter your name"></sp-textfield>
```

<InlineAlert variant="info" slots="header, text" />

Version Requirement

For Premiere Pro plugins, **all Spectrum Web Components must be locked to version 0.37.0** for the time being. This ensures compatibility with the current UXP version.

**Best for**: Production plugins that need the full range of Spectrum components, or when you need to inspect and debug component internals.

**Trade-offs**: Requires Node.js, a package manager (npm/yarn), and a bundler (Webpack, Rollup, etc.) to build your plugin. You'll also need to enable SWC in your `manifest.json`:

```json
{
  "featureFlags": {
    "enableSWCSupport": true
  }
}
```

## Mix and Match

The best part? You can combine all three approaches in a single plugin. UXP seamlessly supports mixing HTML elements, Spectrum UXP Widgets, and Spectrum Web Components:

```html
<form>
  <!-- Standard HTML element -->
  <div class="section">
    <!-- Spectrum Web Component -->
    <sp-banner>
      <div slot="header">Welcome</div>
      <div slot="content">This is a mixed UI example</div>
    </sp-banner>

    <!-- Spectrum UXP Widget -->
    <sp-button variant="primary">Submit</sp-button>
  </div>
</form>
```

This flexibility lets you use the right tool for each part of your interface.

## Which Approach Should You Choose?

Your choice depends on your project requirements, timeline, and experience level.

#### Start with Spectrum UXP Widgets if you:

- Are new to UXP development
- Want to quickly prototype an idea
- Need a simple UI with standard components
- Prefer zero configuration

#### Use Spectrum Web Components if you:

- Are building a production plugin
- Need access to the full Spectrum component library
- Want to inspect and debug component internals
- Are comfortable with npm and build tools

#### Use Standard HTML Elements if you:

- Need highly custom UI components
- Have specific design requirements beyond Spectrum
- Are comfortable writing custom CSS
- Want maximum control over styling and behavior

For most projects, **we recommend starting with Spectrum Web Components**, and using standard HTML elements for very specific custom needs. UXP Widgets are still supported but may be deprecated in the future.

<InlineAlert variant="info" slots="header, text, text2" />

Creative Cloud Marketplace and Visual Language

You are free to use your own visual language in UXP plugins. At the moment, products sent for approval to the Creative Cloud Marketplace don't need to implement the Adobe Spectrum Design System, although we recommend it for consistency.

Best UX practices, as well as adherence to the Adobe Brand Guidelines, [will be enforced](../../distribution/review/index.md) during the approval process.

## Working with JavaScript Frameworks

While vanilla JavaScript, HTML, and CSS are sufficient for many plugins, complex applications can benefit from modern JavaScript frameworks. UXP plugins [work well](../../../plugins/tutorials/udt-deep-dive/plugin-workflows.md#working-with-bundlers) with popular frameworks like **React**, **Vue**, and **Svelte**.

These frameworks help you manage complex state, create reusable components, and build more maintainable code. However, they require additional setup including Node.js, package managers, and build tools.

If you're already familiar with React or plan to build a complex plugin, check out the [Using Spectrum with React](../../../uxp-api/reference-spectrum/Spectrum%20UXP%20Widgets/Using%20with%20React.md) guide for tips on integrating Spectrum components with React.

## Reference Documentation

Ready to start building? Explore the complete documentation for each UI approach.

- **[Spectrum Web Components](../../../uxp-api/reference-spectrum/swc/)**: full SWC component library and usage examples.
- **[Spectrum UXP Widgets](../../../uxp-api/reference-spectrum/Spectrum%20UXP%20Widgets/)**: built-in widget reference and API documentation.
- **[HTML Elements](../../../uxp-api/reference-js/Global%20Members/HTML%20Elements/)**: supported HTML elements in UXP.
- **[HTML Tags Reference](../../../uxp-api/reference-html/)**: complete HTML tag documentation.
- **[Using Spectrum with React](../../../uxp-api/reference-spectrum/Spectrum%20UXP%20Widgets/Using%20with%20React.md)**: integration guide for React developers (see also the [Working with Bundlers](../../../plugins/tutorials/udt-deep-dive/plugin-workflows.md#working-with-bundlers) section of the UXP Developer Tool documentation).

For practical examples and working code, explore the [CSS Styling recipe](../../recipes/css-styling/) to learn how to customize your plugin's appearance.
