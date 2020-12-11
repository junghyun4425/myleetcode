# Problem Link: https://leetcode.com/problems/string-to-integer-atoi/

'''
문제 요약: atoi 작성하기. string to integer
ask: "-0073"
answer: -73

해석:
함수 int() 를 사용하지 않고 문자열을 숫자로 바꾸는 문제.
간단하게 if문을 여럿 사용해 해결하려 했으나, 생각보다 많은 변수를 마주쳐서 실패를 반복함. ex) 0000-123, -00000123, +-111 등.
따라서 정규식을 통해 앞에 +, -, 아무것도 없는 상태 세가지 경우의수를 두고, 뒤에 숫자만 오도록 매칭을 함.
뒤의 숫자인 문자열을 숫자로 바꾸는 작업은 수월하게 마무리.
'''

import re

class Solution:
    def myAtoi(self, s: str) -> int:
        minus = False
        num_s = re.match('^(\+|\-|)\d+', s.lstrip())
        if not num_s:
            return 0
        num_s = num_s.group()
        n = 0
        for c in num_s:
            if c == "-" or c == "+":
                minus = True if c == "-" else False
            else:
                if n == 0 and c == '0':
                    continue
                i = ord(c) - 48
                n = (n * 10) + i

        n = -n if minus else n
        if n > (2 ** 31) - 1:
            n = (2 ** 31) - 1
        elif n < -(2 ** 31):
            n = -(2 ** 31)
        return n