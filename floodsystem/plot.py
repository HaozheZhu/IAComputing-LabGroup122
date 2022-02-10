import matplotlib.pyplot as plt

def plot_water_levels(station, dates, levels): 
    """Function for ploting graphs of water level against data"""
    if station.typical_range_consistent(): 
        high = [station.typical_range[1] for i in levels]
        low = [station.typical_range[0] for i in levels]
    
    # Plot
    plt.plot(dates, levels)
    plt.plot(dates, high, label="Typical High")
    plt.plot(dates, low, label="Typical Low")

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.legend()

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

if __name__ == "__main__": 
    plot_water_levels(1, 1, 1)