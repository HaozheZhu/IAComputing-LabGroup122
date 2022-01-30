# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

def rivers_with_stations(stations): 
    """Given a list of MonitoringStation objects, returns a sorted list of names 
    of rivers with at least 1 monitoring station"""
    ans = set([])
    for station in stations: 
        ans.add(station.river)
    ans = sorted(ans)
    return ans

def stations_by_river(stations): 
    """Given a list of MonitoringStation objects, returns a dictionary with keys being river names
    and values being a sorted list of the names of the monitoring stations on that river"""
    ans = {}
    for station in stations: 
        if(station.river not in ans): 
            ans[station.river] = [station.name]
        else: 
            ans[station.river].append(station.name)
    for key in ans: 
        ans[key].sort()
    return ans

def getStationNum(item): 
    """Helper function to sort the list of tuples (river name, number of stations) according to number of stations"""
    return item[1]

def rivers_by_station_number(stations, N): 
    """Given a list of MonitoringStation objects and an integer N, returns a list of tuples (river name, number of stations)
    of N rivers with the greatest number of monitoring stations"""
    river_stations = stations_by_river(stations)
    ans = [(river, len(river_stations[river])) for river in river_stations]
    ans.sort(key=getStationNum, reverse=True)
    while(ans[N-1][1] == ans[N][1]): 
        N += 1
    return ans[:N]
