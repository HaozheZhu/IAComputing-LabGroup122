from floodsystem.stationdata import build_station_list
import floodsystem.geo as geo


def test_rivers_with_stations(): 
    stations = build_station_list()
    geo.rivers_with_stations(stations)

def test_stations_by_river(): 
    stations = build_station_list()
    geo.stations_by_river(stations)

def test_rivers_by_station_number(): 
    stations = build_station_list()
    geo.rivers_by_station_number(stations, 1)