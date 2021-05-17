import math
import pandas as pd


class GEO_Map:
    """
    It holds the map for zip code and its latitute and longitute
    """
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if GEO_Map.__instance is None:
            GEO_Map()
        return GEO_Map.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if GEO_Map.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            GEO_Map.__instance = self
            self.map = pd.read_csv("zipCodePosId.csv", header=None, names=['lat', 'lon', 'city', 'state', 'pos_id'])
            self.map.index = self.map.index.astype(str)

    def get_lat(self, postcode):
        return self.map.loc[postcode, 'lat']

    def get_long(self, postcode):
        return self.map.loc[postcode, 'lon']

    def distance(self, lat1, long1, lat2, long2):
        theta = long1 - long2
        dist = math.sin(self.deg2rad(lat1)) * math.sin(self.deg2rad(lat2)) + math.cos(self.deg2rad(lat1)) * math.cos(
            self.deg2rad(lat2)) * math.cos(self.deg2rad(theta))
        dist = math.acos(dist)
        dist = self.rad2deg(dist)
        dist = dist * 60 * 1.1515 * 1.609344
        return dist

    def rad2deg(self, rad):
        return rad * 180.0 / math.pi

    def deg2rad(self, deg):
        return deg * math.pi / 180.0

