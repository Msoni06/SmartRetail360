import pandas as pd
from sqlalchemy import create_engine
from src.config.db_config import DB_CONFIG

engine = create_engine(
    f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
)

print("Starting warehouse load...")

# =========================
# DIM CUSTOMER
# =========================

customers = pd.read_csv(
    "data/cleaned/olist_customers_dataset.csv"
)[[
    "customer_id",
    "customer_unique_id",
    "customer_city",
    "customer_state"
]]

customers.to_sql(
    "dim_customer",
    engine,
    schema="retail",
    if_exists="append",
    index=False
)

print(f"dim_customer loaded: {len(customers)}")

# =========================
# DIM PRODUCT
# =========================

products = pd.read_csv(
    "data/cleaned/olist_products_dataset.csv"
)[[
    "product_id",
    "product_category_name",
    "product_weight_g",
    "product_length_cm",
    "product_height_cm",
    "product_width_cm"
]]

products.to_sql(
    "dim_product",
    engine,
    schema="retail",
    if_exists="append",
    index=False
)

print(f"dim_product loaded: {len(products)}")

# =========================
# DIM SELLER
# =========================

sellers = pd.read_csv(
    "data/cleaned/olist_sellers_dataset.csv"
)[[
    "seller_id",
    "seller_city",
    "seller_state"
]]

sellers.to_sql(
    "dim_seller",
    engine,
    schema="retail",
    if_exists="append",
    index=False
)

print(f"dim_seller loaded: {len(sellers)}")

# =========================
# DIM REGION
# =========================

regions = pd.DataFrame({
    "state_code":
    customers["customer_state"].dropna().unique()
})

regions.to_sql(
    "dim_region",
    engine,
    schema="retail",
    if_exists="append",
    index=False
)

print(f"dim_region loaded: {len(regions)}")

# =========================
# DIM DATE
# =========================

dates = pd.read_csv(
    "data/processed/dim_date.csv"
)

dates.to_sql(
    "dim_date",
    engine,
    schema="retail",
    if_exists="append",
    index=False
)

print(f"dim_date loaded: {len(dates)}")

print("Warehouse dimension loading completed successfully")