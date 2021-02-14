# Problem Link: https://leetcode.com/problems/find-peak-element/

'''
문제 요약: peak가 되는 지점의 위치를 반환하는 문제. (local peak 중 아무거나)
ask: [1,2,1,3,5,6,4]
answer: 5 (1도 가능)

해석:
이 문제는 제약조건으로 log time complexity 로 해결하라는 조건이 있었기 때문에 오히려 이게 힌트가 된 경우.
처음엔 당연히 O(n)으로 해결하려 했으나, O(logn)의 경우로 해결하라했으니 사실 이 경우는 이진탐색의 경우가 유력했기 때문.
이진탐색이 된다고 가정하고 귀납적 추론으로 해결함.
원리를 간단하게 증명해 보자면,
1. 중앙에 위치한 값의 오른쪽보다 크다면? 오른쪽 어디엔가 peak가 존재해야 함. 배열의 마지막까지 간다면 그건 배열의 마지막 부분이 local 이기 때문.
    (배열의 마지막 다음의 숫자는 -inf 라고 가정한다고 문제에 명시함째. 배열의 0번째 이전값도 마찬가지.)
2. 반대로 중앙값보다 오른쪽이 작다면? 반대쪽으로 증가하는값이 있을것이고 배열의 첫번째까지 탐색할 것이고 마지막까지 간다면 마지막이 local.
위의 경우가 가능한 이유는 global peak를 찾는게 아니라 local peak를 찾는것이기 때문.
'''

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            m = (l+r)//2
            if nums[m] > nums[m+1]:
                r = m
            else:
                l = m+1
        return l