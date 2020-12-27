# Problem Link: https://leetcode.com/problems/permutations/

'''
문제 요약: 숫자 리스트의 모든 순열을 찾는 문제.
ask: [1,2,3]
answer: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

해석:
for문으로 수행할 수 있었지만 재귀함수의 연습이 부족해 백트래킹 방식으로 문제를 해결.
rest_nums 에 남은 숫자들을, vals에는 여태 만든 순열의 상태를 나타내는 리스트 두개를 가지고 재귀함수를 구현.
역시나 성능은 빠르게 평가되었지만 메모리 사용량이 많았던 결과.
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(rest_nums, vals):
            if not rest_nums:
                ans.append(vals)
                return
            for i, n in enumerate(rest_nums):
                backtrack(rest_nums[0:i] + rest_nums[i + 1:], vals + [n])

        backtrack(nums, [])
        return ans