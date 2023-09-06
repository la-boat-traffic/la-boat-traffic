import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.api import Holt, ExponentialSmoothing
from sklearn.metrics import mean_squared_error


################# PREPROCESS FUNCTION ##################

def preprocess(train, val, test):
    """
    
    """
    # Add weekends to train
    date_range = pd.date_range(start=train.index[0], end=train.index[-1], freq='D')
    train = train.reindex(date_range)
    train['num_at_berth'] = train['num_at_berth'].fillna(0)
    
    # Add weekends to val
    date_range = pd.date_range(start=val.index[0], end=val.index[-1], freq='D')
    val = val.reindex(date_range)
    val['num_at_berth'] = val['num_at_berth'].fillna(0)
    
    # Add weekends to test
    date_range = pd.date_range(start=test.index[0], end=test.index[-1], freq='D')
    test = test.reindex(date_range)
    test['num_at_berth'] = test['num_at_berth'].fillna(0)

    return train, val, test


################### EVALUATE FUNCTION ###################

def evaluate(validate, yhat_df, target_var):
    '''
    This function will take the actual values of the target_var from validate, 
    and the predicted values stored in yhat_df, 
    and compute the rmse, rounding to 0 decimal places. 
    it will return the rmse. 
    '''
    rmse = mean_squared_error(validate[target_var], yhat_df[target_var])**.5
    return rmse


################ PLOT AND EVALUATE FUNCTON ###################

def plot_and_eval(train, val, yhat_df, target_var):
    '''
    This function takes in the target var name (string), and returns a plot
    of the values of train for that variable, validate, and the predicted values from yhat_df. it will also label the rmse. 
    '''
    plt.figure(figsize = (12,4))
    plt.plot(train[target_var], label = 'Train', linewidth = 1)
    plt.plot(val[target_var], label = 'Validate', linewidth = 1)
    plt.plot(yhat_df[target_var])
    plt.title(target_var)
    rmse = evaluate(val, yhat_df, target_var)
    print(target_var, '-- RMSE: {:.2f}'.format(rmse))
    plt.show()
    return rmse


################# BUILD BASELINE MODEL FUNCTON ###############

def build_baseline_model(train, val):
    """
    
    """
    rolling_target = round(train.num_at_berth.rolling(21).mean()[-1], 2)
    yhat_df = pd.DataFrame({'num_at_berth': [rolling_target]}, index=val.index)
    
    plt.figure(figsize = (12,4))
    plt.plot(train['num_at_berth'], label = 'Train', linewidth = 1)
    plt.plot(val['num_at_berth'], label = 'Validate', linewidth = 1)
    plt.plot(yhat_df['num_at_berth'])
    plt.title('Rolling Moving Average of 21 Days')
    rmse = evaluate(val, yhat_df, 'num_at_berth')
    print('num_at_berth', '-- RMSE: {:.2f}'.format(rmse))
    plt.show()
    
    
################# BUILD HOLT LINEAR MODEL FUNCTION ###############

def build_holt_linear_model(train, val):
    """
    
    """
    yhat_df = pd.DataFrame()
    
    holt_model = Holt(train.num_at_berth, exponential=False, damped=False)
    holt_model = holt_model.fit(optimized=True)
    yhat_values = holt_model.predict(start=val.index[0], end=val.index[-1])

    yhat_df['num_at_berth'] = round(yhat_values, 2)

    rmse = plot_and_eval(train, val, yhat_df, 'num_at_berth')

    rmse_df = pd.DataFrame({
    'model': 'HoltsLinear',
    'rmse' : round(rmse, 4)
    }, index=[])
    
    
################### TEST HOLT LINEAR FUNCTION #####################
    
def test_holt_linear():
    """
    
    """
    
    
    