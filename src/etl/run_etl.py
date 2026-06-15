from src.etl.extract import load_csv
from src.etl.transform import (
    standardize_columns,
    remove_duplicates,
    missing_value_report
)

customers = load_csv(
    "olist_customers_dataset.csv"
)

customers = standardize_columns(
    customers
)

customers = remove_duplicates(
    customers
)

print(
    missing_value_report(customers)
)