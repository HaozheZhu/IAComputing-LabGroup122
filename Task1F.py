from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list


def run():
    '''Requirements for Task 1F'''
    stations = build_station_list()
    response = inconsistent_typical_range_stations(stations)
    print(response)

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
