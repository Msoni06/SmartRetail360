import pandas as pd

customers = pd.read_csv(
    "data/raw/olist_customers_dataset.csv"
)

print("\nDataset Shape:")
print(customers.shape)

print("\nColumns:")
print(customers.columns.tolist())

print("\nMissing Values:")
print(customers.isnull().sum())

print("\nData Types:")
print(customers.dtypes)