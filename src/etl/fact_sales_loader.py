import pandas as pd
from sqlalchemy import create_engine
from src.config.db_config import DB_CONFIG

engine = create_engine(
    f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
)

print("Loading source files...")

customers = pd.read_sql(
    "SELECT customer_key, customer_id FROM retail.dim_customer",
    engine
)

products = pd.read_sql(
    "SELECT product_key, product_id FROM retail.dim_product",
    engine
)

sellers = pd.read_sql(
    "SELECT seller_key, seller_id FROM retail.dim_seller",
    engine
)

regions = pd.read_sql(
    "SELECT region_key, state_code FROM retail.dim_region",
    engine
)

dates = pd.read_sql(
    "SELECT date_key, full_date FROM retail.dim_date",
    engine
)

orders = pd.read_csv(
    "data/cleaned/olist_orders_dataset.csv"
)

items = pd.read_csv(
    "data/cleaned/olist_order_items_dataset.csv"
)

payments = pd.read_csv(
    "data/cleaned/olist_order_payments_dataset.csv"
)

reviews = pd.read_csv(
    "data/cleaned/olist_order_reviews_dataset.csv"
)

cust_raw = pd.read_csv(
    "data/cleaned/olist_customers_dataset.csv"
)

print("Building fact table...")

fact = items.merge(
    orders[["order_id","customer_id","order_purchase_timestamp"]],
    on="order_id",
    how="left"
)

fact = fact.merge(
    payments.groupby("order_id")["payment_value"]
    .sum()
    .reset_index(),
    on="order_id",
    how="left"
)

fact = fact.merge(
    reviews[["order_id","review_score"]],
    on="order_id",
    how="left"
)

fact = fact.merge(
    cust_raw[["customer_id","customer_state"]],
    on="customer_id",
    how="left"
)

fact = fact.merge(
    customers,
    on="customer_id",
    how="left"
)

fact = fact.merge(
    products,
    on="product_id",
    how="left"
)

fact = fact.merge(
    sellers,
    on="seller_id",
    how="left"
)

fact = fact.merge(
    regions,
    left_on="customer_state",
    right_on="state_code",
    how="left"
)

fact["full_date"] = pd.to_datetime(
    fact["order_purchase_timestamp"]
).dt.date

dates["full_date"] = pd.to_datetime(
    dates["full_date"]
).dt.date

fact = fact.merge(
    dates,
    on="full_date",
    how="left"
)

fact_sales = fact[[
    "order_id",
    "customer_key",
    "product_key",
    "seller_key",
    "date_key",
    "region_key",
    "price",
    "freight_value",
    "payment_value",
    "review_score"
]]

fact_sales.to_sql(
    "fact_sales",
    engine,
    schema="retail",
    if_exists="append",
    index=False,
    chunksize=5000
)

print("Fact Sales Loaded")
print("Rows:", len(fact_sales))