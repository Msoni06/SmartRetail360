import pandas as pd

print("Loading customer feature store...")

df = pd.read_csv(
    "data/feature_store/customer_features.csv"
)

# --------------------------------
# Estimated CLV
# --------------------------------

df["estimated_clv"] = (
    df["avg_order_value"]
    * df["total_orders"]
)

# --------------------------------
# Customer Tier
# --------------------------------

df["clv_tier"] = pd.qcut(
    df["estimated_clv"],
    4,
    labels=[
        "Low Value",
        "Medium Value",
        "High Value",
        "VIP"
    ]
)

# --------------------------------
# Save
# --------------------------------

df.to_csv(
    "data/feature_store/customer_clv.csv",
    index=False
)

print("\nCLV Dataset Created")

print(
    df["clv_tier"]
    .value_counts()
)

print(
    "\nTop 10 Customers:"
)

print(
    df.sort_values(
        "estimated_clv",
        ascending=False
    )[
        [
            "customer_unique_id",
            "estimated_clv",
            "clv_tier"
        ]
    ].head(10)
)