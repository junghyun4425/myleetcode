-- Problem Link: https://leetcode.com/problems/combine-two-tables/

/*
문제 요약: FirstName, LastName, City, State 정보가 출력되는 SQL 작성.
ask:
Person Table
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
Address Table
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+

해석:
Leetcode에 SQL문제도 있다는것을 처음 알게됨..
문제 자체는 쉬운편이라, left join 으로 쉽게 해결이 가능.
참고로 SELECT 할때 어떤 테이블인지 명시 안해줘도 되긴하지만 성능에 영향을 미치기에 따로 표기를 함.
*/

SELECT P.FirstName, P.LastName, A.City, A.State
FROM Person P LEFT JOIN Address A ON (P.PersonId = A.PersonId);