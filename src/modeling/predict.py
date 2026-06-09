import pandas as pd
import joblib

from src.utils.snowflake_connection import get_connection
import os

# Connect to Snowflake
conn = get_connection()

query = """
SELECT *
FROM CUSTOMER_FEATURES
"""

df = pd.read_sql(query, conn)

# CUSTOMERID exists in CUSTOMER_FEATURES
customer_ids = df['CUSTOMERID'].values

# Convert column names to lowercase
df.columns = df.columns.str.lower()

# Remove id column
df = df.drop(columns=['customerid'])

# Remove target column
df = df.drop(columns=['churn'], errors='ignore')

# Handle null values
df['totalcharges'] = df['totalcharges'].fillna(0)

# Create dummy variables
df = pd.get_dummies(df, drop_first=True)

# Features
X = df

# Load model
model = joblib.load('models/churn_model.pkl')

# Match training columns
model_features = model.feature_names_in_

X = X.reindex(
    columns=model_features,
    fill_value=0
)

# Predictions
probabilities = model.predict_proba(X)[:, 1]
predictions = model.predict(X)

print(X.shape)
print(len(customer_ids))

# Prediction dataframe
prediction_df = pd.DataFrame({
    'customerid': customer_ids,
    'churn_probability': probabilities,
    'predicted_churn': predictions
})

print(prediction_df.head())

# Upload to Snowflake
cursor = conn.cursor()

cursor.execute("""
TRUNCATE TABLE CHURN_PREDICTIONS
""")

#save predictions 
os.makedirs('data/predictions',exist_ok=True)

prediction_df.to_csv(
    'data/predictions/churn_predictions.csv', 
    index=False)

print("predcitions saved successfully")
print(prediction_df.shape)
