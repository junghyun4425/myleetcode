# Problem Link: https://leetcode.com/problems/simplify-path/

'''
문제 요약: 입력으로 들어오는 문자열을 해석하는 문제. (숫자 뒤에 대괄호가 나오면 그 배수만큼 문자를 곱해줌, 숫자가 문자로 들어오는 경우는 없다 가정)
ask: s = "3[a2[c]]"
answer: "accaccacc"

해석:
숫자가 문자로 들어가는일은 없고, 숫자다음엔 무조건 대괄호만 나온다는 제약조건 때문에 간단하게 스택으로 풀수 있었던 문제.
스택에 숫자가 나올때는 곱셈을 해야하기 떄문에 따로 숫자를 저장해 둠.
대괄호가 열린 문자 '[' 가 들어오면, 스택에 곱할 숫자와 문자를 스택에 저장해서 쌓아올려감.
닫힌 문자 ']'가 들어오면, 앞에 숫자가 있는경우는 현재 스택의 문자열에 곱해주고, 없는경우는 이전의 스택 문자에 그대로 붙여주면 됨.
'''

class Solution:
    def decodeString(self, s: str) -> str:
        stack = ['']
        mul = 0
        for c in s:
            if c.isdigit():
                mul = mul * 10 + int(c)
            elif c == '[':
                stack.append(mul)
                stack.append('')
                mul = 0
            elif c == ']':
                cur = stack.pop()
                cur *= stack.pop()
                if stack[-1].isdigit():
                    stack.append(cur)
                else:
                    stack[-1] += cur
            else:
                stack[-1] += c
        return ''.join(stack)