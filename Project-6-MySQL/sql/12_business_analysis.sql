-- ==================================================
-- Query 1
-- Customer Distribution by Gender
-- ==================================================

USE ai_data_platform;
SELECT
    gender,
    COUNT(*) AS total_customers
FROM customers
GROUP BY gender
ORDER BY total_customers DESC;

-- ==================================================
-- Query 2
-- Top 10 States by Customer Count
-- ==================================================

SELECT
    state,
    COUNT(*) AS total_customers
FROM customers
GROUP BY state
ORDER BY total_customers DESC
LIMIT 10;

-- ==================================================
-- Query 3
-- Average Customer Age
-- ==================================================

SELECT
    ROUND(AVG(age), 2) AS average_customer_age
FROM customers;

-- ==================================================
-- Query 4
-- Preferred Customer Registration Channel
-- ==================================================

SELECT
    preferred_channel,
    COUNT(*) AS total_customers
FROM customers
GROUP BY preferred_channel
ORDER BY total_customers DESC;

-- ==================================================
-- Query 5
-- Product Distribution by Category
-- ==================================================

SELECT
    Category,
    COUNT(*) AS total_products
FROM products
GROUP BY Category
ORDER BY total_products DESC;

-- ==================================================
-- Query 6
-- Top 10 Most Expensive Products
-- ==================================================

SELECT
    `Product Name`,
    Brand,
    Category,
    `Unit Price USD`
FROM products
ORDER BY `Unit Price USD` DESC
LIMIT 10;

-- ==================================================
-- Query 7
-- Average Product Price by Category
-- ==================================================

SELECT
    Category,
    ROUND(AVG(`Unit Price USD`), 2) AS average_price
FROM products
GROUP BY Category
ORDER BY average_price DESC;

-- ==================================================
-- Query 8
-- Top 10 Brands by Number of Products
-- ==================================================

SELECT
    Brand,
    COUNT(*) AS total_products
FROM products
GROUP BY Brand
ORDER BY total_products DESC
LIMIT 10;

-- ==================================================
-- Query 9
-- Orders by Currency
-- ==================================================

SELECT
    `Currency Code`,
    COUNT(*) AS total_orders
FROM orders
GROUP BY `Currency Code`
ORDER BY total_orders DESC;

-- ==================================================
-- Query 10
-- Average Quantity Sold per Currency
-- ==================================================

SELECT
    `Currency Code`,
    ROUND(AVG(Quantity), 2) AS average_quantity
FROM orders
GROUP BY `Currency Code`
ORDER BY average_quantity DESC;

-- ==================================================
-- Query 11
-- Top 10 Highest Quantity Orders
-- ==================================================

SELECT
    `Order Number`,
    Quantity,
    `Currency Code`
FROM orders
ORDER BY Quantity DESC
LIMIT 10;

-- ==================================================
-- Query 12
-- Total Quantity Sold by Order Date
-- ==================================================

SELECT
    `Order Date`,
    SUM(Quantity) AS total_quantity
FROM orders
GROUP BY `Order Date`
ORDER BY total_quantity DESC;

-- ==================================================
-- Query 13
-- Shipment Distribution by Country
-- ==================================================

SELECT
    Country,
    COUNT(*) AS total_shipments
FROM shipment
GROUP BY Country
ORDER BY total_shipments DESC
LIMIT 10; 

-- ==================================================
-- Query 14
-- Shipment Distribution by Shipment Mode
-- ==================================================

SELECT
    `Shipment Mode`,
    COUNT(*) AS total_shipments
FROM shipment
GROUP BY `Shipment Mode`
ORDER BY total_shipments DESC;

-- ==================================================
-- Query 15
-- Top 10 Vendors by Shipment Count
-- ==================================================

SELECT
    Vendor,
    COUNT(*) AS total_shipments
FROM shipment
GROUP BY Vendor
ORDER BY total_shipments DESC
LIMIT 10;

-- ==================================================
-- Query 16
-- Average Freight Cost by Shipment Mode
-- ==================================================

SELECT
    `Shipment Mode`,
    ROUND(AVG(`Freight Cost (USD)`), 2) AS average_freight_cost
FROM shipment
GROUP BY `Shipment Mode`
ORDER BY average_freight_cost DESC;

-- ==================================================
-- Query 17
-- Average Delivery Time by Weather
-- ==================================================

SELECT
    Weather,
    ROUND(AVG(Delivery_Time), 2) AS average_delivery_time
FROM amazon
GROUP BY Weather
ORDER BY average_delivery_time DESC;

-- ==================================================
-- Query 18
-- Average Delivery Time by Traffic Condition
-- ==================================================

SELECT
    Traffic,
    ROUND(AVG(Delivery_Time), 2) AS average_delivery_time
FROM amazon
GROUP BY Traffic
ORDER BY average_delivery_time DESC;

-- ==================================================
-- Query 19
-- Average Delivery Time by Vehicle Type
-- ==================================================

SELECT
    Vehicle,
    ROUND(AVG(Delivery_Time), 2) AS average_delivery_time
FROM amazon
GROUP BY Vehicle
ORDER BY average_delivery_time ASC;

-- ==================================================
-- Query 20
-- Average Delivery Time by Area
-- ==================================================

SELECT
    Area,
    ROUND(AVG(Delivery_Time), 2) AS average_delivery_time
FROM amazon
GROUP BY Area
ORDER BY average_delivery_time DESC;