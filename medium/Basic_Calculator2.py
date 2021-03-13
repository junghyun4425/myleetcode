# Problem Link: https://leetcode.com/problems/basic-calculator-ii/

'''
문제 요약: 괄호 없는 사칙연산이 적용된 계산식의 결과를 구하는 문제.
ask: "3+2*2"
answer: 7

해석:
이전 Basic_Calculator 문제와 마찬가지로 쉽게 다가갔지만 의외로 시간이 걸린 문제.
이 문제에서 어려웠던점은 + 혹은 - 연산자를 만날경우 stack에 넣어두고 * 할땐 계산을 한 뒤 스택에 넣어야 하는데 뒤의 숫자를 모르기 때문에 계산이 불가능.
뒤에 숫자를 계산하기 위해 현재 operation을 비교하는게 아니라 이전의 pre_op를 저장해뒀다가 비교하는 것.
여기서 문제는 마지막에는 항상 숫자로 끝나기 때문에 마지막엔 계산하지 않는다는점. 따라서 s 뒤에 '+' 라는 가짜 수식을 넣어줌으로써 계산을 완성함.
한가지 더 주의해야할 것은 나누기에서 음수가 나올경우. 음수일때와 양수일때 나누기를 조금 다르게 해주면 해결 됨.
마지막 단계로 stack의 모든 값을 합해주면 결과가 나옴.
'''

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        val = 0
        s += '+'
        pre_op = '+'
        for c in s:
            if c.isdigit():
                val = (10*val) + int(c)
            elif c == ' ':
                continue
            else:
                if pre_op in "+-":
                    val = val if pre_op == '+' else -val
                    stack.append(val)
                elif pre_op in "*":
                    stack.append(stack.pop() * val)
                elif pre_op in "/":
                    if stack[-1] > 0:
                        stack.append(stack.pop() // val)
                    else:
                        stack.append(-1*(-stack.pop() // val))
                val = 0
                pre_op = c
        return sum(stack)