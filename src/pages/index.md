---
title: The Premiere Pro UXP API
description: An introduction into the Premiere Pro UXP API
keywords:
  - Premiere Pro UXP API
  - Premiere Pro
  - UXP
  - Scripting
  - Extensibility
contributors:
  - https://github.com/icaraps 
  - https://github.com/undavide
---

<Hero slots="heading, text" background = "rgb(200, 10, 10)"/>

# Premiere Pro UXP API

A modern extensibility platform for building Custom Tools and Features that streamline workflows in any unique Premiere Pro environment.

<Resources slots="heading, links"/>

#### Resources

- [What's new](./changelog/index.md)
- [UXP Plugins](./plugins/index.md)
- [Share & Distribute](./resources/distribution/overview/index.md)
- [UXP APIs](./uxp-api/index.md)
- [Premiere Pro DOM APIs](./ppro_reference/index.md)
- [Developer Forums](https://forums.creativeclouddeveloper.com/)

## Overview

UXP (**U**nified e**X**tensibility **P**latform) is an integration framework built into Premiere Pro and other Adobe Creative Cloud applications. It is powered by a modern JavaScript engine and offers the ability to access many Premiere Pro functions at a programmatic level. With UXP, you can build unique tools that integrate with and optimize the most precise, demanding workflows. These tools reduce repetition, maximize efficiency, and transform Premiere Pro into a bespoke application tailored to the needs of any project.

Best of all, UXP Plugins run right in Premiere Pro.

Premiere Pro adds its own set of APIs on top of the base UXP functionality shared across the supported Adobe applications. This website provides documentation for both the Premiere Pro API and the base UXP API.

![UDT Interface](./UDT_sample_image_01_cropped.png)

<DiscoverBlock slots="heading, text"/>

## Features

**Fast and Interactive Development.** Load, run, and update panels directly without restarting Premiere Pro.

<DiscoverBlock slots="text"/>

**Built-in Debugger.** Quickly trace code using the built-in debugger that natively attaches to Premiere Pro.

<DiscoverBlock slots="text"/>

**Threaded Execution.** UXP operates concurrently with other Premiere Pro processes. You can continue working in Premiere Pro while the UXP Plugin functions are running.

## Updates

The Premiere Pro UXP API and this documentation website will be updated regularly as new versions are released and new features are introduced. Check out the [Change Log](./changelog/index.md) for the latest news.

## Join the community

Join the worldwide community of Creative Cloud Developers who are building plugins and integrations to empower creativity!

Here are a few other ways to get involved:

- Join the [Creative Cloud Developer Forums](https://forums.creativeclouddeveloper.com/) to meet other developers, ask questions, and offer help.
- Subscribe to the [Adobe Creative Cloud Developer Newsletter](https://www.adobe.com/subscription/ccdevnewsletter.html).

<!-- ## Discover

<DiscoverBlock width="100%" slots="heading, link, text"/>

### Get Started

[Quickstart Guide](guides/)

Get started with the Cat Analytics APIs.

<DiscoverBlock slots="heading, link, text"/>

### Guides

[Calculated Metrics API](guides/dummy_metrics_api/)

Returns information on the user's company that is necessary for making other Cat Analytics API calls.

<DiscoverBlock slots="link, text"/>

[Segments API](guides/dummy_oauth_client/)

Provides configuration guidance and best practices for the /segments endpoint.

<DiscoverBlock slots="link, text"/>

[Reporting Guide API](guides/dummy_using_postman/)

Provides configuration guidance and best practices for the /reports endpoint.

<DiscoverBlock slots="link, text"/>

[Migrating from 1.4 to 2.0](guides/migrating/)

For help migrating from the 1.4 versions of the Analytics API to the newer and more capable /reports API.

<DiscoverBlock width="100%" slots="heading, link, text"/>

### API References

[Try the API](api/)

Try the Analytics API with Swagger UI. Explore, make calls, with full endpoint descriptions.

## Contributing

We encourage you to participate in our open documentation initiative, if you have suggestions, corrections, additions
or deletions for this documentation, check out the source from [this github repo](https://github.com/adobe/gatsby-theme-spectrum-example), and submit a pull
request with your contribution. For more information, refer to the [contributing page](support/contribute/).

## API Requests & Rate Limits

The timeout for API requests through adobe.io is currently *60 seconds*.

The default rate limit for an Cat Analytics Company is *120 requests per minute*. (The limit is enforced as *12 requests every 6 seconds*).
When rate limiting is being enforced you will get `429` HTTP response codes with the following response body: `{"error_code":"429050","message":"Too many requests"}`. -->
