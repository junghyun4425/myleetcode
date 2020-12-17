# Problem Link: https://leetcode.com/problems/generate-parentheses/

'''
문제 요약: n개의 가능한, 열림과 닫힘이 정확히 맞는 괄호를 모두 나열하는 문제.
ask: 3
answer: ["((()))","(()())","(())()","()(())","()()()"]

해석:
괄호2개의 모양으로 만들수 있는 모든 경우의 수는 2^2n. 모든 경우의 수를 만들기 위해 for문 보다는 재귀식을 사용하는것이 효율적.
모든 경우의 수를 만들고, 완벽히 열리고 닫히는지 확인하기까지하면 해결. 하지만 여기서 쓸데없는 계산이 추가적으로 들어감.
예를 들어, 시작부터 ')' 들어가거나,')' 갯수가 n개이기도 전에 '('갯수가 n개인 경우는 확인 할 필요가 없음.
따라서 규칙을 생각해 보면,
1 - 재귀함수를 호출할때 시작은 무조건 '('.
2 - '(' 갯수 l, ')' 갯수 r 을 재귀함수 인자로 추가.
3 - 재귀호출 처음은 '(' 이 n까지 나열.
4 - 그 이후는 r < l 까지 재귀로 ')' 를 추가. (r 갯수는 l을 넘길 수 없음)
5 - 길이가 맞으면 정답에 추가.
코드는 간단해 보이지만 규칙을 정확하게 찾는데 시간이 꽤 걸림. 다시풀어보기.
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def checkAndGenerate(a='', l=0, r=0):
            if len(a) == 2 * n:
                ans.append(a)
            if l < n:
                checkAndGenerate(a + '(', l + 1, r)
            if r < l:
                checkAndGenerate(a + ')', l, r + 1)

        ans = []
        checkAndGenerate()
        return ans