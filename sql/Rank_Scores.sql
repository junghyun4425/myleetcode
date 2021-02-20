-- Problem Link: https://leetcode.com/problems/rank-scores/

/*
문제 요약: 등수를 매기는 문제 (내림차순이며, 중복으로 같는 등수 다음에 구멍내지 않고 연속되게 등수를 매기기)
ask:
Scores Table
+----+-------+
| Id | Score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
answer:
+-------+---------+
| score | Rank    |
+-------+---------+
| 4.00  | 1       |
| 4.00  | 1       |
| 3.85  | 2       |
| 3.65  | 3       |
| 3.65  | 3       |
| 3.50  | 4       |
+-------+---------+

해석:
랭크 함수를 알고 있으면 간단하게 풀수 있는문제. 단, 여기서는 일반적인 RANK가 아니라 DENSE_RANK함수로 연속된 등수를 매겨야 함.
DENSE_RANK만 알고 있으면 빠르게 해결되는 문제.
*/

# Write your MySQL query statement below
SELECT Score, DENSE_RANK() OVER (ORDER BY Score DESC) "Rank" FROM Scores