-- Practice1 DDL -----------------------------------------------------------------------------------
-- Task 1: Create TRG_DEPT table
CREATE TABLE TRG_DEPT (
    ID INT,
    NAME VARCHAR(25)
);
-- Confirm table creation
EXEC sp_help TRG_DEPT;

-- Task 2: Populate TRG_DEPT with data from DEPARTMENTS
INSERT INTO TRG_DEPT (ID, NAME)
SELECT DEPARTMENT_ID, DEPARTMENT_NAME FROM DEPARTMENTS;

-- Confirm data insertion
SELECT * FROM TRG_DEPT;

-- Task 3: Create TRG_EMP table
CREATE TABLE TRG_EMP (
    ID INT,
    LAST_NAME VARCHAR(25),
    FIRST_NAME VARCHAR(25),
    DEPT_ID INT
);
-- Confirm table creation
EXEC sp_help TRG_EMP;

-- Task 4: Modify TRG_EMP to allow longer LAST_NAME values
ALTER TABLE TRG_EMP ALTER COLUMN LAST_NAME VARCHAR(50);
-- Confirm modification
EXEC sp_help TRG_EMP;

-- Task 5: Create TRG_EMPLOYEES table with specific columns from EMPLOYEES
SELECT EMPLOYEE_ID AS ID, FIRST_NAME, LAST_NAME, SALARY, DEPARTMENT_ID AS DEPT_ID 
INTO TRG_EMPLOYEES
FROM EMPLOYEES;

-- Confirm table creation
EXEC sp_help TRG_EMPLOYEES;

-- Task 6: Drop TRG_EMP table
DROP TABLE TRG_EMP;
-- Confirm deletion
SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'TRG_EMP';

-- Task 7: Rename TRG_EMPLOYEES to TRG_EMP
EXEC sp_rename 'TRG_EMPLOYEES', 'TRG_EMP';
-- Confirm renaming
EXEC sp_help TRG_EMP;

-- Task 8: Drop FIRST_NAME column from TRG_EMP
ALTER TABLE TRG_EMP DROP COLUMN FIRST_NAME;
-- Confirm modification
EXEC sp_help TRG_EMP;




-- Practice DML-1 -------------------------------------------------------
-- Describe the structure of MY_EMPLOYEE table
EXEC sp_help MY_EMPLOYEE;

-- Insert data without listing columns
INSERT INTO MY_EMPLOYEE VALUES (1, 'Patel', 'Ralph', 'rpatel', 895);

-- Insert data explicitly listing columns
INSERT INTO MY_EMPLOYEE (ID, LAST_NAME, FIRST_NAME, USERID, SALARY)
VALUES (2, 'Dancs', 'Betty', 'bdancs', 860);

-- Confirm additions to the table
SELECT * FROM MY_EMPLOYEE;

-- Insert data using variables and generate USERID dynamically
DECLARE @ID INT, @LAST_NAME VARCHAR(50), @FIRST_NAME VARCHAR(50), @SALARY INT;
SET @ID = 3;
SET @LAST_NAME = 'Smith';
SET @FIRST_NAME = 'John';
SET @SALARY = 950;

INSERT INTO MY_EMPLOYEE (ID, LAST_NAME, FIRST_NAME, USERID, SALARY)
VALUES (@ID, @LAST_NAME, @FIRST_NAME, LEFT(@FIRST_NAME,1) + LEFT(@LAST_NAME,7), @SALARY);

-- Update last name of employee with ID = 3 to Drexler
UPDATE MY_EMPLOYEE 
SET LAST_NAME = 'Drexler' 
WHERE ID = 3;

-- Update salary to 1000 for all employees with a salary less than 900
UPDATE MY_EMPLOYEE 
SET SALARY = 1000 
WHERE SALARY < 900;

-- Delete Betty Dancs from MY_EMPLOYEE table
DELETE FROM MY_EMPLOYEE 
WHERE LAST_NAME = 'Dancs' AND FIRST_NAME = 'Betty';

-- Empty the entire table (delete all records)
DELETE FROM MY_EMPLOYEE;
-- or alternatively
-- TRUNCATE TABLE MY_EMPLOYEE;


