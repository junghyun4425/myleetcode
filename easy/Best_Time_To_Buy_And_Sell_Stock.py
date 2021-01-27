# Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

'''
문제 요약: 매일 가격표가 들어오면, 가장 싸게사서 비싸게 팔 수 있는 max_profit 을 구하는 문제.
ask: [7,1,5,3,6,4]
answer: 5 (1에 사서 6에 팔기)

해석:
가격이 오르거나 내리거나에 따라 진행하는 방향이 달라짐.
가격이 내려가면 사야하는 타이밍이기 때문에 buy_p 를 갱신.
가격이 올라가면 팔아야하는 타이밍이기 때문에 max_profit과 p - buy_p 를 비교하며 최대값을 갱신.
배열이 끝나는 시점에서의 max_profit이 최대값.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_p = prices[0]
        max_profit = 0
        for p in prices[1:]:
            if p <= buy_p:
                buy_p = p
            else:
                max_profit = p - buy_p if max_profit < p - buy_p else max_profit
        return max_profit