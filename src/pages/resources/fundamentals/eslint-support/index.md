---
keywords:
  - ESLint
  - Linting
  - UXP
  - JavaScript
  - TypeScript
  - typescript-eslint
  - Premiere Pro
  - Static analysis
title: ESLint Support
description: Learn how to use ESLint and the Premiere Pro plugin to catch API mistakes while you build UXP plugins
contributors:
  - https://github.com/camlegleiter
---

# ESLint Support

Learn how to use ESLint with UXP plugins for Premiere Pro.

## Overview

[ESLint](https://eslint.org/) checks your source for common problems before you run or ship a plugin. That includes general JavaScript issues (undefined variables, suspicious patterns, and so on) and, when you add shared configurations, team-wide style and quality rules.

For Premiere’s UXP DOM APIs, many mistakes only show up at runtime: for example using actions outside `Project.lockedAccess()` / `Project.executeTransaction()`, awaiting work inside those callbacks, or letting action objects escape their lock scope. The [`@adobe/eslint-plugin-premierepro`](https://www.npmjs.com/package/@adobe/eslint-plugin-premierepro) package adds rules aimed at those patterns so you can catch them in the editor or in CI.

The plugin has two tiers:

1. **[Syntactic rules](#syntactic-rules-and-configuration)** — pattern-based rules that run without TypeScript’s type checker. They work in **plain JavaScript** or **TypeScript** projects.
2. **[Type-checked rules](#type-checked-rules-and-configuration)** — rules that use [typed linting](https://typescript-eslint.io/getting-started/typed-linting/) (`typescript-eslint`, a `tsconfig`, and types from [`@adobe/premierepro`](../typescript-support/index.md#type-definitions)). They understand the real Premiere types, which reduces false positives and covers patterns (such as indirection through helpers) that syntactic rules cannot see reliably.

Use **syntactic** configs when you are not using typed ESLint. Use **type-checked** configs when you already have TypeScript and `typescript-eslint` set up.

## `@adobe/eslint-plugin-premierepro`

Install the plugin as a dev dependency:

```sh
npm install -D @adobe/eslint-plugin-premierepro

# Using yarn
yarn add -D @adobe/eslint-plugin-premierepro

# Using pnpm
pnpm add -D @adobe/eslint-plugin-premierepro
```

The package declares a peer dependency on [`@adobe/premierepro`](https://www.npmjs.com/package/@adobe/premierepro) aligned with the ESLint plugin version. Install that package in your project (typically as a dev dependency) so versions stay in sync:

```sh
npm install -D @adobe/premierepro @adobe/eslint-plugin-premierepro
```

Prebuilt configs:

| Config | Purpose |
| ------ | ------- |
| `premierepro.configs.recommended` | Enables **syntactic** Premiere rules with default severities. Safe for any JS/TS project. |
| `premierepro.configs.recommendedTypeChecked` | Enables **type-checked** Premiere rules. Requires typed linting with `typescript-eslint`. |

Type-checked rules **replace** their syntactic counterparts; you normally enable one tier, not both. During migration you can run both briefly, but you may see duplicate messages for the same issue.

### What the Premiere rules cover (summary)

**Syntactic rules** use naming and AST patterns (such as `create*Action()` and `addAction()`). **Type-checked rules** use TypeScript to detect real `Action` types and related APIs. Topics include:

- Requiring `create*Action()` usage inside `Project.lockedAccess()` or `Project.executeTransaction()`
- Requiring `addAction()` inside `Project.executeTransaction()`
- Disallowing `async` work inside `lockedAccess()` / `executeTransaction()` callbacks
- Disallowing `Action` instances from escaping their lock scope
- Optional style rules (undo strings, wrapping `executeTransaction()` in `lockedAccess()`)

For full rule names and descriptions, see the [plugin README](https://github.com/adobe/eslint-plugin-premierepro/blob/main/README.md#rules) on GitHub.

## Syntactic rules and configuration

Use this path for **JavaScript-only** plugins, or TypeScript projects where you have **not** enabled typed ESLint. You only need core ESLint, the shared JavaScript recommendations, and the Premiere ESLint plugin.

### Quick setup

1. **Install ESLint, the shared JS config, and the Premiere plugin**

   ```sh
   npm install -D eslint @eslint/js @adobe/eslint-plugin-premierepro @adobe/premierepro
   ```

2. **Add an ESLint flat config** (ESLint 9+), e.g. `eslint.config.mjs` in the project root:

   ```javascript
   // @ts-check

   import premierepro from "@adobe/eslint-plugin-premierepro";
   import js from "@eslint/js";
   import { defineConfig } from "eslint/config";

   export default defineConfig(
     js.configs.recommended,
     premierepro.configs.recommended
   );
   ```

   This uses [`@eslint/js`](https://www.npmjs.com/package/@eslint/js) `recommended` rules for general JavaScript quality, plus Premiere **syntactic** rules. There are many other plugins and rules available for ESLint that you can use instead depending on your project's or team's requirements: for example a React-based project might want to include plugins like `eslint-plugin-react` or `eslint-plugin-react-hooks`.

3. **Add a lint script** to `package.json`:

   ```json
   {
     "scripts": {
       "lint": "eslint ."
     }
   }
   ```

4. **Run ESLint**

   ```sh
   npm run lint
   ```

If your compiled output lives in a folder such as `dist/`, add an `ignores` entry (or a separate config object with `ignores`) so ESLint does not lint generated files.

### Pros and cons (syntactic)

**Pros:** Minimal tooling; works the same for `.js` and `.ts`; fast; no `tsconfig` or type-aware parser required.

**Cons:** Rules infer Premiere usage from patterns, so some edge cases and refactors may be missed or occasionally noisy compared to type-checked rules.

## Type-checked rules and configuration

When your project uses **TypeScript** and you want ESLint to use the type checker, add **`typescript-eslint`** (the unified package: `typescript-eslint` on npm) alongside `eslint` and `@eslint/js`. Typed linting lets `recommendedTypeChecked` use the same [Premiere type definitions](../typescript-support/index.md#type-definitions) your editor uses, so rules align with real APIs.

### Quick setup

1. **Install dependencies**

   ```sh
   npm install -D eslint @eslint/js typescript-eslint @adobe/eslint-plugin-premierepro @adobe/premierepro
   ```

   `typescript-eslint` pulls in the parser and `@typescript-eslint/*` tooling needed for type-aware rules. Keep `@adobe/premierepro` on a version compatible with the ESLint plugin (see peer dependency ranges on the plugin’s [npm page](https://www.npmjs.com/package/@adobe/eslint-plugin-premierepro)).

2. **Ensure `tsconfig.json` includes your plugin sources**

   Your TypeScript config should cover the files ESLint will lint (for example `src/**/*`). See [TypeScript projects](../typescript-support/index.md#typescript-projects) for a typical `tsconfig.json` layout.

3. **Add an ESLint flat config** that enables `typescript-eslint` **and** type-aware parsing, then layers Premiere type-checked rules:

   ```javascript
   // @ts-check

   import premierepro from "@adobe/eslint-plugin-premierepro";
   import js from "@eslint/js";
   import { defineConfig } from "eslint/config";
   import tseslint from "typescript-eslint";

   export default defineConfig(
     js.configs.recommended,
     tseslint.configs.recommended,
     premierepro.configs.recommendedTypeChecked,
     {
       languageOptions: {
         parserOptions: {
           projectService: true,
         },
       },
     }
   );
   ```

   The [`typescript-eslint` typed linting docs](https://typescript-eslint.io/getting-started/typed-linting/) describe `projectService: true` and other options.

4. **Run ESLint** the same way as in the syntactic setup (`npm run lint`).

### Pros and cons (type-checked)

**Pros:** Stronger, type-accurate Premiere API checks; fewer pattern-based false positives; better results when code wraps actions in helpers.

**Cons:** More setup (TypeScript, `typescript-eslint`, valid `tsconfig`); type-aware linting is slower than syntax-only runs.

## Development workflow

A typical loop:

1. **Terminal** — run `npm run lint` (or wire lint into CI) before packaging or opening a PR.
2. **Editor** — use an ESLint extension so issues surface while you edit.
3. **Premiere** — reload the plugin from the UXP Developer Tool after fixing issues and rebuilding if you use a compile step.

For TypeScript plugins, combine this page with [TypeScript support](../typescript-support/index.md): types power both IntelliSense and type-checked ESLint rules.
