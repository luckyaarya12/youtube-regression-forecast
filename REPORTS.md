1. Introduction:-

   This study analyzes YouTube view data from the past 60 days to identify trends and forecast short-term performance. Using Python and time-series techniques, the analysis aims to understand changes in views and support 
   data-driven content planning.

3. Dataset Description:-

   The dataset used in this study consists of daily YouTube performance metrics collected over a period of 60 days. The data includes key variables such as views, likes, and subscriber count. The dataset is structured in 
   a tabular format and contains no missing or null values.

  The data was sourced from YouTube Analytics and stored in an Excel file. Prior to analysis, the dataset was imported into Python and prepared for time-series analysis without requiring additional imputation or data 
  cleaning.

3.  Research Questions:-

(A) How have Views, Likes, and Subscribers changed over the past 60 days?

(B) Can we identify trends in Views, Likes, and Subscribers using linear regression?

(C) Can we forecast future Views using time-series analysis (ARIMA)?

(D) What is the expected performance of the channel in the next 5 days?

4.  Methodology:-

(A) Data Cleaning: Converted Views/Likes/Subscribers from strings like '1.3K' to numeric values.

(B) Exploratory Analysis (EDA): Plotted historical metrics to visualize trends.

(C) Linear Regression: Modeled metrics against Serial Number (time index) to see trends.

(D) Moving Average: Applied 7-day moving average to smooth short-term fluctuations.

(E) ARIMA Forecasting: Built ARIMA(1,1,1) model on Views to predict next 5 days.

5.  Analytical Summary:-
 
(A) The analysis indicates a positive growth trend in channel performance over the observed 60-day period. Views exhibited high variability with several sharp spikes, while overall engagement increased toward the later 
    part of the dataset.

(B) Linear regression analysis shows an upward trend across views, likes, and subscribers, indicating sustained growth. The 7-day moving average helped smooth short-term fluctuations and revealed increasing stability in 
    audience engagement.

(C) Short-term forecasting using time-series techniques suggests that views are likely to stabilize in the near future, supporting the reliability of recent performance improvements.

6.  Assumptions:-

(A) Past trends in the last 60 days are representative of near-future behavior.

(B) External factors (e.g., viral content, algorithm changes) are not considered.

(C) Metrics like Views/Likes/Subscribers are accurately recorded and free from errors.

(D) ARIMA model assumptions:

The time series is weakly stationary after differencing (ARIMA handles trend with d=1).

No major structural breaks in the data.

7.  Limitations:-

(A) Forecast horizon is short (5 days) because longer forecasts may be unreliable with only 60 days of data.

(B) Forecast only considers Views; Likes/Subscribers are not forecasted in this model.

(C) External events, marketing pushes, or viral content may cause actual values to deviate significantly from forecast.

(D) Small dataset size (60 points) may limit model accuracy.

8.  Implications:-

(A) Helps in planning content strategy based on expected trends.

(B) Identifies short-term growth or decline in Views.

(C) Supports better resource allocation (e.g., promoting videos during predicted high-view days).

(D) Demonstrates the practical application of data analytics in social media forecasting.

9. Conclusion:-

  This study analyzed YouTube performance data over a 60-day period to identify trends and generate short-term forecasts using data analytics and time-series methods. The results indicate a positive growth trend in v 
  views, likes, and subscribers, with short-term fluctuations captured through moving averages.


The use of linear regression and ARIMA forecasting demonstrates how historical engagement data can be leveraged to support data-driven decision making in digital content strategy. Despite certain limitations related to dataset size and external factors, the analysis provides meaningful insights into short-term performance behavior.
