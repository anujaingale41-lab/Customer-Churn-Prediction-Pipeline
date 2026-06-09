use database churn_project;
use schema analytics;

create or replace table customer_features as 
select customerid,
       gender,
       seniorcitizen,
       partner,
       dependents,
       tenure,
       case 
         when tenure <12 then 'New Customer'
         when tenure < 24 then 'Growing Customer'
         else 'Loyal Customer'
       end as tenure_group,
       monthlycharges,
       case 
         when monthlycharges <35 then 'Low Value'
         when monthlycharges <70 then 'Medium Value'
         else 'High Value'
       end as revenue_segment,
       try_to_number(nullif(trim(totalcharges),'')) as totalcharges,
       contract,
       case 
         when contract = 'Month-to-month' then 1
         else 0
      end as contract_risk,
      internetservice,
      paymentmethod,
      churn
from churn_project.raw.customer_data;


select * from customer_features 
limit 20;

--tenure group
select tenure_group,count(*) as customers
from customer_features
group by tenure_group;

--revenue segments
select revenue_segment, count(*) as customers
from customer_features
group by revenue_segment;

--contract risk
select contract_risk,count(*) as customers
from customer_features
group by contract_risk;

select contract_risk,churn,count(*) as customers
from customer_features
group by contract_risk,churn
order by contract_risk;

select current_user();
select current_account();