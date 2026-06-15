import pandas as pd

print("Loading customer feature store...")

df = pd.read_csv(
    "data/feature_store/customer_features.csv"
)

# ----------------------------
# RFM Metrics
# ----------------------------

df["R"] = pd.qcut(
    df["days_since_last_purchase"],
    5,
    labels=[5,4,3,2,1]
)

df["F"] = pd.qcut(
    df["total_orders"].rank(method="first"),
    5,
    labels=[1,2,3,4,5]
)

df["M"] = pd.qcut(
    df["total_spent"],
    5,
    labels=[1,2,3,4,5]
)

# ----------------------------
# RFM Score
# ----------------------------

df["rfm_score"] = (
    df["R"].astype(str)
    + df["F"].astype(str)
    + df["M"].astype(str)
)

# ----------------------------
# Segments
# ----------------------------

def segment_customer(row):

    r = int(row["R"])
    f = int(row["F"])

    if r >= 4 and f >= 4:
        return "Champions"

    elif r >= 3 and f >= 3:
        return "Loyal Customers"

    elif r >= 4:
        return "Potential Loyalists"

    elif r <= 2 and f >= 3:
        return "At Risk"

    else:
        return "Lost Customers"

df["segment"] = df.apply(
    segment_customer,
    axis=1
)

# ----------------------------
# Save
# ----------------------------

df.to_csv(
    "data/feature_store/rfm_segments.csv",
    index=False
)

print("\nRFM Segmentation Complete")

print(
    df["segment"]
    .value_counts()
)