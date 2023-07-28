--NAME:- VICKY HAJONG
--EMP ID:- 469895
---------------------------DB ASSIGNMENT-1-------------------------------------------------
--------------------------------Q1---------------------------------------------------------
CREATE TABLE BankCustomers
 (
 	Customer_Id INTEGER NOT NULL,
    First_Name VARCHAR2(10),
    Last_Name VARCHAR2(10),
    Contact_Number VARCHAR2(15),
    Addr_Line1 VARCHAR2(50),
    Addr_Line2 VARCHAR2(50),
    City VARCHAR2(15),
    State VARCHAR2(15),
    PostalCode VARCHAR(10)
 );
 --------------------------------Q2------------------------------------------------------
 CREATE TABLE AccountTypes
 (
 	AccType_Id INTEGER NOT NULL,
    AccType_Name VARCHAR2(20)
 );
 ---------------------------------Q3-----------------------------------------------------
 CREATE TABLE Accounts
 (
 	Acc_Id INTEGER NOT NULL,
    Cust_Id INTEGER NOT NULL,
    AccType_Id INTEGER NOT NULL,
    Opened_Date DATE,
    Current_Balance NUMERIC(10,2)
 );
 -----------------------------------Q4a-------------------------------------------------
 ALTER TABLE BankCustomers ADD CONSTRAINT pk_Customer_Id PRIMARY KEY (Customer_Id);
 ALTER TABLE BankCustomers ADD CONSTRAINT uq_Contact_Number UNIQUE (Contact_Number);
 -----------------------------------Q4b-------------------------------------------------
 ALTER TABLE AccountTypes ADD CONSTRAINT pk_AccType_Id PRIMARY KEY (AccType_Id);
 ALTER TABLE AccountTypes ADD CONSTRAINT uq_AccType_Name UNIQUE (AccType_Name);
 ------------------------------------Q4c-------------------------------------------------
 ALTER TABLE Accounts ADD CONSTRAINT pk_Acc_Id PRIMARY KEY (Acc_Id);
 ALTER TABLE Accounts ADD CONSTRAINT fk_Cust_Id FOREIGN KEY (Cust_Id) REFERENCES BankCustomers (Customer_Id) ON DELETE CASCADE;
 ALTER TABLE Accounts ADD CONSTRAINT fk_AccType_Id FOREIGN KEY (AccType_Id) REFERENCES AccountTypes (AccType_Id) ON DELETE CASCADE;
 ALTER TABLE Accounts ADD CONSTRAINT Opened_Date CHECK (Opened_Date <= '31-DEC-2023');  -- Current_Date returns dynamic value so we cant use it to compare directly with the 'Opened_Date'. 
 ALTER TABLE Accounts ADD CONSTRAINT Current_Balance CHECK (Current_Balance > 0);
 
 --------------------------------------Q5------------------------------------------------
 INSERT INTO AccountTypes VALUES (1, 'SAVINGS');
 INSERT INTO AccountTypes VALUES (2, 'CURRENT');
 --------------------------------------Q6------------------------------------------------
 INSERT INTO BankCustomers VALUES (1, 'Vicky', 'Hajong', '8927610980', 'JNV Diphu', 'Edgeverve Bangalore', 'Electronic city', 'Karnataka', '560100');
 INSERT INTO BankCustomers VALUES (2, 'Tom', 'Kumar', '8767934980', 'Goal Para', 'Edgeverve Bangalore', 'Electronic city', 'Karnataka', '560100');
 INSERT INTO BankCustomers VALUES (3, 'jerry', 'Hululu', '9827890690', 'Marsland', 'Cratus cricket', 'San Antonio', 'Red planet', '565656');
 INSERT INTO BankCustomers VALUES (4, 'Sixty', 'nine', '6969696969', 'Summerland ', 'Gurugram', 'Hue mario', 'Santamoore', '696969');
 INSERT INTO BankCustomers VALUES (5, 'Guwe', 'Yi', '9679914321', 'Jik se jua', 'Boku para', 'Pluto city', 'Polaris-gugugu', '100000');
 --------------------------------------Q7-------------------------------------------------
 INSERT INTO Accounts VALUES (1, 1, 1, '23-JUL-2023', 1000.00);
 INSERT INTO Accounts VALUES (2, 2, 2, '24-JUL-2023', 5656.00);
 INSERT INTO Accounts VALUES (3, 3, 1, '24-JUL-2023', 696969.00); 
 INSERT INTO Accounts VALUES (4, 4, 2, '25-JUL-2023', 5478.00);
 INSERT INTO Accounts VALUES (5, 5, 2, '26-JUL-2023', 1000000.00);
 --------------------------------------Q8--------------------------------------------------
 SELECT * FROM AccountTypes;
 --------------------------------------Q9--------------------------------------------------
 SELECT * FROM BankCustomers;
 --------------------------------------Q10-------------------------------------------------
 SELECT * FROM Accounts;
 --------------------------------------Q11-------------------------------------------------
 SELECT * FROM  Accounts  WHERE AccType_Id = 1;
 --------------------------------------Q12-------------------------------------------------
 SELECT * FROM Accounts WHERE AccType_Id = 2;
 ---=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--THE END!! :)---=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=---