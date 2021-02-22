-- Problem Link: https://leetcode.com/problems/employees-earning-more-than-their-managers/

/*
문제 요약: Manager보다 Employee가 연봉을 더 많이 받는 사람을 찾는 문제.
ask:
Employee Table
+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+
answer:
+----------+
| Employee |
+----------+
| Joe      |
+----------+

해석:
같은 테이블끼리 비교하는 문제. Self join 으로도 해결이 가능하지만, 두개의 테이블을 바로 비교해줘도 해결이 가능.
*/

SELECT E.Name "Employee"
FROM Employee M, Employee E
WHERE M.Id = E.ManagerId AND M.Salary < E.Salary