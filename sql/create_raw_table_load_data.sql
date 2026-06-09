CREATE OR REPLACE TABLE CUSTOMER_DATA (
    customerID STRING,
    gender STRING,
    SeniorCitizen INTEGER,
    Partner STRING,
    Dependents STRING,
    tenure INTEGER,
    PhoneService STRING,
    MultipleLines STRING,
    InternetService STRING,
    OnlineSecurity STRING,
    OnlineBackup STRING,
    DeviceProtection STRING,
    TechSupport STRING,
    StreamingTV STRING,
    StreamingMovies STRING,
    Contract STRING,
    PaperlessBilling STRING,
    PaymentMethod STRING,
    MonthlyCharges FLOAT,
    TotalCharges STRING,
    Churn STRING
);

copy into customer_data
from @churn_stage
file_format =(format_name=csv_format);