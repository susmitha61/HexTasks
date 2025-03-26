--create database "TechShop";
--use TechShop;
/*CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100) UNIQUE,
    Phone VARCHAR(15),
    Address VARCHAR(255)
);
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Description TEXT,
    Price DECIMAL(10, 2) CHECK (Price >= 0)
);*
-- Create Orders Table
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATETIME DEFAULT GETDATE(),
    TotalAmount DECIMAL(10, 2) CHECK (TotalAmount >= 0),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);
CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT CHECK (Quantity > 0),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);
CREATE TABLE Inventory (
    InventoryID INT PRIMARY KEY,
    ProductID INT,
    QuantityInStock INT CHECK (QuantityInStock >= 0),
    LastStockUpdate DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);*/


-- Insert Data into Customers
/*INSERT INTO Customers (CustomerID, FirstName, LastName, Email, Phone, Address) VALUES
(1, 'John', 'Doe', 'john@example.com', '1234567890', '123 Elm St'),
(2, 'Jane', 'Smith', 'jane@example.com', '0987654321', '456 Oak St'),
(3, 'Alice', 'Johnson', 'alice@example.com', '1112223333', '789 Pine St'),
(4, 'Bob', 'Brown', 'bob@example.com', '4445556666', '321 Maple St'),
(5, 'Charlie', 'Davis', 'charlie@example.com', '7778889999', '654 Cedar St'),
(6, 'Eve', 'Wilson', 'eve@example.com', '2223334444', '987 Birch St'),
(7, 'Frank', 'Moore', 'frank@example.com', '5556667777', '159 Spruce St'),
(8, 'Grace', 'Taylor', 'grace@example.com', '8889990000', '753 Willow St'),
(9, 'Hank', 'Anderson', 'hank@example.com', '3334445555', '159 Ash St'),
(10, 'Ivy', 'Thomas', 'ivy@example.com', '6667778888', '753 Palm St');
GO


-- Insert Data into Products
INSERT INTO Products (ProductID, ProductName, Description, Price) VALUES
(1, 'Smartphone', 'Latest model smartphone', 699.99),
(2, 'Laptop', 'High performance laptop', 999.99),
(3, 'Headphones', 'Noise-cancelling headphones', 199.99),
(4, 'Smartwatch', 'Fitness tracking smartwatch', 249.99),
(5, 'Tablet', 'Portable tablet device', 399.99),
(6, 'Camera', 'DSLR camera with lens', 799.99),
(7, 'Speaker', 'Bluetooth speaker', 149.99),
(8, 'Monitor', 'LED monitor 24 inch', 299.99),
(9, 'Keyboard', 'Mechanical keyboard', 89.99),
(10, 'Mouse', 'Wireless mouse', 49.99);
GO  

-- Insert Data into Orders
INSERT INTO Orders (OrderID, CustomerID, OrderDate, TotalAmount) VALUES
(1, 1, '2025-03-01', 699.99),
(2, 2, '2025-03-02', 999.99),
(3, 3, '2025-03-03', 199.99),
(4, 4, '2025-03-04', 249.99),
(5, 5, '2025-03-05', 399.99),
(6, 6, '2025-03-06', 799.99),
(7, 7, '2025-03-07', 149.99),
(8, 8, '2025-03-08', 299.99),
(9, 9, '2025-03-09', 89.99),
(10, 10, '2025-03-10', 49.99);


-- Insert Data into OrderDetails
INSERT INTO OrderDetails (OrderDetailID, OrderID, ProductID, Quantity) VALUES
(1, 1, 1, 1),
(2, 2, 2, 1),
(3, 3, 3, 1),
(4, 4, 4, 1),
(5, 5, 5, 1),
(6, 6, 6, 1),
(7, 7, 7, 1),
(8, 8, 8, 1),
(9, 9, 9, 1),
(10, 10, 10, 1);
GO

-- Insert Data into Inventory
INSERT INTO Inventory (InventoryID, ProductID, QuantityInStock, LastStockUpdate) VALUES
(1, 1, 50, '2025-03-01'),
(2, 2, 30, '2025-03-01'),
(3, 3, 100, '2025-03-01'),
(4, 4, 70, '2025-03-01'),
(5, 5, 40, '2025-03-01'),
(6, 6, 20, '2025-03-01'),
(7, 7, 80, '2025-03-01'),
(8, 8, 25, '2025-03-01'),
(9, 9, 60, '2025-03-01'),
(10, 10, 90, '2025-03-01');
GO
*/

