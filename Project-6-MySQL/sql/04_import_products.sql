-- ==================================================
-- Project 6 - MySQL
-- Lesson 4 : Import Products Dataset
-- ==================================================

-- Objective:
-- Import the Products dataset into the ai_data_platform database.

USE ai_data_platform;

-- Dataset:
-- Products_Cleaned.csv

-- Table Name:
-- products

-- Note:
-- The Products dataset will be imported using the
-- MySQL Workbench Table Data Import Wizard.
RENAME TABLE products_cleaned TO products;