"""This module provides a line of best fit for the historical data of the water levels

"""

import numpy as np
import matplotlib



def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    y = levels
    p_coeff = np.polyfit(x - x[0], y, p)
    poly = np.poly1d(p_coeff)
    d0 = x[0]
    return poly, d0

def floodrisk(station, dates, levels, p):
    count = 0
    print(type(dates))
    print(dates)
    if dates != None:
        if station.relative_water_level() <100:
            poly, d0 = polyfit(dates, levels, p)
            x = matplotlib.dates.date2num(dates)
            x1 = np.linspace(x[0], x[-1], 1000)
            grad = (poly(x1[999]-d0)-poly(x1[0]-d0))
            if grad > 1.0:
                count += 2
            elif grad > 0.5:
                count += 1
            if station.relative_water_level() > 1:
                count += 1
            if count == 3:
                return "Severe"
            elif count == 2:
                return "High"
            elif count == 1:
                return "Moderate"
            else:
                return "Low"
        else:
            return "Low"
    else:
        return "Low"        