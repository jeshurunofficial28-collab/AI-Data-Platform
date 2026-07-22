-- ==================================================
-- Project 6 - MySQL
-- Lesson 3 : Customer Queries
-- ==================================================

-- Objective:
-- Practice SQL queries using the Customers dataset.

USE ai_data_platform;

-- ==================================================
-- Query 1
-- Display all customer records
-- ==================================================

SELECT *
FROM customers;

-- ==================================================
-- Query 2
-- Display customer names only
-- ==================================================

SELECT full_name
FROM customers;

-- ==================================================
-- Query 3
-- Count the total number of customers
-- ==================================================

SELECT COUNT(*) AS total_customers
FROM customers;

-- ==================================================
-- Query 4
-- Display the table structure
-- ==================================================

DESCRIBE customers;

-- ==================================================
-- Query 5
-- Display all column names
-- ==================================================

SHOW COLUMNS FROM customers;

-- ==================================================
-- Query 6
-- Display customer name and state
-- ==================================================

SELECT full_name, state
FROM customers;

-- ==================================================
-- Query 7
-- Display all unique states
-- ==================================================

SELECT DISTINCT state
FROM customers;

-- ==================================================
-- Query 8
-- Count the number of unique states
-- ==================================================

SELECT COUNT(DISTINCT state) AS total_states
FROM customers;

-- ==================================================
-- Query 9
-- Display customers older than 30
-- ==================================================

SELECT *
FROM customers
WHERE age > 30;

-- ==================================================
-- Query 10
-- Display all female customers
-- ==================================================

SELECT *
FROM customers
WHERE gender = 'Female';

-- ==================================================
-- Query 11
-- Display all male customers
-- ==================================================

SELECT *
FROM customers
WHERE gender = 'Male';

-- ==================================================
-- Query 12
-- Display customers ordered by age
-- ==================================================

SELECT full_name, age
FROM customers
ORDER BY age ASC;