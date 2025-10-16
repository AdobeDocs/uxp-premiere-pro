---
title: Network Operations
description: Learn how to connect your UXP plugin to the web — fetch data, communicate with APIs, and establish WebSocket connections securely.
keywords:
  - network
  - fetch
  - xhr
  - websockets
  - permissions
  - api requests
  - async
  - http
contributors:
  - https://github.com/padmkris123
  - https://github.com/undavide
---

# Network Operations

Learn how to connect your UXP plugin to the web

UXP provides powerful network APIs that let your plugin **fetch data**, **access online services**, and **communicate in real time**—all while keeping users safe through a robust permission model. This guide covers how to use `fetch`, `XMLHttpRequest`, and `WebSocket` in UXP, how to declare network permissions properly, and how to handle errors.

## Prerequisites

Before you begin, make sure your development environment uses the following versions:

- **Premiere Pro v25.6** or higher
- **UDT v2.2.0** or higher
- **Manifest version v5** or higher

## Network Security

By default, UXP plugins can't connect to the internet; this helps keep users safe by preventing unwanted or hidden network activity. If your plugin needs to fetch data, load images, or use WebSockets, **you must declare** the right [network permissions](../../../plugins/concepts/manifest/index.md#permissionsdefinition).

In your plugin's `manifest.json`, use the [`requiredPermissions.network`](../../../plugins/concepts/manifest/index.md#networkpermission) object to lists the domains your plugin can access.

```json
{
  "requiredPermissions": {
    "network": {
      "domains": [
        "https://api.example.com",
        "https://*.adobe.io"
      ]
    }
  }
}
```

You may use wildcards for domain patterns, such as `"https://api.*.example.com"` to match multiple environments (for example, dev, staging, and production). **Any request to an unlisted domain will fail** with a permission error.

<InlineAlert variant="warning" slots="text"/>

All APIs support both HTTP and HTTPS, but macOS restricts `http://` for security reasons. You should use `https://` instead.

## Choose the right Network API

UXP supports three primary ways to perform network communication:

| API            | Best For                            | Supported Features                 |
| -------------- | ----------------------------------- | ---------------------------------- |
| fetch          | Modern, promise-based HTTP requests | JSON, text, binary data, streaming |
| XMLHttpRequest | Legacy compatibility                | Progress events, upload tracking   |
| WebSocket      | Real-time communication             | Persistent bidirectional data flow |

Network APIs are available globally in UXP, you don't need to import them. Let's explore each one in depth.

### Using fetch()

The [`fetch()`](../../../uxp-api/reference-js/Global%20Members/Data%20Transfers/fetch.md) API is the simplest and most flexible way to make network requests. It's modern, asynchronous, and built into the UXP global scope—no `require()` needed.

<CodeBlock slots="heading, code" repeat="2" languages="JavaScript, JSON" />

#### index.js

```js
// Get weather forecast for San Jose ☀️
async function getForecast() {
try {
const response = await fetch(
  "https://api.weather.gov/gridpoints/MTR/99,82/forecast"
  );

  if (!response.ok) {
    throw new Error(
      `HTTP error ${response.status}: ${response.statusText}`
    );
  }
  const data = await response.json(); // 👈 parse the response as JSON
  console.log(
    `Forecast: ${data.properties.periods[0].detailedForecast}`
  );

  } catch (err) {
    console.error("❌ Failed to fetch forecast:", err);
  }
}
```

#### manifest.json

```json
{
  // ...
  "requiredPermissions": {
    "network": {
      "domains": ["https://api.weather.gov"]
    }
  }
  // ...
}
```

<InlineAlert variant="info" slots="text"/>

Remember to parse the `response` object as `json()`, `text()`, and `blob()` for the appropriate data types. These methods return [Promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise), so you must use `await` to get the data.

### Example: Fetching an Image Dynamically

You can even use network data directly in your UI.

<CodeBlock slots="heading, code" repeat="2" languages="HTML, JSON" />

#### index.html

```html
<img src="https://picsum.photos/300/200" alt="A random image" />
```

#### manifest.json

```json
{
  // ...
  "requiredPermissions": {
    "network": {
      "domains": ["https://picsum.photos/"]
    }
  }
  // ...
}
```

The `<img>` tag works seamlessly in UXP, provided the remote domain is allow-listed.

### Example: POST Requests and JSON Payloads

Many web APIs expect [POST requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/POST) with JSON bodies. Here's how to send data safely.

```js
async function postUserData(user) {
  try {
    const response = await fetch("https://api.example.com/users", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(user)
    });

    if (!response.ok) throw new Error(`Server error: ${response.status}`);
    const result = await response.json();
    console.log("✅ User created:", result);

  } catch (err) {
    console.error("Failed to post user data:", err);
  }
}

// Example usage
postUserData({ name: "Jamie", role: "Editor" });
```

<InlineAlert variant="warning" slots="header, text"/>

UXP is not a browser environment

