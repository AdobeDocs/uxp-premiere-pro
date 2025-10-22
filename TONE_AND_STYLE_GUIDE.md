# UXP Premiere Pro Documentation: Tone and Style Guide

This guide defines the writing standards for all UXP Premiere Pro documentation to ensure consistency, clarity, and accessibility across the entire documentation set.

## Voice and Tone

### Overall Voice

- **Professional yet approachable**: Strike a balance between technical accuracy and accessibility
- **Encouraging and supportive**: Use positive language that builds confidence ("Congratulations!", "You're now ready to...")
- **Conversational but precise**: Write as if explaining to a colleague, but maintain technical precision
- **Action-oriented**: Focus on what users can accomplish

### Person and Perspective

- **Use second person** ("you", "your") to directly address the reader
- **Use active voice** whenever possible
- **Use first-person plural** ("we") sparingly, only when referring to Adobe or the documentation team providing guidance

### Examples

✅ **Good**: "You can distribute your plugin through multiple channels."
❌ **Avoid**: "The plugin can be distributed through multiple channels." (passive)

✅ **Good**: "Let's understand how permissions work."
❌ **Avoid**: "Permissions will be explained in this section."

## Document Structure

### Frontmatter

Every markdown file must include YAML frontmatter with:

```yaml
---
title: Page Title (clear, action-oriented when appropriate)
description: Brief description of content
keywords:
  - Keyword 1
  - Keyword 2
contributors:
  - https://github.com/username
  - https://github.com/undavide
---
```

### Heading Hierarchy

- **H1 (`#`)**: Page title only (matches frontmatter `title`)
- **H2 (`##`)**: Major sections (Overview, Concepts, Examples, etc.)
- **H3 (`###`)**: Sub-sections
- **H4 (`####`)**: Specific properties, methods, or details
- **H5 (`#####`)**: Property details (in reference documentation)

### Standard Sections

Include these sections in this order when applicable:

1. **Overview** or introductory paragraph
2. **Prerequisites** or **System Requirements** (if needed)
3. **Concepts** (explain the "why" before the "how")
4. **Example** or **Usage** (practical implementation)
5. **Reference material** (links to related docs)
6. **Additional Notes** or **Troubleshooting** (if needed)

## Content Patterns

### Introducing Concepts

- Define concepts **before** showing code examples
- Use progressive disclosure: simple to complex
- Explain the "why" and "when" before the "how"
- Use analogies or metaphors when helpful ("think of it as...")

### Code Examples

#### Format and Structure

- **Always use proper syntax highlighting** with language specification:

  ````json
  ```json
  { "key": "value" }
  ``` (backticks)
  ````

- **Use comments liberally** in code examples:

  ```javascript
  // Good: explain what this does
  const result = await someFunction();
  ```

- **Use emojis** in code examples:

  ```javascript
  // ⚠️ Warning: this is a warning
  const result = await someFunction(
    "string parameter", // 👈
  );
  ```

- **Include error handling** with try-catch blocks:
  ```javascript
  async function foo() {
      try {
          // Your code here
      } catch (e) {
          console.error(e);
      }
  }
  ```

#### Multi-file Examples

When showing manifest alongside code, use the `<CodeBlock>` component:

````markdown
<CodeBlock slots="heading, code" repeat="2" languages="JavaScript, JSON" />

#### index.js

```js
// JavaScript code here
```

#### manifest.json

```json
{
  "requiredPermissions": {}
}
```

````

#### Code Style Guidelines

- Use `async/await` syntax (not `.then()` callbacks)
- Use `const` and `let` (not `var`)
- Use template literals for string interpolation: `` `File path: ${path}` ``
- Include filesystem path placeholders with comments: `// update the path based on your system`
- Use descriptive function names: `foo()`, `bar()` are acceptable for simple examples

### Alerts and Callouts

Use `<InlineAlert>` component for important information:

```markdown
<InlineAlert variant="info" slots="header, text1, text2"/>

Header Text

First paragraph of information.

Second paragraph if needed.
```

**Variants:**

- `variant="info"`: General information, tips, clarifications
- `variant="warning"`: Cautions, limitations, known issues
- `variant="error"`: Errors, exceptions, failures

### Tables

Use markdown tables for structured data:

