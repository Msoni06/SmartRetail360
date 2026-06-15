import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw")
CLEAN_PATH = Path("data/cleaned")

CLEAN_PATH.mkdir(
    parents=True,
    exist_ok=True
)

FILES = [
    "olist_customers_dataset.csv",
    "olist_orders_dataset.csv",
    "olist_order_items_dataset.csv",
    "olist_order_payments_dataset.csv",
    "olist_order_reviews_dataset.csv",
    "olist_products_dataset.csv",
    "olist_sellers_dataset.csv"
]

for file in FILES:

    print(f"\nProcessing {file}")

    df = pd.read_csv(
        RAW_PATH / file
    )

    rows_before = len(df)

    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
    )

    df = df.drop_duplicates()

    rows_after = len(df)

    print(
        f"Removed {rows_before - rows_after} duplicates"
    )

    output_file = (
        CLEAN_PATH / file
    )

    df.to_csv(
        output_file,
        index=False
    )

    print(
        f"Saved -> {output_file}"
    )

print("\nCleaning Complete")