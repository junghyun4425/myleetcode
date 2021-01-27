# Problem Link: https://leetcode.com/problems/triangle/

'''
문제 요약: 삼각형 모양으로 깊이가 깊어지는 2차원 배열에서 최소값을 가지는 경로의 합을 반환. 단, 깊이로 내려갈때 갈수있는 방법은 j or j+1 두가지.
ask: [[2],[3,4],[6,5,7],[4,1,8,3]]
answer: 11 (2 -> 3 -> 5 -> 1)

해석:
연습삼아 재귀함수로 빠르게 풀어본 다음 시간초과를 맛보고 DP방식으로 다시 품.
가장 아래있는 사이즈의 크기를 메모이제이션으로 활용. depth를 위로 올라가면서 최소값을 찾는 방법.
점화식을 간단히 표기해보자면,
dp[j] = triangle[i][j] + min(dp[j], dp[j+1])

순차적으로 dp값에 변화를 주면 굳이 2차원 배열로 만들지 않아도 문제없이 수행됨. 이전의 최소값중 j번째와 j+1번째 최소값의 최소값을 더해주면 경로내에서 최소값이 됨.
그러면 가장 높은레벨에 도착했을때 dp[0]이 모든 경로내 최소값이 되는 원리.
'''

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        bottoms = triangle[-1][:]
        for i in reversed(range(len(triangle)-1)):
            for j in range(i+1):
                bottoms[j] = triangle[i][j] + min(bottoms[j:j+2])
        return bottoms[0]