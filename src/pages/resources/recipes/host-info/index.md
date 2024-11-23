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
Please make sure your local environment uses the following application versions before proceeding.
- Premiere Pro v25.1 or higher
- UDT v2.1.0 or higher
- Manifest version v5 or higher

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
```
System information: darwin v21.1.0
Application: Premiere Pro v25.1.0 powered by uxp-7.1.0
```


## Reference material
- [Host](../../../uxp-api/reference-js/Modules/uxp/Host%20Information/Host/) APIs
- [Versions](../../../uxp-api/reference-js/Modules/uxp/Versions/Versions/) APIs
- [OS](../../../uxp-api/reference-js/Modules/os/OS/) APIs

