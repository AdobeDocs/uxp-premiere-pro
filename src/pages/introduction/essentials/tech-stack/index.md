---
title: UXP Development Tech Stack
description: Essential tools, technologies, and programming languages you need to master for successful UXP plugin development
keywords:
  - Learning resources
  - JavaScript
  - HTML
  - CSS
  - System requirements
  - JavaScript frameworks
  - Debugging
contributors:
  - https://github.com/padmkris123
  - https://github.com/undavide
---

# Tech Stack Foundations

Learn about the essential technologies you need to be familiar with to develop UXP plugins

## Programming Languages

To begin, a basic understanding of web technologies like **JavaScript, HTML, and CSS** is essential. There are excellent resources available online that can teach you the fundamentals. Here are some of our recommendations, but feel free to explore other sources as well.

<InlineAlert slots="text" />

Most tutorials assume that you are using Web technologies in a browser or a server-side JS engine like Node.js. While it supports modern JavaScript syntax, **UXP is not a standard browser environment**; not all the HTML Elements, CSS classes, or JavaScript APIs will be available in the UXP world.

### Reading Materials

Start by getting acquainted with the basics of JS, HTML, and CSS.

- [Introduction to JavaScript](https://javascript.info/intro) and its [basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
- [JavaScript versions](https://www.w3schools.com/js/js_versions.asp) and [ECMAScript 2015 (ES6)](https://www.w3schools.com/js/js_es6.asp)
- [HTML Basics](https://www.w3schools.com/html/html_intro.asp)
- [CSS Basics](https://www.w3schools.com/css/css_intro.asp), [syntax](https://www.w3schools.com/css/css_syntax.asp), and [selectors](https://www.w3schools.com/css/css_selectors.asp)

Apart from the basics, the following additional topics will also come in handy. You need not go through each of them right away, but do bookmark them for later as it will help you understand the code snippets much more easily.

- [Document Object Model or HTML DOM](https://eloquentjavascript.net/14_dom.html) and the global [window](https://www.w3schools.com/jsref/obj_window.asp) and [document](https://www.w3schools.com/jsref/prop_win_document.asp) object
- [DOM Events](https://javascript.info/introduction-browser-events)
- [Adding CSS](https://www.w3schools.com/css/css_howto.asp)
- [CSS layout using Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- [Promises](https://javascript.info/promise-basics)
- [Async/await](https://javascript.info/async-await)
- Different ways of declaring JavaScript functions: [traditional style](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function) vs. [fat arrow](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)

## Debugging

One of the easiest ways to identify issues with these technologies is by using the Chrome browser's Debug Tool (CDT). The [UXP Developer Tool](../dev-tools/index.md#uxp-developer-tool-udt) (UDT) implements the same engine for debugging; a high-level understanding of CDT will be very useful skill to possess.

Familiarize yourself with the [Chrome Debug tool](https://developer.chrome.com/docs/devtools/overview/), especially the ways to [access DOM](https://developer.chrome.com/docs/devtools/dom/), [modify CSS](https://developer.chrome.com/docs/devtools/css/) and [debug JavaScript](https://developer.chrome.com/docs/devtools/javascript/) by adding breakpoints.

## Frameworks

Besides JavaScript, HTML, and CSS, the industry offers various **frameworks that act as an abstract layer on top of Web technologies**, aiming to provide you with a quicker, and more efficient way of writing reusable code.

[React](https://react.dev/), [Vue](https://vuejs.org/), [Angular](https://angular.io/), and [Svelte](https://svelte.dev/) are among the most popular options. Using these frameworks is optional and is your personal choice.

Any additional tool that expands the capabilities of Vanilla (i.e., plain) JavaScript will require additional tools to run:

- [Node.js](https://nodejs.org/en/): a **JavaScript runtime environment**, also used as a backend server in Web environments. Go to the [Node.js download page](https://nodejs.org/en/download/), download the installer for your platform, and run it. This will also install `npm`.
- [`npm`](https://www.npmjs.com): a **Package Manager** bundled with Node which helps manage your project's dependencies—i.e., other code and files that are needed to make your plugin work.
- [`yarn`](https://yarnpkg.com): an **alternative Package Manager** for Node. To install `yarn` you'll need to have `npm` installed first—see above. Then, use this command:

  ```bash
  npm install yarn --global
  ```

## System Requirements

Finally, make sure your system meets the minimum requirements to run the [Premiere Pro](https://helpx.adobe.com/premiere-pro/system-requirements.html) application.
