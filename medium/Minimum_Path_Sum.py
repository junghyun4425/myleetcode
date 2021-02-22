# Problem Link: https://leetcode.com/problems/minimum-path-sum/

'''
문제 요약: 이동하는 코스트가 적힌 2차원 배열에서 가장 비용이 덜드는 방법의 경로를 합을 반환하는 문제.
ask: grid = [[1,3,1],[1,5,1],[4,2,1]]
answer: 7 (1 -> 3 -> 1 -> 1 -> 1 이 가장 작은 비용의 거리)

해석:
간단한 DP 문제로, 점화식 dp(i, j) = min(dp(i-1, j), dp(i, j-1)) + grid(i, j) 만 알면 구현이 가능.
i 혹은 j가 1보다 작을 때는 dp(i, j) = grid[i][0] + dp[i-1][0] 과 같이 이전 경로의합과 현재 비용을 더함.

Review
처음부터 다시 풀어보는 도중, 굳이 dp를 안만들고 입력으로 들어오는 grid를 바꿔버리면 메모리 사용없이 풀수 있지 않을까 하는 생각이 떠오름.
따라서 따로 dp 리스트를 만들지 않고 그자리에서 점화식을 대입. 결과는 약간의 메모리면에서 성능 향상.
크게 최적화한 부분은 없고 다시한번 풀어봤다는 점에서 의미를 뒀음.
'''

# Second Try Optimized Space complexity O(hw) to O(1)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])
        for i in range(1, h):
            grid[i][0] += grid[i-1][0]
        for j in range(1, w):
            grid[0][j] += grid[0][j-1]
        for i in range(1, h):
            for j in range(1, w):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]

# First Try
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])
        dp = [[0] * w for _ in range(h)]
        dp[0][0] = grid[0][0]
        for i in range(1, h):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        for j in range(1, w):
            dp[0][j] = grid[0][j] + dp[0][j-1]

        for i in range(1, h):
            for j in range(1, w):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]
'''