1. Introduction

This study analyzes YouTube channel performance data collected over the past 60 days to identify trends and forecast short-term performance. Using Python-based data analytics and time-series techniques, the analysis focuses on understanding changes in views, likes, and subscriber growth. The primary objective is to support data-driven content planning and performance evaluation.

2. Dataset Description

The dataset used in this study consists of daily YouTube performance metrics collected over a period of 60 days. It includes key variables such as Views, Likes, and Subscriber Count. The dataset is structured in a tabular format and contains no missing or null values.

The data was sourced from YouTube Analytics and stored in an Excel file. Prior to analysis, the dataset was imported into Python and prepared for time-series analysis. No additional data imputation was required, as the dataset was complete and consistent.

3. Research Questions

The study aims to address the following research questions:

(A) How have Views, Likes, and Subscribers changed over the past 60 days?
(B) Can trends in Views, Likes, and Subscribers be identified using linear regression?
(C) Can future Views be forecasted using time-series analysis (ARIMA)?
(D) What is the expected channel performance over the next 5 days?

4. Methodology

The following analytical steps were applied:

(A) Data Cleaning
Converted Views, Likes, and Subscribers from string formats such as “1.3K” or “2.5M” into numeric values.

(B) Exploratory Data Analysis (EDA)
Plotted historical trends of Views, Likes, and Subscribers to visualize overall performance patterns.

(C) Linear Regression Analysis
Modeled each metric against a numerical time index (Serial Number) to identify long-term trends.

(D) Moving Average Analysis
Applied a 7-day moving average to smooth short-term fluctuations and highlight underlying trends.

(E) ARIMA Forecasting
Implemented an ARIMA(1,1,1) model on Views data to forecast performance for the next 5 days.

5. Analytical Summary

(A) The analysis indicates a positive growth trend in channel performance over the observed 60-day period. Views showed high variability with several sharp spikes, while overall engagement increased toward the later part of the dataset.

(B) Linear regression analysis reveals an upward trend across Views, Likes, and Subscribers, indicating sustained channel growth. The 7-day moving average helped reduce short-term noise and highlighted increasing stability in audience engagement.

(C) Short-term forecasting using time-series techniques suggests that Views are likely to stabilize in the near future, supporting the reliability of recent performance improvements.

6. Assumptions

(A) Trends observed during the last 60 days are representative of near-future behavior.
(B) External factors such as viral content or algorithm changes are not considered.
(C) Views, Likes, and Subscriber metrics are accurately recorded and error-free.

(D) ARIMA Model Assumptions:

The time series becomes weakly stationary after differencing (d = 1).

No major structural breaks exist within the dataset.

7. Limitations

(A) The forecast horizon is limited to 5 days, as longer forecasts may be unreliable with only 60 data points.
(B) Forecasting is performed only for Views; Likes and Subscribers are not forecasted.
(C) External events, promotional campaigns, or viral trends may cause deviations from predicted values.
(D) The relatively small dataset size may limit model accuracy.

8. Implications

(A) Supports data-driven content planning based on expected performance trends.
(B) Helps identify short-term growth or decline in Views.
(C) Assists in efficient resource allocation, such as promoting videos during predicted high-view periods.
(D) Demonstrates the practical application of data analytics and forecasting techniques in social media performance analysis.

9. Conclusion

This study analyzed YouTube performance data over a 60-day period to identify trends and generate short-term forecasts using data analytics and time-series methods. The results indicate a positive growth trend in Views, Likes, and Subscribers, with short-term fluctuations effectively captured using moving averages.

The application of linear regression and ARIMA forecasting demonstrates how historical engagement data can be leveraged to support data-driven decision-making in digital content strategy. Despite limitations related to dataset size and external factors, the analysis provides meaningful insights into short-term performance behavior.
