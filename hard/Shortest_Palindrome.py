# Problem Link: https://leetcode.com/problems/shortest-palindrome/

'''
문제 요약: 입력으로 들어오는 문자열에 문자를 추가해서 가장 짧게 Palindrome 을 만족하는 문자를 반환하는 문제.
ask: "abcd"
answer: "dcbabcd"

해석:
너무 어렵게 생각해서 오래걸렸던 문제. (난이도 hard 라서..)
원래 특별한 알고리즘이 안떠오르면 Brute Force 방식으로 먼저 풀어보고 추가적으로 생각하는데, 어렵게 생각해서 인지 쉬운방법조차 안떠오름.
결국 O(n^2) 시간복잡도를 가지는 방법으로 해결했는데 time limit을 초과하지 않아서 이 방법을 설명함.
핵심은 s를 뒤집어서 0번째부터 순차적으로 같은지 다른지 비교해 줌.
s는 왼쪽에서 줄어들고, s_rev는 오른쪽에서 줄어들며 같은지 값을 비교함.
(가운데 문자열들이 좌우대칭이더라도 끝 문자가 좌우대칭이 아니면 결국 모든 string을 다 써줘야 palindrome이 되기 때문에 끝에서부터 끝까지 탐색)

이를 O(n)으로 푸는 알고리즘이 있다고 함. 따라서 다음 복습때는 그 방법을 연구해보는 방향으로 리뷰.
아니면 재귀함수 연습하는 방향으로 리뷰.
'''

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        s_len = len(s)
        s_rev = s[::-1]
        for i in range(s_len):
            if s[:s_len-i] == s_rev[i:]:
                return s_rev[:i] + s
        return ""