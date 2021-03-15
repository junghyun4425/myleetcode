# Problem Link: https://leetcode.com/problems/different-ways-to-add-parentheses/

'''
문제 요약: 입력으로 들어오는 수식에 괄호를 넣을수 있는 모든 경우의 수에 대해 결과를 구하는 문제. (단, 괄호, 나누기는 없음)
ask: "2-1-1"
answer: [0,2] (((2-1)-1) = 0, (2-(1-1)) = 2)

해석:
재귀를 통해서 나눈다음 합치는 방법으로 해결하면 될것같은데 이런식의 Divide and Conquer 경험이 거의 없어 감이 안잡힘.
감이 안잡히는 요인을 살펴보면,
1.도대체 어디서 나눠야 하는지를 모름.
2.for문이 여러개 들어갈텐데 시간복잡도는 괜찮을까?
1번 고민을 해결하기 위해 먼저 regular expression으로 숫자, 기호단위로 나눈다음 left, operation, right 세단위로 나누기로 함.
이게 가능했던 이유는 앞에 무조건 숫자부터 시작하고 끝에도 숫자로 끝난기 때문.
2번 고민은 사실 최적화문제 같은데 일단 풀어보고 생각하기로 결정.

풀이
숫자와 기호를 나눈다면 첫번째 숫자 두번째 기호 ... 이런식으로 진행될것.
나누는 구간은 operation 기호로 왼쪽과 오른쪽의 결과들을 모을것임. 결과는 여러개가 되기 때문에 list들을 만들어 서로 값을 만들어가야함.
즉, 왼쪽에서 나올수있는 모든 경우의수와 오른쪽의 모든 경우의수끼리 operation 을통해 계산해주면 됨.
for문이 3중첩인데도 성능이 굉장히 좋게 나옴. 이런방식으로 푸는게 의도된 방향이었던것 같음.
생각보다 Div_and_Con 문제를 푸는데 익숙하지않아 오래 걸려서 이 문제를 나중에 꼭 복습 하는걸로.
'''

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        exp = re.findall(r'(\d+|\W)', expression)
        def div_and_con(exp):
            if len(exp) == 1:
                return [int(exp[0])]
            res = []
            for op in range(1, len(exp), 2):
                lefts = div_and_con(exp[:op])
                rights = div_and_con(exp[op+1:])
                for l in lefts:
                    for r in rights:
                        if exp[op] == '+':
                            res.append(l+r)
                        elif exp[op] == '-':
                            res.append(l-r)
                        else:
                            res.append(l*r)
            return res
        return div_and_con(exp)