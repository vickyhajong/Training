SELECT * FROM SYSTEM.customers;
SELECT * FROM SYSTEM.products;
SELECT * FROM SYSTEM.categories;
SELECT * FROM SYSTEM.orders;
SELECT * FROM SYSTEM.order_details;
SELECT * FROM SYSTEM.employees;
--1. PROJECTION
-- what to extract from the table
SELECT CUSTOMER_ID, COMPANY_NAME, CONTACT_NAME
FROM SYSTEM.customers;

-- * -> DB replaces the * from all the colum names
--literal coloumns
SELECT 'The customer', COMPANY_NAME, 'IS LOCATED IN', city
FROM SYSTEM.customers;

-- Column name alias - alternate name in the output
SELECT CUSTOMER_ID AS CustId, COMPANY_NAME as "Company Name",
CITY, COUNTRY
FROM SYSTEM.customers;
-- Derived Columns are supported - combining 2 or more coulmns in the output--
SELECT CUSTOMER_CODE AS "Cust_Code",
	CITY || ', ' || COUNTRY AS "Location"
FROM SYSTEM.customers;
--another way
SELECT PRODUCT_ID, PRODUCT_NAME, UNIT_PRICE,UNITS_IN_STOCK,
(UNIT_PRICE * UNITS_IN_STOCK) AS StockValue
FROM SYSTEM.products;