- Include headers with clear column names
- Align columns appropriately (`:---` for left, `:---:` for center, `---:` for right)
- Use **bold** for field names or emphasis

Example:

```markdown
| Required Properties | Optional Properties |
| :------------------ | :------------------ |
| [`width`](#width)   | [`scale`](#scale)   |
```

### Links and Cross-References

- **Use descriptive link text**: "read about [manifest permissions](../path/to/file.md)"
- **Not**: "click [here](../path/to/file.md)"
- **Internal links**: Use relative paths: `../../../plugins/concepts/manifest/index.md`
- **External links**: Include full URL for official documentation
- **Anchor links**: Use for same-page references: `[HostDefinition](#hostdefinition)`

### Lists

- Use **numbered lists** for sequential steps or ordered items
- Use **bulleted lists** for features, options, or unordered items
- Use **definition lists** (bold term followed by explanation) for key concepts
- Keep list items parallel in structure

Examples:

```markdown
1. **First step**: Do this thing first.
2. **Second step**: Then do this thing.

Features include:
- **Automation** of repetitive tasks
- **Customization** to fit your workflow
- **Integration** with existing tools
```

## Technical Writing Best Practices

### Terminology

#### Consistency

- **Plugin** (not plug-in or extension)
- **UXP** (Unified Extensibility Platform)
- **Manifest** (the manifest.json file)
- **Entrypoint** (not entry point)
- **Panel** and **Command** (capitalized when referring to the UI elements)
- **Creative Cloud Desktop application** (full name on first use, then "Creative Cloud Desktop")
- **Premiere Pro** (not PPro, not Pr)

#### Code Elements

- Use backticks for inline code: `manifest.json`, `localFileSystem`, `async/await`
- Use backticks for file paths: `plugin:/sample.png`
- Use backticks for property names: `requiredPermissions`
- Use backticks for keyboard shortcuts: `Cmd+Shift+P`

#### Menu items

- Use bold for menu items: **File** > **Save**

#### Highlight important information

Highlight important information in longer paragraphs with **bold** text and the very occasional _italic_ text.

The Temporary folder is _transitory_ and may be cleared automatically; the Data folder is _persistent_ across app upgrades, but will be removed on uninstall or if the user clears it. Always **provide users with options to back up critical data** to locations of their choice.

While the sandbox is sufficient for many use cases, you may need to access other locations—such as the user's Documents folder or a specific project directory. UXP supports this through a **permission-based system**.

### Permissions and Security

When discussing permissions:

1. **Explain the security model** and why permissions exist
2. **List available options** with clear definitions
3. **Provide best practices** (choose least-permissive option)
4. **Warn about user consent** and installation friction
5. **Show manifest and code together**

Example pattern:

```markdown
*Protip*: Make sure you pick the most accurate permission for your use case because in the future we may ask users to provide their consent based on it. You may find 'fullAccess' to be the least restrictive and hence the safest to pick, but a user may not be comfortable giving full access to their system unless it's absolutely necessary and might deny the installation of your plugin.
```

### Version Requirements

Always specify version requirements clearly. Stick to those versions:

```markdown
## System requirements

Please make make sure your development environment uses the following **minimum versions** to avoid compatibility issues:

- **Premiere Pro v25.6**
- **UDT v2.2**
- **Manifest v5**
```

### Platform-Specific Instructions

When providing platform-specific guidance:

- Use clear headings: "### On macOS" and "### On Windows"
- Show both platforms when commands differ
- Use appropriate path separators: `/` for macOS, `\` for Windows (but note both work in most contexts)

## Writing Style

### Sentence Structure

- **Keep sentences concise**: Aim for 15-25 words per sentence
- **One idea per sentence**: Break complex ideas into multiple sentences
- **Use transition words**: "However", "Additionally", "For example", "In contrast"
- **Vary sentence length**: Mix short and medium sentences for readability

### Word Choice

- **Use simple words** when possible: "use" not "utilize", "help" not "facilitate"
- **Be specific**: "click the Save button" not "proceed with saving"
- **Avoid jargon** or explain it on first use
- **Use contractions sparingly**: "don't" is okay, but prefer full forms in formal contexts

### Tense

- **Use present tense** for current actions: "The plugin displays..."
- **Use future tense** for results: "This will create a new file"
- **Use past tense** for completed examples: "In the example above, we created..."

### Punctuation

- **Use Oxford commas** to separate items in a list: "apple, banana, and cherry", "apple, banana, or cherry" when the list is three or more items.
- **Use periods** to end sentences and bullet points alike.

### Avoid

- ❌ Excessive exclamation marks (one per major section maximum)
- ❌ Marketing language or hype
- ❌ Vague statements: "very powerful", "simply", "just"
- ❌ Assumptions about user knowledge (provide links instead)
- ❌ Gender-specific pronouns (use "they" or rephrase)

## Code Comments and Examples

### Inline Comments

```javascript
// Good: Explains the why
const token = await fsProvider.createPersistentToken(entry); // store for future use

