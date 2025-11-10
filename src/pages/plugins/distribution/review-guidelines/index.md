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

# Review & Guidelines

If you are looking to distribute your plugin to the Adobe Creative Cloud Marketplace, you will need to submit it for review and follow our guidelines.

## Overview

Plugins submitted to the Creative Cloud Marketplace always go through a review process, designed to ensure that every product—whether free or paid—meets Adobe's quality standards.

A dedicated team carefully audits and approves extensibility listings. To help avoid delays and keep the review queue moving smoothly, please ensure your plugin fully complies with our requirements.

<InlineAlert slots="text" variant="info"/>

We aim to review your plugin within **10 business days** of submission and will notify you whether it has been accepted or requires changes.

## Review Criteria

The review team will assess your submission based on a variety of factors, including:

- **Branding and Trademark Compliance**: proper use of Adobe trademarks, brand assets, and naming conventions
- **Listing Quality**: clear descriptions, valid links, appropriate subtitle, and support channel availability
- **Functional Testing**: UI behavior, button functionality, input handling, error feedback, and keyboard shortcuts
- **Platform Compatibility**: multi-architecture support, code signing, and installation behavior
- **External Services Integration**: login/logout flows, test credentials, and service connectivity
- **User Experience**: responsive layouts, loading indicators, scrolling behavior, and accessibility
- **Performance**: resource usage (CPU/RAM) and compatibility with host applications
- **Localization**: multi-locale support and keyboard compatibility
- **Content Safety**: harmful or unacceptable content policies
- **Transparency**: privacy policies, terms of service, and third-party dependencies
- **Code Quality**: presence of bugs, harmful code, or exposed developer tools

## Submission Checklist

Check off the tasks in this list before submitting. If you have any questions, feel free to contact us at [ccintrev@adobe.com](mailto:ccintrev@adobe.com).

### 1. Assets

Ensure that all required assets are included and named correctly in your plugin submission, as per the [Create Listing guide](../listing/index.md), including:

- **Files**: all required plugin files and dependencies
- **Icons**: custom-designed icons for all themes, resolutions, and display scales (no placeholder or default icons)
- **Screenshots**: high-quality screenshots that accurately represent your plugin's functionality
- **Release notes**: clear documentation of changes and new features
- **Testing information**: comprehensive testing instructions and scenarios
- **Test credentials**: share login credentials, license keys, or test accounts with the review team so they can validate all functionality, including any paid or premium features

All visual assets must:

- Be free of unauthorized Adobe logos or trademarks
- Display correctly in both light and dark themes
- Meet the required dimensions specified in Adobe's documentation
- Use unique icons for each panel (if your plugin has multiple panels)

### 2. Metadata

Provide accurate and up-to-date information, including:

