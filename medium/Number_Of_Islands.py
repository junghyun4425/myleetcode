# Problem Link: https://leetcode.com/problems/number-of-islands/

'''
문제 요약: 2차원 배열에 '0'은 물, '1'은 섬을 나타낼때, 섬이 몇개 있는지 구하는 문제.
ask: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
answer: 3

해석:
DFS 혹은 BFS로 모든 붙어있는 '1'을 찾아서 카운팅하는 문제.
주의할 점은, '1'이 visited 되었는지 아닌지를 표시해야 함. visited[] 배열을 쓰거나, '1' 을 'x'와 같이 다른 문자로 변환시켜야 함.
추가 메모리를 줄이기 위해 'x' 로 방문했다는 표시를 하고 탐색.
DFS로 몇번 탐색을 수행했는지가 정답을 의미.
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        h, w = len(grid), len(grid[0])
        di = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ans = 0
        def dfs(i, j):
            if 0 > i or i >= h or 0 > j or j >= w:
                return
            if grid[i][j] == '1':
                grid[i][j] = 'x'
            else:
                return
            for d in di:
                dfs(i + d[0], j + d[1])

        for i in range(h):
            for j in range(w):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i, j)
        return ans