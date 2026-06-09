import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)
from src.utils.snowflake_connection import get_connection
from sklearn.metrics import roc_auc_score
import joblib
import os

os.makedirs('models',exist_ok=True)

# Load data
conn = get_connection()

query = """
select *
from customer_features
"""

df = pd.read_sql(query, conn)
df.columns = df.columns.str.lower()
print(df.columns.tolist())

# Drop customer id
df = df.drop(columns=['customerid'])

# Convert target
df['churn'] = df['churn'].astype(str).str.strip()
print(df['churn'].unique())

# --- FIX: chain .astype(int) so dtype is int64, not object ---
# After astype(str), .replace() stores 0/1 as Python objects inside
# a string-backed array. sklearn sees dtype=object and raises
# "Unknown label type: unknown". Casting to int resolves it.
df['churn'] = df['churn'].replace({
    "No": 0,
    "Yes": 1
}).astype(int)

print(df['churn'].value_counts(dropna=False))
print(df['churn'].isna().sum())
print(df['churn'].dtype)   # should print int64

# Separate features and target BEFORE one-hot encoding
X = df.drop('churn', axis=1)
Y = df['churn']

# One-hot encode categorical columns (only on X)
X = pd.get_dummies(X, drop_first=True)

# Train/test split
X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, Y_train)

# Prediction
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:,1]

print("Accuracy:")
print(accuracy_score(Y_test, y_pred))

print("\nROC AUC Score:")
print(roc_auc_score(Y_test, y_prob))

print("\nConfusion Matrix:")
print(confusion_matrix(Y_test, y_pred))

print("\nClassification Report:")
print(classification_report(Y_test, y_pred))

#feature importance
feature_importance = pd.DataFrame({
    "feature":X.columns,
    "importance": model.feature_importances_
})

feature_importance = feature_importance.sort_values(
    by="importance",
    ascending=False
)

print(feature_importance.head(15))

#save model
joblib.dump(
    model,
    'models/churn_model.pkl'
)
