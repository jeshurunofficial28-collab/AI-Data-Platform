-- ==================================================
-- Project 6 - MySQL
-- Lesson 6 : Import Orders Dataset
-- ==================================================

-- Objective:
-- Import the Orders dataset into the ai_data_platform database.

USE ai_data_platform;

-- Dataset:
-- Sales_Cleaned.csv

-- Table Name:
-- orders

-- Note:
-- The Orders dataset will be imported using the
-- MySQL Workbench Table Data Import Wizard.

-- ==================================================
-- Rename imported table (if MySQL creates it as
-- sales_cleaned instead of orders)
-- ==================================================

RENAME TABLE sales_cleaned TO orders;

-- ==================================================
-- Project 6 - MySQL
-- Lesson 6 : Import Orders Dataset
-- ==================================================

-- Objective:
-- Import the Orders dataset into the ai_data_platform database.

USE ai_data_platform;

-- Dataset:
-- Sales_Cleaned.csv

-- Table Name:
-- orders

-- Note:
-- The Orders dataset will be imported using the
-- MySQL Workbench Table Data Import Wizard.

-- ==================================================
-- Rename imported table (if MySQL creates it as
-- sales_cleaned instead of orders)
-- ==================================================

RENAME TABLE sales_cleaned TO orders;

DESCRIBE orders;