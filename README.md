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

We utilized Time Series Analysis to predict boat traffic, defined as number of boats at berth per day, in the Los Angeles port docks. Data came from March 2015 to December 2018 records for the Port of Los Angeles.

[[Back to top](#top)]

 ## <a name="project_goal"></a>Project Goal:

 The Port of Los Angeles is the busiest shipping port in the United States. Staffing and resource allocation for such a major trade hub is crucial to maintaining logistical integrity for US importation and exportation. In pursuit of informing planners of such logistics, our goal was to analyze port traffice data over time to create a model for predicting daily traffic. 

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
- Acquire:
    - Our data was acquired through the Port of LA website at ["LA Port Traffic]([https://www.portoflosangeles.org/business/supply-chain/ships]))
   
- The data encompasses all weekday, non-holiday port of LA traffic days from March 2015 through December 2018
- Data was originally formatted as a PDF and converted into CSV format through the python tabula library
- Each row represents data for a day of port operations including occupancy, anchorage, and wait times
- Prepare:
- Renamed columns to be more easily interpretable
- Separated date column into additional year, month, and date columns, keeping original date as index
- Created a backlog column representing difference between days at birth and days at birth plus anchorage days
 
- Exploration:
- 

- Modeling:
  - 
- 
- 
***


### Target Programming Language



*********************

# Modeling:

### Model 1

- 

### Model 2

- 

### Model 3

- 

- 


# Conclusion

- 
- 


# Recommendations
- 
- 
- 



# Takaways

- 
- 
- 



# Next Steps

- 
- 
- 

# Steps on How to Reproduce Project:
1. Go to 
2. 
3. 
4. 
5. 
6. 
7. 
