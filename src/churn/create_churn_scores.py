import pandas as pd
import joblib

df = pd.read_csv(
    "data/feature_store/customer_features.csv"
)

model = joblib.load(
    "models/churn_model.pkl"
)

X = df[
    [
        "total_orders",
        "total_spent",
        "avg_order_value"
    ]
]

df["churn_probability"] = (
    model.predict_proba(X)[:,1]
)

df.to_csv(
    "data/feature_store/churn_scores.csv",
    index=False
)

print(df[
    [
        "customer_unique_id",
        "churn_probability"
    ]
].head())