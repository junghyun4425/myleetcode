-- Problem Link: https://leetcode.com/problems/consecutive-numbers/

/*
문제 요약: 연속해서 같은 숫자가 3개 나오는 값들을 가져오는 문제
ask:
Logs Table
+----+-----+
| Id | Num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
answer:
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+

해석:
Id 라는 기본키가 정렬된 상태에서 연속으로 3개의 값을 뽑아오는 문제. LAG와 LEAD 함수 두개를 활용하면 비교적 간단하게 풀 수 있음.
LAG로 현재 NUM의 이전값을, LEAD로 다음값을 서브쿼리로 호출해, LAG LEAD NUM 세개의 값이 같은지 판단.
연속으로 3개이상 나오면 중복이 존재할 테니 DISTINCT 로 중복을 방지.
*/

SELECT DISTINCT Num ConsecutiveNums
FROM (SELECT Num, LAG(Num) OVER (ORDER BY Id) Bef, LEAD(Num) OVER (ORDER BY Id) Aft
     FROM Logs) RES
WHERE RES.Bef = RES.Num AND RES.Aft = RES.Num