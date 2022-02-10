from floodsystem.stationdata import build_station_list, update_water_levels
import floodsystem.flood as flood

def run(): 
    stations = build_station_list()
    update_water_levels(stations)
    ans = flood.stations_level_over_threshold(stations, 0.8)
    for entry in ans: 
        print("{} {}".format(entry[0], entry[1]))

if __name__ == "__main__": 
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()