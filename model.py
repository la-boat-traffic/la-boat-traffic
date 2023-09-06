################## INITIAL IMPORTS ####################

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.api import Holt, ExponentialSmoothing
from sklearn.metrics import mean_squared_error


################# PREPROCESS FUNCTION ##################

def preprocess(train, val, test):
    """
    Preprocess the data by adding weekends to the train, val, and test sets
    and filling missing values with zeros.
    
    Args:
        train (DataFrame): Training dataset.
        val (DataFrame): Validation dataset.
        test (DataFrame): Test dataset.
        
    Returns:
        DataFrame, DataFrame, DataFrame: Preprocessed train, val, and test sets.
    """
    # Add weekends to train
    date_range = pd.date_range(start=train.index[0], end=train.index[-1], freq='D')
    train = train.reindex(date_range)
    train['num_at_berth'] = train['num_at_berth'].fillna(train.num_at_berth.mean())
    
    # Add weekends to val
    date_range = pd.date_range(start=val.index[0], end=val.index[-1], freq='D')
    val = val.reindex(date_range)
    val['num_at_berth'] = val['num_at_berth'].fillna(val.num_at_berth.mean())
    
    # Add weekends to test
    date_range = pd.date_range(start=test.index[0], end=test.index[-1], freq='D')
    test = test.reindex(date_range)
    test['num_at_berth'] = test['num_at_berth'].fillna(test.num_at_berth.mean())

    return train, val, test


################### EVALUATE FUNCTION ###################

def evaluate(validate, yhat_df, target_var):
    '''
    Calculate the Root Mean Squared Error (RMSE) between actual and predicted values.
    
    Args:
        validate (DataFrame): Validation dataset containing actual values.
        yhat_df (DataFrame): DataFrame containing predicted values.
        target_var (str): Name of the target variable.
        
    Returns:
        float: The RMSE value.
    '''
    rmse = mean_squared_error(validate[target_var], yhat_df[target_var])**.5
    return rmse


################ PLOT AND EVALUATE FUNCTION ###################

def plot_and_eval(train, val, yhat_df, target_var):
    '''
    Plot the actual values of train, validate, and predicted values from yhat_df, 
    and calculate and display the RMSE.
    
    Args:
        train (DataFrame): Training dataset.
        val (DataFrame): Validation dataset.
        yhat_df (DataFrame): DataFrame containing predicted values.
        target_var (str): Name of the target variable.
        
    Returns:
        float: The RMSE value.
    '''
    plt.figure(figsize=(12, 4))
    plt.plot(train[target_var], label='Train', linewidth=1)
    plt.plot(val[target_var], label='Validate', linewidth=1)
    plt.plot(yhat_df[target_var])
    plt.title(target_var)
    rmse = evaluate(val, yhat_df, target_var)
    print(target_var, '-- RMSE: {:.2f}'.format(rmse))
    plt.show()
    return rmse


################# BUILD BASELINE MODEL FUNCTION ###############

def build_baseline_model(train, val):
    """
    Build and evaluate a baseline model using the rolling mean.

    Args:
        train (DataFrame): Training dataset.
        val (DataFrame): Validation dataset.

    Returns:
        None
    """
    # Calculate the rolling mean of the training data
    rolling_target = round(train.num_at_berth.rolling(21).mean()[-1], 2)
    
    # Create a DataFrame with constant predictions for the validation period
    yhat_df = pd.DataFrame({'num_at_berth': [rolling_target]}, index=val.index)
    
    # Plot the training, validation, and predicted values
    plt.figure(figsize=(12, 4))
    plt.plot(train['num_at_berth'], label='Train', linewidth=1)
    plt.plot(val['num_at_berth'], label='Validate', linewidth=1)
    plt.plot(yhat_df['num_at_berth'])
    plt.title('Rolling Moving Average of 21 Days')
    
    # Evaluate the model and display RMSE
    rmse = evaluate(val, yhat_df, 'num_at_berth')
    print('num_at_berth', '-- RMSE: {:.2f}'.format(rmse))
    plt.show()
    
    
################# BUILD HOLT LINEAR MODEL FUNCTION ###############

def build_holt_linear_model(train, val):
    """
    Build and evaluate a Holt Linear model.

    Args:
        train (DataFrame): Training dataset.
        val (DataFrame): Validation dataset.

    Returns:
        None
    """
    # Initialize an empty DataFrame for predictions
    yhat_df = pd.DataFrame()
    
    # Create and fit the Holt Linear model
    holt_model = Holt(train.num_at_berth, exponential=False, damped=False)
    holt_model = holt_model.fit(optimized=True)
    
    # Generate predictions for the validation period
    yhat_values = holt_model.predict(start=val.index[0], end=val.index[-1])

    # Store predictions in the DataFrame
    yhat_df['num_at_berth'] = round(yhat_values, 2)

    # Plot actual values, predicted values, and evaluate the model
    rmse = plot_and_eval(train, val, yhat_df, 'num_at_berth')

    # Create a DataFrame to store RMSE values
    rmse_df = pd.DataFrame({
        'model': 'HoltsLinear',
        'rmse': round(rmse, 4)
    }, index=[])
    
    
################### TEST HOLT LINEAR FUNCTION #####################

def test_holt_linear(train, val, test):
    """
    Build, evaluate, and test a Holt Linear model on the test dataset.

    Args:
        None

    Returns:
        None
    """
    # Create and fit the Holt Linear model
    holt_model = Holt(train.num_at_berth, exponential=False, damped=False)
    holt_model = holt_model.fit(optimized=True)
    
    # Initialize a DataFrame for predictions
    yhat_df = pd.DataFrame()
    
    # Generate predictions for the test period
    yhat_df['num_at_berth'] = holt_model.predict(start=test.index[0], end=test.index[-1])

    # Plot actual values, predicted values, and evaluate the model
    plt.figure(figsize=(12, 4))
    plt.plot(train['num_at_berth'], label='Train', linewidth=1)
    plt.plot(val['num_at_berth'], label='Validate', linewidth=1)
    plt.plot(test['num_at_berth'], label='Test', linewidth=1)
    plt.plot(yhat_df['num_at_berth'])
    plt.title("Holt's Linear Model")
    rmse = evaluate(test, yhat_df, 'num_at_berth')
    print('num_at_berth', '-- RMSE: {:.2f}'.format(rmse))
    plt.show()

    