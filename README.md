# Building Footprints

Pre-processing of building footprints data

## Contents

### Code

* Downlaod_Footprints.py - Download building footprints data for a given city
* Check_Tess_Input.py - Run momepy.CheckTessellationInput and save data as parquets
* Explore_Issues.ipynb - Explore buildings on map
* Buildings_Berlin.ipynb - Explore Berlin Building Footprint data from OSM
* Fix_Overlaps.ipynb - Preliminary exploration of fixing overlapping buildings


### Environment

```
conda env create -f environment.yml
conda activate py312_uscuni_buildingfootprints
```

### Data

* OSM_Data - Geofabrik OpenStreetMap data (too large for Github)
* buildings.parquet - Building footprint data for Berlin (too large for Github)
* collapse, split, and overlap.parquet - Output of momepy.CheckTessellationInput for Berlin building footprints (footprints which may be prone to errors)
