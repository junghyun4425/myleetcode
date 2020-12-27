# Problem Link: https://leetcode.com/problems/permutations-ii/

'''
문제 요약: 숫자 리스트의 모든 순열을 찾는 문제. (중복된 숫자가 포함되며, 결과에선 중복결과는 빼야함)
ask: [1,1,2]
answer: [[1,1,2],[1,2,1],[2,1,1]]

해석:
이전의 Permutations문제와 동일하지만, 결과에 넣기전에 구한 리스트가 중복인지 아닌지 체크하고 없으면 넣게끔 추가함.
예상대로 서칭을 한번더 해야하는 작업이다보니 성능, 메모리 면에서 모두 안좋은 퍼포먼스를 보임.
따라서 수정할 계획.
'''

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def backtrack(rest_nums, vals):
            if not rest_nums:
                if not vals in ans:
                    ans.append(vals)
                return
            for i, n in enumerate(rest_nums):
                backtrack(rest_nums[0:i] + rest_nums[i + 1:], vals + [n])

        backtrack(nums, [])
        return ans