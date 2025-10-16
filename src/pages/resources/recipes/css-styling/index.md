---
title: CSS Styling
description: Style your plugin's user interface using CSS classes, inline styles, or JavaScript
keywords:
  - CSS
  - styling
  - UI
  - Spectrum
contributors:
  - https://github.com/padmkris123
  - https://github.com/undavide
---

# CSS Styling

Style your plugin's user interface using CSS classes, inline styles, or JavaScript

UXP supports standard CSS for styling your plugin's interface. You can apply styles using **CSS classes**, **inline styles**, or **JavaScript**—choose the approach that fits your workflow best.

## Prerequisites

Before you begin, make sure your development environment uses the following versions:

- **Premiere Pro v25.6** or higher
- **UDT v2.2** or higher
- **Manifest version v5** or higher

## Three Ways to Apply Styles

<CodeBlock slots="heading, code" repeat="3" languages="HTML, JavaScript, CSS" />

#### index.html

```html
<!-- 1. Using CSS classes -->
<div class="green-background">
  <h1>Styled with CSS class</h1>
</div>

<!-- 2. Using inline styles -->
<div style="background-color: yellow;">
  <h1>Styled inline</h1>
</div>

<!-- 3. Using JavaScript -->
<div id="exampleDiv">
  <h1>Styled with JavaScript</h1>
</div>
```

#### index.js

```js
// Apply styles via JavaScript
const exampleDiv = document.getElementById("exampleDiv");
exampleDiv.style.backgroundColor = "orange";
```

#### styles.css

```css
/* Define styles in a stylesheet */
.green-background {
  background-color: green;
}
```

## Important Considerations

<InlineAlert variant="warning" slots="header, text"/>

UXP is not a browser

UXP does not support all CSS properties. For example, CSS Grid Layout is not available. Check the [CSS reference](../../../uxp-api/reference-css/) for a complete list of supported properties.

### CSS Preprocessors

UXP only understands standard CSS. If you want to use preprocessors like **Sass** or **SCSS**, you must transpile them to CSS before bundling your plugin. This requires build tools like Webpack and a slightly different [debugging workflow](../../../plugins/tutorials/udt-deep-dive/plugin-workflows.md#working-with-bundlers).

### Use Spectrum for Consistency

We recommend using [Spectrum](../../fundamentals/user-interfaces/index.md#spectrum-web-components-swc) for UI elements whenever possible. Spectrum is Adobe's design system and provides a consistent look and feel across all Adobe applications.

## Reference Material

- [CSS Reference](../../../uxp-api/reference-css/index.md): complete list of supported CSS properties.
- [Spectrum Web Components](../../../uxp-api/reference-spectrum/index.md) Reference.
