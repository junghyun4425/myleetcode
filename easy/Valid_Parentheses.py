# Problem Link: https://leetcode.com/problems/valid-parentheses/

'''
문제 요약: 괄호가 유효한지 검사하는 문제.
ask: "{[]}"
answer: True

해석:
Stack을 활용하면 간단하게 풀 수 있는 문제.
검색해보니 해시맵을 쓰면 조금더 빠르게 수행이 가능한 것을 확인.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '{':
                stack.append('}')
            elif c == '[':
                stack.append(']')
            elif c == '(':
                stack.append(')')
            else:
                if not stack or c != stack.pop():
                    return False
        return True if not stack else False