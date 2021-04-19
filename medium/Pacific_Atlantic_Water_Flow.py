# Problem Link: https://leetcode.com/problems/pacific-atlantic-water-flow/

'''
문제 요약: pacific과 atlantic 사이를 오가는 물의 위치들을 찾는 문제.
(물은 낮은곳에서 같거나 높은곳으로만 흐르고, 왼쪽 우측 경계면은 모두 pacific, 모든 오른쪽 아래 경계면은 atlantic 임.)
ask: heights = [
[1,2,2,3,5],
[3,2,3,4,4],
[2,4,5,3,1],
[6,7,1,4,5],
[5,1,1,2,4]
]
answer: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

해석:
왼쪽, 위쪽의 경계면에서 오른쪽, 아래쪽의 경계면까지 도달하는 점들의 좌표를 구하면 되는 문제.
하나의 경로에 관련된 모든 좌료들을 찍어야 하기 때문에 visited에 모든 경로들을 기록할 겸 방문했는지 안했는지 판별하는 용도로도 씀.
BFS를 통해 모든 경로를 다 기록하되, pacific에 대해서도 atlantic에 대해서도 모두 기록을 함.
둘다 기록을 하는 이유는 양쪽에서 흐르는 물이 겹친다면 두군데서 물이 함께 흐른다는 뜻이므로, 양 해양간 물이 흐른다는 것을 의미하기 때문.
따라서 두 해양의 물이 흐르는 모든 경로를 찾고, set에서 함수 intersection 혹은 & 로 겹치는 좌표만 저장하면 답이 됨.
'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        h, w = len(heights), len(heights[0])
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        def bfs(starts):
            queue = deque(starts)
            visited = set(starts)
            while queue:
                i, j = queue.popleft()
                for d in direction:
                    new_i, new_j = i + d[0], j + d[1]
                    if 0 <= new_i < h and 0 <= new_j < w and heights[i][j] <= heights[new_i][new_j] and (new_i, new_j) not in visited:
                        queue.append((new_i, new_j))
                        visited.add((new_i, new_j))
            return visited
        pacific = [(i, 0) for i in range(h)] + [(0, j) for j in range(1, w)]
        atlantic = [(h-1, i) for i in range(w)] + [(j, w-1) for j in range(h-1)]
        pacific_set = bfs(pacific)
        atlantic_set = bfs(atlantic)
        return pacific_set & atlantic_set