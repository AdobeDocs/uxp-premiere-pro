---
title: Drag and Drop Media into Premiere Pro
description: Drag and drop media into the Premiere Pro Project panel or Timeline.
keywords:
  - drag and drop
  - payload
  - multiple items
  - local files
contributors:
  - https://github.com/Mberikerajan
---

# Drag and Drop Media into Premiere Pro

UXP plugins can use web-based drag-and-drop capabilities to add local media files directly to the Premiere Pro **Project panel** or **Timeline**.

## What you can do

- Drag one or more local media files from a UXP panel into Premiere Pro. Third-party panels support local files only.
- Drop the files onto the **Project panel**—in Icon, List, or Freeform view, including onto a bin—or onto an open sequence in the **Timeline**.
- Use common video, audio, and image formats (see [Accepted content types](#accepted-content-types)).

## Requirements

| Requirement | Value |
| :--- | :--- |
| Premiere Pro | 27.0.0 or later |
| UXP manifest | `manifestVersion` 5 or later, with a panel entrypoint |
| Permission | `"requiredPermissions": { "localFileSystem": "request" }` to allow users to select local files |

## How it works

1. Mark an element in your panel as draggable.
2. On `dragstart`, serialize information about the selected files as a JSON payload.
3. Add the payload to the drag's `dataTransfer` as `text/plain`.
4. When the user drops the files onto a supported target, Premiere Pro reads the payload and imports the referenced local files.

There is no custom UXP drag API or drag-and-drop manifest entry. The implementation uses standard HTML drag-and-drop with a JSON payload recognized by Premiere Pro.

## Add drag and drop to your panel

The following example lets the user select one or more local files and then drag them from the panel into Premiere Pro.

Add elements for selecting and dragging the files:

```html
<button id="select-files">Select files</button>
<div id="file-item" draggable="false">No files selected</div>
```

Declare the filesystem permission in `manifest.json`:

```json
{
  "manifestVersion": 5,
  "requiredPermissions": {
    "localFileSystem": "request"
  }
}
```

Add the file-selection and drag-start logic:

```js
const fs = require('uxp').storage.localFileSystem;

const selectButton = document.querySelector('#select-files');
const fileItem = document.querySelector('#file-item');

const MIME_BY_EXT = {
  '.mp4': 'video/mp4',
  // Add mappings for the other content types your plugin supports.
};

let selectedFiles = [];

selectButton.addEventListener('click', async () => {
  const picked = await fs.getFileForOpening({ allowMultiple: true });

  selectedFiles = (
    Array.isArray(picked) ? picked : picked ? [picked] : []
  );

  if (selectedFiles.length === 0) {
    fileItem.textContent = 'No files selected';
    fileItem.setAttribute('draggable', 'false');
    return;
  }

  fileItem.textContent =
    selectedFiles.length === 1
      ? selectedFiles[0].name
      : `${selectedFiles.length} files selected`;

  fileItem.setAttribute('draggable', 'true');
});

fileItem.addEventListener('dragstart', (event) => {
  const items = selectedFiles.map((file) => {
    const dotIndex = file.name.lastIndexOf('.');
    const extension =
      dotIndex >= 0 ? path.extname(file.name).slice(1).toLowerCase() : '';
    const contentType = MIME_BY_EXT[extension];

    if (!contentType) {
      throw new Error(`Unsupported file type: ${file.name}`);
    }

    let path = file.nativePath;

    if (/^[A-Za-z]:\\/.test(path)) {
      path = `/${path.replace(/\\/g, '/')}`;
    }

    return {
      name: file.name,
      content_type: contentType,
      uri: `file://${encodeURI(path)}`,
    };
  });

  const payload = JSON.stringify({
    version: '1.0.0',
    items,
  });

  event.dataTransfer.setData('text/plain', payload);
  event.dataTransfer.effectAllowed = 'copyMove';
  event.dataTransfer.dropEffect = 'copy';
});
```

Add mappings to `MIME_BY_EXT` for any additional content types your plugin supports.

## Payload reference

The payload is a JSON object serialized to a string.

### Top-level object

| Field | Type | Required | Notes |
| :--- | :--- | :--- | :--- |
| `version` | string | Yes | Must be exactly `"1.0.0"`. Any other value rejects the entire drag. |
| `items` | array | Yes | Contains one or more item objects. |

### Item object

| Field | Type | Required | Notes |
| :--- | :--- | :--- | :--- |
| `name` | string | Yes | File name used as the imported clip's name. |
| `display_name` | string | No | Overrides the name displayed for the imported item in Premiere Pro. |
| `content_type` | string | Yes | MIME type. The item is skipped if the value is not supported. |
| `uri` | string | Yes | `file://` URI for a local file. See [URI rules](#uri-rules). |

### Example payload

```json
{
  "version": "1.0.0",
  "items": [
    {
      "name": "clip.mov",
      "display_name": "My Clip",
      "content_type": "video/quicktime",
      "uri": "file:///Users/example/Videos/clip.mov"
    }
  ]
}
```

## URI rules

- Third-party panels may reference local files only. Always use the `file://` scheme.
- Percent-encode the path with `encodeURI()` so that spaces and Unicode characters produce a valid URI.
- On Windows, convert a path such as `C:\path\clip.mov` to `file:///C:/path/clip.mov`.

## Accepted content types

- **Video:** `video/mp4`, `video/quicktime`, `video/x-quicktime`, `video/x-ms-wmv`, `video/x-ms-asf`, `video/mpeg`
- **Audio:** `audio/wav`, `audio/x-wav`, `audio/vnd.wav`, `audio/wave`, `audio/mpeg`, `audio/x-mpeg`, `audio/mp3`, `audio/mpeg3`, `audio/x-mpeg-3`, `audio/m4a`, `audio/aac`, `audio/aacp`, `audio/aif`, `audio/x-aiff`
- **Image:** `image/jpeg`, `image/jpg`, `image/png`, `image/gif`, `image/bmp`, `image/tiff`, `image/webp`

## Dragging multiple items

To drag multiple files, add an item object for each file to the `items` array. All items must reference local files.

```json
{
  "version": "1.0.0",
  "items": [
    {
      "name": "a.mov",
      "content_type": "video/quicktime",
      "uri": "file:///Users/example/Videos/a.mov"
    },
    {
      "name": "b.wav",
      "content_type": "audio/wav",
      "uri": "file:///Users/example/Audio/b.wav"
    }
  ]
}
```

A common implementation is to include all selected files when the dragged file is part of the current selection. Otherwise, include only the file being dragged.

## Limitations and troubleshooting

- Third-party panels can drag local files only.
- An item is skipped if its `content_type` is not supported.
- If nothing happens when you drop the files:
  - Confirm that the dragged element has `draggable="true"`.
  - Confirm that the payload is set as `text/plain`.
  - Confirm that the payload uses version `"1.0.0"`.
  - Confirm that each item uses a supported `content_type`.
  - Confirm that each `uri` is a valid, percent-encoded `file://` URI for an existing file.

## References

- [HTML Drag and Drop API](https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API)