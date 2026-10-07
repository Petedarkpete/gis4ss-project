"""Post-render script: convert _book/search.json into _book/search-index.js.

search-fallback.html loads search-index.js as a classic script so that
Quarto's search works when the book is opened via file:// (where fetch()
of search.json is blocked by the browser). Wired up in _quarto.yml via
`project: post-render`.
"""
import json
import pathlib

book = pathlib.Path(__file__).resolve().parents[1] / "_book"
search_json = book / "search.json"

if search_json.exists():
    data = json.loads(search_json.read_text(encoding="utf-8"))
    out = (
        "// Auto-generated from search.json by tools/build-local-search-index.py. Do not edit.\n"
        "window.__quartoSearchIndex = " + json.dumps(data, ensure_ascii=False) + ";\n"
    )
    (book / "search-index.js").write_text(out, encoding="utf-8")
    print(f"build-local-search-index: wrote search-index.js ({len(data)} entries)")
else:
    print("build-local-search-index: _book/search.json not found; skipped")