- **Plugin name**: must be unique and use ASCII-only characters in the manifest
- **Subtitle**: must be relevant and clearly describe what the plugin does
- **Description**: must be clear, accurate, and localized where applicable; avoid vague or misleading language
- **Version**: current version number
- **Author**: developer or company name
- **Contact information**: valid email or support channel (email, GitHub, or website with contact form)
- **Website and support links**: must open successfully and contain valid contact information
- **Privacy policy and terms of service**: must provide valid, accessible URLs
- **Third-party dependencies**: clearly mention if your plugin requires another application or service
- **Pricing information**: if your plugin is paid, offers a trial, or has a free tier, this must be clearly stated
- **Trader information**: required in the publisher profile if you wish to distribute your plugins in the EU region. See the [EU Digital Services Act Trader Requirements](https://developer.adobe.com/compliance/) for more information.

<InlineAlert slots="text" variant="warning"/>

Avoid mentioning competitor names (e.g., Figma, Canva) in your plugin listing or materials.

### 3. Legal

Ensure that all legal and licensing requirements are met, including:

- Attribution
- Copyright
- Intellectual property rights

### 4. Branding Guidelines

Review the [Adobe Branding Guidelines](https://developer.adobe.com/developer-distribution/creative-cloud/docs/guides/branding-guidelines) thoroughly to ensure your plugin and all related materials—including advertising, websites, and other media—comply with Adobe's branding standards.

These guidelines regulate, among other things, the correct usage of:

- The Adobe logo and other trademarks
- Adobe product names (do not use Adobe trademarks like "Photoshop Enhancer" without written permission)
- Approved badges and icons
- Social media presence
- Public profile and website content

<InlineAlert slots="header, text" variant="info"/>

Do not underestimate the importance of adhering to guidelines.

Any violation may result in an immediate rejection of your submission. If you want to use Adobe brand assets, fill out the Trademark Request Form and email it to [permissions2@adobe.com](mailto:permissions2@adobe.com) and [brand@adobe.com](mailto:brand@adobe.com). Allow up to 2 weeks for processing. If you have any questions about the branding guidelines, please contact us at [CCDeveloperMarketing@adobe.com](mailto:CCDeveloperMarketing@adobe.com).

### 5. Platform Compatibility

Ensure your plugin works correctly across all supported platforms and architectures:

- **Multi-architecture support**: for UXP Hybrid C++ plugins, test on Mac M1, Mac Intel, and Windows Intel
- **Code signing**: macOS plugins must be code signed and notarized with a valid certificate (minimum 1 year validity)
- **Installation**: avoid OS-level warning prompts during installation; ensure no crashes during install or use
- **Host application compatibility**: test that your plugin does not crash or negatively impact host applications

### 6. Functional Requirements

Your plugin must meet the following functional standards:

- **Launch behavior**: plugin must launch successfully via the Plugins menu, Plugins panel, or other entry points
- **User interface**: no empty screens, blank panels, or clipped modal dialogs; every screen must display meaningful content
- **Loading indicators**: display progress feedback for any content or operations that take time to load
- **Buttons and controls**: all interactive elements must be visible, not overlap, and perform their expected actions
- **Input handling**: text fields must support English characters, special characters, numbers, and localized keyboards
- **Error handling and feedback**: provide clear user guidance when actions fail, selections are unsupported, or internet is disconnected; plugin must recover gracefully after reconnecting
- **Keyboard shortcuts**: must work as expected (except in applications where unsupported, such as InDesign v18.5 or Premiere Pro v25.6)
- **Scrolling behavior**: scrollbars must appear when needed; content must be accessible without resizing the panel
- **Responsive layout**: plugin must work without requiring users to resize the panel
- **No developer tools**: do not expose debug consoles or developer tools in production builds

### 7. External Services Integration

If your plugin connects to external services, ensure the following:

- **Test credentials**: provide valid test login credentials or license keys in the "Notes to Reviewer" section
- **Login and signup flow**: users must be able to sign up or log in; if login is browser-based, the plugin must handle abandoned login gracefully and provide a link back to your website
- **Logout functionality**: users must be able to log out from within the plugin
- **Service connectivity**: handle network failures gracefully with appropriate user feedback

### 8. Companion Apps

If your plugin uses a companion application:

- The companion app must install successfully on all supported operating systems
- The plugin must communicate with the companion app successfully
- Monitor for abnormal CPU or RAM usage
- The plugin must not launch external applications (only browser links are allowed)

### 9. Localization

If your plugin supports multiple languages:

- Test plugin functionality in all supported locales (Mac only for review purposes)
- Ensure no string truncation occurs in any supported language
- Support localized keyboard layouts and input methods

### 10. Performance and Resource Usage

Your plugin must demonstrate responsible resource management:

- Monitor and optimize CPU and RAM consumption
- Ensure the plugin does not cause performance degradation in host applications
- Avoid memory leaks or excessive background processing

## Common Rejections Causes

The following table lists frequent reasons for plugin submission rejections, along with recommended actions to resolve them.

| Cause                                                                                                                                                                                             | Resolution                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Violation of Adobe Branding Guidelines**: your plugin, documentation, or marketing materials use Adobe trademarks or design elements in a way that conflicts with the official branding policy. | Review and align all assets with the Adobe Branding Guidelines. Remove or adjust any unapproved logos, icons, or references before resubmission.                  |
| **Blank User Interface on Launch**: the plugin opens with no visible or interactive elements due to initialization errors or missing assets.                                                      | Verify that all UI components, scripts, and dependencies load correctly. Test the plugin in a clean installation of the host application.                         |
| **Use of default/placeholder Icons**: the plugin includes default icons or missing variants for supported themes and sizes.                                                                       | Provide custom-designed icons for all required themes, resolutions, and display scales.                                                                           |
| **Non-functional buttons or silent failures**: interactive elements such as buttons or menus do not trigger actions or feedback, resulting in unclear or broken user flows.                       | Ensure all interactive components trigger expected actions, provide user feedback and progress indicators. Implement proper error handling for failed operations. |
| **AI-generated content contains inappropriate material**: AI features in the plugin generate or display explicit, offensive, or policy-violating content.                                         | Apply robust content filtering or moderation to comply with Adobe's content safety policies.                                                                      |
| **Missing test data or credentials**: reviewers cannot access the plugin's features because required test datasets, demo accounts, or credentials are not provided.                               | Include valid test data and credentials in the submission package, along with any access or setup instructions needed for review.                                 |
| **Clipped or invisible modal dialogs**: modal dialogs are partially visible or appear off-screen, preventing user interaction.                                                                    | Test modal dialogs at various panel sizes and ensure they are fully visible and properly centered.                                                                |
| **Missing loading indicators**: the plugin appears unresponsive during long operations without feedback to the user.                                                                              | Add loading spinners, progress bars, or status messages for any operation that takes more than 1-2 seconds.                                                       |
| **Poor input field handling**: text fields fail with special characters, numbers, or localized keyboard input.                                                                                    | Test input fields with various character sets, including special characters and non-English keyboards. Implement proper validation and error messages.            |
| **Inadequate error messaging**: the plugin fails silently or shows generic errors without guidance on how to resolve issues.                                                                      | Provide specific, actionable error messages that guide users toward solutions. Handle edge cases like network failures gracefully.                                |
| **Code signing issues**: macOS plugins are not properly code signed or notarized, triggering security warnings.                                                                                   | Ensure plugins are signed with a valid Developer ID certificate and notarized through Apple. Certificate must be valid for at least 1 year.                       |
| **Multi-architecture failures**: UXP Hybrid C++ plugins crash or fail on specific architectures (M1, Intel, Windows).                                                                             | Test on all supported architectures: Mac M1, Mac Intel, and Windows Intel. Build separate binaries for each architecture if needed.                               |
| **Exposed developer tools**: debug consoles, developer menus, or testing features are accessible in the production build.                                                                         | Remove all development and debugging interfaces before submission. Ensure production builds do not include dev dependencies.                                      |
| **Poor responsive design**: plugin requires manual resizing to access controls or content; scrollbars don't appear when needed.                                                                   | Implement responsive layouts that adapt to panel sizes. Ensure scrollbars appear automatically when content exceeds visible area.                                 |
| **Companion app integration issues**: the plugin cannot communicate with its companion application, or the companion app causes excessive resource usage.                                         | Test companion app integration thoroughly. Optimize resource usage and ensure reliable communication between plugin and companion app.                            |
| **Localization problems**: strings are truncated in non-English languages, or the plugin fails with localized keyboards.                                                                          | Test all supported locales and ensure UI elements accommodate longer text strings. Support international keyboard layouts.                                        |
| **Invalid or broken links**: website URLs, support links, privacy policy, or terms of service links are broken or lead to incorrect pages.                                                        | Verify all links open successfully and direct users to the correct, relevant content.                                                                             |
| **Missing third-party dependency disclosure**: the plugin requires an external application but does not inform users in the listing.                                                              | Clearly state any third-party application requirements in your plugin description and documentation.                                                              |
| **Inadequate support channel**: no contact method is provided, or the provided support email/link is invalid.                                                                                     | Provide a valid support channel such as email, GitHub issues, or a website contact form.                                                                          |

## Content Requirements

Plugins must adhere to [Adobe's General Terms of Use](https://www.adobe.com/legal/terms.html) and Content Policies found in the [Adobe Transparency Center](https://www.adobe.com/trust/transparency.html). For example, in the interests of user safety and acceptable standards, plugins must not:

- Contain or generate illegal content (such as CSAM, content that encourages illegal drug use, etc.).
- Contain or generate adult content (such as sexual content, nudity—consensual and non-consensual, gore, graphic gore or violence, or strong language).
- Contain or generate hate speech or speech that promotes violence or bullying or cruel behavior to anyone.
- Generate content that promotes, automates, or facilitates highly regulated activities (such as financial advice, medical advice or diagnosis, legal advice or documents, contracts).
- Contain or generate code that is malicious (such as viruses, malware, spyware, etc.).
- Participate in misinformation/disinformation campaigns.
- Violate intellectual property rights, including copyright, of other persons and companies.
- Automatically perform actions determined by AI that would be destructive or that can't be undone without explicit user consent.

## Generative AI Guidelines

If your plugin leverages generative AI to create content, it must adhere to [Adobe's General Terms of Use](https://www.adobe.com/legal/terms.html), Developer Terms of Use and Content Policies found in the [Adobe Transparency Center](https://www.adobe.com/trust/transparency.html). Specifically:

- Your plugin must not generate illegal, adult, or hateful content.
- Your plugin must leverage filtering technologies to prevent the generation of prohibited content.
- You must thoroughly test your plugin to ensure that illegal content is not generated.
- Your plugin must not automate regulated activities (such as financial, medical, or legal advice) without proper disclaimers and user consent.
- Your plugin must not generate malicious code or participate in misinformation campaigns.
- Your plugin must not violate intellectual property rights of other persons and companies.
- Your plugin must not perform destructive actions without explicit user consent.

<InlineAlert slots="text" variant="warning"/>

Before a plugin leveraging generative AI is approved for publication, you may be asked to certify that you have read these guidelines and agree to abide by them. If your plugin is found to be generating illegal content, your plugin will be removed. If you believe that we made a mistake in removing or restricting your plugin, then you may appeal that action through the [Adobe Transparency Center](https://www.adobe.com/trust/transparency.html).
