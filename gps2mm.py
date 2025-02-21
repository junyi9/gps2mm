import pandas as pd
import numpy as np
from pyproj import Geod
# Create a Geod object for WGS84 ellipsoid
geod = Geod(ellps="WGS84")
mm_locations = pd.read_csv("calc_mm_locations", sep=",")
def gps2mm(lon, lat, mm_locations=mm_locations, geod=geod):
    """
    Function to find the nearest mile marker location to a given GPS coordinate.
    Parameters:
    lon: float, longitude of the GPS coordinate
    lat: float, latitude of the GPS coordinate
    mm_locations: DataFrame, mile marker locations
    geod: Geod object, WGS84 ellipsoid
    Returns:
    milemarker: int, nearest mile marker
    """
    mm_locations["distance"] = mm_locations.apply(lambda x: geod.inv(lon, lat, x["longitude"], x["latitude"])[2], axis=1)
    # find the minimum distance and report the mm location
    min_distance = mm_locations["distance"].min()
    milemarker = mm_locations[mm_locations["distance"] == min_distance].mm.values[0]
    return milemarker