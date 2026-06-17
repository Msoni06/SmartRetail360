import pandas as pd
from prophet import Prophet

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

daily_revenue = (
    orders.merge(
        payments,
        on="order_id"
    )
)

daily_revenue["date"] = (
    daily_revenue[
        "order_purchase_timestamp"
    ].dt.date
)

daily_revenue = (
    daily_revenue
    .groupby("date")
    ["payment_value"]
    .sum()
    .reset_index()
)

daily_revenue.columns = [
    "ds",
    "y"
]

print(
    daily_revenue.head()
)

model = Prophet()

model.fit(
    daily_revenue
)

future = model.make_future_dataframe(
    periods=90
)

forecast = model.predict(
    future
)

forecast.to_csv(
    "data/exports/forecast.csv",
    index=False
)

print(
    "\nForecast created successfully"
)

print(
    forecast[
        [
            "ds",
            "yhat"
        ]
    ].tail()
)