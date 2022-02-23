import matplotlib.pyplot as plt
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
import datetime

def run(N): 
    stations = build_station_list()
    update_water_levels(stations)
    stations_plot = stations_highest_rel_level(stations, N)

    if N <= 6:
        fig, axs = plt.subplots(N) 
        for i in range(len(stations_plot)): 
            dates, levels = fetch_measure_levels(stations_plot[i].measure_id,
                                                dt=datetime.timedelta(days=10))   
            if stations_plot[i].typical_range_consistent(): 
                high = [stations_plot[i].typical_range[1] for j in range(len(levels))]
                low = [stations_plot[i].typical_range[0] for j in range(len(levels))]
            
            axs[i].plot(dates, levels, label=stations_plot[i].name)
            axs[i].plot(dates, high, label="Typical High")
            axs[i].plot(dates, low, label="Typical Low")
            axs[i].legend()
            axs[i].set(xlabel="Data", ylabel="Water level (m)")
        fig.suptitle('Selected river data ploted on a single figure')
        plt.show()
    else: 
        for station in stations_plot: 
            dates, levels = fetch_measure_levels(station.measure_id,
                                                dt=datetime.timedelta(days=10))
            plot_water_levels(station, dates, levels)
    

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run(7)