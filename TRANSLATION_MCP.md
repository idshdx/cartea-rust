# DeepL Translation Integration via MCP

The project is configured to use the DeepL MCP server for translation.

## Prerequisites

- Node.js installed
- `npx` available in your path
- DeepL API key configured in `.ai/mcp/mcp.json`

## Configuration

The DeepL MCP server is configured in `.ai/mcp/mcp.json`.

## Usage

You can run the DeepL MCP server using `npx`:

```bash
npx deepl-mcp-server
```

### Batch Translation

To translate all Markdown files in the `src/` directory, you can use the `tools/batch_translate.py` script:

```bash
python tools/batch_translate.py
```

This script will recursively look for `.md` files in `src/` and translate them into corresponding `.ro.md` files, skipping those that have already been translated.

### Review and Refinement Process

After translation, perform a manual review to identify terminology issues, awkward phrasing, and formatting errors.
- Document findings in `REVIEW_NOTES.md`.
- Refine the content by fixing encoding issues (ensure UTF-8) and improving linguistic quality.

*(Note: The current `tools/translate.py` uses the DeepL API directly as a fallback/primary method. Future updates will move the translation logic to use the MCP server tools directly.)*
