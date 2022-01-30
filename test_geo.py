from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_with_stations


def test_rivers_with_stations(): 
    stations = build_station_list()
    rivers_with_stations(stations)

def test_stations_by_river(): 
    stations = build_station_list()
    stations_by_river(stations)

def test_rivers_by_station_number(): 
    stations = build_station_list()
    rivers_by_station_number(stations, 1)