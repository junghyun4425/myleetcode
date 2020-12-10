# Problem Link: https://leetcode.com/problems/median-of-two-sorted-arrays/

'''
문제 요약: 두개의 숫자배열을 받아 중앙값(median)을 구하는 문제.
ask: [1,2] , [3,7]
answer: [1,2,3,7] 에서 (2+3)/2 값을 구하면, 2.50000

해석:
리스트 두개를 합쳐서 가운데값을 찾으면 쉽게 구할수 있음. 단, O(n)의 속도.
이 문제가 hard 난이도인 이유는 O(log(n+m))의 속도로 구할 수 있는지에 대한 해답을 원하기 때문.
문제가 원하는 대로 풀려면 중앙값에 대한 통계적 시점에서 바라본 수식을 증명해낼 수 있어야 함...
시간이 남는다면 해보겠지만 다른 쪽에 공부를 더 하는것으로 결정.
'''


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        total_len = len(nums)
        median = 0

        if total_len % 2 == 0:
            mid = total_len // 2
            median = (nums[mid] + nums[mid - 1]) / 2
        else:
            median = nums[(total_len - 1) // 2]
        return median