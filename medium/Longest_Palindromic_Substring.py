# Problem Link: https://leetcode.com/problems/longest-palindromic-substring/

'''
문제 요약: 문자열 하나를 받아 가장 긴 좌우대칭(palindromic) 문자열을 반환
ask: kjhdhk
answer: hdh

해석:
모든 경우의 수를 확인하면 O(n^3) 시간이 걸림. 필요없는 계산을 위해 동적 프로그래밍 방식을 사용함.
문자열 시작점 i 와 끝점 j 는 각각 움직이며, i와 j가 좌우대칭이라면 P(i, j) = True 라 가정함.
좌우대칭이기 위해선 문자열 s 의 s[i] == s[j] 만족하며 동시에 P(i+1, j-1) = True 여야함.
예외로, i == j 일때는 True, j = i+1 and s[i] == s[j] 일때 True 가 있음.

Retry:
처음부터 점화식을 세우고 다시 풀어봄.
i가 시작점, j가 끝점이라고 가정한다면 점화식은,
dp[i][j] = ((j-i==1) or dp[i+1][j-1]) and (s[i]==s[j])      if j-i == 1
         = True                                             if i == j
'''

# Review
class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        dp = [[False] * s_len for _ in range(s_len)]
        ans = ""
        max_len = 0
        for j in range(s_len):
            for i in range(0, j+1):
                if i == j:
                    dp[i][j] = True
                else:
                    dp[i][j] = (s[i] == s[j]) and (j-i==1 or dp[i+1][j-1])
                if dp[i][j] and j-i+1 > max_len:
                    max_len = j-i+1
                    ans = s[i:j+1]
        return ans

# First Try
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        m = [[False] * s_len for i in range(s_len)]
        ans = ''
        max_len = 0
        for j in range(s_len):
            for i in range(0, j+1):
                if i == j:
                    m[i][j] = True
                else:
                    if s[i] == s[j] and ((j - i == 1) or m[i + 1][j - 1]):
                        m[i][j] = True
                if m[i][j]:
                    if (j - i + 1) > max_len:
                        max_len = j - i + 1
                        ans = s[i:j+1]
        return ans
'''