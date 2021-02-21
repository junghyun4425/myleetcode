# Problem Link: https://leetcode.com/problems/unique-paths/

'''
문제 요약: 로봇의 시작점(0,0) 부터 끝점(m,n) 까지 가는 경로의 수를 계산하는 문제. (단, 로봇은 아래, 오른쪽으로만 이동 가능)
ask: m = 7, n = 3
answer: 28

해석:
바로 생각이 나는건 재귀함수로, (0,0)에서 갈수 있는 경우의수 (1,0) 과 (0,1) 을 더해주면서 끝까지 가면 완료.
하지만 DP로도 풀 수 있는것이 생각났기에 익숙치 않은 방법으로 풀기로 결정.
우선, (x,0) (0,y) 에서 모든 x와 y값에 대해 1로 정의할 수 있음. ((0,0)에서 로봇이 갈수있는 경로는 오직 하나뿐이므로)
dp(m,n) = dp(m-1,n) + dp(m,n-1) 라는 간단한 점화식을 구할 수 있고, 그대로 구현하면 해결됨.

Review
이차원 배열의 DP를 일차원으로 구현이 가능. (이전값을 참조할때 현재위치 기준으로 왼쪽과 상단을 더해주기 때문에 모든 향을 따로 저장할 필요 없음)
따라서 점화식은,
dp[i] = dp[i] + dp[i-1]
로 계산하면 되는 간단한 문제.
'''

# Second Try (Optimized Space complexity O(mn) to O(n))
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for i in range(1, n):
                dp[i] += dp[i-1]
        return dp[-1]

# First Try
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
'''