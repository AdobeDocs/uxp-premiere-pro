---
title: Our Review Process
description: Review process
keywords:
  - UXP Plugins
  - Distribution
  - Review process
  - Branding Guidelines
  - Submission Checklist
contributors:
  - https://github.com/undavide
---

# Our Review Process

If you are looking to distribute your plugin to the Adobe Creative Cloud Marketplace, you will need to submit it for review.

## Overview

Plugins submitted to the Creative Cloud Marketplace always go through a review process, designed to ensure that every product—whether free or paid—meets Adobe's quality standards.

A dedicated team carefully audits and approves extensibility listings. To help avoid delays and keep the review queue moving smoothly, please ensure your plugin fully complies with our requirements.

<InlineAlert slots="text" variant="info"/>

We aim to review your plugin within **10 business days** of submission and will notify you whether it has been accepted or requires changes.

## Review Criteria

The review team will assess your submission based on a variety of factors, including:

- Branding
- Performance
- Harmful or unacceptable content
- User Experience
- Transparency
- Presence of bugs or harmful code
- Compatibility with operating systems, browsers, devices and other plugins

## Submission Checklist

Check off the tasks in this list before submitting. If you have any questions, feel free to contact us at [ccintrev@adobe.com](mailto:ccintrev@adobe.com).

### 1. Assets

Ensure that all required assets are included and named correctly in your plugin submission, as per the [Create Listing guide](../listing/index.md), including:

- Files
- Assets
- Release notes
- Testing information
- Share testing credentials with the review team so they can validate any paid/premium functionality (if applicable)

### 2. Metadata

Provide accurate and up-to-date information, including:

- Plugin name
- Version
- Author
- Contact information
- Trader information in the publisher profile if you wish to distribute your add-ons in the EU region. See the [EU Digital Services Act Trader Requirements](https://developer.adobe.com/compliance/) for more information.

### 3. Legal

Ensure that all legal and licensing requirements are met, including:

- Attribution
- Copyright
- Intellectual property rights

### 4. Branding Guidelines

Review the [Adobe Branding Guidelines](https://developer.adobe.com/developer-distribution/creative-cloud/docs/guides/branding-guidelines) thoroughly to ensure your plugin and all related materials—including advertising, websites, and other media—comply with Adobe’s branding standards.

These guidelines regulate, among other things, the correct usage of:

- The Adobe logo and other trademarks
- Adobe product names
- Approved badges and icons
- Social media presence

<InlineAlert slots="header, text" variant="info"/>

Do not underestimate the importance of adhering to guidelines.

Any violation may result in an immediate rejection of your submission. If you have any questions about the branding guidelines, please contact us at [CCDeveloperMarketing@adobe.com](mailto:CCDeveloperMarketing@adobe.com).

## Common Rejections Causes

The following table lists frequent reasons for plugin submission rejections, along with recommended actions to resolve them.

| Cause                                                                                                                                                                                             | Resolution                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Violation of Adobe Branding Guidelines**: your plugin, documentation, or marketing materials use Adobe trademarks or design elements in a way that conflicts with the official branding policy. | Review and align all assets with the Adobe Branding Guidelines. Remove or adjust any unapproved logos, icons, or references before resubmission.                  |
| **Blank User Interface on Launch**: the plugin opens with no visible or interactive elements due to initialization errors or missing assets.                                                      | Verify that all UI components, scripts, and dependencies load correctly. Test the plugin in a clean installation of the host application.                         |
| **Use of default/placeholder Icons**: the plugin includes default icons or missing variants for supported themes and sizes.                                                                       | Provide custom-designed icons for all required themes, resolutions, and display scales.                                                                           |
| **Non-functional buttons or silent failures**: interactive elements such as buttons or menus do not trigger actions or feedback, resulting in unclear or broken user flows.                       | Ensure all interactive components trigger expected actions, provide user feedback and progress indicators. Implement proper error handling for failed operations. |
| **AI-generated content contains inappropriate material**: AI features in the plugin generate or display explicit, offensive, or policy-violating content.                                         | Apply robust content filtering or moderation to comply with Adobe’s content safety policies.                                                                      |
| **Missing test data or credentials**: reviewers cannot access the plugin’s features because required test datasets, demo accounts, or credentials are not provided.                               | Include valid test data and credentials in the submission package, along with any access or setup instructions needed for review.                                 |
