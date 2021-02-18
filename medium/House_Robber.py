# Problem Link: https://leetcode.com/problems/house-robber/

'''
문제 요약: 재산이 나열된 집이 있고, 도둑이 최대로 훔칠 수 있는 금액을 반환하는 문제. (연속된 집을 훔치면 경비에 걸리게 됨)
ask: [2,7,9,3,1]
answer: 12 (2 + 9 + 1)

해석:
DP 중에서도 간단히 해결할 수 있는 문제.
이웃집만 고려하지 않으면 되기 때문에 그점을 고려해서 점화식을 세워보면,
dp[i] = max(dp[i-1], dp[i-2]+nums[i])       if i > 1
      = max(nums[i], nums[i-1])             if i == 1
      = nums[0]                             if i == 0
메모리 절약을 위해서 dp[i]를 변수 두개만 가지고 최적화 가능. 이전값과 그 이전값 만 저장하고 갱신하면 됨.
나중에 모든 DP문제들 다시풀어볼때 메모리 최적화해서 풀어보기.
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        n_len = len(nums)
        if n_len == 1:
            return nums[0]
        dp = [nums[0]] * n_len
        dp[1] = max(dp[0], nums[1])
        for i in range(2, n_len):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]