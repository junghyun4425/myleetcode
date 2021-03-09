# Problem Link: https://leetcode.com/problems/combination-sum-iii/

'''
문제 요약: k개의 숫자의 합으로 n을 만들수 있는 모든 조합을 반환하는 문제 (숫자는 1~9의 숫자만 유효, 2 <= k <= 9)
ask: k = 3, n = 9
answer: [[1,2,6],[1,3,5],[2,3,4]]

해석:
숫자의 유효범위가 1에서 9까지만 가능하고 k개의 숫자는 9이하 라는 제한이 있어서 재귀로 쉽게 풀수 있었던 문제.
범위가 작기때문에 모든 경우의 수를 top-down방식으로 탐색하고 일치하는 값을 가져올 수 있음.
현재 숫자가 포함되었을때와 안되었을때 두가지를 재귀로 하나씩 호출해 나가게 됨.
'''

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def recursion(comb, sums, cur):
            if len(comb) == k and sums == n:
                ans.append(comb)
                return
            if cur > 9:
                return
            recursion(comb+[cur], sums+cur, cur+1)
            recursion(comb, sums, cur+1)
        recursion([], 0, 1)
        return ans