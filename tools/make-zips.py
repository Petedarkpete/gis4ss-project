r"""Build a distribution zip of this project into `_share/`.

Run it by hand, from the project root or from tools/:

    uv run tools/make-zips.py

It also runs automatically after every `quarto render`, wired into
`_quarto.yml`'s `post-render:` list, so `_share/<project>_source.zip` is
always up to date with your latest render.

Creates `_share/<project>_source.zip`, overwriting whatever was there
before. No old zip is kept — every file in it also still lives in the
project folder, so nothing is lost by overwriting, and keeping old
copies would only grow without bound as you re-render.

The zip contains the whole project except:

  _share/            the zip lives here; including it would nest the archive
  _backup/           pre-edit copies — a backup of the project inside a zip
                     of the project, and it grows every round
  _to_delete/        files staged for deletion, not for reproducing anything
  .venv/ venv/ renv/ .Rproj.user/    environments (reconstructible)
  .quarto/ _freeze/ .jupyter_cache/  Quarto build state
  __pycache__/ etc.                  language and tool caches
  .git/              version history, if you have put this project under git

Everything else goes in: the chapters and appendices, `_quarto.yml` and
the appearance files, `references.bib`, `data/`, `pic/`, `ref/`,
`notes/` — everything needed to reproduce the book — plus the
rendered book itself (`_book/`), the working record (`CLAUDE.md`,
`todo.md`, `log.md`, `prompt.md`, `_prompt/`), and any saved AI
conversation exports (`transcripts/`).

Because this is a deny list rather than a hand-picked list, a folder
you add later (a `code/` folder, a new subfolder under `ref/`) is
carried automatically instead of silently missed. If you add something
that should NOT be shared — draft material, a large raw-data folder —
add its name to EXCLUDE_DIRS below.

Before sending `_share/<project>_source.zip` to anyone, read what is
actually in it — it carries your prompt history and working notes, not
only the finished book.
"""

import sys
import zipfile
from pathlib import Path

# ---------------------------------------------------------------- project root
here = Path.cwd()
root = here.parent if here.name == "tools" else here
if not (root / "_quarto.yml").exists():
    sys.exit(f"ERROR: _quarto.yml not found in {root} - run from the project root (or tools/).")

name = root.name.lower()

dist = root / "_share"
dist.mkdir(exist_ok=True)

# ---------------------------------------------------------------- what to skip
EXCLUDE_DIRS = {
    "_share",
    "_backup",
    "_to_delete",
    ".venv", "venv", "renv", ".Rproj.user",
    ".quarto", "_freeze", ".jupyter_cache",
    "__pycache__", ".ipynb_checkpoints", ".mypy_cache",
    ".pytest_cache", ".ruff_cache", ".tox", "node_modules",
    ".git",
}


def skipped(rel: Path) -> bool:
    return any(part in EXCLUDE_DIRS for part in rel.parts[:-1])


files = sorted(f for f in root.rglob("*")
               if f.is_file() and not skipped(f.relative_to(root)))

zip_path = dist / f"{name}_source.zip"
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
    for f in files:
        zf.write(f, f.relative_to(root))

size = zip_path.stat().st_size / 1e6
print(f"wrote {zip_path.relative_to(root)}  ({len(files)} files, {size:.1f} MB)")
