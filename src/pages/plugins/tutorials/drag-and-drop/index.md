---
title: Drag and Drop Media into Premiere Pro
description: Drag and Drop media into Premiere Pro project panel or timeline. 
keywords:
  - drag and drop
  - payload
  - multiple items
  - local files drop
contributors:
  - https://github.com/Mberikerajan
---

# Drag and Drop Media into Premiere Pro

Let users drag media from UXP panel and drop it directly into the Premiere Pro **Project panel** or **Timeline**. Premiere Pro imports the files and adds them to the project. You can drag a single item or multiple items at once.

**Scope:** third-party panels can drag **local files only**.

## What you can do

- Drag one or more local media files from uxp panel into Premiere Pro.
- Drop onto the **Project panel** (Icon, List, or Freeform view, including onto a bin) or onto the **Timeline**.
- Support common video, audio, and image formats (see [Accepted content types](#accepted-content-types)).

## Requirements

| Requirement | Value |
| :--- | :--- |
| Premiere Pro | 27.0.0 or later |
| UXP manifest | `manifestVersion` 6, with a panel entrypoint |
| Permission | `"requiredPermissions": { "localFileSystem": "fullAccess" }` — needed to read the OS path of picked files |

## How it works, at a glance

Drag local media from your UXP panel; on dragstart a JSON payload is attached; dropping onto Premiere Pro's Project panel or Timeline imports the files.

1. Mark an element in your panel as draggable.
2. On `dragstart`, attach a small JSON payload describing the items — as plain text on the drag's `dataTransfer`.
3. When the user drops onto a supported target, Premiere Pro reads the payload and imports the referenced local files.

There is no custom UXP drag API and no manifest entry for drag-and-drop — it is standard HTML5 drag-and-drop plus the JSON payload.

## Supported drop targets

- **Project panel** — all three views (Icon, List, Freeform), including dropping onto a bin.
- **Timeline** — drop onto an open sequence.

## Add drag-and-drop to your panel

### 1. Make the element draggable

Set `draggable="true"` on the element the user grabs, and give its children `pointer-events: none` so the drag events fire on the element itself:

```html
<li class="file-item" draggable="true">
  <span style="pointer-events:none;">clip.mov</span>
</li>
```


### 2. Build the payload and set it on `dragstart`

Attach the JSON as text. Set it on both `text/plain`, and set the drag effects:

```js
element.addEventListener('dragstart', (e) => {
  const payload = buildPayload(getSelectedFiles());   // one or many items
  e.dataTransfer.setData('text/plain', payload);
  e.dataTransfer.effectAllowed = 'copyMove';
  e.dataTransfer.dropEffect = 'copy';
});
```

### 3. Minimal, complete example

```js
const fs = require('uxp').storage.localFileSystem;

// Map file extensions to content types Premiere Pro accepts for import.
const MIME_BY_EXT = {
  '.mp4': 'video/mp4', '.mov': 'video/quicktime', '.wmv': 'video/x-ms-wmv', '.mpg': 'video/mpeg',
  '.wav': 'audio/wav',  '.mp3': 'audio/mpeg',      '.aac': 'audio/aac',      '.m4a': 'audio/m4a', '.aif': 'audio/aif',
  '.png': 'image/png',  '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.gif': 'image/gif',
  '.bmp': 'image/bmp',  '.tiff': 'image/tiff', '.webp': 'image/webp',
};

function extname(name) { const i = name.lastIndexOf('.'); return i < 0 ? '' : name.slice(i).toLowerCase(); }
function mimeFor(name) { return MIME_BY_EXT[extname(name)]; }

// Convert a local filesystem path to a file:// URI.
function pathToFileUri(path) {
  let p = path;
  if (/^[A-Za-z]:\\/.test(path)) p = '/' + path.replace(/\\/g, '/'); // Windows: C:\… -> /C:/…
  return 'file://' + encodeURI(p);                                   // percent-encodes spaces & unicode
}

function toDragItem(file) {
  return {
    name: file.name,
    content_type: mimeFor(file.name),
    uri: pathToFileUri(file.nativePath),
  };
}

function buildPayload(files) {
  return JSON.stringify({
    version: '1.0.0',
    items: files.map(toDragItem),
  });
}

// Pick local files with the UXP file picker (requires localFileSystem: "fullAccess").
async function pickFiles() {
  const picked = await fs.getFileForOpening({ allowMultiple: true });
  return (Array.isArray(picked) ? picked : [picked]).filter(Boolean);
}
```

Wire `buildPayload(...)` into the `dragstart` handler from step 2.

## Payload reference

The payload is a JSON object serialized to a string.

### Top-level object

| Field | Type | Required | Notes |
| :--- | :--- | :--- | :--- |
| `version` | string | yes | Must be exactly `"1.0.0"`. Any other value rejects the whole drag. |
| `items` | array | yes | One or more item objects. |

### Item object

| Field | Type | Required | Notes |
| :--- | :--- | :--- | :--- |
| `name` | string | yes | File name; used as the imported clip's name. |
| `display_name` | string | no | Overrides the name shown in Premiere Pro for the imported item. |
| `content_type` | string | yes | MIME type — must be one of the accepted values, otherwise the item is skipped. |
| `uri` | string | yes | `file://` URI to a local file (see [URI rules](#uri-rules)). |

### Example payload

```json
{
  "version": "1.0.0",
  "items": [
    {
      "name": "clip.mov",
      "display_name": "My Clip",
      "content_type": "video/quicktime",
      "uri": "file:///Users/.../clip.mov"
    }
  ]
}
```

## URI rules

- Third-party panels may reference **local files only** — always the `file://` scheme.
- Percent-encode the path (`encodeURI`) so spaces and unicode characters produce a valid URI.
- Windows: convert `C:\path\clip.mov` to `file:///C:/path/clip.mov`.

## Accepted content types

- **Video:** `video/mp4`, `video/quicktime`, `video/x-quicktime`, `video/x-ms-wmv`, `video/x-ms-asf`, `video/mpeg`
- **Audio:** `audio/wav`, `audio/x-wav`, `audio/vnd.wav`, `audio/wave`, `audio/mpeg`, `audio/x-mpeg`, `audio/mp3`, `audio/mpeg3`, `audio/x-mpeg-3`, `audio/m4a`, `audio/aac`, `audio/aacp`, `audio/aif`, `audio/x-aiff`
- **Image:** `image/jpeg`, `image/jpg`, `image/png`, `image/gif`, `image/bmp`, `image/tiff`, `image/webp`

Items with any other `content_type` are silently skipped; the rest of the drag still imports.

## Dragging multiple items

To drag several items, put multiple objects in `items`. All items must be local files. A common pattern: let the user select items in your panel, and on `dragstart` include every selected item (or just the grabbed one if it isn't part of the selection).

```json
{
  "version": "1.0.0",
  "items": [
    { "name": "a.mov", "content_type": "video/quicktime", "uri": "file:///Users/.../a.mov" },
    { "name": "b.wav", "content_type": "audio/wav",       "uri": "file:///Users/.../b.wav" }
  ]
}
```

## Limitations & troubleshooting

- **Local files only.**
- `content_type` must match one of the accepted values, or the item is skipped.
- **Nothing happens on drop?**
  - Confirm the dragged element has `draggable="true"` and its children use `pointer-events: none`.
  - Confirm the payload is set on both `text/plain`.
  - Confirm each `uri` is a valid, percent-encoded `file://` URI pointing at an existing file.
