-- ==================================================
-- Project 6 - MySQL
-- Lesson 5 : Product Queries
-- ==================================================

-- Objective:
-- Practice SQL queries using the Products dataset.

USE ai_data_platform;

-- ==================================================
-- Query 1
-- Display all products
-- ==================================================

SELECT *
FROM products;

-- ==================================================
-- Query 2
-- Display product names
-- ==================================================

SELECT `Product Name`
FROM products;

-- ==================================================
-- Query 3
-- Count the total number of products
-- ==================================================

SELECT COUNT(*) AS total_products
FROM products;

-- ==================================================
-- Query 4
-- Display the table structure
-- ==================================================

DESCRIBE products;

-- ==================================================
-- Query 5
-- Display all column names
-- ==================================================

SHOW COLUMNS FROM products;

-- ==================================================
-- Query 6
-- Display product name and brand
-- ==================================================

SELECT `Product Name`, Brand
FROM products;

-- ==================================================
-- Query 7
-- Display all unique brands
-- ==================================================

SELECT DISTINCT Brand
FROM products;

-- ==================================================
-- Query 8
-- Display all unique categories
-- ==================================================

SELECT DISTINCT Category
FROM products;

-- ==================================================
-- Query 9
-- Display products with Unit Price greater than 100
-- ==================================================

SELECT `Product Name`, `Unit Price USD`
FROM products
WHERE `Unit Price USD` > 100;

-- ==================================================
-- Query 10
-- Display products ordered by Unit Price
-- ==================================================

SELECT `Product Name`, `Unit Price USD`
FROM products
ORDER BY `Unit Price USD` DESC;

-- ==================================================
-- Query 11
-- Display products ordered by Brand
-- ==================================================

SELECT `Product Name`, Brand
FROM products
ORDER BY Brand ASC;

-- ==================================================
-- Query 12
-- Display products ordered by Category
-- ==================================================

SELECT `Product Name`, Category
FROM products
ORDER BY Category ASC;