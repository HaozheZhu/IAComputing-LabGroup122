from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    '''Requirements for Task 1B'''
    stations = build_station_list()
    p = tuple((52.2053, 0.1218))
    response = stations_by_distance[:10]
    print(response)

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()