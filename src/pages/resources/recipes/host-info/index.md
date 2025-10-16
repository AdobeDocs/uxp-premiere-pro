---
title: Host information
description: Find the host info to determine locale, os etc
keywords:
  - Host API
  - code sample
  - locale
contributors:
  - https://github.com/padmkris123
---

# Host Environment

Sometimes it's necessary to find out the host environment where a plugin or script is running. You can find a range of information such as the host OS, locale, home folder, installed application version, etc, by using UXP APIs.

## System requirements

Please make make sure your development environment uses the following **minimum versions** to avoid compatibility issues:

- **Premiere Pro v25.6**
- **UDT v2.2**
- **Manifest v5**

## Example

<CodeBlock slots="heading, code" repeat="2" languages="JavaScript,text" />

#### JavaScript

```js
async function foo() {
    const { host, versions } = require('uxp');
    const osInfo = require('os');

    console.log(`System information: ${osInfo.platform()} v${osInfo.release()}`);
    console.log(`Application: ${host.name} v${host.version} powered by ${versions.uxp}`);
}
```

#### Output

```text
System information: darwin v21.1.0
Application: Premiere Pro v25.2.0 powered by uxp-7.1.0
```

## Reference material

- [Host](../../../uxp-api/reference-js/Modules/uxp/Host%20Information/Host.md) APIs
- [Versions](../../../uxp-api/reference-js/Modules/uxp/Versions/Versions.md) APIs
- [OS](../../../uxp-api/reference-js/Modules/os/OS.md) APIs
