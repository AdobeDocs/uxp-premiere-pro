---
id: "sequenceeditor"
title: "SequenceEditor"
sidebar_label: "SequenceEditor"
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
    - Premiere Pro
---

# SequenceEditor

Used to add projectItems as trackItems to sequences, or remove trackItems from sequences.

## Static Methods

### getEditor

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_SequenceEditor_

Get Sequence Editor reference for editing the sequence timeline

#### Parameters

| Name           | Type  | Description |
| :------------- | :---- | :---------- |
| sequenceObject | _any_ | -           |

---

## Instance Methods

### createCloneTrackItemAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Create insert or overwrite to timeline with clone of input trackItem action. Input should be offset value in comparison to original input trackItem's time and track indexes

#### Parameters

| Name                     | Type                                        | Description |
| :----------------------- | :------------------------------------------ | :---------- |
| trackItem                | _any_                                       | -           |
| timeOffset               | _any_                                       | -           |
| videoTrackVerticalOffset | [_Number_](/ppro_reference/classes/number/) | -           |
| audioTrackVerticalOffset | [_Number_](/ppro_reference/classes/number/) | -           |
| alignToVideo             | _boolean_                                   | -           |
| isInsert                 | _boolean_                                   | -           |

---

### createInsertProjectItemAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Create insert ProjectItem into Sequence Action

#### Parameters

| Name            | Type                                                  | Description |
| :-------------- | :---------------------------------------------------- | :---------- |
| projectItem     | [_ProjectItem_](/ppro_reference/classes/projectitem/) | -           |
| time            | [_TickTime_](/ppro_reference/classes/ticktime/)       | -           |
| videoTrackIndex | [_Number_](/ppro_reference/classes/number/)           | -           |
| audioTrackIndex | [_Number_](/ppro_reference/classes/number/)           | -           |
| limitShift      | [_Boolean_](/ppro_reference/classes/boolean/)         | -           |

---

### createOverwriteItemAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_Action_

Create overwrite Sequence with ProjectItem Action

#### Parameters

| Name            | Type                                                  | Description |
| :-------------- | :---------------------------------------------------- | :---------- |
| projectItem     | [_ProjectItem_](/ppro_reference/classes/projectitem/) | -           |
| time            | [_TickTime_](/ppro_reference/classes/ticktime/)       | -           |
| videoTrackIndex | [_Number_](/ppro_reference/classes/number/)           | -           |
| audioTrackIndex | [_Number_](/ppro_reference/classes/number/)           | -           |

---

### createRemoveItemsAction

<span class="minversion" style="display: block; margin-bottom: -1em; margin-left: 36em; float:left; opacity:0.5;">25.0</span>

_action_

Create remove action for sequence

#### Parameters

| Name               | Type      | Description |
| :----------------- | :-------- | :---------- |
| trackItemSelection | _object_  | -           |
| ripple             | _boolean_ | -           |
| mediaType          | _object_  | -           |
| shiftOverLapping   | _boolean_ | -           |

---
