"""Clean the Albany County median gross rent data.

Reads the prepared file from scripts/02-download-acs.py and treats the Census
Bureau's "not computed" codes as missing data instead of real numbers.
"""

from pathlib import Path

import pandas as pd

IN = Path("data/acs-rent.csv")
OUT = Path("data/acs-rent-clean.csv")
LOG = Path("data/acs-rent-cleaning-log.txt")

log_lines = []

def log(line):
    print(line)
    log_lines.append(line)

rent = pd.read_csv(IN, dtype={"state": str, "county": str, "tract": str})
log(f"Step 1: loaded {IN}, {len(rent)} rows")

assert rent["tract"].is_unique, "Expected one row per tract"
log("Step 2: confirmed one row per tract")

not_computed = rent["B25064_001E"] == -666666666
rent.loc[not_computed, "B25064_001E"] = pd.NA
rent.loc[not_computed, "B25064_001M"] = pd.NA
log(f"Step 3: set {not_computed.sum()} tract(s) with code -666666666 to missing: "
    f"{rent.loc[not_computed, 'tract'].tolist()}")

rent.to_csv(OUT, index=False)
log(f"Step 4: wrote {len(rent)} rows to {OUT}")

LOG.write_text("\n".join(log_lines) + "\n")