---Task-2---

-- 1. Retrieve customer names and emails
--SELECT FirstName, LastName, Email FROM Customers;

/*-- 2. List all orders with order dates and customer names
SELECT Orders.OrderID, Orders.OrderDate, Customers.FirstName, Customers.LastName
FROM Orders
JOIN Customers ON Orders.CustomerID = Customers.CustomerID;*/
--select * from Customers;
/*--3.Insert a new customer
--insert into Customers values(11,'Reeta','Roy','reeta@example.com','0975422785','145 Church Street');
-- 4. Increase prices of all products by 10%
UPDATE Products SET Price = Price * 1.10;*/
-- 5. Delete an order and its details (Input: OrderID)
/*DELETE FROM OrderDetails WHERE OrderID = 1;
DELETE FROM Orders WHERE OrderID = 1;*/
-- 6. Insert a new order
--INSERT INTO Orders (OrderID, CustomerID, OrderDate, TotalAmount) VALUES (11,11, '2025-03-15', 500.00);
-- 7. Update customer contact info (Input: CustomerID)
--UPDATE Customers SET Email = 'newemail@email.com', Address = '150 MArry Land' WHERE CustomerID = 2;


-- 8. Update total cost of each order
/*UPDATE Orders 
SET TotalAmount = (SELECT SUM(Products.Price * OrderDetails.Quantity)
                   FROM OrderDetails
                   JOIN Products ON OrderDetails.ProductID = Products.ProductID
                   WHERE OrderDetails.OrderID = Orders.OrderID);
-- 9. Delete orders for a specific customer (Input: CustomerID)
DELETE FROM OrderDetails WHERE OrderID IN (SELECT OrderID FROM Orders WHERE CustomerID = 2);
DELETE FROM Orders WHERE CustomerID = 2;
*/
-- 10. Insert a new electronic gadget
--INSERT INTO Products  VALUES (11,'Tablet', '10-inch Android tablet', 499.99);
-- 11. Update order status (Assuming "Status" column exists)
/*ALTER TABLE Orders ADD Status VARCHAR(20); 
UPDATE Orders SET Status = 'Shipped' WHERE OrderID = 3;

-- 12. Update number of orders per customer
ALTER TABLE Customers ADD OrderCount INT DEFAULT 0;
UPDATE Customers 
SET OrderCount = (SELECT COUNT(*) FROM Orders WHERE Orders.CustomerID = Customers.CustomerID);*/

---Task-3---

