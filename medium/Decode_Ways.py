# Problem Link: https://leetcode.com/problems/decode-ways/

'''
문제 요약: 숫자로 구성된 문자열을 해독하는 방법의 갯수를 반환하는 문제 (1='A',2='B', ... 26='Z')
ask: "226"
answer: 3 ([2, 26], [2, 2, 6], [22, 6])

해석:
재귀함수로 간단하게 해결할 수 있지만 시간초과 때문에 중복 계산을 필할 수 있는 DP방식을 활용.
점화식을 찾는데 생각보다 오래걸림... (2자리 수 인데, dp[i-1]만 활용해서 어떻게 하려고 하니 안풀렸고 dp[i-2]가 필요하다는 것을 늦게 깨우침)
dp[i] = dp[i-1]                 if s[i] != '0' and s[i-1:i+1] > '26'
      = dp[i-2]                 if s[i] == '0' and '10' <= s[i-1:i+1] < '27'
      = dp[i-1] + dp[i-2]       if s[i] != '0' and '10' <= s[i-1:i+1] < '27'
      = 1                       if i == 0
      = 0                       if i == 0 and s[i] == '0'
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        s_len = len(s)
        dp = [0] * s_len
        if s[0] != '0':
            dp[0] = 1
        for i in range(1, s_len):
            if s[i] != '0':
                dp[i] += dp[i-1]
            if '10' <= s[i-1:i+1] < '27':
                dp[i] += dp[i-2] if i > 1 else 1
        return dp[-1]