from floodsystem.stationdata import build_station_list, update_water_levels
import floodsystem.flood as flood

def run(): 
    stations = build_station_list()
    update_water_levels(stations)
    list = flood.stations_hightst_rel_level(stations, 10)
    for entry in list: 
        print("{} {}".format(entry.name, entry.relative_water_level(    )))

if __name__ == "__main__": 
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()