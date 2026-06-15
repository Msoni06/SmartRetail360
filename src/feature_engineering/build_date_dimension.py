import pandas as pd
from pathlib import Path

orders = pd.read_csv(
    "data/cleaned/olist_orders_dataset.csv"
)

orders[
    "order_purchase_timestamp"
] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)

dates = pd.DataFrame()

dates["full_date"] = (
    orders["order_purchase_timestamp"]
    .dt.date
    .drop_duplicates()
)

dates["year"] = pd.to_datetime(
    dates["full_date"]
).dt.year

dates["quarter"] = pd.to_datetime(
    dates["full_date"]
).dt.quarter

dates["month"] = pd.to_datetime(
    dates["full_date"]
).dt.month

dates["month_name"] = pd.to_datetime(
    dates["full_date"]
).dt.month_name()

dates["week"] = pd.to_datetime(
    dates["full_date"]
).dt.isocalendar().week

dates["day"] = pd.to_datetime(
    dates["full_date"]
).dt.day

dates = dates.sort_values(
    "full_date"
)

dates.to_csv(
    "data/processed/dim_date.csv",
    index=False
)

print(
    f"Date records created: {len(dates)}"
)