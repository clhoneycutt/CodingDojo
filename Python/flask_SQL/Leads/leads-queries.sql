
-- INSERT INTO users (first_name, last_name, email, pw_hash, created_at)
-- VALUES ("Wes", "H", "wharper@codingdojo.com", "password", NOW());

-- INSERT INTO leads (customer_id, name,  created_at)
-- VALUES(3, "OhioHealth", "2015-06-13 00:00:00");

-- INSERT INTO leads (customer_id, name,  created_at)
-- VALUES(3, "Microsoft", "2015-08-17 00:00:00");

-- INSERT INTO leads (customer_id, name,  created_at)
-- VALUES(3, "Zoolilly", "2015-06-13 00:00:00");

-- INSERT INTO leads (customer_id, name,  created_at)
-- VALUES(1, "Chuck Norris", "2015-08-17 00:00:00");

-- INSERT INTO leads (customer_id, name,  created_at)
-- VALUES(4, "Miramax", "2015-06-13 00:00:00");

-- INSERT INTO leads (customer_id, name,  created_at)
-- VALUES(4, "Universal Studios", "2015-08-17 00:00:00"); 


SELECT CONCAT(customers.first_name, ' ', customers.last_name) AS cust_name, customers.created_at AS cust_created, COUNT(DISTINCT leads.id) AS num_leads
FROM customers
LEFT JOIN leads ON customers.id = leads.customer_id
GROUP BY customers.id
;

