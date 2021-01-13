# Problem Link: https://leetcode.com/problems/maximal-rectangle/

'''
문제 요약: 2차원 숫자 배열에서 가장 크게 만들 수 있는 사각형의 넓이를 반환하는 문제.
ask: [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
answer: 6

해석:
해결하는 방법을 사실 이전문제 Largest_Rectangle_In_Histogram을 풀어봤기 때문에 풀 수 있었음.
DP방식으로 각각의 줄마다 히스토그램을 만들고 난 후, 그 히스토그램에 대해서 모두 이전의 알고리즘을 대입하면 쉽게 해결이 가능.
고로, row마다 DP를 적용해 히스토그램을 만들고 스택읉 통해 최대 사각형의 넓이를 구해서 최대값을 찾음.
'''

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        h, w, ans = len(matrix), len(matrix[0]), 0
        dp = [[0] * w for _ in range(h)]
        for i in range(h):
            for j in range(w):
                if i == 0:
                    dp[0][j] = int(matrix[0][j])
                else:
                    dp[i][j] = dp[i-1][j] + int(matrix[i][j]) if matrix[i][j] == '1' else 0
            stack = []
            for index, v in enumerate(dp[i]):
                start = index
                while stack and v < stack[-1][1]:
                    s = stack.pop()
                    ans = max(ans, s[1] * (index - s[0]))
                    start = s[0]
                stack.append((start, v))
            for s in stack:
                ans = max(ans, s[1] * (w - s[0]))
        return ans