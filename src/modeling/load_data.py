import pandas as pd
from src.utils.snowflake_connection import get_connection

query=""" select * 
from customer_features
"""

conn= get_connection()

df=pd.read_sql(query,conn)

df.to_csv(
    'data/predictions/customer_features.csv',
    index=False
)

print("Dataset shape:", df.shape)