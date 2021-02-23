-- Problem Link: https://leetcode.com/problems/duplicate-emails/

/*
문제 요약: 같은 이메일 주소를 가진 결과를 출력하는 문제.
ask:
Person Table
+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
answer:
+---------+
| Email   |
+---------+
| a@b.com |
+---------+

해석:
그룹핑의 기본기를 묻는 문제. 이메일 중복을 각각 찾아서 DISTINCT로 해결할 수 있겠지만, 그룹핑하면 더 쉽게 해결됨.
그룹핑해서 값을 카운트하고 두개 이상의 결과는 중복이므로 출력하면 해결.
*/

SELECT Email FROM Person GROUP BY Email HAVING COUNT(Email) > 1