# Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

'''
문제 요약: 매일 가격표가 들어오면, 최종 수익이 가장 높은값을 구하는 문제.
ask: [7,1,5,3,6,4]
answer: 7 (1에 사서 5에 팔기 + 3에 사서 6에 팔기)

해석:
난이도가 easy인것 치고는 생각이 꽤나 했던 문제.
실제로 최대 수익을 구하려면 여러 경우의 수를 이중탐색으로 비교해야하기 때문에 Brute Force 방식으로 풀면 최악의 속도가 나올테니 고려하지 않음.
처음에는 스택을 써서 값이 내려가면 저장해놓고 올라갈때마다 profit을 더해주려는데 [1,2,3,4,5] 와 같은 예시에서 막힘.
이때, 깨달은게 5-1 = 4 를 하나, (2-1)+(3-2)+(4-3)+(5-4)를 하나 결과가 같음. 그래서 값이 커질때마다 차이를 합에 더해줌.
남들이 설명한 방식을 보니, 내가 푼 방식이 peak-valley approach를 응용한 방식.
valley를 찾고, peak를 찾아서 뺀다음 profit_sum에 저장하는 방식이며, 내가 푼 방식은 vally에서부터 peak까지 차이를 쭉 더해가는 응용된 방법이었던 것.
나름 규칙을 찾아 풀었고 나중에 해설을보니 굉장히 재밌었던 문제.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p_len = len(prices)
        p_sum = 0
        for i in range(1, p_len):
            if prices[i-1] < prices[i]:
                p_sum += prices[i] - prices[i-1]
        return p_sum