# Problem Link: https://leetcode.com/problems/remove-element/

'''
문제 요약: 숫자 리스트에서 target의 숫자를 제거하는 문제 (단, 새로운 배열을 만들지 않고)
ask: [3,2,2,3], target = 3
answer: output = 2, array = [2,2,_,_]

해석:
target이 아닌 숫자면 output을 하나씩 더해주고 target인 숫자는 무시하면 간단하게 해결되는 문제.
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = 0

        for v in nums:
            if v != val:
                nums[ans] = v
                ans += 1
        return ans