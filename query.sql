insert {dataset}.{table} (customer, score_type, status, score_month) VALUES('Rohith Bheemreddy', 'P', 'active', 2);
select * from {dataset}.{table} where customer like '%Rohith%';
