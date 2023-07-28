--NAME: VICKY HAJONG
--EMP ID: 469895
--DB Assignments 2
--Q1 Write a query to display all the orders placed first 15 days of a month.

    SELECT * FROM ORDERS;
    WHERE EXTRACT(DAY FROM ORDER_DATE) <=15
    ORDER BY ORDER_DATE ASC;

--Q2 write a query to display the orders placed in January 1998 

    SELECT * FROM ORDERS
    WHERE TO_CHAR(ORDER_DATE, 'MON') = 'JAN' AND TO_CHAR(ORDER_DATE, 'YYYY') = 1998
    ORDER BY ORDER_DATE ASC;

--Q3 Write a query to display the orders placed in the third week of each month of 1997 

    SELECT * FROM ORDERS
    WHERE TO_CHAR(ORDER_DATE, 'W') = 3;
    ORDER BY ORDER_DATE ASC;

--Q4 Write a query to display the number of orders placed in each month of 1996,1997 and 1998.

    SELECT SUM(cnt) AS Order_Count, OD AS Year_Month 
    FROM (SELECT COUNT(order_id) AS cnt, TO_CHAR(Order_Date, 'YYYY-MONTH') AS OD FROM Orders
    GROUP BY Order_Date)
    GROUP BY OD
    ORDER BY OD ASC;

--Q5 Write a query to display the number of orders placed in each year 

    SELECT SUM(cnt) AS ORDER_COUNT, YR AS "ORDERED_YEAR" 
    FROM (SELECT COUNT(Order_id) AS cnt,TO_CHAR(Order_date, 'YYYY') AS YR FROM Orders
    GROUP BY Order_Date)
    GROUP BY YR;

--Q6 Write a query to display the number of orders placed by each customer 

    SELECT COUNT(Order_id) AS Order_Count, Customer_id,Ship_Name FROM Orders
    GROUP BY Customer_Id,Ship_Name;

--q7 Write a query to display the number and value of orders placed [ Use order_details table ]

    SELECT 
    Order_ID,
    COUNT(Order_ID) AS "No_Of_Orders",
    SUM((Unit_Price * Quantity)-(Unit_Price * Quantity * Discount)) AS "Total_Value" 
    FROM Order_details
    GROUP BY Order_Id;


--JOINS

--8. Write a query to display the following details from customers and orders table 
--OUTPUT: Customer_Code, Company_Name, Order_Id, Order_Date 
--HINT: Customers (Customer_Id), Orders (Customer_Id)

    SELECT C.Customer_Code,C.Company_Name,O.Order_Id,O.Order_Date
    FROM Customers C INNER JOIN Orders O ON O.Customer_Id = C.Customer_Id;

--9. Write a query to display the list of customers and the number of orders placed by them as follows: 
--OUTPUT: Customer_Code, Company_Name, CountOfOrders 
--NOTE: If the customer has not placed any orders, the CountOfOrders should display 0.
--HINT: use outer join and its variations. Customers (Customer_Id), Orders (Customer_id)

    SELECT C.Customer_Code, C.Company_Name, COUNT(O.Order_ID) AS CountOfOrders
    FROM Customers C LEFT OUTER JOIN Orders O ON C.Customer_Id = O.Customer_Id
    GROUP  BY C.Customer_Code,C.Company_Name;

--10. Write a query to display the value of each order using Orders and Order_details table
--OUTPUT: OrderId, OrderValue (SUM(UNITPRICE*QUANTITY))
--HINT: Orders (Order_ID), Order_details (Order_ID)

    SELECT O.Order_id,SUM(OD.Unit_Price * OD.Quantity) AS "OrderValue"
    FROM Orders O LEFT OUTER JOIN Order_Details OD ON O.Order_Id = OD.Order_Id
    GROUP BY O.Order_Id;



























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































A'S'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''D'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD'DDDDDDDDDDDDDDDDDDDDDDDDDDD][