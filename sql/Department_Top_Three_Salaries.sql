-- Problem Link: https://leetcode.com/problems/department-top-three-salaries/

/*
문제 요약: 부서별 연봉 상위 3번째까지 데이터를 가져오는 문제.
ask:
Employee Table
+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 85000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
| 5  | Janet | 69000  | 1            |
| 6  | Randy | 85000  | 1            |
| 7  | Will  | 70000  | 1            |
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
| IT         | Randy    | 85000  |
| IT         | Joe      | 85000  |
| IT         | Will     | 70000  |
| Sales      | Henry    | 80000  |
| Sales      | Sam      | 60000  |
+------------+----------+--------+

해석:
DENSE_RANK() 함수를 그룹으로 묶어서 랭크를 정하는 PARTITION BY 를 알고 있으면 해결이 가능한 문제.
Employee 테이블에 연봉으로 랭크를 매겨놓은 테이블과 Department 테이블과 조인하면 3이하의 등수를 가져오면 끝.

함수를 안쓰고 조금 더 빠르게 하는 방법도 있지만 이부분은 직접 푼게 아니라 이런 방법도 있다는것을 확인함.
같은 부서끼리 연봉을 비교했을때 연봉이 높은사람들을 카운트로 그룹핑하면 높은순위 사람은 적은 수를 가짐. (랭크가 됨)
랭크를 조금 다르게 해석하는 방식으로, 익혀두면 좋을것 같아서 코드를 옮겨옴.
*/

SELECT D.Name Department, A.Name Employee, A.Salary
FROM (SELECT E.*, DENSE_RANK() OVER (PARTITION BY DepartmentId ORDER BY E.Salary DESC) R FROM Employee E) A
JOIN Department D on A.DepartmentId = D.Id
WHERE A.R <= 3

/*
SELECT
    d.Name AS 'Department', e1.Name AS 'Employee', e1.Salary
FROM
    Employee e1
        JOIN
    Department d ON e1.DepartmentId = d.Id
WHERE
    3 > (SELECT
            COUNT(DISTINCT e2.Salary)
        FROM
            Employee e2
        WHERE
            e2.Salary > e1.Salary
                AND e1.DepartmentId = e2.DepartmentId
        )
*/