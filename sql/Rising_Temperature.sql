-- Problem Link: https://leetcode.com/problems/rising-temperature/

/*
문제 요약: 이전날 보다 기온이 올라간 날을 모두 가져오는 문제.
ask:
+----+------------+-------------+
| id | recordDate | Temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+

answer:
+----+
| id |
+----+
| 2  |
| 4  |
+----+

해석:
1일 차이를 비교하기 위해 DATEDIFF함수를 알고 있는지에 대해 묻는 문제.
DATEDIFF로 1일차이 나는 존건에 대해 이전날 보다 다음날의 기온이 높은경우 데이터를 가져옴.
*/

SELECT W1.id
FROM Weather W1, Weather W2
WHERE W1.Temperature > W2.Temperature and DATEDIFF(W1.Recorddate, W2.Recorddate) = 1