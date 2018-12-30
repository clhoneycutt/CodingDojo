
-- ### Primary query on pageload.
-- SELECT CONCAT(customers.first_name, ' ', customers.last_name) AS cust_name, customers.created_at AS cust_created, COUNT(DISTINCT leads.id) AS num_leads
-- FROM customers
-- LEFT JOIN leads ON customers.id = leads.customer_id
-- GROUP BY customers.id
-- ;

-- ### Query for Date Range Finder
-- SELECT CONCAT(customers.first_name, ' ', customers.last_name) AS cust_name, customers.created_at AS cust_created, COUNT(DISTINCT leads.id) AS num_leads
-- FROM customers
-- LEFT JOIN leads ON customers.id = leads.customer_id
-- WHERE leads.created_at BETWEEN '2015-06-01 00:00:00' and '2015-06-31 23:59:00'
-- GROUP BY customers.id;


-- ### Query for all data
-- SELECT * FROM customers
-- LEFT JOIN leads on customers.id = leads.customer_id;

