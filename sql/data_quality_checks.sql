select count(*) from customer_data;

select * from customer_data 
limit 10;

--check churn distribution
select churn , count(*) as customer_count,
       round(count(*)*100/sum(count(*))over(),2) as percentage
from customer_data
group by churn;

--check missing values
select count(*) from customer_data
where trim(totalcharges)='';

--contract type analysis
select contract,count(*) as customers
from customer_data
group by contract
order by customers desc;

--average monthly charges
select round(avg(monthlycharges),2) as avg_monthly_charges
from customer_data;

--churn by contract type
select contract , churn, count(*) as cutomers
from customer_data
group by contract,churn
order by contract;
