# Problem Link: https://leetcode.com/problems/arranging-coins/

'''
문제 요약: n개의 동전으로 계단모양을 만들려고 한다면, 몇층까지 만들수 있는지를 묻는 문제.
ask: 5
answer: 2 (1 + 2 층은 되지만, 3층을 쌓기엔 하나가 부족함)

해석:
난이도가 쉬운만큼, 직관적으로 쉽게 파악할 수 있었던 문제.
우선, 1부터 k까지의 합이 k(k+1) / 2 라는 공식만 이해한다면 n으로 최대 층을 만들수 있는 경우를 알 수 있음.
k(k+1) <= 2n 으로 계산해보면 결과가
n = root(2n + 1/4) + 1/2
따라서 이 수식을 구해주고 나머지는 버려주면 최대로 만들수 있는 층을 알수 있게 됨.
'''

class Solution:
    def arrangeCoins(self, n: int) -> int:
        return (int)((2 * n + 0.25)**0.5 - 0.5)