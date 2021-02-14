# Problem Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

'''
문제 요약: 정렬된 숫자에서 n번 rotated 되었다고 할때, 최소값을 반환하는 문제. (중복된 숫자도 존재)
ask: [2,2,2,0,1]
answer: 0

해석:
지난번 문제에서는 중복을 허용하지 않았기 때문에 이진탐색으로 쉽게 해결 할 수 있었지만, 이번엔 중복된 숫자가 들어감.
예외가 생각보다 많기 때문에 다양한 방법을 포괄하는 방법으로 풀어야 함. (이진탐색에서 조건을 추가해서 해결)
물론 O(n) 솔루션으로 풀려면 간단하게 해결되지만 이진탐색으로 해결함.
l = left_index, r = right_index, m = (r+l) // 2, min_val = global minimum value
1. nums[l] < nums[m]
    현재 l부터 m까지 정령된 상태이기 때문에 min_val = min(min_val, nums[l] 로 최소값 갱신하고 l = m+1
2. nums[l] == nums[m]
    l과 m이 같은상황. 하지만 l = m+1 로 해주면 특정 상황에 위반됨. ex) [10,10,10,10,10,1,10]
    따라서 같은 값은 l += 1 로 하나씩 증가시켜서 m을 뒤로 한칸씩 가게 만들어야 함.
3. otherwise
    m보다 l값이 크기 때문에 m뒤에 있는 값들(r까지)은 l보다 크고 m보다 작은 수들. 그래서 비교할 가치가 없기 때문에 r = m-1
위의 세가지 조건을 while loop로 수행하면 min_max에 최소값을 저장하게 됨.
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        min_val = float('inf')
        while l <= r:
            m = (l + r) // 2
            if nums[l] == nums[m]:
                min_val = min(min_val, nums[l])
                l += 1
            elif nums[l] < nums[m]:
                min_val = min(min_val, nums[l])
                l = m+1
            else:
                min_val = min(min_val, nums[m])
                r = m-1
        return min_val

