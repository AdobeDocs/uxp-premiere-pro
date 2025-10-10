---
title: Plugin manifest
description: Details of plugin manifest and its configuration.
keywords:
  - plugin manifest
  - UXP configuration
  - manifest.json
contributors:
  - https://github.com/padmkris123
  - https://github.com/undavide
---

# UXP Manifest

The Manifest file is a JSON file located at the root of the plugin bundle that contains metadata about the plugin.

## Overview

Each UXP plugin must have one `manifest.json` file that the host application uses to **load and manage** the plugin. In addition to core metadata such as the plugin's name, version, icons, and entry points, the manifest specifies permissions, compatibility details, and other definitions that shape how the plugin integrates with the host environment.

Most importantly, it contains your **plugin ID**, which uniquely identifies your plugin when it's installed in the host application. Valid plugin IDs are required for distributing in Adobe's Marketplace—read more [in the Developer Distribution documentation](https://developer.adobe.com/developer-distribution/creative-cloud/docs/guides/plugin_id/).

## Manifest Keys

<br/><br/>

| Required properties                   | Optional properties                           |
| :------------------------------------ | :-------------------------------------------- |
| [`manifestVersion`](#manifestversion) | [`main`](#main)                               |
| [`id`](#id)                           | [`icons`](#icons)                             |
| [`name`](#name)                       | [`strings`](#strings)                         |
| [`version`](#version)                 | [`requiredPermissions`](#requiredpermissions) |
| [`host`](#host)                       | [`featureFlags`](#featureflags)               |
| [`entrypoints`](#entrypoints)         | [`addon`](#addon)                             |

#### Example

```json
{
	"manifestVersion": 5,
	"id": "YOUR_ID_HERE",
	"name": "Name of your plugin",
	"version": "1.0.0",
	"main": "index.html",
	"host": {
		"app": "HOST_APPLICATION",
		"minVersion": "HOST_VERSION"
	},
	"entrypoints": [
		{
			"type": "command",
			"id": "commandFn",
			"label": {
				"default": "Show A Dialog"
			}
		},
		{
			"type": "panel",
			"id": "panelName",
			"label": {
				"default": "Panel Name"
			}
		}
	],
	"icons": [
		{
			"width": 24,
			"height": 24,
			"path": "icons/icon.png",
			"scale": [
				1,
				2
			]
		}
	],
	"requiredPermissions": {
		"network": {
			"domains": "all"
		}
	}
}
```

## Required properties

#### `manifestVersion`

| Name              | Type     | Default |
| :---------------- | :------- | :------ |
| `manifestVersion` | `string` | -       |

Indicates the version of the manifest schema. Premiere Pro supports version `"5"`.

### `id`

| Name | Type     | Default |
| :--- | :------- | :------ |
| `id` | `string` | -       |

Uniquely identifies a plugin and is used to disambiguate plugin contexts, storage, errors, etc. For plugins distributed through the plugin marketplace, the `id` has to match the one set in the [Developer Distribution portal](https://developer.adobe.com/developer-distribution/creative-cloud/docs/guides/plugin_id/).

### `name`

| Name   | Type                                              | Default |
| :----- | :------------------------------------------------ | :------ |
| `name` | `string` or [`LocalizedString`](#localizedstring) | -       |

Visually identifies the plugin in the user interface. It is usually used in a plugin menu listing or launcher for top-level action items. The name can be a string, a key from the [`StringsDefinition`](#stringsdefinition) object, or a localized string.

### `version`

| Name      | Type     | Default |
| :-------- | :------- | :------ |
| `version` | `string` | -       |

Indicates the plugin's version. The string has a format of `major.minor.patch`.

### `host`

| Name   | Type                                | Default |
| :----- | :---------------------------------- | :------ |
| `host` | [`HostDefinition`](#hostdefinition) | -       |

The host object indicates the plugin's compatibility with the host. Incompatible plugins will:

- fail to install if attempted in the given host
- be invisible in the in-app plugin marketplace for the given host
- be unavailable for update if the update is no longer compatible.

Check the [HostDefinition](#hostdefinition) section for more details.

<InlineAlert slots="text" variant="info"/>

**Only during development**, for convenience, you can assign to the `host` property an array of `HostDefinition` objects, allowing the plugin to be loaded in multiple applications simultaneously. See the [Package with the UXP Developer Tool](../../../resources/distribution/package/index.md#host-applications) section for more details.

### `entrypoints`

| Name          | Type                                              | Default |
| :------------ | :------------------------------------------------ | :------ |
| `entrypoints` | [`EntrypointDefinition[]`](#entrypointdefinition) | -       |

This array defines the entrypoints that the plugin provides; currently, only Commands and Panels are supported. Check the [EntrypointDefinition](#entrypointdefinition) section for more details.

## Optional properties

### `main`

| Name   | Type     | Default   |
| :----- | :------- | :-------- |
| `main` | `string` | `main.js` |

Indicates the primary JavaScript or HTML file, relative to the plugin's installation directory. It supports HTML and JS files, such as `index.html` and `index.js`. If not specified (for deprecations), `main.js` is used.

### `icons`

| Name    | Type                                  | Default |
| :------ | :------------------------------------ | :------ |
| `icons` | [`IconDefinition[]`](#icondefinition) | `[]`    |

An array of icons representing the overall plugin or panel icon. The host application uses these icons to present the plugin to the user. If the icons array is missing, a default icon will be used. See the [IconDefinition](#icondefinition) section for more details.

### `strings`

| Name      | Type                                      | Default |
| :-------- | :---------------------------------------- | :------ |
| `strings` | [`StringsDefinition`](#stringsdefinition) | `{}`    |

A set of strings used to localize the plugin name and other user-facing strings. It can also be a path to a JSON file containing them. See the [StringsDefinition](#stringsdefinition) section for more details.

### `requiredPermissions`

| Name                  | Type                                              | Default |
| :-------------------- | :------------------------------------------------ | :------ |
| `requiredPermissions` | [`PermissionsDefinition`](#permissionsdefinition) | `{}`    |

Indicates the various permissions this plugin requires before accessing certain API surfaces. Without them, access may fail or throw an error. **Users will be asked for their consent** when your plugin attempts to use `openExternal()`, `openPath()`, and `<sp-link>` anchor tags. For everything else, it is given at install time. See the [PermissionsDefinition](#permissionsdefinition) section for more details.

### `featureFlags`

| Name           | Type                            | Default |
| :------------- | :------------------------------ | :------ |
| `featureFlags` | [`FeatureFlags`](#featureflags) | `{}`    |

A set of feature flags that can be used to enable or disable certain features of the plugin. These flags are used to gate features that are not yet ready for general availability. See the [FeatureFlags](#featureflags) section for more details.

### `addon`

| Name    | Type     | Default |
| :------ | :------- | :------ |
| `addon` | `object` | `{}`    |

Addon definitions for hybrid plugins. A UXP Hybrid plugin is a UXP plugin that can access the power of C++ native libraries.

<InlineAlert variant="warning"slots="text" />

Premiere Pro **doesn't support hybrid plugins** yet.

## Supporting Definitions

### `StringsDefinition`

Represents a set of strings used to localize the plugin name and other user-facing strings. `StringsDefinition` keys can be used anywhere where [`LocalizedString`](#localizedstring) is supported.

```json
{
  "name": "my-plugin",
    "strings": {
      "my-plugin": {
        "default": "My Plugin",
        "it": "Il mio Plugin",
        "fr": "Mon Plugin"
      }
  }
}
```

### `LocalizedString`

Represents a localized string. The key is the locale, and the value is the translated string.

```json
{
  "default": "Settings",
  "it": "Impostazioni",
  "fr": "Paramètres"
}
```

#### Required Properties

| Name      | Type     | Default |
| :-------- | :------- | :------ |
| `default` | `string` | -       |

The default string used when no translation is available for the current locale.

### `IconDefinition`

Represents an icon used by the plugin or specific entry point. The icon may be used in the plugin list, toolbar, or other places.

| Required Properties | Optional Properties   |
| :------------------ | :-------------------- |
| [`width`](#width)   | [`scale`](#scale)     |
| [`height`](#height) | [`theme`](#theme)     |
| [`path`](#path)     | [`species`](#species) |

#### Properties

##### `width`

| Name    | Type     | Required | Default |
| :------ | :------- | :------- | ------- |
| `width` | `number` | required | -       |

The width of the icon in pixels.

##### `height`

| Name     | Type     | Required | Default |
| :------- | :------- | :------- | ------- |
| `height` | `number` | required | -       |

The height of the icon in pixels.

##### `path`

| Name   | Type     | Required | Default |
| :----- | :------- | :------- | ------- |
| `path` | `string` | required | -       |

The path to the icon, relative to the plugin's installation directory. Supports PNG (`.png`), JPG (`.jpg` or `.jpeg`), and SVG (`.svg`) files.

##### `scale`

| Name    | Type       | Required | Default |
| :------ | :--------- | :------- | ------- |
| `scale` | `number[]` | optional | [1]     |

Specifies the scaling factors that the icon supports.

```json
{
    "path": "icon.png",
    "width": 24,
    "height": 24,
    "scale": [1, 2, 2.5]
}
```

Results in the following icon files being used (if available):

- `icon.png` or `icon@1x.png` (24x24px) for 100% scaling
- `icon@2x.png` (48x48px) for 200% scaling
- `icon@2.5x.png` (60x60px) for 250% scaling

##### `theme`

| Name    | Type       | Required | Default |
| :------ | :--------- | :------- | ------- |
| `theme` | `string[]` | optional | ["all"] |

Specifies the themes that the icon supports. Available themes in UXP are: `"all"` (default), `"lightest"`, `"light"`, `"medium"`, `"dark"`, `"darkest"`.

```json
{
    "path": "icon-light.png",
    "width": 24,
    "height": 24,
    "theme": ["lightest", "light"]
},
{
    "path": "icon-dark.png",
    "width": 24,
    "height": 24,
    "theme": ["darkest", "dark"]
}
```

##### `species`

| Name      | Type       | Required | Default     |
| :-------- | :--------- | :------- | ----------- |
| `species` | `string[]` | optional | ["generic"] |

Specifies the species that the icon supports. Indicates the suitable use of this icon. Available species are:

- `"generic"`: suitable for display anywhere
- `"toolbar"`: suitable for display in a toolbar. Icon sizes are 23x23px for 100% scaling and 46x46px for 200% scaling.
- `"pluginList"`: suitable for display in a plugin list. Icon sizes are 24x24px for 100% scaling and 48x48px for 200% scaling.

### `EntrypointDefinition`

Represents an entrypoint that the plugin provides. An entrypoint is a point of entry for the plugin. It is used to identify the code that implements the entrypoint.

| Required Properties | Optional Properties                                                       |
| :------------------ | :------------------------------------------------------------------------ |
| [`type`](#type)     | [`description`](#description)                                             |
| [`id`](#id-1)       | [`shortcut`](#shortcut)                                                   |
| [`label`](#label)   | [`icon`](#icon)                                                           |
|                     | [`minimumSize`](#minimumsize-and-maximumsize)                             |
|                     | [`maximumSize`](#minimumsize-and-maximumsize)                             |
|                     | [`preferredDockedSize`](#preferreddockedsize-and-preferredfloatingsize)   |
|                     | [`preferredFloatingSize`](#preferreddockedsize-and-preferredfloatingsize) |

#### Properties

##### `type`

| Name   | Type                     | Required | Default |
| :----- | :----------------------- | :------- | ------- |
| `type` | `"command"` or `"panel"` | required | -       |

The type of entrypoint. Currently, only Commands and Panels are supported.

##### `id`

| Name | Type     | Required | Default |
| :--- | :------- | :------- | ------- |
| `id` | `string` | required | -       |

The ID of the entrypoint. This ID must be unique within the plugin. It is used to identify the code that implements the entrypoint.

##### `label`

| Name    | Type                          | Required | Default |
| :------ | :---------------------------- | :------- | ------- |
| `label` | `string` or `LocalizedString` | required | -       |

The label of the entrypoint. This label is used to display the entrypoint to the user, such as in the plugin menu.

##### `description`

| Name          | Type                          | Required | Default     |
| :------------ | :---------------------------- | :------- | ----------- |
| `description` | `string` or `LocalizedString` | optional | `undefined` |

A description of the entrypoint. This description is used in tooltips and other places where a longer description is appropriate, depending on the host app. Default value is the plugin's name.

##### `shortcut`

| Name       | Type                           | Required | Default     |
| :--------- | :----------------------------- | :------- | ----------- |
| `shortcut` | `{ mac: string, win: string }` | optional | `undefined` |

<InlineAlert variant="warning" slots="text" />

Keyboard shortcuts are **not available in Premiere Pro** yet.

A keyboard shortcut that can be used to invoke the entrypoint. They are specified separately for Windows and macOS platforms. If the shortcut is not available in the host application, it will be ignored.

```json
"shortcut": {
    "mac": "Cmd+Shift+P",
    "win": "Ctrl+Shift+P"
}
```

Keyboard shortcuts are defined separately for each platform. Each definition is a string that follows this syntax:

- One or more modifier keys, in any order, each one followed by `+`.
- Mac: modifiers may be Cmd, Ctrl, Opt/Alt, or Shift. The shortcut must contain at least one of Cmd or Ctrl.
- Win: modifiers may be Ctrl, Alt, or Shift. The shortcut must contain Ctrl.
- A letter or number key.

Letters are case-insensitive (e.g., `"Cmd+P"` and `"Cmd+p"` mean the same thing and neither requires pressing Shift). Other keys (including punctuation, arrow keys, or F1-F12) are currently not supported.

<InlineAlert variant="warning"slots="text" />

If your shortcut collides with a built-in command in the host app, or another plugin's shortcut, your shortcut will be ignored, and you'll see a warning printed to the developer console.

##### `icon`

| Name   | Type                                | Required | Default |
| :----- | :---------------------------------- | :------- | ------- |
| `icon` | [`IconDefinition`](#icondefinition) | optional | `[]`    |

An icon specific to the entrypoint. If specified, this icon overrides the plugin icon in places where the entrypoint is specifically displayed. Default value is the plugin icon.

##### `minimumSize` and `maximumSize`

| Name          | Type                                | Required |
| :------------ | :---------------------------------- | :------- |
| `minimumSize` | `{ width: number, height: number }` | optional |
| `maximumSize` | `{ width: number, height: number }` | optional |

Indicates the desired minimum and maximum size of the panel, defined by `width` and `height` in pixels, although the host application _may not_ be able to honor them. When not specified, default values will be used.

Panel size can be **locked to a specific size** by setting `minimumSize` equal to `maximumSize`.

##### `preferredDockedSize` and `preferredFloatingSize`

| Name                    | Type                                | Required |
| :---------------------- | :---------------------------------- | :------- |
| `preferredDockedSize`   | `{ width: number, height: number }` | optional |
| `preferredFloatingSize` | `{ width: number, height: number }` | optional |

Indicates the preferred size of the panel when docked (for panels or modal dialogs without a `reference_node_id`) or floating. The host application _may not_ be able to honor them. When not specified, default values will be used.

### `HostDefinition`

Represents the host application that the plugin is compatible with.

| Required Properties         | Optional Properties         |
| :-------------------------- | :-------------------------- |
| [`app`](#app)               | [`maxVersion`](#maxversion) |
| [`minVersion`](#minversion) |                             |

#### Properties

##### `app`

| Name  | Type                                          | Required |
| :---- | :-------------------------------------------- | :------- |
| `app` | `"PS"` or `"ID"` or `"premierepro"` or `"XD"` | required |

The host app that the plugin supports. Possible values are:

- `"PS"`: Adobe Photoshop
- `"ID"`: Adobe InDesign
- `"premierepro"`: Adobe Premiere Pro
- `"XD"`: Adobe XD

##### `minVersion`

| Name         | Type     | Required | Default |
| :----------- | :------- | :------- | ------- |
| `minVersion` | `string` | required | -       |

The minimum version of the host app that the plugin supports in the `x.y.z` format.

##### `maxVersion`

| Name         | Type     | Required | Default     |
| :----------- | :------- | :------- | ----------- |
| `maxVersion` | `string` | optional | `undefined` |

The maximum version of the host app that the plugin supports in the `x.y.z` format. Default value is the latest version of the host app.

### `PermissionsDefinition`

To ensure that plugins are secure, UXP requires that plugins declare the permissions they need to function. Permissions not explicitly declared will be denied by default.

<InlineAlert variant="info" slots="header, text1, text2"/>

Best practices

Make sure you **configure the most accurate permission** for your use case because in the future we will ask users to provide their consent based on it.

For example, for file operations, you may find `"fullAccess"` to be the least restrictive and hence the easiest to pick, but a user may not be comfortable giving full access to their system unless it's absolutely necessary; they might deny the installation of your plugin altogether.

| Required Properties | Optional Properties                                                 |
| :------------------ | :------------------------------------------------------------------ |
|                     | [`clipboard`](#clipboard)                                           |
|                     | [`localFileSystem`](#localfilesystem)                               |
|                     | [`network`](#network)                                               |
|                     | [`webview`](#webview)                                               |
|                     | [`launchProcess`](#launchprocess)                                   |
|                     | [`allowCodeGenerationFromStrings`](#allowcodegenerationfromstrings) |
|                     | [`enableUserInfo`](#enableUserInfo)                                 |
|                     | [`ipc`](#ipc)                                                       |

#### Properties

##### `clipboard`

| Name        | Type                         | Required | Default     |
| :---------- | :--------------------------- | :------- | ----------- |
| `clipboard` | `"read"` or `"readAndWrite"` | optional | `undefined` |

Enables the plugin to read and write to the clipboard. The [clipboard recipe](../../../resources/recipes/clipboard/index.md) has more examples.

- `read`: enables the plugin to read from the clipboard.
- `readAndWrite`: enables the plugin to read from and write to the clipboard.

Default value is `undefined` (no clipboard access).

##### `localFileSystem`

| Name              | Type                                        | Required | Default     |
| :---------------- | :------------------------------------------ | :------- | ----------- |
| `localFileSystem` | `"plugin"` or `"request"` or `"fullAccess"` | optional | `undefined` |

Enables the plugin to access the file system. The [file-operation recipe](../../../resources/recipes/file-operation/index.md) has a detailed example.

- `"plugin"`: enables the plugin to access the file system in the plugin folder.
- `"request"`: enables the plugin to request access to the file system.
- `"fullAccess"`: enables the plugin to access the file system without requesting access.

Default value is `undefined` (no file system access).

##### `network`

| Name      | Type                                      | Required | Default     |
| :-------- | :---------------------------------------- | :------- | ----------- |
| `network` | [`NetworkPermission`](#networkpermission) | optional | `undefined` |

Enables the plugin to access the network—for example, to make HTTP requests (XHR, fetch, etc.), load images (`<img src="" />`), etc.

- `"all"`: enables the plugin to access all domains.
- `"domains"`: enables the plugin to access the specified domains.

Default value is `undefined` (no network access). See the [`NetworkPermission`](#networkpermission) section for more details, or the [network recipe](../../../resources/recipes/network/index.md) for examples.

##### `webview`

| Name      | Type                                      | Required | Default     |
| :-------- | :---------------------------------------- | :------- | ----------- |
| `webview` | [`WebviewPermission`](#webviewpermission) | optional | `undefined` |

Enables the plugin to use webviews in its UI to display web content or complex UI.

Default value is `undefined` (no webview usage). See the [`WebviewPermission`](#webviewpermission) section for more Details.

##### `launchProcess`

| Name            | Type                                                  | Required | Default     |
| :-------------- | :---------------------------------------------------- | :------- | ----------- |
| `launchProcess` | [`LaunchProcessPermission`](#launchprocesspermission) | optional | `undefined` |

Enables the plugin to launch processes using APIs like `require("uxp").shell.openPath()` or `shell.openExternal()`.

Default value is `undefined` (no process launching). See the [`LaunchProcessPermission`](#launchprocesspermission) section for more details and the [launch process recipe](../../../resources/recipes/launch-process/index.md) for examples.

##### `allowCodeGenerationFromStrings`

| Name                             | Type      | Required | Default |
| :------------------------------- | :-------- | :------- | ------- |
| `allowCodeGenerationFromStrings` | `boolean` | optional | `false` |

Enables the plugin to generate code from strings. You will need this while using inline event handlers for HTML elements, `eval()`, and `new Function()` syntax.

Default value is `false`.

##### `enableUserInfo`

| Name             | Type      | Required | Default |
| :--------------- | :-------- | :------- | ------- |
| `enableUserInfo` | `boolean` | optional | `false` |

Enables the plugin to access the user's anonymized GUID information. Default value is `false`.

```javascript
// set "enableUserInfo" to true in the manifest

let userId = require('uxp').userInfo.userId(); // Get the GUID of user
console.log(userId);
// "dad8483a3682a0c3e0fa990281142353901a69fc371254edde8b7dd38ca604c6"
```

##### `ipc`

| Name  | Type                              | Required | Default     |
| :---- | :-------------------------------- | :------- | ----------- |
| `ipc` | [`IpcPermission`](#ipcpermission) | optional | `undefined` |

Enables the plugin to communicate with other plugins.

Default value is `undefined` (no IPC). See the [`IpcPermission`](#ipcpermission) section for more details.

##### `NetworkPermission`

Specifies the domains that the plugin can access in network requests.

```json
{
  "domains": [
    "https://example.com",
    "https://*.adobe.com/",
    "wss://*.myplugin.com"
  ]
}
```

Then, in your plugin code, you can make network requests like this:

```javascript
const response = await fetch("https://example.com");
```

Or load images like this:

```html
<img src="https://example.com/image.png" />
```

You can also allow access to all domains by setting `domains` to `"all"`.

```json
{
  "domains": "all"
}
```

The [network recipe](../../../resources/recipes/network/index.md) has more details.

##### `WebviewPermission`

Enables the plugin to use webviews in its UI to display web content or complex UI.

```json
{
  "allow": "yes",
  "domains": ["https://example.com"],
  "enableMessageBridge": "localAndRemote"
}
```

Then, in your plugin code, you can use a webview like this:

```html
<webview src="https://example.com" />
```

To communicate between the webview and the plugin, you can use the message API:

```javascript
// In the plugin:
const webview = document.querySelector("webview");
webview.addEventListener("message", (event) => {
  console.log("Received message from webview:", event.data);
  webview.postMessage("Hello from the plugin!");
});

// In the webview:
window.addEventListener("message", (event) => {
  console.log("Received message from plugin:", event.data);
  window.uxpHost.postMessage("Hello from the webview!");
});
```

| Required Properties   | Optional Properties                           |
| :-------------------- | :-------------------------------------------- |
| [`allow`](#allow)     | [`enableMessageBridge`](#enablemessagebridge) |
| [`domains`](#domains) |                                               |

##### `allow`

| Name    | Type              | Required |
| :------ | :---------------- | :------- |
| `allow` | `"yes"` or `"no"` | required |

Must be set to `"yes"` to enable webviews.

##### `domains`

| Name      | Type                  | Required |
| :-------- | :-------------------- | :------- |
| `domains` | `string[]` or `"all"` | required |

The domains that the plugin can access. Can be a list of domains, or the string `"all"` to allow access to all domains.

##### `enableMessageBridge`

| Name                  | Type                         | Required | Default |
| :-------------------- | :--------------------------- | :------- | ------- |
| `enableMessageBridge` | `"no"` or `"localAndRemote"` | optional | `"no"`  |

Specifies whether the plugin can communicate with the webview using the message API.

Find the detailed [WebView API reference](../../../uxp-api/reference-js/Global%20Members/HTML%20Elements/HTMLWebViewElement.md) or use the `webview-starter` template plugin in UDT.

##### `LaunchProcessPermission`

Specifies the schemes and extensions that the plugin can launch. For example, if the plugin can launch a web browser, it should specify the `"http"` and `"https"` schemes.

```json
{
  "schemes": ["http", "https"],
  "extensions": ["pdf"]
}
```

| Required Properties         | Optional Properties |
| :-------------------------- | :------------------ |
| [`schemes`](#schemes)       |                     |
| [`extensions`](#extensions) |                     |

##### `schemes`

| Name      | Type       | Required |
| :-------- | :--------- | :------- |
| `schemes` | `string[]` | required |

A set of schemes that the plugin can launch, for example `["http", "https", "mailto"]`.

##### `extensions`

| Name         | Type       | Required |
| :----------- | :--------- | :------- |
| `extensions` | `string[]` | required |

A set of extensions that the plugin can launch, for example `["pdf", "png", "jpg"]`. Only relevant for local files (using the `file://` schema).

The [launch process recipe](../../../resources/recipes/launch-process/index.md) has more details.

##### `IpcPermission`

Specifies the IPC channels that the plugin can use.

```json
{
  "enablePluginCommunication": true
}
```

##### `enablePluginCommunication`

| Name                        | Type      | Required |
| :-------------------------- | :-------- | :------- |
| `enablePluginCommunication` | `boolean` | required |

Enables the plugin to communicate with other plugins. The [inter plugin communication tutorial](../../../plugins/tutorials/inter-plugin-comm/index.md) has more details.

### `FeatureFlags`

Specifies which experimental features the plugin can use.

```json
{
  "enableFillAsCustomAttribute": true,
  "enableSWCSupport": true
  "enableAlerts": true
}
```

| Required Properties | Optional Properties                                           |
| :------------------ | :------------------------------------------------------------ |
|                     | [`enableFillAsCustomAttribute`](#enablefillascustomattribute) |
|                     | [`enableSWCSupport`](#enableswcsupport)                       |
|                     | [`enableAlerts`](#enablealerts)                               |

#### Properties

##### `enableFillAsCustomAttribute`

| Name                          | Type      | Required | Default |
| :---------------------------- | :-------- | :------- | ------- |
| `enableFillAsCustomAttribute` | `boolean` | optional | `false` |

Enables the plugin to use CSS variable in the fill attribute on SVG elements.

```html
<svg width="100" height="100">
  <rect width="100" height="100"
        fill="var(--iconColor, red)"
  />
</svg>
```

With the following CSS:

```css
:root {
  --iconColor: blue;
}
```

##### `enableSWCSupport`

| Name               | Type      | Required | Default |
| :----------------- | :-------- | :------- | ------- |
| `enableSWCSupport` | `boolean` | optional | `false` |

Enables the plugin to use [Spectrum Web Components](../../../uxp-api/reference-spectrum/swc/index.md). Requires installing and importing the components separately.

```html
<sp-button variant="primary">
    Click me
</sp-button>
```

Note that you will need to **manually install** the library (via `npm` or `yarn`), **import** the components (for example, `import '@spectrum-web-components/button/sp-button.js'`), and **bundle** the code with a tool like [Webpack](https://webpack.js.org/) or [Esbuild](https://esbuild.github.io/) so that it's included in your plugin.

##### `enableAlerts`

| Name           | Type      | Required | Default |
| :------------- | :-------- | :------- | ------- |
| `enableAlerts` | `boolean` | optional | `false` |

Enable the plugin to use create simple dialogs via [`alert()`](../../../uxp-api/reference-js/Global%20Members/HTML%20DOM/alert.md), [`prompt()`](../../../uxp-api/reference-js/Global%20Members/HTML%20DOM/prompt.md) and [`confirm()`](../../../uxp-api/reference-js/Global%20Members/HTML%20DOM/confirm.md)
