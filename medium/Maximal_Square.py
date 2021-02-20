# Problem Link: https://leetcode.com/problems/maximal-square/

'''
문제 요약: 연속된 1의 최대 정사각형 크기를 구하는 문제.
ask: [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
answer: 4

해석:
정사각형의 넓이를 바로 구하기 보다는 최대 길이를 DP방식으로 찾도록 함.
정사각형이어야 하기 때문에 현재의 값이 1이고 좌측, 상단, 좌상단 세곳이 1이어야만 2가 될 수 있는 제약이 있음.
따라서 Bottom-up 방식으로 위의 조건에 만족할때만 길이를 하나씩 늘려주면 됨.
이를 점화식으로 표현하면,
dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1            if matrix == '1'
         = 0                                                        if matrix == '0'
dp의 처음이나 마지막에 최대길이를 저장하는게 아니기 때문에 중간에 max_len을 비교해서 최대값을 갱신해야 함.
현재는 공간을 O(h*w) 를 사용하지만, O(w) 만큼 줄일 수 있음.
dp[i-1][j-1]만 따로 prev 로 저장해놓고, dp[i][j-1] dp[i-1][j]는 배열에 저장되는 순서기 때문에 셋을 한번에 비교할 수 있음.
'''

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        h, w = len(matrix), len(matrix[0])
        dp = [[0]*(w+1) for _ in range(h+1)]
        max_len = 0
        for i in range(1, h+1):
            for j in range(1, w+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                    max_len = max(max_len, dp[i][j])
        return max_len ** 2