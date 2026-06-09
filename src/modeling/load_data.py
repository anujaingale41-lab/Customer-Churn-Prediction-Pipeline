import pandas as pd
from src.utils.snowflake_connection import get_connection

query=""" select * 
from customer_features
"""

conn= get_connection()

df=pd.read_sql(query,conn)

print("Dataset shape:" ,df.shape)
print("Dataset columns:" ,df.columns)
print("First 5 rows:",df.head(5))