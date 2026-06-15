import pandas as pd
from pathlib import Path
from src.utils.logger import logger

RAW_PATH = Path("data/raw")

def load_csv(file_name):
    try:
        file_path = RAW_PATH / file_name

        df = pd.read_csv(file_path)

        logger.info(f"{file_name} loaded successfully")

        print(
            f"{file_name} | Rows: {df.shape[0]} | Columns: {df.shape[1]}"
        )

        return df

    except Exception as e:
        logger.error(
            f"Error loading {file_name}: {e}"
        )
        raise

if __name__ == "__main__":

    datasets = [
        "olist_customers_dataset.csv",
        "olist_orders_dataset.csv",
        "olist_order_items_dataset.csv",
        "olist_order_payments_dataset.csv",
        "olist_order_reviews_dataset.csv",
        "olist_products_dataset.csv",
        "olist_sellers_dataset.csv",
        "olist_geolocation_dataset.csv"
    ]

    for file in datasets:
        load_csv(file)