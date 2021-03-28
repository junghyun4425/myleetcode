# Problem Link: https://leetcode.com/problems/integer-break/

'''
문제 요약: n을 덧셈으로 분할해서 곱한결과가 최대값을 반환하는 문제.
ask: 10
answer: 36 ( 3+3+4: 3*3*4=36 )

해석:
n의 값이 제한조건으로 1 <= n <= 58 이 나왔기 때문에 DP를 사용해도 적은양의 메모리를 소모하게 됨.
따라서 bottom-up방식으로 쉽게 접근이 가능. (이전에 곱한값의 최대를 저장해놓고 진행)
간단한 점화식을 세워보자면,
dp[i] = max(dp[i-j] * j, (i-j) * j, dp[i])    단, 1 <= j < i
      = 1                                     if i == 1 or 2
      = 0                                     if i == 0
즉, 이전에 곱셈한 결과에서 최대값을 저장해놓고 이후에 사용할수 있도록 구현.
성능이 중위권인것을 보면 어떤 최적화 방식이 있으리라 예상. 다음복습때 최적화를 도전해보는 것으로.
'''

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i-j] * j, (i-j) * j , dp[i])
        return dp[-1]