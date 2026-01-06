# ---------------------------------------------
# YouTube Metrics Forecasting 
# ---------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima.model import ARIMA

data = pd.read_excel('youtube_data_past_60days.xlsx') 
data['Date'] = pd.to_datetime(data['Date'])

# Function to convert strings like '1.3K', '2.5M' to integers
def convert_to_number(x):
    if isinstance(x, str):
        x = x.strip()
        if x[-1] == 'K':
            return float(x[:-1]) * 1_000
        elif x[-1] == 'M':
            return float(x[:-1]) * 1_000_000
        else:
            return float(x.replace(',', ''))  # remove commas
    return x

# Apply to all metric columns
for col in ['Views', 'Likes', 'Subscribers']:
    data[col] = data[col].apply(convert_to_number)


# Sort data by Date
data = data.sort_values('Date')

print("First 5 rows of the dataset:")
print(data.head())

# ---------------------------------------------
# Exploratory Data Analysis (EDA)
# ---------------------------------------------
plt.figure(figsize=(12,6))
plt.plot(data['Date'], data['Views'], label='Views')
plt.plot(data['Date'], data['Likes'], label='Likes')
plt.plot(data['Date'], data['Subscribers'], label='Subscribers')
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('YouTube Metrics Over Time')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------------------------------------------
# Linear Regression (Trend Analysis)
# ---------------------------------------------
metrics = ['Views', 'Likes', 'Subscribers']
X = data[['Serial Number']]  # numerical time index

for metric in metrics:
    y = data[metric]

    model = LinearRegression()
    model.fit(X, y)

    # Store predictions
    data[f'Predicted_{metric}'] = model.predict(X)

    # Plot actual vs predicted
    plt.figure(figsize=(10,5))
    plt.plot(data['Serial Number'], y, label=f'Actual {metric}')
    plt.plot(data['Serial Number'], data[f'Predicted_{metric}'],
             label=f'Predicted {metric}', linestyle='--')
    plt.xlabel('Day Index')
    plt.ylabel(metric)
    plt.title(f'Linear Regression Trend: {metric}')
    plt.legend()
    plt.tight_layout()
    plt.show()

    # RMSE
    rmse = np.sqrt(mean_squared_error(y, data[f'Predicted_{metric}']))
    print(f'RMSE for {metric}: {rmse:.2f}')

# ---------------------------------------------
# Moving Average (7-day Smoothing)
# ---------------------------------------------
for metric in metrics:
    data[f'{metric}_MA_7'] = data[metric].rolling(window=7).mean()

    plt.figure(figsize=(10,5))
    plt.plot(data['Date'], data[metric], label='Original')
    plt.plot(data['Date'], data[f'{metric}_MA_7'],
             label='7-day Moving Average', linestyle='--')
    plt.xlabel('Date')
    plt.ylabel(metric)
    plt.title(f'7-day Moving Average: {metric}')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# ---------------------------------------------
# ARIMA Forecasting (Views Only)
# ---------------------------------------------
# Set Date as index for time-series model
views_ts = data.set_index('Date')['Views']

# Build ARIMA model
arima_model = ARIMA(views_ts, order=(1, 1, 1))
arima_fit = arima_model.fit()

# Forecast next 5 days
forecast = arima_fit.forecast(steps=5)

print("\nNext 5 Days Views Forecast:")
print(forecast)

# ---------------------------------------------
# Plot Forecast with Historical Data
# ---------------------------------------------
plt.figure(figsize=(10,5))
plt.plot(views_ts, label='Historical Views')
plt.plot(views_ts.rolling(7).mean(), label='7-day MA', linestyle='--')

forecast.plot(label='5-day Forecast', marker='o', linestyle='--')

plt.xlabel('Date')
plt.ylabel('Views')
plt.title('Views Forecast Using ARIMA')
plt.legend()
plt.tight_layout()
plt.show()
