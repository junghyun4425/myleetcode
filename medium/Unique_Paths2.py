# Problem Link: https://leetcode.com/problems/unique-paths-ii/

'''
문제 요약: 로봇의 시작점(0,0) 부터 끝점(m,n) 까지 가는 경로의 수를 계산하는 문제. (단, 로봇은 아래, 오른쪽으로만 이동 가능, 장애물이 하나 존)
ask: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]] (1이 장애물의 위치)
answer: 2

해석:

'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        h = len(obstacleGrid)
        w = len(obstacleGrid[0])
        dp = [[0] * (w+1) for _ in range(h+1)]
        dp[1][1] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(1, h+1):
            for j in range(1, w+1):
                if i == 1 and j == 1:
                    continue
                if i <= h and j <= w and obstacleGrid[i-1][j-1] == 1:
                    dp[i][j] = 0
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[h][w]