// Avoid: Explains the obvious
const x = 5; // set x to 5
```

Try to keep the line length in code samples to a maximum of ~80-90 characters.

### Full Code Examples

- **Should be complete and runnable** (as much as possible)
- **Include all necessary requires/imports**
- **Show error handling**
- **Demonstrate best practices**
- **Include explanatory comments for complex logic**
- **Use meaningful names for functions and variables**

Example pattern:

```javascript
const { localFileSystem, types } = require('uxp').storage;

async function createFolder() {
    // Create new folder in the plugin's temp directory
    try {
        const newFolder = await localFileSystem.createEntryWithUrl(
            "plugin-temp:/temp",
            { type: types.folder }
        );
        console.log(`Created folder: ${newFolder.nativePath}`);
    } catch (e) {
        console.error("Failed to create folder:", e);
    }
}
```

## Reference Documentation

### Property Documentation Format

```markdown
##### `propertyName`

| Name           | Type     | Required | Default     |
| :------------- | :------- | :------- | ----------- |
| `propertyName` | `string` | required | `undefined` |

Brief description of what this property does and when to use it.

Optional longer explanation or examples if needed.
```

### Type Definitions

- Link to type definitions: `[LocalizedString](#localizedstring)`
- Use inline code for types: `string`, `number`, `boolean`
- Use union types: `"plugin"` or `"request"` or `"fullAccess"`

## Specific UI Components

### Buttons and UI Elements

- **Bold** UI element names: **Create Plugin**, **Load & Watch**, **Window** > **UXP Plugins**
- Use > for menu paths: **File** > **Save**
- Quote button labels when inline: click the "Save" button

### File Paths and Schema

- Show schema usage clearly: `plugin:/`, `plugin-data:/`, `plugin-temp:/`, `file:/`
- Include example paths with system placeholders:
  ```html
  <img src="file:/Users/user/Downloads/sample.png" /> <!-- update the path based on your system -->
  ```

## Testing Your Documentation

Before submitting, verify:

- [ ] All code examples are syntactically correct
- [ ] All internal links work and point to correct sections
- [ ] Screenshots are up-to-date and clearly show the described feature
- [ ] Version numbers are current and accurate
- [ ] Terminology is consistent throughout
- [ ] Content flows logically from simple to complex
- [ ] All required frontmatter fields are present
- [ ] InlineAlerts are used appropriately (not overused)

## Examples of Good Documentation Patterns

### Opening Paragraph Pattern

```markdown
# Page Title

Brief, engaging introduction that explains what this page covers and why it matters.

## Overview

More detailed explanation of the topic, its place in the larger system, and what users will accomplish.
```

### Tutorial Pattern

```markdown
# Tutorial Title

This tutorial will walk you through [specific task]. You will learn to [outcome 1], [outcome 2], and [outcome 3].

## Prerequisites

Before you start, make sure you have:
- Requirement 1
- Requirement 2

## Step-by-step Instructions

### 1. First Step

Explanation and code.

#### 1.1 First Sub-step

Explanation and code. When using sub-steps, avoid the dot at the end of the number, for example: "1.1" and "1.1.1" instead of "1.1." and "1.1.1."

### 2. Second Step

Explanation and code.

## Next steps

[Link to related tutorial] or [Link to reference material]
```

### Concept Explanation Pattern

```markdown
## Concept Name

Brief definition.

More detailed explanation with examples and use cases.

### When to Use

Specific guidance on when this concept applies.

### Example

Practical code example demonstrating the concept.
```

---

## Revision History

- **Version 1.0**: Initial style guide creation based on analysis of existing UXP Premiere Pro documentation
