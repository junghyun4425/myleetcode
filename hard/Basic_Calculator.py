# Problem Link: https://leetcode.com/problems/basic-calculator/

'''
문제 요약: 사칙연산 중 덧셈과 뺄셈을 수행해 계산식의 결과를 구하는 문제.
ask: "(1+(4+5+2)-3)+(6+8)"
answer: 23

해석:
금방 해결할 수 있을거라 생각했지만 의외로 어려운점이 몇군데 있었음.
1.앞에 숫자없이 음수가 올때
2.괄호안과 바깥의 결과를 처리하는 방법
2번은 조금만 생각해보면 결과 자체를 stack에 저장하면 해결이 되기 때문에 문제없지만 1번의 경우는 조금 복잡했음.
결론은 부호 자체를 따로 변수로 두고 이또한 stack에 함꼐 저장하는 방법을 선택함.
만약 숫자를 만나면 값을 val에 저장. 연속적으로 숫자가 나올수 있으니 10을 곱해가면서 저장해야 함.
'+'를 만나면 sign은 양수를, res에 값이 있다면 더해줌.와 (res는 괄호안의 결과값을 의미함)
'-'를 만나면 위와 반대.
'('를 만나면 여태 계산했던 res와 현재 sign을 stack에 저장.
')'를 만나면 res를 구하고 sign응 pop해서 곱해줌. 마지막으로 이전의 res값과 더해주면 끝.
'''

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        val = res = 0
        sign = 1
        for c in s:
            if c.isdigit():
                val = (val*10) + int(c)
            elif c in '-+':
                res += sign * val
                sign = 1 if c == '+' else -1
                val = 0
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif c == ')':
                res += sign * val
                res *= stack.pop()
                res += stack.pop()
                val = 0
        return res + sign * val