import pandas as pd
from pathlib import Path

print("Loading datasets...")

customers = pd.read_csv(
    "data/cleaned/olist_customers_dataset.csv"
)

orders = pd.read_csv(
    "data/cleaned/olist_orders_dataset.csv"
)

payments = pd.read_csv(
    "data/cleaned/olist_order_payments_dataset.csv"
)

print("Datasets loaded")

# ----------------------------------
# Date Conversion
# ----------------------------------

orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)

# ----------------------------------
# Customer + Orders
# ----------------------------------

customer_orders = orders.merge(
    customers,
    on="customer_id",
    how="left"
)

# ----------------------------------
# Order Revenue
# ----------------------------------

order_revenue = (
    payments.groupby("order_id")["payment_value"]
    .sum()
    .reset_index()
)

customer_orders = customer_orders.merge(
    order_revenue,
    on="order_id",
    how="left"
)

# ----------------------------------
# Customer Aggregation
# ----------------------------------

feature_store = (
    customer_orders
    .groupby("customer_unique_id")
    .agg(
        total_orders=("order_id", "nunique"),
        total_spent=("payment_value", "sum"),
        avg_order_value=("payment_value", "mean"),
        first_purchase=("order_purchase_timestamp", "min"),
        last_purchase=("order_purchase_timestamp", "max")
    )
    .reset_index()
)

# ----------------------------------
# Recency
# ----------------------------------

max_date = feature_store[
    "last_purchase"
].max()

feature_store[
    "days_since_last_purchase"
] = (
    max_date
    - feature_store["last_purchase"]
).dt.days

# ----------------------------------
# Save
# ----------------------------------

Path(
    "data/feature_store"
).mkdir(
    exist_ok=True
)

feature_store.to_csv(
    "data/feature_store/customer_features.csv",
    index=False
)

print(
    "\nCustomer Feature Store Created"
)

print(
    f"Rows: {feature_store.shape[0]}"
)

print(
    f"Columns: {feature_store.shape[1]}"
)

print(
    feature_store.head()
)