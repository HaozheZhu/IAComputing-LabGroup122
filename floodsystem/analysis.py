"""This module provides a line of best fit for the historical data of the water levels
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt



def polyfit(dates, levels, p):
    try:
        x = matplotlib.dates.date2num(dates)
        y = levels
        p_coeff = np.polyfit(x - x[0], y, p)
        poly = np.poly1d(p_coeff)
        d0 = x[0]
        return poly, d0
    except:
        return False, False

def floodrisk(station, dates, levels, p):
    count = 0
    poly, d0 = polyfit(dates, levels, p)
    if poly != False:
        x = matplotlib.dates.date2num(dates)
        x1 = np.linspace(x[0], x[-1], 100)
        grad = (poly(x1[49]-d0)-poly(x1[0]-d0))
        if grad > 1.0:
            count += 2
        elif grad > 0.5:
            count += 1
        if station.relative_water_level() > 1.2:
            count += 2
        elif station.relative_water_level() > 0.8:
            count += 1
        if count >= 3:
            return "Severe"
        elif count == 2:
            return "High"
        elif count == 1:
            return "Moderate"
        else:
            return "Low"