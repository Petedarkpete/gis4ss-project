---
title: "Working Log"
---

::: {.callout-note}

## Provenance

Internal working document. Human author: the project owner (sets direction, makes decisions, bears responsibility for content). AI assistant: review, literature search, editing, drafting, code checking. This file is never rendered into or shipped with the book.

:::

This file logs substantive decisions (what changed, why, and what was deliberately left unchanged) and worked misjudgments worth remembering. Entries are organized newest first, dated absolutely (YYYY-MM-DD). Open items and questions live in `todo.md`, not here.

## 2026-11-01: PR8 modeling decisions

- **Queen contiguity chosen as the primary spatial weights**, k-nearest-neighbors (k=4) as the comparison scheme, per Lecture 21's requirement to report both. Queen suits irregularly-shaped census tracts better than a fixed-distance or fixed-k scheme; KNN is the sensitivity check, not a candidate for the main analysis.
- **Spatial error model chosen over spatial lag**, despite the LM diagnostics being genuinely ambiguous (both plain LM tests significant, neither robust version significant). Decided on the lower robust p-value as the tiebreaker (LM-error p=0.16 vs LM-lag p=0.77) rather than defaulting to lag or picking arbitrarily. This is a judgment call, not a clean result — recorded here so it isn't mistaken for a confident choice later.
- **FDR correction implemented manually** (Benjamini-Hochberg) rather than via `esda.moran.FDR`, which doesn't exist in the installed esda version (2.10.0). Deliberate choice to not chase the right import path across versions when the underlying procedure is a few lines of arithmetic.
- **Deliberately left unchanged for now:** all of PR7's "worth fixing" (not counted) feedback items — the stale sentences in `02-data.qmd`, the documentation table's missing Script column and notes, `01-proposal.qmd`'s outdated Data section numbers, answering Bornwell's presentation question, the `_quarto.yml` appendices fix, and the stray zip cleanup. None of these block PR8's own scoring; they're queued for a dedicated cleanup session rather than done piecemeal under today's deadline pressure.

## 2026-10-08: added a VS Code multi-root workspace

Created a `.code-workspace` file with three folders open together: this project (`book`), the shared class project folder (`OneDrive_3_10-6-2026`), and the course textbook source (`gis4ss-lecture_source`) — the latter two for reference only, not part of this project's own submission.

## 2026-09-01: project created from template

(First log entry — replace the date with the day you actually started.)
