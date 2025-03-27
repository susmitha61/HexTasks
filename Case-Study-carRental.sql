create database CarRental;
use CarRental;
-- Create Vehicle Table
CREATE TABLE Vehicle (
    vehicleID INT PRIMARY KEY,
    make VARCHAR(50),
    model VARCHAR(50),
    year INT,
    dailyRate DECIMAL(10, 2),
    status VARCHAR(20) CHECK (status IN ('available', 'notAvailable')),
    passengerCapacity INT,
    engineCapacity INT
);

-- Create Customer Table
CREATE TABLE Customer (
    customerID INT PRIMARY KEY,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    email VARCHAR(100),
    phoneNumber VARCHAR(15)
);

-- Create Lease Table
CREATE TABLE Lease (
    leaseID INT PRIMARY KEY,
    vehicleID INT,
    customerID INT,
    startDate DATE,
    endDate DATE,
    type VARCHAR(20) CHECK (type IN ('DailyLease', 'MonthlyLease')),
    FOREIGN KEY (vehicleID) REFERENCES Vehicle(vehicleID),
    FOREIGN KEY (customerID) REFERENCES Customer(customerID)
);

-- Create Payment Table
CREATE TABLE Payment (
    paymentID INT PRIMARY KEY,
    leaseID INT,
    paymentDate DATE,
    amount DECIMAL(10, 2),
    FOREIGN KEY (leaseID) REFERENCES Lease(leaseID)
);

INSERT INTO Vehicle (vehicleID, make, model, year, dailyRate, status, passengerCapacity, engineCapacity)
VALUES 
    (1, 'Toyota', 'Camry', 2022, 50.00, 'available', 5, 1500),
    (2, 'Honda', 'Civic', 2023, 45.00, 'available', 5, 1400),
    (3, 'Ford', 'Focus', 2022, 48.00, 'notAvailable', 5, 1600),
    (4, 'Nissan', 'Altima', 2023, 52.00, 'available', 5, 1800),
    (5, 'Chevrolet', 'Malibu', 2022, 47.00, 'available', 5, 1700),
    (6, 'Hyundai', 'Sonata', 2023, 49.00, 'available', 5, 1400),
    (7, 'BMW', '3 Series', 2023, 60.00, 'available', 5, 2000),
    (8, 'Mercedes', 'C-Class', 2022, 58.00, 'notAvailable', 5, 2200),
    (9, 'Audi', 'A4', 2022, 55.00, 'available', 5, 2100),
    (10, 'Lexus', 'ES', 2023, 54.00, 'available', 5, 2300);

INSERT INTO Customer (customerID, firstName, lastName, email, phoneNumber)
VALUES 
    (1, 'John', 'Doe', 'johndoe@example.com', '555-555-5555'),
    (2, 'Jane', 'Smith', 'janesmith@example.com', '555-123-4567'),
    (3, 'Robert', 'Johnson', 'robert@example.com', '555-789-1234'),
    (4, 'Sarah', 'Brown', 'sarah@example.com', '555-456-7890'),
    (5, 'David', 'Lee', 'david@example.com', '555-987-6543'),
    (6, 'Laura', 'Hall', 'laura@example.com', '555-234-5678'),
    (7, 'Michael', 'Davis', 'michael@example.com', '555-876-5432'),
    (8, 'Emma', 'Wilson', 'emma@example.com', '555-432-1098'),
    (9, 'William', 'Taylor', 'william@example.com', '555-321-6547'),
    (10, 'Olivia', 'Adams', 'olivia@example.com', '555-765-4321');

INSERT INTO Lease (leaseID, vehicleID, customerID, startDate, endDate, type)
VALUES 
    (1, 1, 1, '2023-01-01', '2023-01-05', 'DailyLease'),
    (2, 2, 2, '2023-02-15', '2023-02-28', 'MonthlyLease'),
    (3, 3, 3, '2023-03-10', '2023-03-15', 'DailyLease'),
    (4, 4, 4, '2023-04-20', '2023-04-30', 'MonthlyLease'),
    (5, 5, 5, '2023-05-05', '2023-05-10', 'DailyLease'),
    (6, 6, 6, '2023-06-15', '2023-06-30', 'MonthlyLease'),
    (7, 7, 7, '2023-07-01', '2023-07-10', 'DailyLease'),
    (8, 8, 8, '2023-08-12', '2023-08-15', 'MonthlyLease'),
    (9, 9, 9, '2023-09-07', '2023-09-10', 'DailyLease'),
    (10, 10, 10, '2023-10-10', '2023-10-31', 'MonthlyLease');

INSERT INTO Payment (paymentID, leaseID, paymentDate, amount)
VALUES 
    (1, 1, '2023-01-03', 200.00),
    (2, 2, '2023-02-20', 1000.00), 
    (3, 3, '2023-03-12', 75.00),  
    (4, 4, '2023-04-25', 900.00),  
    (5, 5, '2023-05-07', 60.00),   
    (6, 6, '2023-06-18', 1200.00), 
    (7, 7, '2023-07-03', 40.00),   
    (8, 8, '2023-08-14', 1100.00), 
    (9, 9, '2023-09-09', 80.00),   
    (10, 10, '2023-10-25', 1500.00);

