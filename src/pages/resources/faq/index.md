---
title: Frequently Asked Questions
description: Frequently Asked Questions
keywords:
  - FAQ
  - Frequently Asked Questions
  - UXP
  - Premiere Pro
  - UXP Developer Tool
  - UXP Developer Tool FAQ
  - UXP Developer Tool Frequently Asked Questions
---

# Frequently Asked Questions

This section contains frequently asked questions about UXP and Premiere Pro.

## Questions

### 🛠️ Development Environment & Tooling

- [How can I enable Developer Mode?](#how-can-i-enable-developer-mode)
- [In UDT, I get the error "Plugin Load Failed, Host Application specified is not available. Make sure the host application is started."](#in-udt-i-get-the-error-plugin-load-failed-host-application-specified-is-not-available-make-sure-the-host-application-is-started)

### 🎨 User Interfaces

- [How can I use Spectrum Web Components in my plugin?](#how-can-i-use-spectrum-web-components-in-my-plugin)
- [Can I use React Spectrum instead of Spectrum Web Components?](#can-i-use-react-spectrum-instead-of-spectrum-web-components)

### 📦 Installers and Packages

- [I am unable to install a plugin.](#i-am-unable-to-install-a-plugin)
- [My `.ccx` package is being rejected when submitted to the Creative Cloud Marketplace. What could be wrong?](#my-ccx-package-is-being-rejected-when-submitted-to-the-creative-cloud-marketplace-what-could-be-wrong)
- [Should I use an Array or an Object for the `host` property in the `manifest.json`?](#should-i-use-an-array-or-an-object-for-the-host-property-in-the-manifestjson)
-

### 🇪🇺 EU Compliance & DSA Requirements

- [Why is my plugin not visible in the EU region?](#why-is-my-plugin-not-visible-in-the-eu-region)
- [How can I update my trader details in the publisher profile after submission?](#how-can-i-update-my-trader-details-in-the-publisher-profile-after-submission)
- [What happens if an EU user has a deep link to my plugin and I am not compliant with the European Union Digital Services Act (DSA) trader requirements?](#what-happens-if-an-eu-user-has-a-deep-link-to-my-plugin-and-i-am-not-compliant-with-the-european-union-digital-services-act-dsa-trader-requirements)
- [Can an EU user still use my plugin if they have already installed it, but I am not compliant with the DSA trader requirements?](#can-an-eu-user-still-use-my-plugin-if-they-have-already-installed-it-but-i-am-not-compliant-with-the-dsa-trader-requirements)

## Answers

<!-- Let's keep the answers in the same order as the questions! -->

<!-- ### 🛠️ Development Environment & Tooling -->

#### How can I enable Developer Mode?

You need to enable Developer mode in both the UXP Developer Tool and the host application. Follow the instructions in the [UXP Developer Tool](../../introduction/essentials/dev-tools/index.md#first-launch) and [Premiere Pro](../../plugins/index.md#prerequisites) guides.

#### In UDT, I get the error "Plugin Load Failed, Host Application specified is not available. Make sure the host application is started."

Ensure that Premiere Pro is running. If it is, check that the host application's Developer Mode is enabled; follow the instructions in the [this guide](../../plugins/index.md#prerequisites).

<!-- 🎨 User Interfaces -->

#### How can I use Spectrum Web Components in my plugin?

You can use Spectrum Web Components in your plugin by following the instructions in the [Spectrum Web Components](../../uxp-api/reference-spectrum/swc/index.md) guide.

#### Can I use React Spectrum instead of Spectrum Web Components?

Given that UXP does not support the entire set of HTML Elements and CSS properties, [React Spectrum](https://react-spectrum.adobe.com/react-spectrum/index.html) components may not work as expected. For this reason, we recommend using [React Wrappers for Spectrum Web Components](https://opensource.adobe.com/spectrum-web-components/using-swc-react/) instead. Make sure you have enabled the `enableSWCSupport` feature flag in your `manifest.json` file and installed the right version of the components.

<!-- 📦 Installers and Packages -->

#### I am unable to install a plugin.

Please refer to [these troubleshooting steps](../../plugins/distribution/install/index.md#troubleshooting) for more details.

#### My `.ccx` package is being rejected when submitted to the Creative Cloud Marketplace. What could be wrong?

Check if the [`host`](../../plugins/concepts/manifest/index.md#host) property in your `manifest.json` is an object, not an array. If it's an array, the validation will fail. See [Host Applications](../../plugins/distribution/package/index.md#host-applications) for details.

#### Should I use an Array or an Object for the `host` property in the `manifest.json`?

The `host` property must be a single [`HostDefinition`](../../plugins/concepts/manifest/index.md#hostdefinition) Object for production. Arrays are only allowed during development for convenience. See the [Package a UXP plugin](../../plugins/distribution/package/index.md#host-applications) section for details.

<!-- 🇪🇺 EU Compliance & DSA Requirements -->

#### Why is my plugin not visible in the EU region?

This could be due to incomplete or outdated trader information in your publisher profile. Please make sure all required details are updated and accurate.

#### How can I update my trader details in the publisher profile after submission?

To update only your trader details in the publisher profile after submission, please contact our team at [ccintrev@adobe.com](mailto:ccintrev@adobe.com). At this time, we are not processing change requests for other fields in the publisher profile.

#### What happens if an EU user has a deep link to my plugin and I am not compliant with the European Union Digital Services Act (DSA) trader requirements?

If you are not compliant with the European Union Digital Services Act trader requirements, an EU user with a deep link to your plugin will not be able to install it. They will see a banner with a message indicating the compliance issue.

#### Can an EU user still use my plugin if they have already installed it, but I am not compliant with the DSA trader requirements?

Yes, if an EU user has already installed your plugin, they will still be able to use it even if you are not compliant with the DSA trader requirements. However, they will see a banner with a message indicating the compliance issue.
