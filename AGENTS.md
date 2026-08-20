# AGENTS.md — Cartea Rust

Romanian translation of the Rust Book, maintained and reviewed in this repository.

## Project identity
- Canonical path: `D:/GitHub/cartea-rust`
- Source reference: `rust-lang/book`
- Romanian sources under active maintenance: `rust-lang-ro/book` and `GeorgianBadita/rust-book-ro`

## Language and scope
- Source language: English
- Target language: Romanian
- Do not translate upstream code examples unless explicitly requested.
- Preserve existing terminology and Romanian glossary choices across files.

## Translation rules
- Treat `SUMMARY.md`, book TOML configs, and existing issue templates as project interfaces.
- Changes to glossary-sensitive terms should be tracked in documentation before edits.
- Keep Markdown anchors, code fences, frontmatter, and build metadata intact.

## Quality gates
- Run repository validation/CI scripts before declaring a section complete.
- Spellcheck/dictionary files in `ci/` are part of the expected maintenance surface.

## BMAD and tooling notes
- This repo may host localized project context only.
- If a broader product brief, PRD, architecture, or implementation plan is needed, keep it in the dedicated project workspace at `D:/GitHub/transl`.