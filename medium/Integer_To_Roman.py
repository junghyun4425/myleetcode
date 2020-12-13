# Problem Link: https://leetcode.com/problems/integer-to-roman/

'''
문제 요약: 정수를 받아 로마숫자로 바꾸는 문제.
ask: 4
answer: IV

해석:
Dictionary를 쓰면 너무 간단하게 풀리는 문제.

'''

class Solution:
    def intToRoman(self, num: int) -> str:
        m = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        s = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        ans = ''
        for n in s:
            qout = num // n
            ans += m[n] * qout
            num -= n * qout
        return ans