CREATE STAGE CHURN_STAGE;

list @churn_stage;

use database churn_project;
use schema raw;
create or replace file format csv_format
type=csv
field_optionally_enclosed_by='"'
skip_header = 1;