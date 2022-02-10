def getRelLevel(item): 
    """Helper function to sort the list of tuples (river name, relative level) according to number of stations"""
    
    return item[1]

def stations_level_over_threshold(stations, tol): 
    ans = []
    for station in stations: 
        if station.relative_water_level() != None:
            if station.relative_water_level() > tol: 
                ans.append(tuple((station.name, station.relative_water_level())))
                ans.sort(key=getRelLevel, reverse=True)
    return ans

