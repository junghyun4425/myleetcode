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

Review
이전값에서 최대값만을 필요로 하기 때문에 dp배열이 필요없고 이전의 dp값 하나만 있으면 됨.
따라서 공간복잡도를 O(n)에서 O(1)로 줄일 수 있음.
거기에 식을 간소화 함. dp[i-1] + nums[i] < nums[i] ----> dp[i-1] < 0
최적화 시켜서 마무리 한 결과 잘 수행됨.
'''

# Second Try (Optimized Space complexity O(n) to O(1))
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n_len = len(nums)
        pre_dp = max_sum = nums[0]

        for i in range(1, n_len):
            pre_dp = nums[i] + (pre_dp if pre_dp > 0 else 0)
            max_sum = max(max_sum, pre_dp)
        return max_sum

# First Try
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n_len = len(nums)
        dp = [nums[0]] * n_len

        for i in range(1, n_len):
            dp[i] = nums[i] if dp[i-1] + nums[i] < nums[i] else dp[i-1] + nums[i]

        return max(dp)
'''