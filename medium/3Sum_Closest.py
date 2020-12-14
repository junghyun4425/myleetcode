# Problem Link: https://leetcode.com/problems/3sum-closest/

'''
문제 요약: 숫자 리스트에서 셋을더한 합이 target과 가장 가까운 값을 찾는 문제.
ask: [-1, 2, 1, -4], target = 1
answer: 2, (타겟과 같은 1은 불가능이므로 가장 근접한 숫자 2가 정답)

해석:
O(n^2) 걸리는 시간으로 세개의 합을 서치하는 문제는 이전에 3Sum 문제에서 이미 구현했기에 같은 방식으로 접근.
여기서 추가되어야 할 부분은 타겟과 차이값을 구해서 이전값보다 차이가 작은지를 찾아주면 되는 문제.
'''


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n_len = len(nums)
        nums.sort()
        gap = float('inf')
        ans = 0

        for i, v in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, n_len - 1
            while l < r:
                s = v + nums[l] + nums[r]
                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    return target
                if abs(target - s) < gap:
                    gap = abs(target - s)
                    ans = s
        return ans