# <a name="top"></a>LA Port Traffic Project
![]()


***
[[Project Description](#project_description)]
[[Project Goal](#project_goal)]
[[Initial Thoughts/Questions](#initial_thoughts_questions)]
[[Data Dictionary](#dictionary)]
[[Project Planning](#planning)]
[[Key Findings](#findings)]
[[Statistical Analysis](#stats)]
[[Modeling](#model)]
[[Conclusion](#conclusion)]
___



## <a name="project_description"></a>Project Description:

We utilized Time Series Analysis to predict boat traffic, defined as number of boats at berth per day, in the Los Angeles port docks. Data came from May 2015 to December 2018 records for the Port of Los Angeles.

[[Back to top](#top)]

 ## <a name="project_goal"></a>Project Goal:

 The Port of Los Angeles is the busiest shipping port in the United States. Staffing and resource allocation for such a major trade hub is crucial to maintaining logistical integrity for US importation and exportation. In pursuit of informing planners of such logistics, our goal was to analyze port traffic data over time to create a model for predicting daily traffic. 

 [[Back to top](#top)]
 
 
## <a name="initial_thoughts_questions"></a>Initial Thoughts/Questions:
1. We predict that there will be some autocorrelation (predictive capability) between lagged (offset) daily values. 
2. We predict that there will also be some seasonality in the data resulting from global supply and demand patterns. 

 [[Back to top](#top)]

## <a name="dictionary"></a>Data Dictionary  
[[Back to top](#top)]


### Data Used
---
| Attribute | Definition | Data Type |
| ----- | ----- | ----- |
|num_at_berth| Number of ships docked at the Port of LA, Target Variable |integer|
|date| Day of the year in year-month-day format, index |date|
|num_at_anchor| Number of vessels anchored and awaiting docking |integer|
|departed| Number of vessels that departed that day |integer|
|avg_days_at_berth| Average days docked per day for all vessels docked |float|
|avg_days_anchor_berth| Average days docked plus average days anchored per day for all vessels docked and anchored |float|
**

***

## <a name="planning"></a>Project Plan: 
[[Back to top](#top)]
- Acquire/Prepare:
    - Our data was acquired through the Port of LA website at ["LA Port Traffic]([https://www.portoflosangeles.org/business/supply-chain/ships]))
   
- The data encompasses all weekday, non-holiday port of LA traffic days from March 2015 through December 2018
- Data was originally formatted as a PDF and converted into CSV format through the python tabula library
- Each row represents data for a day of port operations including occupancy, anchorage, and wait times
- Prepare:
- Renamed columns to be more easily interpretable
- Separated date column into additional year, month, and date columns, keeping original date as index
- Created a backlog column representing difference between days at birth and days at birth plus anchorage days
- Split data chronologically in 70/15/15 split with test data starting in April 2015 and the remaining split sections as 15 percent respectively of the remaining time

***




*********************

# Conclusions:

### Model 1

- Rolling Average baseline model had an RMSE of of 4.95 ships

### Model 2

- Holt's Linear Model was set at non-exponential smoothing and no dampening
- RMSE was 5.64, not exceeding baseline

### Model 3

- 

- 

# Findings

- Exploration of the data showed that the most predictable trends are weekly traffic patterns. Since the port is closed on weekends, total berth occupancy tends to build up toward the middle of the week as ships arrive. The port is consequently busiest in the last half of the week.
- The original data included March of 2015, but an unusually large number of anchored ships and backlog time indicated an anomaly. From internet research, there was a US West Coast dock workers strike at this time that increased wait time for ships. We ultimately excluded March and half of April and re-split our data. 
- The modal average of ships in port was 10, by a wide margin. 

# Recommendations
- Staffing, shifts, and material focus should remain on latter parts of the week as port traffic, as well as backlog, tends to reach a maximum
- The port should be prepared to handle at least 10 ships, likely including one non-container ship at berth on high-occupancy days

# Next Steps

- Attempt additional time series models including: Holt Winter and Facebook Prophet models
- Check with Port of LA to obtain additional data on ship type and individual dock data
- Collect data on when shipping companies "slow steam" to save money on repairs and fuel
- Obtain point of origin weather data from most common trade partner ports to see if this affects LA port traffic

# Steps on How to Reproduce Project:
1. Download files from our Repository
2. Functions in wrangle.py file will acquire PDFs of port data ranging between 05/2015 to 12/2018 from https://www.portoflosangeles.org/business/supply-chain/ships
3. This can be acquired manually by following the above link and downloading and converting each PDF separately using the Python tabula library
4. Remaining wrangle functions will convert PDFs to a pandas dataframe 
5. Open the final notebook and run included lines of code

