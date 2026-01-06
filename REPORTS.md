# YouTube Performance Analysis Report

## 1. Introduction

This study analyzes YouTube view data from the past 60 days to identify trends and forecast short-term performance. Using Python and time-series techniques, the analysis aims to understand changes in views and support data-driven content planning.

---

## 2. Dataset Description

The dataset used in this study consists of daily YouTube performance metrics collected over a period of 60 days.

- Key Variables: Views, Likes, and Subscriber Count  
- Format: Tabular (Excel source)  
- Integrity: No missing or null values  
- Preparation: Data was imported into Python and converted for time-series analysis without requiring additional imputation  

---

## 3. Research Questions

- How have Views, Likes, and Subscribers changed over the past 60 days?  

- Can we identify trends in these metrics using linear regression?  

- Can we forecast future Views using time-series analysis (ARIMA)?  

- What is the expected performance of the channel in the next 5 days?  

---

## 4. Methodology

The analysis was conducted using the following technical pipeline:

- Data Cleaning: Converted metric strings (e.g., "1.3K") into numeric integers  
- Exploratory Data Analysis (EDA): Visualized historical metrics to identify patterns  
- Linear Regression: Modeled metrics against a time-based index to quantify growth rate  
- Moving Average: Applied a 7-day moving average to smooth high-frequency noise  
- ARIMA Forecasting: Developed an ARIMA(1,1,1) model to predict views for a 5-day horizon  

---

## 5. Analytical Summary

The analysis indicates a positive growth trend over the 60-day period. While Views exhibited high variability with several sharp spikes, overall engagement increased toward the later part of the dataset.

- Trend Analysis: Linear regression shows a consistent upward trajectory across all KPIs  
- Stability: The 7-day moving average revealed increasing stability in audience engagement  
- Projection: Short-term forecasting suggests that views are likely to stabilize in the near future, validating recent performance gains  

---

## 6. Assumptions

- Past trends are representative of near-future (5-day) behavior  
- External factors such as algorithm changes and viral spikes remain constant  
- Model-Specific: The time series is weakly stationary after differencing (d = 1), and the dataset contains no major structural breaks  

---

## 7. Limitations

- Forecast Window: Limited to 5 days; longer-term accuracy is constrained by the 60-day sample size  
- Scope: Forecast focuses exclusively on Views; Likes and Subscribers are excluded from the predictive model  
- External Volatility: Unexpected marketing events or viral content may cause deviations from the statistical forecast  

---

## 8. Implications

- Content Strategy: Facilitates planning based on expected high-traffic windows  
- Trend Identification: Enables early detection of short-term growth or decline  
- Resource Allocation: Supports data-backed decisions for video promotion schedules  

---

## 9. Conclusion

This study leveraged historical performance data to generate actionable short-term forecasts. By combining Linear Regression and ARIMA modeling, the analysis successfully identifies a growth phase for the channel. Despite limitations related to dataset size, the findings provide a reliable foundation for data-driven decision-making in digital content strategy.
