-- ==================================================
-- Project 6 - MySQL
-- Lesson 8 : Import Shipment Dataset
-- ==================================================

-- Objective:
-- Import the Shipment dataset into the ai_data_platform database.

USE ai_data_platform;

-- Dataset:
-- Shipment_Cleaned.csv

-- Table Name:
-- shipment

-- Note:
-- The Shipment dataset will be imported using the
-- MySQL Workbench Table Data Import Wizard.

-- ==================================================
-- Rename imported table (if MySQL creates it as
-- shipment_cleaned instead of shipment)
-- ==================================================

RENAME TABLE shipment_cleaned TO shipment;

DESCRIBE shipment;