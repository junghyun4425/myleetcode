# Problem Link: https://leetcode.com/problems/range-sum-query-2d-immutable/

'''
문제 요약: 2차원 배열의 범위에 존재하는 값들을 모두 더해서 반환해주는 클래스를 구현하는 문제.
ask:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
sumRegion(2, 1, 4, 3)
sumRegion(1, 1, 2, 2)
sumRegion(1, 2, 2, 4)

answer:
[null, 8, 11, 12]

해석:
이전의 1D array에서 하던 것과 같은 방법으로 해결이 가능.
DP방식으로 Matrix를 하나씩 합한 배열을 생성하고, 필요한 범위값을 O(1) 의 시간 복잡도로 구해낼 수 있음.
지금 풀었던 방식은 메모리를 아주조금 아끼기 위해서 이런 복잡해보이는 코드로 구현함.
다음에 풀때는 sums 크기를 [[0] * (w+1) for _ in range(h+1)] 로 해서 깔끔하게 계산 하는 방법으로 풀어볼 것.
'''

# First Try
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix: return
        h, w = len(matrix), len(matrix[0])
        self.sums = [[0] * w for _ in range(h)]
        self.sums[0][0] = matrix[0][0]
        for i in range(1, h):
            self.sums[i][0] = matrix[i][0] + self.sums[i-1][0]
        for j in range(1, w):
            self.sums[0][j] = matrix[0][j] + self.sums[0][j-1]
        for i in range(1, h):
            for j in range(1, w):
                self.sums[i][j] = matrix[i][j] + self.sums[i][j-1] + self.sums[i-1][j] - self.sums[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.sums[row2][col2]
        if row1 == 0:
            return self.sums[row2][col2] - self.sums[row2][col1-1]
        if col1 == 0:
            return self.sums[row2][col2] - self.sums[row1-1][col2]
        return self.sums[row2][col2] - self.sums[row2][col1-1] - self.sums[row1-1][col2] + self.sums[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)