create database ecommerce
use ecommerce
create schema Ecommerce;
-- Create Customers Table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100),
    password VARCHAR(50)
);

-- Create Products Table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name VARCHAR(50),
    price DECIMAL(10, 2),
    description VARCHAR(255),
    stockQuantity INT
);

-- Create Cart Table
CREATE TABLE cart (
    cart_id INT PRIMARY KEY,
    customer_id INT FOREIGN KEY REFERENCES customers(customer_id),
    product_id INT FOREIGN KEY REFERENCES products(product_id),
    quantity INT
);

-- Create Orders Table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT FOREIGN KEY REFERENCES customers(customer_id),
    order_date DATE,
    total_price DECIMAL(10, 2),
    shipping_address VARCHAR(255)
);

-- Create Order Items Table
CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY,
    order_id INT FOREIGN KEY REFERENCES orders(order_id),
    product_id INT FOREIGN KEY REFERENCES products(product_id),
    quantity INT
);

-- Insert Customers Data
INSERT INTO customers (customer_id, name, email, password) VALUES
(1, 'John Doe', 'johndoe@example.com', 'password123'),
(2, 'Jane Smith', 'janesmith@example.com', 'password123'),
(3, 'Robert Johnson', 'robert@example.com', 'password123'),
(4, 'Sarah Brown', 'sarah@example.com', 'password123'),
(5, 'David Lee', 'david@example.com', 'password123'),
(6, 'Laura Hall', 'laura@example.com', 'password123'),
(7, 'Michael Davis', 'michael@example.com', 'password123'),
(8, 'Emma Wilson', 'emma@example.com', 'password123'),
(9, 'William Taylor', 'william@example.com', 'password123'),
(10, 'Olivia Adams', 'olivia@example.com', 'password123');

-- Insert Products Data
INSERT INTO products (product_id, name, price, description, stockQuantity) VALUES
(1, 'Laptop', 800.00, 'High-performance laptop', 10),
(2, 'Smartphone', 600.00, 'Latest smartphone', 15),
(3, 'Tablet', 300.00, 'Portable tablet', 20),
(4, 'Headphones', 150.00, 'Noise-canceling', 30),
(5, 'TV', 900.00, '4K Smart TV', 5),
(6, 'Coffee Maker', 50.00, 'Automatic coffee maker', 25),
(7, 'Refrigerator', 700.00, 'Energy-efficient', 10),
(8, 'Microwave Oven', 80.00, 'Countertop microwave', 15),
(9, 'Blender', 70.00, 'High-speed blender', 20),
(10, 'Vacuum Cleaner', 120.00, 'Bagless vacuum cleaner', 10);

-- Insert Orders Data
INSERT INTO orders (order_id, customer_id, order_date, total_price, shipping_address) VALUES
(1, 1, '2023-01-05', 1200.00, '123 Main St, City'),
(2, 2, '2023-02-10', 900.00, '456 Elm St, Town'),
(3, 3, '2023-03-15', 300.00, '789 Oak St, Village'),
(4, 4, '2023-04-20', 150.00, '101 Pine St, Suburb'),
(5, 5, '2023-05-25', 1800.00, '234 Cedar St, District'),
(6, 6, '2023-06-30', 400.00, '567 Birch St, County'),
(7, 7, '2023-07-05', 700.00, '890 Maple St, State'),
(8, 8, '2023-08-10', 160.00, '321 Redwood St, Country'),
(9, 9, '2023-09-15', 140.00, '432 Spruce St, Province'),
(10, 10, '2023-10-20', 1400.00, '765 Fir St, Territory');

-- Insert Order Items Data
INSERT INTO order_items (order_item_id, order_id, product_id, quantity) VALUES
(1, 1, 1, 2),
(2, 1, 3, 1),
(3, 2, 2, 3),
(4, 3, 5, 2),
(5, 4, 4, 4),
(6, 5, 6, 1),
(7, 6, 10, 2),
(8, 6, 9, 3),
(9, 7, 7, 2);

--1.Update refrigerator product price to 800.
UPDATE products
SET price = 800
WHERE product_id = 7;
--2.Remove all cart items for a specific customer.
DELETE FROM cart
WHERE customer_id = 5;
--3.Retrieve Products Priced Below $100.
SELECT *
FROM products
WHERE price < 100;
--4.Find Products with Stock Quantity Greater Than 5.
SELECT *
FROM products
WHERE stockQuantity > 5;
--5.Retrieve Orders with Total Amount Between $500 and $1000.
SELECT *
FROM orders
WHERE total_price BETWEEN 500 AND 1000;
--6.Find Products which name end with letter ‘r’.
SELECT *
FROM products
WHERE name LIKE '%r';
--7.Retrieve Cart Items for Customer 5.
SELECT *
FROM cart
WHERE customer_id = 5;
--8.Find Customers Who Placed Orders in 2023.
SELECT DISTINCT c
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE YEAR(o.order_date) = 2023;
--9.Determine the Minimum Stock Quantity for Each Product Category.
SELECT MIN(stockQuantity) AS MinStockQuantity
FROM products
GROUP BY name;
--10.Calculate the Total Amount Spent by Each Customer.
SELECT c.customer_id, c.name, SUM(o.total_price) AS TotalSpent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name;
--11.Find the Average Order Amount for Each Customer.
SELECT c.customer_id, c.name, AVG(o.total_price) AS AverageOrderAmount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name;
--12.Count the Number of Orders Placed by Each Customer.
SELECT c.customer_id, c.name, COUNT(o.order_id) AS OrderCount
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name;
--13.Find the Maximum Order Amount for Each Customer.
SELECT c.customer_id, c.name, MAX(o.total_price) AS MaxOrderAmount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name;
--14.Get Customers Who Placed Orders Totaling Over $1000.
SELECT DISTINCT c
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
HAVING SUM(o.total_price) > 1000;
--15.Subquery to Find Products Not in the Cart.
SELECT *
FROM products p
WHERE p.product_id NOT IN (SELECT product_id FROM cart);
--16.Subquery to Find Customers Who Haven't Placed Orders.
SELECT *
FROM customers c
WHERE c.customer_id NOT IN (SELECT customer_id FROM orders);
--17.Subquery to Calculate the Percentage of Total Revenue for a Product.
SELECT p.name, 
       (SUM(oi.quantity * p.price) * 100.0 / (SELECT SUM(total_price) FROM orders)) AS PercentageRevenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.name;
--18.Subquery to Find Products with Low Stock.
SELECT *
FROM products
WHERE stockQuantity < (SELECT AVG(stockQuantity) FROM products);
--19.Subquery to Find Customers Who Placed High-Value Orders.
SELECT *
FROM customers c
WHERE c.customer_id IN (SELECT customer_id FROM orders WHERE total_price > 1000);
