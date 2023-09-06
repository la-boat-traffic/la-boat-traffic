################## INITIAL IMPORTS #################

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

########## SEASONAL DECOMPOSITION FUNCTION #########

def seasonal_decomposition(train):
    """
    Perform seasonal decomposition on the time-series data.

    Args:
        train (DataFrame): Input DataFrame containing time-series data.

    Returns:
        None
    """
    # Resample 'train' to weekly data and calculate the mean
    weekly_mean = train.sales.resample('W').mean()

    # Perform seasonal decomposition
    decomposition = sm.tsa.seasonal_decompose(weekly_mean)

    # Plot each component separately
    decomposition.plot()

    
##################### NUM SHIPS DOCKED FUNCTION #################

def num_ships_docked(train):
    """
    Plot the distribution of the number of ships docked.

    Args:
        train (DataFrame): Input DataFrame containing ship docking data.

    Returns:
        None
    """
    train.num_at_berth.plot.hist()
    plt.title('Distribution of Number of Ships Docked')
    plt.show()

    
################### DAILY PORT OCCUPANCY ########################

def daily_port_occupancy(train):
    """
    Plot the mean port occupancy by day of the week.

    Args:
        train (DataFrame): Input DataFrame containing port occupancy data.

    Returns:
        None
    """
    train.groupby('weekday').mean().sort_values('day_num').num_at_berth.plot.bar()
    plt.title('Mean Port Occupancy By Day')
    plt.show()

    