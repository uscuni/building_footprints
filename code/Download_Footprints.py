from pyrosm import get_data
from pyrosm import OSM

#set local CRS for the city
local_crs=31468

# Download OSM data for city (https://pyrosm.readthedocs.io/en/latest/basics.html#read-buildings)
fp = get_data("Berlin",directory="OSM_data")

# Initialize the OSM parser object
osm = OSM(fp)

buildings = osm.get_buildings()
print('got buildings')
buildings = buildings[buildings.geom_type == "Polygon"].reset_index(drop=True)
buildings = buildings[["geometry"]].to_crs(local_crs)
buildings["uID"] = range(len(buildings))
buildings.to_parquet('buildings.parquet')