import json
import os
from datetime import date
from pathlib import Path

import pandas as pd
import requests

#fetches from my environment
API_KEY = os.environ["CENSUS_API_KEY"]
BASE_URL = "https://api.census.gov/data/2024/acs/acs5"

DATASETS = {
    "rent": {
        "variable": "B25064_001E",
        "moe": "B25064_001M",
        "raw": Path("data/raw/acs-B25064-rent.json"),
        "out": Path("data/acs-rent.csv"),
    },
    "income": {
        "variable": "B19013_001E",
        "moe": "B19013_001M",
        "raw": Path("data/raw/acs-B19013-income.json"),
        "out": Path("data/acs-income.csv"),
    },
}

for name, spec in DATASETS.items():
    url = (
        f"{BASE_URL}?get=NAME,{spec['variable']},{spec['moe']}"
        f"&for=tract:*&in=state:36+county:001&key={API_KEY}"
    )
    response = requests.get(url, timeout=60)
    response.raise_for_status()

    spec["raw"].parent.mkdir(parents=True, exist_ok=True)
    spec["raw"].write_text(response.text)
    print(f"Downloaded {name} data on {date.today()}")

    rows = response.json()
    df = pd.DataFrame(rows[1:], columns=rows[0])
    df.to_csv(spec["out"], index=False)

    print(f"{name}: {len(df)} tracts, wrote {spec['out']}")
