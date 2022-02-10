from floodsystem.stationdata import build_station_list
import floodsystem.flood as flood

def test_stations_level_over_threshold(): 
    stations = build_station_list()
    flood.stations_level_over_threshold(stations, 0.9)

def test_stations_hightst_rel_level(): 
    stations = build_station_list()
    flood.stations_hightst_rel_level(stations, 10)