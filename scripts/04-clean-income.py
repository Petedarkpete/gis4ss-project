"""Clean the Albany County median household income data.

Reads the prepared file from scripts/02-download-acs.py and treats the Census
Bureau's "not computed" codes as missing data instead of real numbers.
"""

from pathlib import Path

import pandas as pd

IN = Path("data/acs-income.csv")
OUT = Path("data/acs-income-clean.csv")
LOG = Path("data/acs-income-cleaning-log.txt")

log_lines = []

def log(line):
    print(line)
    log_lines.append(line)

income = pd.read_csv(IN, dtype={"state": str, "county": str, "tract": str})
log(f"Step 1: loaded {IN}, {len(income)} rows")

assert income["tract"].is_unique, "Expected one row per tract"
log("Step 2: confirmed one row per tract")

not_computed = income["B19013_001E"] == -666666666
income.loc[not_computed, "B19013_001E"] = pd.NA
income.loc[not_computed, "B19013_001M"] = pd.NA
log(f"Step 3: set {not_computed.sum()} tract(s) with code -666666666 to missing: "
    f"{income.loc[not_computed, 'tract'].tolist()}")

income.to_csv(OUT, index=False)
log(f"Step 4: wrote {len(income)} rows to {OUT}")

LOG.write_text("\n".join(log_lines) + "\n")
