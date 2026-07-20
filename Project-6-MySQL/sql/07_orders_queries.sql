-- ==================================================
-- Project 6 - MySQL
-- Lesson 7 : Orders Queries
-- ==================================================

-- Objective:
-- Practice SQL queries using the Orders dataset.

USE ai_data_platform;

-- ==================================================
-- Query 1
-- Display all orders
-- ==================================================

SELECT *
FROM orders;

-- ==================================================
-- Query 2
-- Display Order Numbers
-- ==================================================

SELECT `Order Number`
FROM orders;

-- ==================================================
-- Query 3
-- Count the total number of orders
-- ==================================================

SELECT COUNT(*) AS total_orders
FROM orders;

-- ==================================================
-- Query 4
-- Display the table structure
-- ==================================================

DESCRIBE orders;

-- ==================================================
-- Query 5
-- Display all column names
-- ==================================================

SHOW COLUMNS FROM orders;

-- ==================================================
-- Query 6
-- Display Order Number and Quantity
-- ==================================================

SELECT `Order Number`, Quantity
FROM orders;

-- ==================================================
-- Query 7
-- Display unique Currency Codes
-- ==================================================

SELECT DISTINCT `Currency Code`
FROM orders;

-- ==================================================
-- Query 8
-- Count unique Currency Codes
-- ==================================================

SELECT COUNT(DISTINCT `Currency Code`) AS total_currency_codes
FROM orders;

-- ==================================================
-- Query 9
-- Display orders with Quantity greater than 5
-- ==================================================

SELECT *
FROM orders
WHERE Quantity > 5;

-- ==================================================
-- Query 10
-- Display orders sorted by Quantity
-- ==================================================

SELECT `Order Number`, Quantity
FROM orders
ORDER BY Quantity DESC;

-- ==================================================
-- Query 11
-- Display Order Number and Order Date
-- ==================================================

SELECT `Order Number`, `Order Date`
FROM orders;

-- ==================================================
-- Query 12
-- Display Order Number and Delivery Date
-- ==================================================

SELECT `Order Number`, `Delivery Date`
FROM orders;