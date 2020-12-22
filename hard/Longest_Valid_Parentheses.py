# Problem Link: https://leetcode.com/problems/longest-valid-parentheses/

'''
문제 요약: 가장 긴 완벽한 괄호쌍의 길이를 반환하는 문제.
ask: ))()()()())
answer: 8

해석:
처음에 스택을 활용해 O(n)의 시간복잡도로 풀려고 도전. 스택에 '(' 의 캐릭터를 넣어서 풀려했지만 ()(() 나왔을때 해결이 불가능. (4가 반환이돼서 오답)
따라서 스택에 캐릭터대신 위치값인 숫자를 저장해서 해결. 처음에 -1을 넣는 이유는 시작부터 ()와 같이 완벽한 괄호쌍이 나왔을떄를 대비.
문제를 보고 DP로도 풀수 있다는걸 느꼈기 때문에 시간나면 DP를 활용해 풀어보도록 할 생각.
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    max_len = max(max_len, i - stack[-1])
                else:
                    stack.append(i)

        return max_len