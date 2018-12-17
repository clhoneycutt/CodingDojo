-- SELECT * FROM billing;
-- SELECT * FROM clients;
-- SELECT * FROM leads;
-- SELECT * FROM sites;

-- SELECT CONCAT(clients.first_name, ' ', clients.last_name) as client_name, billing.amount, billing.charged_datetime
-- FROM clients
-- JOIN billing ON clients.id = billing.clients_id;

-- SELECT CONCAT(leads.first_name, ' ', leads.last_name) AS lead_name, sites.domain_name
-- FROM sites
-- JOIN leads ON sites.id = leads.sites_id;

-- SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, sites.domain_name, leads.first_name
-- FROM clients
-- JOIN sites ON clients.id = sites.clients_id
-- JOIN leads ON sites.id = leads.sites_id;

-- SELECT CONCAT(clients.first_name, ' ', clients.last_name) as client_name, sites.domain_name
-- FROM clients
-- LEFT JOIN sites ON clients.id = sites.clients_id;

-- SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, GROUP_CONCAT(sites.domain_name) AS domains
-- FROM clients
-- JOIN sites ON clients.id = sites.clients_id
-- GROUP BY clients.id;

