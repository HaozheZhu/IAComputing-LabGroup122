from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    '''Requirements for Task 1C'''
    stations = build_station_list()
    centre = tuple((52.2053, 0.1218))
    r = 10.0
    response = stations_within_radius(stations, centre, r)
    response2 = []
    for i in range(len(response)):
        response2.append(response[i].name)
    print(response2)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
