# Problem Link: https://leetcode.com/problems/guess-number-higher-or-lower-ii/

'''
문제 요약: 지정된 숫자를 맞추는 게임으로, 최악의 경우에서 가장 적은 가격으로 숫자를 맞추는 경우를 찾는 문제. (1번 선택시 cost=1, 5는 cost=5)
ask: n = 2
answer: 1 (1과 2에서 1을 선택시 틀리면 1, 2를 선택시 틀리면 2이므로 코스트가 최소인 1을 선택)

해석:
Brute Force로 먼저 풀어보면, 모든 선택지 i에 대해서 가장 작은 코스트를 찾아가는 방법으로 재귀함수를 사용함.
left 부터 i-1 까지 왼쪽, i+1 부터 right 까지 오른쪽. i는 틀렸을 경우이니 cost에 더해줘야 함.
모든 i에 대해서 왼쪽과 오른쪽중 최악의 경우를 찾아야함. 왜냐면 각 i에 대해 최악의 경우에서 최소 cost를 찾는것이기 때문.
마지막으로 모든 i에 대한 최악의 cost 중에서 최고 효율이 좋은 i를 골라야 함. (최소 cost 찾기)
이를 Top-down DP방식으로 해결하려면 memoization의 자료구조가 필요하기 때문에 dictionary타입으로 정의.
(l, r)에 대해 값을 저장해놓으면 중복계산을 회피할 수 있음.
'''

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = {}
        def recursion(l, r):
            if l >= r:
                return 0
            if (l, r) in dp:
                return dp[(l,r)]
            min_res = float('inf')
            for i in range(l, r+1):
                res = i + max(recursion(l, i-1), recursion(i+1, r))
                min_res = min(res, min_res)
            dp[(l, r)] = min_res
            return min_res
        return recursion(1, n)