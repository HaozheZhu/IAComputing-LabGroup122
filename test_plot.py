from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def test_plot_water_levels(): 
    stations = build_station_list()
    dates, levels = fetch_measure_levels(stations[0].measure_id,
                                                dt=datetime.timedelta(days=10))
    plot_water_levels(stations[0], dates, levels)