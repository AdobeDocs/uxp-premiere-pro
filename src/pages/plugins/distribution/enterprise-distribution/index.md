---
title: Enterprise Distribution
description: How to distribute UXP plugins in enterprise environments using the Admin Console
keywords:
  - UXP Plugins
  - Enterprise Deployment
  - Admin Console
  - Distribution
  - Creative Cloud Marketplace
  - CCX
  - UPIA Tool
contributors:
  - https://github.com/undavide
---

# Enterprise Distribution

As an Enterprise or Team administrator, you can distribute UXP plugins to users across your organization through the [Adobe Admin Console](https://adminconsole.adobe.com/) or the [Unified Plugin Installer Agent (UPIA) tool](https://helpx.adobe.com/creative-cloud/apps/integration-with-other-apps/manage-plugins/install-plugins-using-upia-tool.html).

## Overview

There are two primary ways to deploy UXP plugins at scale:

1. **Via the [Admin Console](https://adminconsole.adobe.com/) with Creative Cloud Marketplace integration**  
   [Add plugins](https://helpx.adobe.com/enterprise/using/manage-extensions.html#named-user-licenses) directly to your deployment packages or make them available for self-service installation.

2. **By bundling plugin installers (`.ccx` files) into [managed packages](https://helpx.adobe.com/enterprise/using/customize-creative-cloud-app.html#customize)**  
   [Manually place plugin files](https://helpx.adobe.com/enterprise/using/manage-extensions.html#others) in package folders and deploy them alongside Creative Cloud apps.

## 1. Deploy plugins through the Admin Console

When building a package in the Admin Console (for _Named User Licensing_):

- **Select plugins from the Adobe Marketplace** during package creation.  
  These plugins install automatically when the package is deployed.
- **Control user permissions**:
  - Allow users to self-install plugins from the Marketplace via the Creative Cloud desktop app.
  - Restrict installation rights so only IT manages plugin deployment.
- **Automatic updates**:  
  Marketplace plugins update through the Creative Cloud desktop app unless restricted.

This option works well when plugins are available on the Marketplace and you want streamlined, policy-driven distribution. See [this Admin Console documentation page](https://helpx.adobe.com/enterprise/using/manage-extensions.html#named-user-licenses) for more details.

## 2. Bundle `.ccx` plugins in managed packages

If your plugin isn't listed in the Marketplace—for example, for internal distribution:

- When creating a package, **enable the “create a folder for extensions” option** and [include the UPIA tool](https://helpx.adobe.com/enterprise/using/manage-extensions.html#others).
- A folder will be generated in the package structure; place your plugin’s `.ccx` files in this folder.
- When the package is deployed, the included plugins install automatically with the Creative Cloud apps.

See [this Admin Console documentation page](https://helpx.adobe.com/enterprise/using/manage-extensions.html#others) and the [UPIA tool documentation](https://helpx.adobe.com/creative-cloud/apps/integration-with-other-apps/manage-plugins/install-plugins-using-upia-tool.html) for more details.

## Important Considerations

- **App dependency**: Plugins only install if the corresponding host app (e.g., Premiere Pro) is also present in the package or already installed.
- **Error handling**: A plugin installation failure does _not_ block the package installation.
- **Activation**: If a plugin requires the host app to restart, users must restart the app before the plugin becomes active.
- **Unique IDs**: If you plan to distribute a plugin _both_ internally and through the Creative Cloud Marketplace, create a clone of your plugin with a different ID as explained [here](../package/index.md#mind-your-plugins-id).
- **UPIA tool**: An administrator can [deploy plugins](https://helpx.adobe.com/in/creative-cloud/apps/integration-with-other-apps/manage-plugins/install-plugins-using-upia-tool.html) anytime from the command line.
- **Offline use**: As outlined in [this FAQ](https://developer.adobe.com/developer-distribution/creative-cloud/docs/guides/faq#i-work-exclusively-offline-or-in-a-setting-where-access-to-the-internet-is-extremely-limited-can-i-use-scripts-plugins-extensions-or-c-plugins-how-can-i-install-all-of-the-above-without-the-creative-cloud-desktop-app-or-while-offline), in environments with limited internet access or under Adobe's Feature Restricted Licensing, it is still possible to install and use UXP plugins using `.ccx` files and the UPIA tool.
