---
title: Network
description: Network pi
keywords:
  - fetch
  - xhr
  - websockets
contributors:
  - https://github.com/padmkris123
---

# Network I/O

You may be looking for ways to make network calls for various reasons such as fetching an image, accessing a web API, browsing remote resources, synchronizing content, etc. UXP supports a range of network APIs that can fit your use case.

<!--InlineAlert variant="info" slots="header, text1, text2"/-->

<!--Plugins and Scripts-->

**In plugins**, you should seek permission for `` access in the manifest and specify the `domains` of the endpoints. <br></br>
IMPORTANT: Please read about the [manifest permissions](../../../plugins/concepts/manifest/index.md#networkpermission) module before you proceed.

<!-- **In scripts**, the permission for `network` is fixed. You can ignore the manifest details in the following examples. Learn about these values in the [manifest fundamentals section](../../fundamentals/manifest/). -->

The fastest way to try out a network call is by rendering an image from the web

<CodeBlock slots="heading, code" repeat="2" languages="HTML, JSON" />

#### HTML

```html
<img src='https://picsum.photos/200/300' />
```

#### manifest

```json
{
    "requiredPermissions": {
        "network": {
            "domains": [
                "https://picsum.photos/"
            ]
        }
    }
}
```

As mentioned earlier, UXP has `fetch`, `XHR (XML HTTP Request)`, and `WebSocket` available in the global scope. If you aren't aware of the difference and want to understand which one is the right option for you, we recommend you learn about them first - [fetch](https://javascript.info/fetch) | [WebSocket](https://javascript.info/websocket) | [XHR](https://javascript.info/xmlhttprequest)

## System requirements

Please make sure your local environment uses the following application versions before proceeding.

- Premiere Pro v25.2 or higher
- UDT v2.1.0 or higher
- Manifest version v5 or higher

## Examples

Now, let's look at some examples.

### fetch

<CodeBlock slots="heading, code" repeat="2" languages="JavaScript, JSON" />

#### JavaScript

```js
async function foo() {
    // Get weather forecast for San Jose
    try {
        const response = await fetch(`https://api.weather.gov/gridpoints/MTR/99,82/forecast`);
        if (!response.ok) {
            throw new Error(`HTTP error fetching weather station; status: ${response.status}`);
        }
        const responseJson = await response.json();
        console.log(`Forecast ${responseJson.properties.periods[0].detailedForecast}`);

    } catch (e) {
        console.error(e);
    }
}
```

#### manifest

```json
{
    "requiredPermissions": {
        "network": {
            "domains": [
                "https://api.weather.gov"
            ]
        }
    }
}
```

### XHR

<CodeBlock slots="heading, code" repeat="2" languages="JavaScript, JSON" />

#### JavaScript

```js
function foo() {
    // Get weather forecast for San Jose via XHR
    const xhr = new XMLHttpRequest();
    xhr.open('GET', 'https://api.weather.gov/gridpoints/MTR/99,82/forecast');
    xhr.responseType = 'json';
    xhr.send();

    xhr.onload = function() {
        const responseObj = xhr.response;
        console.log(`Forecast ${responseObj.properties.periods[0].detailedForecast}`);
    };
}
```

#### manifest

```json
{
    "requiredPermissions": {
        "network": {
            "domains": [
                "https://api.weather.gov"
            ]
        }
    }
}
```

### WebSockets

<CodeBlock slots="heading, code" repeat="2" languages="JavaScript, JSON" />

#### JavaScript

```js
let socket;
async function foo() {
    // Establish web socket connection
    if (!!socket) {
        console.log("Already connected; disconnecting first.");
        await socket.close();
        return;
      }

    socket = new WebSocket("wss://javascript.info/article/websocket/demo/hello");

    socket.onopen = function(e) {
      console.log("Connection established");
      // sending data to server
      socket.send("My name is John");
    };

    socket.onmessage = function(event) {
      alert(`Data received from server: ${event.data}`);
    };

    socket.onclose = function(event) {
      console.log("Connection closed");
      socket = null;
    };

    socket.onerror = function(error) {
      console.error(`Connection error ${error}`);
    };
}
```

#### manifest

```json
{
    "requiredPermissions": {
        "network": {
            "domains": [
                "wss://javascript.info"
            ]
        }
    }
}
```

## Additional notes

- These APIs are available in the global scope. Observe that you didn't have to mount them using `require`.
- The `domains` in the plugin's manifest also let you configure variations of the endpoints. For example, your plugin may like to access 'api.dev.example.com', 'api.stage.example.com' or 'api.prod.example.com' depending upon the environment. You can configure the domains with `["https://api.*.example.com"]` to manage all three.
<!-- While using `http` domains, keep in mind that Photoshop only allows http protocol on Win32 but not on macOS. Premiere Pro has no such restrictions. -->

## Reference material

- [fetch API](../../../uxp-api/reference-js/Global%20Members/Data%20Transfers/fetch.md)
- [XHR API](../../../uxp-api/reference-js/Global%20Members/Data%20Transfers/XMLHttpRequest.md)
- [WebSocket API](../../../uxp-api/reference-js/Global%20Members/Data%20Transfers/WebSocket.md)