/*-- 1. Retrieve a list of all orders along with customer information (customer name) for each order
SELECT O.OrderID, C.FirstName, C.LastName, O.OrderDate, O.TotalAmount 
FROM Orders O
JOIN Customers C ON O.CustomerID = C.CustomerID;

-- 2. Find the total revenue generated by each electronic gadget product
SELECT P.ProductName, SUM(OD.Quantity * P.Price) AS TotalRevenue
FROM OrderDetails OD
JOIN Products P ON OD.ProductID = P.ProductID
GROUP BY P.ProductName
ORDER BY TotalRevenue DESC;

-- 3. List all customers who have made at least one purchase
SELECT DISTINCT C.CustomerID, C.FirstName, C.LastName, C.Email, C.Phone
FROM Customers C
JOIN Orders O ON C.CustomerID = O.CustomerID;

-- 4. Find the most popular electronic gadget (highest total quantity ordered)
SELECT P.ProductName, SUM(OD.Quantity) AS TotalQuantityOrdered
FROM OrderDetails OD
JOIN Products P ON OD.ProductID = P.ProductID
GROUP BY P.ProductName
ORDER BY TotalQuantityOrdered DESC;


-- 5. Retrieve a list of electronic gadgets along with their corresponding categories
SELECT ProductID, ProductName, Description
FROM Products;

-- 6. Calculate the average order value for each customer
SELECT C.CustomerID, C.FirstName, C.LastName, AVG(O.TotalAmount) AS AvgOrderValue
FROM Orders O
JOIN Customers C ON O.CustomerID = C.CustomerID
GROUP BY C.CustomerID, C.FirstName, C.LastName;

-- 7. Find the order with the highest total revenue
SELECT O.OrderID, O.TotalAmount, C.FirstName, C.LastName, C.Email
FROM Orders O
JOIN Customers C ON O.CustomerID = C.CustomerID
ORDER BY O.TotalAmount DESC;

-- 8. List electronic gadgets and the number of times each product has been ordered
SELECT P.ProductName, COUNT(OD.OrderID) AS NumberOfOrders
FROM OrderDetails OD
JOIN Products P ON OD.ProductID = P.ProductID
GROUP BY P.ProductName
ORDER BY NumberOfOrders DESC;

-- 9. Find customers who have purchased a specific electronic gadget (user input as parameter)
SELECT DISTINCT C.CustomerID, C.FirstName, C.LastName
FROM Customers C
JOIN Orders O ON C.CustomerID = O.CustomerID
JOIN OrderDetails OD ON O.OrderID = OD.OrderID
JOIN Products P ON OD.ProductID = P.ProductID
WHERE P.ProductName = 'Tablet'; 


-- 10. Calculate the total revenue generated by all orders placed within a specific time period (user input)
SELECT SUM(TotalAmount) AS TotalRevenue
FROM Orders
WHERE OrderDate BETWEEN '2025-01-01' AND '2025-12-31'; */

---Task-4--
/*-- 1. Find customers who have not placed any orders
SELECT * FROM Customers
WHERE CustomerID NOT IN (SELECT DISTINCT CustomerID FROM Orders);

-- 2. Find the total number of products available for sale
SELECT COUNT(ProductID) AS TotalProducts FROM Products;

-- 3. Calculate the total revenue generated by TechShop
SELECT SUM(TotalAmount) AS TotalRevenue FROM Orders;*/


-- 4. Calculate the average quantity ordered for products in a specific category (user input)
--ALTER TABLE Products ADD Category VARCHAR(50);

/*UPDATE Products 
SET Category = 'Electronics' 
WHERE ProductID IN (2, 4, 6, 8, 10, 12, 14, 16, 18, 20);*/

/*SELECT AVG(od.Quantity) AS avg_quantity_ordered
FROM OrderDetails od
JOIN Products p ON od.ProductID = p.ProductID
WHERE p.Category = 'Laptops';
*/

-- 5. Calculate the total revenue generated by a specific customer (user input)
/*SELECT SUM(o.TotalAmount) AS total_revenue
FROM Orders o
WHERE o.CustomerID = 3;
*/

-- 6. Find customers who have placed the most orders
/*SELECT c.FirstName, c.LastName, COUNT(o.OrderID) AS order_count
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID
GROUP BY c.CustomerID, c.FirstName, c.LastName
ORDER BY order_count DESC;*/

--7. Find the most popular product category (highest total quantity ordered)
/*SELECT p.Category, SUM(od.Quantity) AS total_quantity_ordered
FROM OrderDetails od
JOIN Products p ON od.ProductID = p.ProductID
GROUP BY p.Category
ORDER BY total_quantity_ordered DESC;
*/

--8. Find the customer who has spent the most money
/*SELECT c.FirstName, c.LastName, SUM(o.TotalAmount) AS total_spent
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID
JOIN OrderDetails od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
WHERE p.ProductName IN ('Laptop', 'Smartphone', 'Tablet', 'Gaming Console', 'SmartWatch')
GROUP BY c.CustomerID, c.FirstName, c.LastName
ORDER BY total_spent DESC;*/

/*-- 9. Calculate the average order value for all customers
SELECT AVG(TotalAmount) AS AverageOrderValue FROM Orders;
*/
-- 10. Find the total number of orders placed by each customer
SELECT C.CustomerID, C.FirstName, C.LastName, COUNT(O.OrderID) AS OrderCount
FROM Customers C
LEFT JOIN Orders O ON C.CustomerID = O.CustomerID
GROUP BY C.CustomerID, C.FirstName, C.LastName
ORDER BY OrderCount DESC;

