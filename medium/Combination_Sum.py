# Problem Link: https://leetcode.com/problems/combination-sum/

'''
문제 요약: 숫자 리스트에서 target을 만들 수 있는 모든 조합을 반환. (중복은 제거)
ask: [2,3,6,7], target = 7
answer: [[2,2,3],[7]]

해석:
재귀함수 (DFS) 방식으로 풀려했는데 생각보다 여러 난관에 봉착해서 시간이 오래 걸린 문제. 무조건 다시 풀어봐야함.
다른방법인 DP 방식으로도 풀수 있으니 다시풀땐 이 방법으로.
이 문제에서 하나 큰 깨달음을 얻은 부분은 "append" 와 "+" 를 사용한 방식의 차이점.
append(~~) 는 앞리스트에 뒤의 숫자를 포함시켜 주지만 return 값은 None. + 는 리턴 자체가 리스트.
따라서 dfs(a.append(3), 4) 는 Nonetype을 반환하는 append때문에 에러가 생김.
따라서 이때는 dfs(a + [3], 4) 를 해주는 것이 옳음.
'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def dfs(vals, next_target):
            if not next_target:
                ans.append(vals)
            for i in candidates:
                if i > next_target:
                    break
                elif not vals or i >= vals[-1]:
                    dfs(vals + [i], next_target - i)

        dfs([], target)
        return ans