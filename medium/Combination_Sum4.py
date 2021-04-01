# Problem Link: https://leetcode.com/problems/combination-sum-iv/

'''
문제 요약: 입력으로 들어온 배열의 숫자들의 합이 target이 되는 조합의 개수를 구하는 문제.
ask: nums = [1,2,3], target = 4
answer: 7

해석:
숫자열에서 하나의 숫자를 여러번 중복사용이 되기 때문에 iterative보다는 recursion을 활용하는게 편리.
일단 Brute Force방식으로 구현해보면 target이 0될때까지 재귀함수를 호출함.
nums에 들어있는 모든 수들을 하나씩 빼가면서 진행하게 됨.
물론 시간초과가 나오지만 Top-down방식의 DP를 활용하면 성능문제가 깔끔히 해결됨.
여기서는 target을 키로하고 그 target에 대한 개수를 값으로 하는 해쉬맵으로 중복계산을 피하면 됨.
기존의 Brute Force방식에서 DP만 추가해서 해결.
'''

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(target):
            if target == 0:
                return 1
            if target in dp:
                return dp[target]
            res = 0
            for n in nums:
                if target - n >= 0:
                    res += dfs(target - n)
            dp[target] = res
            return res
        return dfs(target)