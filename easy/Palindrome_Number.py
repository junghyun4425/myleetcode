# Problem Link: https://leetcode.com/palindrome-number/

'''
문제 요약: 정수를 받아 좌우대칭(palindromic) 인지 판단하는 함수를 구현.
ask: 121
answer: True

해석:
정수를 문자열로 바꾸면 간단히 해결되지만, 문제에서는 변환함수를 쓰지 않는것을 제한으로 두자고 함.
따라서 10씩 나눠서 한자리수씩 리스트에 저장하고 좌우대칭인지 판별을 함.
'''

import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        nums = []
        while x:
            nums.append(x % 10)
            x //= 10
        for i in range(math.ceil(len(nums) / 2)):
            if nums[i] != nums[-1 - i]:
                return False
        return True