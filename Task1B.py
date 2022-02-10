from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    '''Requirements for Task 1B'''
    stations = build_station_list()
    p = tuple((52.2053, 0.1218))
    response = stations_by_distance(stations, p)
    response2 = []
    for i in range(len(response)):
        response2.append((response[i][0].name, response[i][0].town, response[i][1]))
    print(response2[:10])
    print(response2[-10:])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
