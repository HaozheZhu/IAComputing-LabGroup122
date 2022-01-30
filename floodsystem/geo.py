# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

def rivers_with_stations(stations): 
    ans = set([])
    for station in stations: 
        if(station.river not in ans): 
            ans.add(station.river)
    ans = sorted(ans)
    return ans

def stations_by_river(stations): 
    ans = {}
    for station in stations: 
        if(station.river not in ans): 
            ans[station.river] = [station.name]
        else: 
            ans[station.river].append(station.name)
    for key in ans: 
        ans[key].sort()
    return ans