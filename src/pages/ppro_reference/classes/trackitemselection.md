---
id: "trackitemselection"
title: "TrackItemSelection"
sidebar_label: "TrackItemSelection"
repo: "uxp-premierepro"
product: "premierepro"
keywords:
  - Creative Cloud
  - API Documentation
  - UXP
  - Plugins
  - JavaScript
  - ExtendScript
  - SDK
  - C++
  - Scripting
  - Premiere
---

# TrackItemSelection

## Static Methods

### createEmptySelection

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Create empty selection

#### Parameters

| Name      | Type                                      | Description |
| :-------- | :---------------------------------------- | :---------- |
| undefined | _(selection: TrackItemSelection) => void_ | -           |

---

## Instance Methods

### addItem

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Add a track item to this selection

#### Parameters

| Name               | Type                                                                                                                                       | Description                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------- |
| trackItem          | [_VideoClipTrackItem_](/ppro_reference/classes/videocliptrackitem/) or [_AudioClipTrackItem_](/ppro_reference/classes/audiocliptrackitem/) | trackItem to be added to selection |
| skipDuplicateCheck | _boolean_                                                                                                                                  | -                                  |

---

### getTrackItems

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_(VideoClipTrackItem | AudioClipTrackItem)[]_

return list of trackItems inside of trackItemSelection

---

### removeItem

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_boolean_

Remove a track item from this selection

#### Parameters

| Name      | Type                                                                                                                                       | Description                            |
| :-------- | :----------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------- |
| trackItem | [_VideoClipTrackItem_](/ppro_reference/classes/videocliptrackitem/) or [_AudioClipTrackItem_](/ppro_reference/classes/audiocliptrackitem/) | trackItem to be removed from selection |

---
