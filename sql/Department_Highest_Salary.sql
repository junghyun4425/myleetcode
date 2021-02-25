-- Problem Link: https://leetcode.com/problems/department-highest-salary/

/*
문제 요약: 부서에서 최고액의 연봉을 받는 사람들을 가져오는 문제.
ask:
Employee Table
+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
Department Table
+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+

answer:
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
+------------+----------+--------+

해석:
조인해서 MAX로 최고액을 찾는건 간단한 일이지만, MAX값이 중복으로 존재하면 문제가 발생.
단 하나만 가져오기 때문에, 해결법은 RANK나 서브쿼리로 맥스값에 존재하는 레코드들을 가져오는 방법 등이 있음.
서브쿼리로 MAX값을 가져온 다음, 그값이 JOIN한 레코드와 일치하는 결과를 나열하도록 구현.
한가지 주의할 점은 INNER JOIN이 아닐시엔 NULL값을 가져오기 때문에 이점만 고려하면 해결.
*/

SELECT D.Name "Department", E.Name "Employee", E.Salary
FROM Employee E JOIN Department D on E.DepartmentId = D.Id
WHERE (E.DepartmentId, E.Salary) IN
        (   SELECT DepartmentId, MAX(Salary)
            From Employee
            GROUP BY DepartmentId
        )