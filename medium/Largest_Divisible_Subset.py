# Problem Link: https://leetcode.com/problems/largest-divisible-subset/

'''
문제 요약: 숫자배열이 들어올때, nums[i] % nums[j] == 0 을 만족하는 가장 큰 sub-array를 출력하는 문제. (i와 j는 순서는 상관없음)
ask: nums = [1,2,3]
answer: [1,2] ( [1,3]도 정답이 가능 )

해석:
DP로 O(n^2)의 시간복잡도를 가지도록 구현이 가능함.
이를 위해서는 오름차순으로 정렬이 되었다는 가정하에서 해야하기 때문에 정렬을 수행. (1 % 3 과 같이 뒤에 숫자가 더 크면 같은숫자 외에는 무조건 0이 될수 없음)
따라서 작은수부터 차례대로 비교해가며 나누어떨어지면 dp[i]에 추가해나가는 방식.
i는 추가할 대상을 의미하고 j는 i보다 작은값들 중 나누어 떨어지는지 비교할 값을 의미.
점화식을 간단하게 나타내면,
dp[i] = dp[j] + [nums[i]]               if len(dp[j]) >= len(dp[i]) and (nums[i] % nums[j] == 0)
      = [nums[i]]                       otherwise
'''

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n_len = len(nums)
        dp = defaultdict(list)
        nums.sort()
        ans = []
        for i in range(n_len):
            dp[i] += [nums[i]]
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if len(dp[i]) <= len(dp[j]):
                        dp[i] = dp[j] + [nums[i]]
            if len(ans) < len(dp[i]):
                ans = dp[i]
        return ans