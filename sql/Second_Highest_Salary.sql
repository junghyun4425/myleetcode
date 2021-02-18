-- Problem Link: https://leetcode.com/problems/second-highest-salary/

/*
문제 요약: Employee 테이블에서 2번째로 연봉이 높은 금액을 뽑는 문제.
ask:
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+

answer:
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+

해석:
이 문제를 통해 생각보다 SQL에 많이 약하다는걸 깨우친 문제. RANK 사용법도 까먹어서 못쓰고, LIMIT도 오프셋 있는지 한참 헤매임.
문제에서 예외로 하나만 존재할때 NULL을 반환하게 하는것과 연봉이 같은 경우 처리를 안해줬어서 몇번 실패를 함.
DISTINCT 로 중복의 경우 처리하고, IFNULL로 데이터가 하나만 존재할때를 처리함.
SQL관련 문제를 많이 찾아서 풀어봐야함.
*/

SELECT
    IFNULL(
        (SELECT DISTINCT Salary
         FROM Employee
         ORDER BY Salary DESC
         LIMIT 1 OFFSET 1),
        NULL) SecondHighestSalary;