# Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

'''
문제 요약: 매일 가격표가 들어오면, 가장 싸게사서 비싸게 팔 수 있는 max_profit 을 구하는 문제. (최대 k번의 거래까지 허용)
ask: k = 2, prices = [3,2,6,5,0,3]
answer: 7

해석:
이전의 sell-stock-iii 문제에서 이미 k번의 트랜잭션을 고려해 풀었기 때문에 복습차원에서 다시 점화식을 세우고 풀어본 문제.
점화식은 이전과 같이,

dp[i][j] = max(dp[i][j-1], prices[i] + max(-prices[x] + dp[i-1][x]))      if 0 <= x < i

여기서 한가지 실수해서 시간이 지체된 부분이 있었음.
before_max 를 구할때 prices[i] 까지 포함해 max값을 구하려 했었지만 이는 잘못된 접근.
현재값이 영향을 안주는 선에서 최대로 더하는값을 찾아야 하기 때문.
고로, max(prices[i] - prices[x] + dp[i-1][x]) 에서 prices[i]를 max()함수에 포함시키지 말고 밖에서 더해줘야 함.
'''

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        p_len = len(prices)
        if p_len < 2: return 0
        dp = [[0] * p_len for _ in range(k + 1)]

        for i in range(1, k + 1):
            before_max = float('-inf')
            for j in range(1, p_len):
                before_max = max(before_max, -prices[j - 1] + dp[i - 1][j - 1])
                dp[i][j] = max(dp[i][j - 1], prices[j] + before_max)
        return dp[-1][-1]