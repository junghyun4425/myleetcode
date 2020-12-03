# Problem Link: https://leetcode.com/problems/reverse-integer/

'''
문제 요약: 정수를 받아 반대로 출력. 단, 결과가 integer 허용범위를 넘어서면 0으로 출력.
ask: -123
answer: -321

해석:
간단히 정수를 문자열로 치환해서 순서를 바꾸면 되는 문제.
'''

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        s = str(x)
        minus = False
        if s[0] == '-':
            minus = True
            s = s[1:]

        ans = int(s[::-1])
        if ans > 2 ** 31 - 1:
            return 0

        return -ans if minus else ans