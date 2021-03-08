# Problem Link: https://leetcode.com/problems/kth-largest-element-in-an-array/

'''
문제 요약: k번째로 큰 수를 찾는 문제.
ask: nums = [3,2,3,1,2,4,5,5,6], k = 4
answer: 4

해석:
정렬을 사용하는 방식으로 해결이 가능. 단순히 정렬보다는 heap을 사용해 풀기로 결정.
힙을 안써봐서 몰랐지만, heapq에서 기본적으로 max_heap을 지원해주지 않음.
튜플로 음수를 대입해 max_heap을 만드는 방법이 있지만 메모리 낭비를 유발하기 때문에 그냥 min_heap으로 해결함.
'''

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        ans = 0
        for i in range(len(nums)-k+1):
            ans = heapq.heappop(nums)
        return ans