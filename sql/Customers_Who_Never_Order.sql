-- Problem Link: https://leetcode.com/problems/customers-who-never-order/

/*
문제 요약: 아무것도 구입하지 않은 사람의 목록을 가져오는 문제.
ask:
Customers Table
+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Orders Table
+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+

answer:
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+

해석:
두가지 방법으로 문제를 해결.
첫번째는 모든 CUSTOMERID의 목록을 가져와 그 안에 없는 목록의 고객만 가져오는 방법.
두번째는 LEFT JOIN을 통해 NULL값인 경우만 가져오는 방법.
*/

SELECT CUSTOMERS.NAME "Customers"
FROM CUSTOMERS
WHERE CUSTOMERS.ID NOT IN (SELECT CUSTOMERID FROM ORDERS)

/*
SELECT C.NAME "Customers"
FROM CUSTOMERS C LEFT JOIN ORDERS O ON C.ID = O.CUSTOMERID
WHERE O.CUSTOMERID IS NULL
*/