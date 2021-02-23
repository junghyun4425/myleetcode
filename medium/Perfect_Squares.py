# Problem Link: https://leetcode.com/problems/perfect-squares/

'''
문제 요약: 들어오는 숫자 n을 perfect넘버로 만들수 있는 경우의 수 중에서 가장 짧은 수를 반환하는 문제. (perfect num = 1, 4, 9, 16 ...)
ask: 12
answer: 3 (4 + 4 + 4)

해석:
Brute-force 방식으로 하기엔 O(n^3)의 시간복잡도를 가지기 때문에 굉장히 비효율적. 따라서 중복 계산을 제거해줘야 함.
Bottom-up 방식으로 1부터 계산한 최소 결과값을 dp에 저장하는 방식.
그리고 모든 가능한 perfect num에 대해 minimum값을 찾으면 O(n^2)에 해결이 가능함.
점화식은,
dp[i] = min(dp[i], dp[i-j*j])       if 0 < j and j*j < i
      = 0                           if i == 0
'''

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            j = 1
            while j*j <= i:
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j += 1
        return dp[-1]