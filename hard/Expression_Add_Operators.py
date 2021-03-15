# Problem Link: https://leetcode.com/problems/expression-add-operators/

'''
문제 요약: 숫자로 구성된 문자열이 주어질때 target을 결과로 계산되는 모든 수식의 조합을 반환하는 문제.
ask: num = "123", target = 6
answer: ["1*2*3","1+2+3"]

해석:
DFS방식으로 시간복잡도 성능이 안좋게 나오겠지만 해결할 수 있음.
쉽게 해결할 수 있을거라 생각했는데 몇가지 예외를 고려하지 않아서 코드를 고치느라 시간이 오래걸림.
1. 1+2*3 의 경우 곱셈부터 해야함
2. 123이 있으면 1,2,3 만되는게 아니라 12, 3 123 다 됨.
3. 100 에서 00은 숫자로 취급하면 안됨
이런 예외들을 만나서면서 많은 시간을 보냄.

우선 1번 해결은 간단함. 재귀함수르 통해 인자로 계산결과를 받아오는데 이전값 2를 함께 인자로 보냄.
1+2 면 3이지만 여기서 이전값 2를 함께 가져와서 1+2-2+2*3 을 하면 뒤의 곱을 먼저 계산한 효과를 보게되므로 문제없이 해결.
2번은 생각지 못해서 for loop를 하나 넣어줘서 해결. 이때 i가 의미하는 바는 길이이고 모든 숫자 길이에 대해 DFS를 수행.
3번은 DFS하기 전에 i값을 검사해서 해결.
결과는 성능면에서 최상위권이기 때문에 이런식으로 푸는게 맞는것 같음.
'''

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []
        n_len = len(num)
        def dfs(cur, path, res, pre_n):
            if cur == n_len:
                if res == target:
                    ans.append(path)
                return
            for i in range(cur, n_len):
                val = num[cur:i+1]
                if len(val) > 1 and val[0] == '0':
                    continue
                n = int(val)
                if not path:
                    dfs(i+1, str(val), n, n)
                else:
                    dfs(i+1, path+'+'+val, res+n, n)
                    dfs(i+1, path+'-'+val, res-n, -n)
                    dfs(i+1, path+'*'+val, res-pre_n+pre_n*n, pre_n*n)
        dfs(0, '', 0, 0)
        return ans