use database churn_project;
use schema analytics;

create or replace table churn_predictions(
    customer_id string,
    churn_probability float,
    predicted_churn integer
);

create or replace stage prediction_stage;

CHURN_PROJECT.ANALYTICS.PREDICTION_STAGECHURN_PROJECT.ANALYTICS.PREDICTION_STAGECHURN_PROJECT.ANALYTICS.PREDICTION_STAGE
list @prediction_stage;

create or replace file format predictions_csv_format
type = csv
skip_header = 1
field_optionally_enclosed_by = '"';


truncate table churn_predictions;

copy into churn_predictions
from @prediction_stage/churn_predictions.csv
file_format = (format_name = predictions_csv_format);

select * from churn_predictions
limit 10;