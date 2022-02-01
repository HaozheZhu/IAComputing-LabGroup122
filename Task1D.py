from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_stations, stations_by_river

def run(): 
    """Requirements for Task 1D"""
    stations = build_station_list()
    ans = rivers_with_stations(stations)
    ans1 = stations_by_river(stations)
    print("{:d} stations. First 10 - {}".format(len(ans), ans[:10]))
    print("River Aire: {}".format(ans1["River Aire"]))
    print("River Cam: {}".format(ans1["River Cam"]))
    print("River T hames: {}".format(ans1["River Thames"]))



if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()