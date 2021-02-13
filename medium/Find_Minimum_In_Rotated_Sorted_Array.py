# Problem Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

'''
문제 요약: 정렬된 숫자에서 n번 rotated 되었다고 할때, 최소값을 반환하는 문제.
ask: [3,4,5,1,2]
answer: 1

해석:
먼저 간단하게 O(n) 솔루션으로 문제를 해결해 봄. 도중에 이전값보다 다음값이 더 작다면 바로 반환하도록 함.
생각보다 성능이 굉장히 잘나와서 놀랐던 케이스.
그리고 좀더 최적화를 위해 O(logn) 솔루션으로 이진탐색을 시도.
도중에 빠르게 빠져나가기 위해서 m과 m+1 // m과 m-1 을 비교해 가면서 만약 최대값과 최소값을 찾으면 바로 반환하게 함.
그리고 나머지는 바이너리 서치와 동일.

재밌는건 최적화된 솔루션이 더 빠를거라 예상했지만 반대로 O(n)솔루션이 빨랐음.
개인적으로 생각했을때 O(n)이 워스트 케이스이고, 나머진 굉장히 빨리 문제를 해결하기 때문이라고 봄.
그렇다는 말은 입력으로 들어오는 케이스들이 0번 rotated 된 예제가 많이 없어서 내 첫번째 솔루션이 더 빠른 결과를 낸것 같음.
'''

# First Solution. Worst case -> O(n), but faster than Second Solution at submission time.
class Solution:
    def findMin(self, nums: List[int]) -> int:
        prev = nums[0]
        for n in nums[1:]:
            if prev > n:
                return n
            prev = n
        return nums[0]

# Second Solution. Worst case -> O(logn)
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        if nums[l] < nums[r] or r == 0:
            return nums[l]
        while r >= l:
            m = (l+r) // 2
            if nums[m] > nums[m+1]:
                return nums[m+1]
            if nums[m] < nums[m-1]:
                return nums[m]

            if nums[l] > nums[m]:
                r = m-1
            else:
                l = m+1
'''