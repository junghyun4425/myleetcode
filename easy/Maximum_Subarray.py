# Problem Link: https://leetcode.com/problems/maximum-subarray/

'''
문제 요약: 숫자 리스트에서 가장 합이 높은 연속된 값들을 찾아 최고값을 반환.
ask: [-2,1,-3,4,-1,2,1,-5,4]
answer: 6 ([4,-1,2,1] 이므로 6)

해석:
이전에 구했던 값을 굳이 다시 계산하지 않아도 되는 DP방식으로 문제를 해결.
점화식은
m[i] = m[i-1] + nums[i] otherwise
     = nums[i] if dp[i-1] + nums[i] < nums[i]
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n_len = len(nums)
        dp = [nums[0]] * n_len

        for i in range(1, n_len):
            dp[i] = nums[i] if dp[i - 1] + nums[i] < nums[i] else dp[i - 1] + nums[i]

        return max(dp)