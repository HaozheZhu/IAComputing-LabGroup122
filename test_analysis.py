'''File to test Analysis submodule'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from floodsystem.stationdata import build_station_list, update_water_levels 
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit, floodrisk
import datetime

def test_polyfit():
    stations = build_station_list()
    update_water_levels(stations)
    dates, levels = fetch_measure_levels(stations[0].measure_id, dt=datetime.timedelta(days=2))
    polyfit(dates, levels, 4)

def test_floodrisk():
    stations = build_station_list()
    for station in stations:
        count += 1
        try:
            dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=1))
            risk = floodrisk(station, dates, levels, 4)
        except:
            risk = "Low"
    assert risk
