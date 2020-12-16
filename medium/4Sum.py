# Problem Link: https://leetcode.com/problems/4sum/

'''
문제 요약: 숫자 리스트에서 넷을더한 합이 targert이 되는 조합을 찾는 문제.
ask: [0, 0, 0, 0, 1], target = 0
answer: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]] (중복은 제거)

해석:
3Sum과 마찬가지로 2개의 포인트를 고정한 뒤 l, r 변수를 옮겨가며 O(n^3)으로 풀려고 시도.
문제없이 잘 수행됨.
'''


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n_len = len(nums)
        nums.sort()
        ans = []

        for i, v1 in enumerate(nums):
            if i > 0 and v1 == nums[i - 1]:
                continue
            for j in range(i + 1, n_len):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l, r = j + 1, n_len - 1
                while l < r:
                    s = v1 + nums[j] + nums[l] + nums[r]
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        ans.append([v1, nums[j], nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
        return ans