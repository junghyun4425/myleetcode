# Problem Link: https://leetcode.com/problems/maximal-rectangle/

'''
문제 요약: 2차원 숫자 배열에서 가장 크게 만들 수 있는 사각형의 넓이를 반환하는 문제.
ask: [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
answer: 6

해석:
해결하는 방법을 사실 이전문제 Largest_Rectangle_In_Histogram을 풀어봤기 때문에 풀 수 있었음.
DP방식으로 각각의 줄마다 히스토그램을 만들고 난 후, 그 히스토그램에 대해서 모두 이전의 알고리즘을 대입하면 쉽게 해결이 가능.
고로, row마다 DP를 적용해 히스토그램을 만들고 스택읉 통해 최대 사각형의 넓이를 구해서 최대값을 찾음.

Review
히스토그램 방식으로 푼다는게 아직 기억나서 다시푸는데 어려움이 없었던 문제.
다만, row단위의 DP를 구할때 이차원 배열이 아니라 1차원 배열로도 충분히 계산 가능한 것을 알았기에 이 부분은 최적화.
start point 계산하는 부분이 아직 적응되지 않아서 오래걸림. 스택에서 pop() 한 다음, 스택에 저장할때 start 포인트를 주의해야 함.
'''

# Second Try: Same algorithm. Optimized space complexity O(hw) to O(w)
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        h, w = len(matrix), len(matrix[0])
        max_len = 0
        dp = [0] * w
        for i in range(h):
            for j in range(w):
                dp[j] = int(matrix[i][j]) + dp[j] if matrix[i][j] == '1' else 0
            stack = []
            for j, n in enumerate(dp):
                start = j
                while stack and n < stack[-1][1]:
                    bar = stack.pop()
                    max_len = max(max_len, bar[1] * (j - bar[0]))
                    start = bar[0]
                stack.append((start, n))
            for s in stack:
                max_len = max(max_len, s[1] * (w - s[0]))
        return max_len

# First Try
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
'''