---
title: require('uxp').host
description: Includes useful information about the operating environment the plugin finds itself executing in.
---

# require('uxp').host
Includes useful information about the operating environment the plugin finds itself executing in.
`require("uxp").host`



## name ⇒ `string`
**Returns**: `string` - name of the host application. For ex, returns "photoshop" for Photoshop  


## version ⇒ `string`
**Returns**: `string` - version of host application. For ex, "20.0.0"  


## uiLocale ⇒ `string`
**Returns**: `string` - 5 letter UI locale of host application. For ex, "en_US"


## applicationPath ⇒ `string`
**Returns**: the absolute path to the current host application binary

**Since**: Premiere 26.5
**Example**:
```js
const uxp = require("uxp");
console.log(uxp.host.applicationPath);
// e.g., "/Applications/Adobe Premiere Pro (Beta)/Adobe Premiere Pro (Beta).app" on macOS
//       "C:\\Program Files\\Adobe\\Adobe Premiere Pro (Beta)\\Adobe Premiere Pro (Beta).exe" on Windows
```


## getBackgroundColor() ⇒ `Promise<string>`
**Returns**: a stringified JSON object containing the current background color as RGB values:
```json
{
  "type": "rgb",
  "value": {
    "alpha": 1,
    "blue": 0,
    "green": 0,
    "red": 0
  }
}
```

The `blue`, `green`, and `red` properties are a number between 0 and 1.

**Since**: Premiere 26.5
**Example**:
```js
const uxp = require("uxp");
const backgroundColor = JSON.parse(await uxp.host.getBackgroundColor());
backgroundColor.type; // "rgb"
backgroundColor.value.alpha; // 1
// RGB colors are a value between 0 and 1
backgroundColor.value.blue;
backgroundColor.value.green;
backgroundColor.value.red;
```
