from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold

def test_stations_level_over_threshold(): 
    stations = build_station_list()
    stations_level_over_threshold(stations, 0.9)
