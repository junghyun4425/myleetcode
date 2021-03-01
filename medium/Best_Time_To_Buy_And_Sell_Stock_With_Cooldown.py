# Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

'''
문제 요약: 주식을 사고 팔때, 가장 많은 수익을 낼수있는 값을 구하는 문제. (팔았을때 다음날 구매불가, 연속된 구매는 불가능)
ask: [1,2,3,0,2]
answer: 3

해석:
cooldown 이라는 제한이 생겼기 때문에 조금 복잡해 지긴 했으나, 상태만 잘 파악하면 해결이 가능한 문제.
상태를 구매, 판매, 쿨다운 세가지로 나누고 그에 맞게 DP방식으로 해결.
여기서 쿨다운은 판매할때는 적용되지 않기 때문에 구매할때 2일 떨어진곳을 찾아주면 따로 배열을 만들지 않아도 됨.
구매와 판매에 대한 DP를 각각 만들어 점화식을 세워보면,
sell_dp[i] = 0                                         i == 0
           = buy[0]+prices[1]                          i == 1
           = max(sell_dp[i-1], buy[i-1]+prices[i])     otherwise
buy_dp[i] = -prices[0]                                 i == 0
          = max(buy[0], -prices[1]                     i == 1
          = max(buy_dp[i-1], sell[i-2]-prices[i])      otherwise
구매에 대해서, 어제 구매한값을 hold vs 이틀전 수익에 오늘 구매한 값     둘중 최대값으로
판매에 대해서, 어제 판매한값을 hold vs 어제 구매한거를 파는 값         둘중 최대값으로
구매와 판매 DP에서 최대 수익을 찾으면 문제를 해결할 수 있음.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p_len = len(prices)
        if p_len < 2:
            return 0
        sell = [0] * p_len
        buy = [0] * p_len
        buy[0] = -prices[0]
        buy[1] = max(buy[0], -prices[1])
        sell[1] = max(sell[0], buy[0]+prices[1])
        for i in range(2, p_len):
            buy[i] = max(buy[i-1], sell[i-2]-prices[i])
            sell[i] = max(sell[i-1], buy[i-1]+prices[i])
        return max(0, buy[-1], sell[-1])
