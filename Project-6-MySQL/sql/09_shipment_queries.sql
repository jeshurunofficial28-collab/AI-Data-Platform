-- ==================================================
-- Project 6 - MySQL
-- Lesson 9 : Shipment Queries
-- ==================================================

-- Objective:
-- Practice SQL queries using the Shipment dataset.

USE ai_data_platform;

-- ==================================================
-- Query 1
-- Display all shipment records
-- ==================================================

SELECT *
FROM shipment;

-- ==================================================
-- Query 2
-- Display Shipment IDs
-- ==================================================

SELECT ID
FROM shipment;

-- ==================================================
-- Query 3
-- Count total shipments
-- ==================================================

SELECT COUNT(*) AS total_shipments
FROM shipment;

-- ==================================================
-- Query 4
-- Display the table structure
-- ==================================================

DESCRIBE shipment;

-- ==================================================
-- Query 5
-- Display all column names
-- ==================================================

SHOW COLUMNS FROM shipment;

-- ==================================================
-- Query 6
-- Display Country and Vendor
-- ==================================================

SELECT Country, Vendor
FROM shipment;

-- ==================================================
-- Query 7
-- Display unique shipment modes
-- ==================================================

SELECT DISTINCT `Shipment Mode`
FROM shipment;

-- ==================================================
-- Query 8
-- Display unique product groups
-- ==================================================

SELECT DISTINCT `Product Group`
FROM shipment;

-- ==================================================
-- Query 9
-- Display shipments with Line Item Value greater than 100000
-- ==================================================

SELECT ID, `Line Item Value`
FROM shipment
WHERE `Line Item Value` > 100000;

-- ==================================================
-- Query 10
-- Display shipments ordered by Line Item Value
-- ==================================================

SELECT ID, `Line Item Value`
FROM shipment
ORDER BY `Line Item Value` DESC;

-- ==================================================
-- Query 11
-- Display Vendor and Country
-- ==================================================

SELECT Vendor, Country
FROM shipment;

-- ==================================================
-- Query 12
-- Display Product Group and Shipment Mode
-- ==================================================

SELECT `Product Group`, `Shipment Mode`
FROM shipment;