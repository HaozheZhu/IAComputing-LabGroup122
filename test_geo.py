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

def test_stations_by_distance():
    stations = build_station_list()
    p = tuple((52.2053, 0.1218))
    geo.stations_by_distance(stations, p)

def test_stations_within_radius():
    stations = build_station_list()
    centre = tuple((52.2053, 0.1218))
    r = 10.0
    geo.stations_within_radius(stations, centre, r)
