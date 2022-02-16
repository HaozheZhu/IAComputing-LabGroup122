from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
import datetime


def run(N):
    stations = build_station_list()
    update_water_levels(stations)
    stations_plot = stations_highest_rel_level(stations, N)
    for station in stations_plot: 
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=2))
        print(dates)
        plot_water_level_with_fit(station, dates, levels, 4)


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run(5)