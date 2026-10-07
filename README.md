# Book project

(One-paragraph description: what this book is about, and who it is for. Replace this line.)

> This project was created from `book-template.zip`, a template shared by Dr. Shiguo Jiang, Department of Geography, Planning, and Sustainability, University at Albany, SUNY — distributed to his students on 2026-09-01 through a shared OneDrive folder, for academic projects, and free to use and modify for your own purposes. The template is © 2026 Shiguo Jiang, released under the MIT License (see `LICENSE`), and provided "as is," without warranty of any kind: Dr. Jiang is not responsible or liable for any loss of data or other damage arising from its use. Back up your work, and verify anything produced with it before relying on it. The book you write from this template is your own work and carries no obligation from the license — it only covers the template itself.

## Getting started

1. Download `book-template.zip` from the shared OneDrive folder and unzip it. It unzips to a folder named `book` — move that folder to wherever you keep your work and rename it for your project (`smith-thesis`, `crime-hotspots`, and so on). Work in your renamed copy, never in the zip: keep the original `book-template.zip` where it is, so you can always start a second project from a clean one.
2. In `_quarto.yml`, set the book `title:` and `author:`.
3. In `CLAUDE.md`, replace the title and fill in "What this project is".
4. **Build the Python environment**: open the folder in VS Code, open the terminal, and run `uv sync`. This reads `pyproject.toml` and `uv.lock` and creates a `.venv/` folder with the exact packages the project needs — Jupyter, pandas, matplotlib — so that code chunks in your chapters will run. You only do this once per machine. Check it with `uv run quarto check jupyter`: the `Path:` line it prints should end in your own project's `.venv`.
5. Add chapters as files at the project root, named for their subject (`02-data.qmd`, `03-methods.qmd`, …), and list each one under `chapters:` in `_quarto.yml`.
6. Render with `quarto render`; preview while writing with `quarto preview`. The rendered book lands in `_book/`, and a zip of the whole project — everything needed to reproduce it, the rendered book, and your working record — is rebuilt automatically as `_share/<project>_source.zip` after every render (see `tools/make-zips.py`). Look inside that zip before sending it to anyone: it carries your prompt history and working notes, not only the finished book. If something in there shouldn't go out, move it to `_to_delete/` (already excluded from the zip) or delete it outright, then re-render.
7. If `quarto render` fails, paste the error message into an AI session and ask it to fix the problem — the error text is usually enough for the assistant to find the cause and correct it.

A few files stay current on their own whenever you work with an AI assistant: this file's companion `CLAUDE.md` (its Layout section and `Last updated:` line), `todo.md`, `log.md`, `transcripts/` (automatically for Claude Code; for other tools, ask the assistant directly — see `CLAUDE.md`'s Conversation records section), and `_prompt/`. You don't need to update them by hand — but that only happens while a session is actually doing the editing, so a change you make yourself with no AI session running won't be reflected until a session next works in the project.

## Layout

See `CLAUDE.md`'s Layout section for the current file layout. It's kept up to date there automatically as the project changes, so this file doesn't duplicate it — and a copy here would only go stale the first time the two disagreed.
