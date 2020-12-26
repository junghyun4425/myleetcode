# Problem Link: https://leetcode.com/problems/combination-sum-ii/

'''
문제 요약: 숫자 리스트에서 target을 만들 수 있는 모든 조합을 반환. (중복은 제거, 같은 숫자를 재활용 불가능.)
ask: [2,5,2,1,2], target = 5
answer: [[1,2,2],[5]]

해석:
Combination_Sum 과 유사한 문제라, 풀었었던 DFS를 조금만 더 활용하면 해결 할 수 있는 문제.
원래의 숫자리스트 candidates를 하나씩 줄여가면서 반복사용을 피했고, for문 안에 if문으로 중복사용을 제거해서 해결.
그외에는 Combination_Sum과 동일.
'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def dfs(rest_candid, vals, next_target):
            if next_target == 0:
                ans.append(vals)
            if next_target < 0:
                return
            for i, n in enumerate(rest_candid):
                if i > 0 and n == rest_candid[i-1]:
                    continue
                dfs(rest_candid[i+1:], vals + [n], next_target - n)

        dfs(candidates, [], target)
        return ans