# Problem Link: https://leetcode.com/problems/spiral-matrix/

'''
문제 요약: 주어진 2차원 배열을 소용돌이 방향순으로 반환
ask: [[1,2,3],[4,5,6],[7,8,9]]
answer: [1,2,3,6,9,8,7,4,5]

해석:
이 문제를 맵에서 길찾는 방식으로 풀수 있었지만 메모리를 절약하는 방법으로 시도.
바운더리를 정해놓고, 순서대로 탐색. 하지만 문제는 마지막에 중복탐색을 하는 경우가 발생.
예를들어, 1,2,3/4,5,6/7,8,9/10,11,12 와같이 정사각형이 아닐때, 끝자리 8이 두번 출력되게됨.
마지막 바운더리떄 직사각형은 상,하 또는 좌,우 로 마지막엔 두번씩 나오게 됨.
이는 정답 배열의 최대길이 (h * w)로 제한할 수 있어서 마무리 가능.
'''


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        h = len(matrix) - 1
        w = len(matrix[0]) - 1
        ans = []
        b = 0

        while w - b >= 0 and h - b >= 0:
            for j in range(b, w - b + 1):
                ans.append(matrix[b][j])
            for i in range(b + 1, h - b + 1):
                ans.append(matrix[i][w - b])
            for j in range(w - b - 1, b, -1):
                ans.append(matrix[h - b][j])
            for i in range(h - b, b, -1):
                ans.append(matrix[i][b])
            b += 1
        return ans[:(h + 1) * (w + 1)]