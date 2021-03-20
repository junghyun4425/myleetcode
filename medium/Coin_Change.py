# Problem Link: https://leetcode.com/problems/coin-change/

'''
문제 요약: 코인이 주어질때, amount에 도달할 수 있는 최소 코인의 개수를 반환. (불가능하다면 -1을 반환)
ask: coins = [1,2,5], amount = 11
answer: 3

해석:
코인문제는 greedy로 쉽게 가능하기 때문에 coins를 내림차순 정렬하고 시도해봤지만 Fail.
이유는 최적으로만 구하면 결과가 -1 (불가능) 인 경우가 존재하기 때문. 하지만 최적이 아닐때는 동전이 딱 맞아떨어지는 경우가 있음.
따라서, greedy문제를 확장해 DP방식으로 도전.
DP로 최대한 메모리를 아끼려고 하다보니 amount만 배열로 정의하고 coin의 개수에 대해서는 따로 배열을 할당하지 않음.
왜냐면 amount 자체가 이미 엄청난 메모리를 잡아먹기 때문.
점화식으로는,
dp[i] = min(dp[i], dp[i-c]+1)   if c <= i
      = 0                       if i == 0
      = inf                     otherwise
결과는 메모리부분에서 최하를 받을것 같았지만 최상을 받고, 성능은 낮은 결과로 나옴.
아마 성능을 높이기위해서 코인의 개수까지 메모리에 추가하면 성능을 높이되 공간복잡도가 낮은 결과가 나올것이라 예상.
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if c <= i and dp[i-c] != float('inf'):
                    dp[i] = min(dp[i], 1+dp[i-c])
        return dp[-1] if dp[-1] != float('inf') else -1