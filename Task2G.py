from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
import datetime
from floodsystem.analysis import floodrisk

def run():
    stations = build_station_list()
    update_water_levels(stations)
    severe=[]
    high=[]
    moderate=[]
    low=[]
    for station in stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=1))
        if floodrisk(dates, levels) == "Severe":
            severe.append(station.name)
        elif floodrisk(dates, levels) == "High":
            high.append(station.name)
        elif floodrisk(dates, levels) == "Moderate":
            moderate.append(station.name)
        elif floodrisk(dates, levels) == "Low":
            low.append(station.name)
    print (severe) 



if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()