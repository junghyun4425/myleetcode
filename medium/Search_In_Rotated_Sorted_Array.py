# Problem Link: https://leetcode.com/problems/search-in-rotated-sorted-array/

'''
문제 요약: pivot을 기점으로 반복되는 정렬된 숫자 리스트에서 target의 index를 반환하는 문제.
ask: [4,5,6,7,0,1,2], target = 0
answer: 4

해석:
우선 반복되는 끝점을 알기위해서 last값을 구한다음, 있으면 index를 없으면 -1을 반환하게 구현.
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n_len = len(nums)
        last = n_len

        for i in range(1, n_len):
            if nums[0] == nums[i]:
                last = i
                break

        if not target in nums[:last]:
            return -1
        return nums[:last].index(target)