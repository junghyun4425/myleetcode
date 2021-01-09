# Problem Link: https://leetcode.com/problems/combinations/

'''
문제 요약: 입력으로 들어오는 n과 k에 대한 모든 조합을 반환하는 문제.
ask: n = 4, k = 2
answer: [[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]]

해석:
조합 n이 1부터 n까지 순차적인 값만 들어있기 때문에, 이전의 값보다 큰값들만 재귀를 수행하면 됨.
따라서 현재까지 완성된 조합을 리스트에 담을 comb와, 담아야할 숫자 rest, 이전값을 인자로 받는 함수가 필요.
rest값이 0이 될때 ans에 붙여넣으면 해결.
'''

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def recursive(prev, comb, rest):
            if rest == 0:
                ans.append(comb)
                return
            for i in range(prev + 1, n + 1):
                recursive(i, comb + [i], rest - 1)

        recursive(0, [], k)
        return ans