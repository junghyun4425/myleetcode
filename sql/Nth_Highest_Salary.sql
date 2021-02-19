-- Problem Link: https://leetcode.com/problems/nth-highest-salary/

/*
문제 요약: N번째로 높은 연봉을 반환하는 문제.
ask:
Employee Table
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
answer:
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+

해석:
함수의 형태는 제공되어 있었기에 Return값만 만들면 되는 문제.
우선 서브쿼리로 Salary로 정렬된 N개의 데이터를 뽑아옴.
그리고 거기에 Min함수로 N번째 연봉을 가져올 수 있지만, 문제는 테이블이 N보다 작을때.
그래서 IF문을 통해 제거해줌. IFNULL로 처리해도 됨.
*/

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT IF(COUNT(*) < N, NULL, MIN(Salary))
      FROM (SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT N) a
  );
END