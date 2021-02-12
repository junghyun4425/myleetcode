# Problem Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/

'''
문제 요약: Reverse_Polish_Natation 의 방식으로 배열에 숫자와 기호가 들어올때, 결과값을 계산해 반환하는 문제. (0으로 나눠지는 경우는 들어오지 않음)
ask: ["2", "1", "+", "3", "*"]
answer: 9 ( (2 + 1) * 3 )

해석:
숫자를 스택에 쌓아가면서 기호를 만나면 두개의 스택을 꺼내온뒤 계산.
계산한 결과를 다시 스택에 쌓으면서 진행하면 최종적으로 스택에 하나의 숫자만 남게되며, 이 숫자는 결과값이 됨.
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {"+": lambda x,y: x+y, "-": lambda x,y: x-y, "/": lambda x,y: int(x/y), "*": lambda x,y: x*y}
        for t in tokens:
            if t in op:
                stack.append(op[t](stack.pop(-2), stack.pop()))
            else:
                stack.append(int(t))
        return stack[0]