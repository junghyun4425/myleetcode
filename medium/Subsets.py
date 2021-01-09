# Problem Link: https://leetcode.com/problems/subsets/

'''
문제 요약: 숫자 리스트의 power set을 리스트에 담아 반환하는 문제.
ask: [1,2,3]
answer: [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]

해석:
멱집합을 구하기 위해서는 보기로 주어진 숫자들의 갯수 0 ~ n 까지의 각각 조합을 만들면 해결.
0일때: []
1일때: [1], [2], ..., [n]
2일때: [1,2], [1,3], ... [n-1,n]
...
n일때: [1,2,3,...,n]
따라서 이전에 만들었던 조합의 방식(재귀함수)을 for문 안에 넣으면 끝.
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n_len = len(nums)
        def combinations(cur, comb, l):
            if l == 0:
                ans.append(comb)
                return
            for i in range(cur, n_len):
                combinations(i+1, comb + [nums[i]], l-1)
        for i in range(n_len+1):
            combinations(0, [], i)
        return ans