# Problem Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

'''
문제 요약: 정렬된 숫자리스트를 받아서 target과 동일한 숫자의 처음과 끝의 인덱스를 반환하는 문제.
ask: [0,0,1,2,4,5,5,6,7,8], targat = 5
answer: [5,6] (만약 target이 리스트에 없으면 -1)

해석:
최대한 Binary Search 와같은 효과를 보기 위해서 반씩 나눠서 찾아가는 방식으로 구현.
구현하고 속도가 생각보다 높지 않은것을 본 후, 왼쪽과 오른쪽의 index를 찾는곳에 while문이 최악의경우 O(n) 의 복잡도를 가지기 때문이라 판단.
시간이 되면 다른방법을 생각해 보기로 함.
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n_len = len(nums)
        first, last = 0, n_len
        while first < last:
            m = (first + last) // 2
            if nums[m] == target:
                first = last = m
                while first > 0 and target == nums[first-1]:
                    first -= 1
                while last < (n_len-1) and target == nums[last+1]:
                    last += 1
                return [first, last]
            elif nums[m] > target:
                last = m
            else:
                first = m + 1
        return [-1, -1]