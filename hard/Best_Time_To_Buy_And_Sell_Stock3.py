# Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

'''
문제 요약: 매일 가격표가 들어오면, 가장 싸게사서 비싸게 팔 수 있는 max_profit 을 구하는 문제. (최대 2번의 거래까지 허용)
ask: prices = [3,3,5,0,0,3,1,4]
answer: 6 ( (3-0) + (4-1) = 6 )

해석:
최대 거래수(transaction)이 들어가면서 난이도가 확 높아진 문제.
기존방법의 valley, peak 를 가져와서 하나하나 다 비교하는것은 굉장히 비효율적이기에 다른방법을 생각해야함.
역시 DP방식으로 점화식을 찾는 방법이 효율적.
각각의 row는 transaction수를, column은 day를 의미한다고 가정했을때 점화식은,

dp[i][j] = max(dp[i][j-1], prices[i] + max(-prices[x] + dp[i-1][x]))      if 0 <= x < i

식을 설명하자면, max() 함수의 첫번째 인자는 이전 날에 구매했던 값을 가져오는것이므로, 오늘 팔지 않는 상태를 의미.
두번째 인자는 오늘 파는 상태를 의미하는데, 오늘 가격에 팔았을때 추가적인 계산을 함. 샀었던 날을 최대값으로 만드는 날을 찾아 오늘가격에 팔아야 하기 때문.
이때 transaction이 2 라면(i==2) 이 값이 1이었을때 x날의 최대값을 더해주고, x날 산 가격을 빼주면 됨. 이를 최대값으로 하는 x를 찾으면 끝.
결국 x는 이전에 있었던 모든 경우의 수를 계산해서 최대값을 반환하는 계산법이고, 이것 또한 before_max 로 저장해놓으면 계산량이 줄어들게됨.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p_len = len(prices)
        n_trans = 2
        dp = [[0] * p_len for _ in range(n_trans + 1)]

        for i in range(1, n_trans + 1):
            before_max = float('-inf')
            for j in range(1, p_len):
                before_max = max(before_max, -prices[j - 1] + dp[i - 1][j - 1])
                dp[i][j] = max(dp[i][j - 1], prices[j] + before_max)
        return dp[-1][-1]