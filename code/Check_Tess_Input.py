import momepy
import geopandas as gpd

buildings=gpd.read_parquet('buildings.parquet')

check=momepy.CheckTessellationInput(buildings)

check.collapse.to_parquet('collapse.parquet')
check.split.to_parquet('split.parquet')
check.overlap.to_parquet('overlap.parquet')