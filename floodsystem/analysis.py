"""This module provides a line of best fit for the historical data of the water levels

"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    print(x)
    y = levels
    p_coeff = np.polyfit(x - x[0], y, p)
    poly = np.poly1d(p_coeff)
    d0 = x[1]
    return poly, d0