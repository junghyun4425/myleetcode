# Problem Link: https://leetcode.com/problems/super-ugly-number/

'''
문제 요약: 주어진 prime number들의 n번째 Super Ugly number를 찾는 문제. (주어진 소수들의 곱으로만 이뤄진 형태)
ask: n = 12, primes = [2,7,13,19]
answer: 32 ([1,2,4,7,8,13,14,16,19,26,28,32] 12개의 super ugly number)

해석:
기존에 풀었던 Ugly Number 문제를 DP방식으로 해결했었다면 이번에도 같은방법으로 해결이 가능한 문제.
prime number들의 곱 중에서 최소값을 찾아서 dp에 넣어주고 n번째까지 계산해주면 됨.
이전 문제에서 prime number의 개수만 늘어났고 같은 방식.
'''

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        p_len = len(primes)
        pos = [0] * p_len
        dp = [1]
        while len(dp) < n:
            val = min([dp[pos[i]]*primes[i] for i in range(p_len)])
            dp.append(val)
            for i in range(p_len):
                if val % primes[i] == 0:
                    pos[i] += 1
        return dp[-1]