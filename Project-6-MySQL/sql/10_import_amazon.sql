-- ==================================================
-- Project 6 - MySQL
-- Lesson 10 : Import Amazon Dataset
-- ==================================================

-- Objective:
-- Import the Amazon Delivery dataset into the
-- ai_data_platform database.

USE ai_data_platform;

-- Dataset:
-- amazon_delivery_cleaned.csv

-- Table Name:
-- amazon

-- Note:
-- The Amazon Delivery dataset will be imported using
-- the MySQL Workbench Table Data Import Wizard.

-- ==================================================
-- Rename imported table (if MySQL creates it as
-- amazon_delivery_cleaned instead of amazon)
-- ==================================================

RENAME TABLE amazon_delivery_cleaned TO amazon;

DESCRIBE amazon;