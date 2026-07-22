-- ==================================================
-- Project 6 - MySQL
-- Lesson 11 : Amazon Queries
-- ==================================================

-- Objective:
-- Practice SQL queries using the Amazon Delivery dataset.

USE ai_data_platform;

-- ==================================================
-- Query 1
-- Display all delivery records
-- ==================================================

SELECT *
FROM amazon;

-- ==================================================
-- Query 2
-- Display Order IDs
-- ==================================================

SELECT Order_ID
FROM amazon;

-- ==================================================
-- Query 3
-- Count total deliveries
-- ==================================================

SELECT COUNT(*) AS total_deliveries
FROM amazon;

-- ==================================================
-- Query 4
-- Display the table structure
-- ==================================================

DESCRIBE amazon;

-- ==================================================
-- Query 5
-- Display all column names
-- ==================================================

SHOW COLUMNS FROM amazon;

-- ==================================================
-- Query 6
-- Display Agent Age and Agent Rating
-- ==================================================

SELECT Agent_Age, Agent_Rating
FROM amazon;

-- ==================================================
-- Query 7
-- Display unique Weather conditions
-- ==================================================

SELECT DISTINCT Weather
FROM amazon;

-- ==================================================
-- Query 8
-- Display unique Vehicle types
-- ==================================================

SELECT DISTINCT Vehicle
FROM amazon;

-- ==================================================
-- Query 9
-- Display deliveries taking more than 30 minutes
-- ==================================================

SELECT Order_ID, Delivery_Time
FROM amazon
WHERE Delivery_Time > 30;

-- ==================================================
-- Query 10
-- Display deliveries ordered by Delivery Time
-- ==================================================

SELECT Order_ID, Delivery_Time
FROM amazon
ORDER BY Delivery_Time DESC;

-- ==================================================
-- Query 11
-- Display Weather and Traffic
-- ==================================================

SELECT Weather, Traffic
FROM amazon;

-- ==================================================
-- Query 12
-- Display Area and Category
-- ==================================================

SELECT Area, Category
FROM amazon;