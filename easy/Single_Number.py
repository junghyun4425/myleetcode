# Problem Link: https://leetcode.com/problems/single-number/

'''
문제 요약: 값이 쌍으로 존재하는 숫자배열에 하나만 존재하는 값을 찾아 반환하는 문제. (단, 추가 메모리x, linear time complexity)
ask: [2,1,2,1,3]
answer: 3

해석:
우선 추가 메모리를 쓰지 못하기 때문에 set() 함수로 중복 제거한 다음 * 2를 한 결과와, 모두 더한 결과와 빼기가 불가능.
2 * (a + b + c) - (a + a + b + b + c) = c
그래서 추가 메모리를 쓰지 않기위해 정렬해서 찾아내는 방법으로 구현.
역시 성능이 안좋게 나왔기 때문에 O(n) 솔루션을 봤는데 XOR 게이트를 활용.
a XOR a = 0 / 0 XOR a = a 라는 XOR 특징을 활용해 중복숫자를 모두 지워줌.
'''

# XOR
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for n in nums:
            a ^= n
        return a

# Sort
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n_len = len(nums)
        if n_len == 1:
            return nums[0]
        nums.sort()
        for i in range(1, n_len, 2):
            if nums[i-1] != nums[i]:
                return nums[i-1]
        return nums[-1]
'''