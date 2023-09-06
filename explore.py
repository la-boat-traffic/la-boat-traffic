import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

########## SEASONAL DECOMPOSITION FUNCTION #########

def seasonal_decomposition(train):
    """
    Takes in the train dataframe and performs seasonal decomposition on the time-series data
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
    
    """
    train.num_at_berth.plot.hist()
    plt.title('Distribution of Number of Ships Docked')
    plt.show()


################### DAILY PORT OCCUPANCY ########################

def daily_port_occupancy(train):
    """
    
    """
    train.groupby('weekday').mean().sort_values('day_num').num_at_berth.plot.bar()
    plt.title('Mean Port Occupancy By Day')
    plt.show()
    
    