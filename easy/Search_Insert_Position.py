# Problem Link: https://leetcode.com/problems/search-insert-position/

'''
문제 요약: 정렬된 숫자 리스트 내에서 target의 위치 혹은 어디에 삽입되어야 하는지 해결하는 문제.
ask: [1,3,4,5,6,8], target = 0
answer: 0 (target값이 없으니 0이 삽입되어야 할 위치는 index = 0)

해석:
O(n)의 시간 복잡도로 풀면 간단하지만 좀더 나은 성능을 위해서 바이너리 서치로 O(logn)까지 줄이는 방법으로 해결.
무한루프를 돌지 않게하기 위해 r 과 l을 m으로 바꿀때 값을 하나씩 더해주거나 뺌.
답이 마지막 인덱스인 경우, l을 반환하면 len(nums) 보다 하나 작게 나오기 때문에 l < r 이 아닌 l <= r 의 반복문을 수행.
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
        return l