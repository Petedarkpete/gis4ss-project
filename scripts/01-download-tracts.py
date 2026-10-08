"""Download the 2024 TIGER/Line census tracts for New York and keep Albany County.

Source:  US Census Bureau, TIGER/Line Shapefiles 2024, census tracts
         https://www2.census.gov/geo/tiger/TIGER2024/TRACT/
License: US government work, not under copyright in the United States
"""

from datetime import date
from pathlib import Path

import geopandas as gpd
import requests

URL = "https://www2.census.gov/geo/tiger/TIGER2024/TRACT/tl_2024_36_tract.zip"
RAW = Path("data/raw/tl_2024_36_tract.zip")
OUT = Path("data/albany-tracts.gpkg")

# Download the file and save it unchanged in data/raw/.
RAW.parent.mkdir(parents=True, exist_ok=True)
response = requests.get(URL, timeout=300)
response.raise_for_status()
RAW.write_bytes(response.content)
print(f"Downloaded {URL} on {date.today()}")

# Keep Albany County: state FIPS 36 is New York, county FIPS 001 is Albany.
tracts = gpd.read_file(RAW)
albany = tracts[tracts["COUNTYFP"] == "001"]
albany.to_file(OUT)

print(f"{len(tracts)} tracts in New York, {len(albany)} in Albany County")
print(f"Coordinate reference system: {albany.crs}")
print(f"Wrote {OUT}")
