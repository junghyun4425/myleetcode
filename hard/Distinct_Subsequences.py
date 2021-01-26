# Problem Link: https://leetcode.com/problems/distinct-subsequences/

'''
문제 요약: t의 순서와 일치하는 sub string의 갯수를 s에서 찾아 반환하는 문제.
ask: s = "rabbbit", t = "rabbit"
answer: 3 (rabb_it, rab_bit, ra_bbit 언더바는 없는 문자로 취급)

해석:
반복 계산을 피하기 위해서 DP방식으로 시도. i는 s의 index를, j는 t의 index라 가정.
bottom-up방식으로 작은문제에서 큰문제로 나아가는 방식을 위해 s를 뒤에서부터 늘려가며 확인.
점화식은,
dp[i][j] = dp[i+1][j+1] + dp[i+1][j]        if s[i] == t[j]
         = 1                                if j == len(t)
         = 0                                if i == len(s)
         = dp[i+1][j]                       otherwise
j == len(t) 의 경우는, 마지막 글자가 일치할때 하나를 추가해주기 위함.
i == len(s) 는 s가 존재하지 않는 상태 즉, "" 와 동일한 상태이며 비교할 수 없기에 0. 그 외에도 t의 길이가 s보다 더 길면 0.
만약 s[i] != t[j] 라면, 이전의 결과값을 가져오면 됨. (ex, s = "it", t = "t" 일때 "i" != "t" 이지만 이전에 s에 "t"가 있었기 때문에 값은 1이 되어야 함)
s[i] == t[j] 일때는 이전의 결과값에 현재의 sequence를 더해줘야 함.
dp[0][0]에 최종 결과값이 저장.
'''

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        s_len = len(s)
        t_len = len(t)
        dp = [[0] * (t_len+1) for _ in range(s_len+1)]
        for i in range(s_len+1):
            dp[i][t_len] = 1
        for i in reversed(range(s_len)):
            for j in reversed(range(t_len)):
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j+1]
                dp[i][j] += dp[i+1][j]
        return dp[0][0]