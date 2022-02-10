def getRelLevel1(item): 
    """Helper function to sort the list of tuples (river name, relative level) according to relative level"""
    
    return item[1]

def getRelLevel2(item): 
    """Helper function to sort the list of station objects according to relative level"""

    return item.relative_water_level()

def stations_level_over_threshold(stations, tol): 
    '''Function to return a list of tuples of stations whose relative water level is greater than the input threshold value '''
    ans = []
    for station in stations: 
        if station.relative_water_level() != None:
            if station.relative_water_level() > tol: 
                ans.append(tuple((station.name, station.relative_water_level())))
                ans.sort(key=getRelLevel1, reverse=True)
    return ans

def stations_highest_rel_level(stations, N): 
    '''Function which returns the N stations with highest relative water levels'''
    valid_stations = []
    for station in stations: 
        if station.relative_water_level() != None: 
            valid_stations.append(station)
    valid_stations.sort(key=getRelLevel2, reverse=True)
    return valid_stations[:N]