We have [mentioned this before](../../../introduction/index.md#uxp-is-not-a-browser); some features you're familiar with are not available. For example, you can't use the `TextDecoder` class to read a data stream.

```js
async function fetchStreamedData() {
  const response = await fetch("https://api.example.com/stream");
  const reader = response.body.getReader();
  const decoder = new TextDecoder(); // ❌ decoder is undefined here!!
  // ...
}
```

### Using XMLHttpRequest (XHR)

`XMLHttpRequest` is the older, event-driven API. It's still useful when you need progress events or upload monitoring.

<CodeBlock slots="heading, code" repeat="2" languages="JavaScript, JSON" />

#### index.js

```js
function getForecastWithXHR() {
const xhr = new XMLHttpRequest();
xhr.open(
  "GET",
  "https://api.weather.gov/gridpoints/MTR/99,82/forecast"
);
xhr.responseType = "json";

xhr.onload = () => {
  if (xhr.status === 200) {
    console.log(
      `Forecast: ${xhr.response.properties.periods[0].detailedForecast}`
    );
  } else {
    console.error(`XHR failed with status ${xhr.status}`);
  }
};

  xhr.onerror = () => console.error("Network error occurred");
  xhr.send();
}
```

#### manifest.json

```json
{
  // ...
  "requiredPermissions": {
    "network": {
      "domains": ["https://api.weather.gov"]
    }
  }
  // ...
}
```

### Using WebSocket

WebSockets let your plugin maintain a live connection to a server—ideal for apps that need to update in real time.

<CodeBlock slots="heading, code" repeat="2" languages="JavaScript, JSON" />

#### index.js

```js
let socket;

async function connectToServer() {
  try {
    if (socket) {
      console.log("🔌 Disconnecting existing socket...");
      socket.close();
      socket = null;
      return;
    }

    socket = new WebSocket(
      "wss://javascript.info/article/websocket/demo/hello"
    );

    socket.onopen = () => {
      console.log("✅ WebSocket connection established");
      socket.send("Hello from Premiere Pro plugin!");
    };

    socket.onmessage = (event) => {
      console.log(`📩 Message from server: ${event.data}`);
    };

    socket.onerror = (err) => {
      console.error("⚠️ WebSocket error:", err);
    };

    socket.onclose = () => {
      console.log("Connection closed");
      socket = null;
    };

  } catch (e) {
    console.error("Failed to connect via WebSocket:", e);
  }
}
```

#### manifest.json

```json
{
  // ...
  "requiredPermissions": {
    "network": {
     "domains": ["wss://javascript.info"]
    }
  }
  // ...
}
```

<InlineAlert variant="info" slots="header,text"/>

UXP supports WebSocket clients only

Plugins can connect to WebSocket servers, but cannot host or accept incoming connections.

### Handling Errors and Timeouts

Network calls can fail—the user may be offline, the endpoint may be down, or your permission list might be incomplete.

Best practices:

- Always wrap network calls in `try...catch` blocks.
- Use `response.ok` to detect HTTP errors.
- Set reasonable timeouts for long operations.
- Log informative errors using `console.error()`.

```js
async function safeFetch(url, options = {}, timeoutMs = 8000) {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), timeoutMs);

  try {
    const res = await fetch(url, { ...options, signal: controller.signal });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();
  } catch (err) {
    console.error("Network request failed:", err);
    throw err;
  } finally {
    clearTimeout(timeout);
  }
}
```

### Troubleshooting Common Issues

| Symptom                                  | Likely Cause                       | Solution                                                                        |
| ---------------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------- |
| TypeError: Failed to fetch               | Domain not allow-listed            | Add the domain under `requiredPermissions.network.domains`                      |
| Connection fails only on macOS           | HTTPS required                     | Premiere Pro disallows http:// URLs on macOS                                    |
| Request blocked by CORS                  | Remote server missing CORS headers | Ensure your server allows requests from UXP (check Access-Control-Allow-Origin) |
| WebSocket connection closed unexpectedly | Server-side disconnect             | Check for idle timeout or SSL misconfiguration                                  |

## Reference Material

- [`fetch`](../../../uxp-api/reference-js/Global%20Members/Data%20Transfers/fetch.md) API Reference.
- [`XMLHttpRequest`](../../../uxp-api/reference-js/Global%20Members/Data%20Transfers/XMLHttpRequest.md) Reference.
- [`WebSocket`](../../../uxp-api/reference-js/Global%20Members/Data%20Transfers/WebSocket.md) Reference.
- [Manifest Permissions](../../../plugins/concepts/manifest/index.md#permissionsdefinition).
- [Network Permission Details](../../../plugins/concepts/manifest/index.md#networkpermission).

## Summary

1. **Network Security Model**: By default, UXP plugins cannot access the internet. All network operations require explicit declaration of permitted domains in the `manifest.json` file under `requiredPermissions` to prevent unwanted network activity.
   - Add specific domains to the `domains` array (e.g., `"https://api.example.com"`).
   - Use wildcards for flexible domain patterns (e.g., `"https://*.adobe.io"`),
   - Any request to an unlisted domain will fail with a permission error,
   - On macOS, `http://` URLs are restricted for security reasons; use `https://` instead.
2. **Three Network APIs**: Choose based on your use case:
   - **`fetch()`**: Modern, promise-based API for HTTP requests; supports JSON, text, binary data, and streaming; ideal for most use cases.
   - **`XMLHttpRequest`**: Legacy, event-driven API; useful for progress events and upload tracking; provides compatibility with older code patterns.
   - **`WebSocket`**: Real-time, bidirectional communication; maintains persistent connections to servers; client-only (plugins cannot host WebSocket servers).
