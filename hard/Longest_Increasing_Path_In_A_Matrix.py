# Problem Link: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

'''
문제 요약: 2차원 배열이 주어질때, 증가하는 숫자들의 최대 길이를 구하는 문제.
ask: matrix = [
[9,9,4],
[6,6,8],
[2,1,1]]
answer: 4 ([1, 2, 6, 9] 가 가장 긴 증가하는 숫자열)

해석:
문제만 대충 봐도 DP로 풀면 효율적인지 바로 감이 잡히는 유형.
이미 방문한곳의 카운팅을 미리 저장해놓으면 다음에 다시들렸을때 다시 계산하지 않아도 되는 이점을 살려서 구현하면 효율성이 극대화.
모든 배열을 하나씩 찾으면서 4방향에 대해 DFS방식으로 탐색을 수행.
DFS로 탐색하면서 결과를 시작점에서 카운팅했을때 위치의 DP에 저장해놓으면 재사용이 가능.
'''

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        h, w = len(matrix), len(matrix[0])
        di = [(1,0),(0,1),(-1,0),(0,-1)]
        dp = [[-1]*w for _ in range(h)]
        def dfs(i, j):
            if dp[i][j] != -1:
                return dp[i][j]
            res = 1
            for d in di:
                new_i, new_j = i + d[0], j + d[1]
                if 0 <= new_i < h and 0 <= new_j < w:
                    if matrix[i][j] < matrix[new_i][new_j]:
                        res = max(1 + dfs(new_i, new_j), res)
            dp[i][j] = res
            return res
        return max([dfs(i,j) for i in range(h) for j in range(w)])