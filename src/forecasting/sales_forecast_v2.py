import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import matplotlib.pyplot as plt

print("Loading data...")

orders = pd.read_csv(
    "data/cleaned/olist_orders_dataset.csv"
)

payments = pd.read_csv(
    "data/cleaned/olist_order_payments_dataset.csv"
)

orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)

sales = orders.merge(
    payments,
    on="order_id",
    how="inner"
)

sales["date"] = (
    sales["order_purchase_timestamp"]
    .dt.date
)

daily_sales = (
    sales.groupby("date")["payment_value"]
    .sum()
    .reset_index()
)

daily_sales.columns = [
    "date",
    "revenue"
]

daily_sales["date"] = pd.to_datetime(
    daily_sales["date"]
)

daily_sales = daily_sales.set_index("date")

daily_sales = daily_sales.asfreq("D")

daily_sales["revenue"] = (
    daily_sales["revenue"]
    .fillna(0)
)

print(
    f"Days of history: {len(daily_sales)}"
)

model = ExponentialSmoothing(
    daily_sales["revenue"],
    trend="add",
    seasonal=None
)

fit = model.fit()

forecast = fit.forecast(
    90
)

forecast_df = pd.DataFrame(
    {
        "forecast_date": forecast.index,
        "forecast_revenue": forecast.values
    }
)

forecast_df.to_csv(
    "data/exports/forecast.csv",
    index=False
)

plt.figure(figsize=(12,6))

plt.plot(
    daily_sales.index,
    daily_sales["revenue"]
)

plt.plot(
    forecast.index,
    forecast.values
)

plt.title(
    "90 Day Revenue Forecast"
)

plt.savefig(
    "reports/forecast_plot.png"
)

print(
    "\nForecast created successfully"
)

print(
    forecast_df.head()
)