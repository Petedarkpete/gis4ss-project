"""Build the analysis file: cleaned rent, cleaned income, and tract boundaries,
joined into one file in the project coordinate reference system.
"""

from pathlib import Path

import geopandas as gpd
import pandas as pd

RENT = Path("data/acs-rent-clean.csv")
INCOME = Path("data/acs-income-clean.csv")
TRACTS = Path("data/albany-tracts.gpkg")
OUT = Path("data/albany-analysis.gpkg")

rent = pd.read_csv(RENT, dtype={"tract": str}).rename(
    columns={"B25064_001E": "median_rent", "B25064_001M": "median_rent_moe"}
)
income = pd.read_csv(INCOME, dtype={"tract": str}).rename(
    columns={"B19013_001E": "median_income", "B19013_001M": "median_income_moe"}
)
tracts = gpd.read_file(TRACTS)

print(f"Loaded: {len(rent)} rent rows, {len(income)} income rows, {len(tracts)} tracts")

data = rent[["tract", "median_rent", "median_rent_moe"]].merge(
    income[["tract", "median_income", "median_income_moe"]], on="tract", how="inner"
)
assert len(data) == 85, f"Expected 85 rows after merge, got {len(data)}"
print(f"Merged rent + income: {len(data)} rows, no unmatched rows on either side")

gdf = tracts.merge(data, left_on="TRACTCE", right_on="tract", how="inner")
assert len(gdf) == 85, f"Expected 85 rows after joining tracts, got {len(gdf)}"
gdf = gdf.to_crs("EPSG:26918")
print(f"Joined to tracts and reprojected to {gdf.crs}: {len(gdf)} rows")

gdf.to_file(OUT)
print(f"Wrote {OUT}")
