# Problem Link: https://leetcode.com/problems/longest-increasing-subsequence/

'''
문제 요약: 증가하는 수로만 구성이 된 sub_array 의 최대 길이를 반환하는 문제.
ask: [10,9,2,5,3,7,101,18]
answer: 4 ( [2,3,7,101] )

해석:
실력이 향상된건지 문제가 쉬운건지 모르겠지만 5분안에 간단하게 풀었던 문제.
Bottum-up 방식으로 길이가 1일때부터 최대길이를 구해주면 해결이 가능.
점화식은,
dp[i] = max(dp[0], dp[1], ... ,dp[j])       otherwise / nums[i] > nums[j] ( 0 < j < i )
      = 1                                   if i == 0
주의할 점은, 끝에서의 결과 dp[n] 값이 최대라는 보장이 되진 않기 때문에 도중에 max_len을 계속 찾아줘야 한다는 점.
그외에는 어려운점이 없었던 문제.
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n_len = len(nums)
        dp = [1] * n_len
        max_len = 1

        for i in range(1, n_len):
            compare = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    compare = max(compare, dp[j] + 1)
            dp[i] = compare
            max_len = max(max_len, compare)
        return max_len