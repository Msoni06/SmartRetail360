import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)
from xgboost import XGBClassifier
import joblib

print("Loading customer features...")

df = pd.read_csv(
    "data/feature_store/customer_features.csv"
)

# -------------------------
# Create Churn Label
# -------------------------

df["churn"] = (
    df["days_since_last_purchase"] > 180
).astype(int)

# -------------------------
# Features
# -------------------------

X = df[
    [
        "total_orders",
        "total_spent",
        "avg_order_value"
    ]
]

y = df["churn"]

# -------------------------
# Train/Test Split
# -------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# -------------------------
# Model
# -------------------------

model = XGBClassifier(
    n_estimators=100,
    max_depth=4,
    learning_rate=0.1,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

# -------------------------
# Predictions
# -------------------------

preds = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    preds
)

print(
    f"\nAccuracy: {accuracy:.4f}"
)

print(
    "\nClassification Report:"
)

print(
    classification_report(
        y_test,
        preds
    )
)

# -------------------------
# Save Model
# -------------------------

joblib.dump(
    model,
    "models/churn_model.pkl"
)

print(
    "\nModel saved successfully"
)