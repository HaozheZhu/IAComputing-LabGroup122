from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
import datetime

def run(): 
    stations = build_station_list()
    update_water_levels(stations)
    stations_plot = stations_highest_rel_level(stations, 5)
    for station in stations_plot: 
        dates, levels = fetch_measure_levels(station.measure_id,
                                             dt=datetime.timedelta(days=10))
        plot_water_levels(station, dates, levels)
    

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()