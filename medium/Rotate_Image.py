# Problem Link: https://leetcode.com/problems/rotate-image/

'''
문제 요약: 이미지를 받았다는 가정하에, 2차월 리스트의 90도 회전된 배열로 바꾸는 문제 (단, 추가적 공간 사용은x O(1))
ask: [[1,2,3],[4,5,6],[7,8,9]]
answer: [[7,4,1],[8,5,2],[9,6,3]]

해석:
석사과정에서 이미지 프로세싱을 해봤기 때문에 간단하게 해결하는법을 알고 있어서 쉽게 해결.
여러 방법이 있겠지만 배운내용대로 Transpose 를 시킨다음 가운데 세로축을 기준으로 뒤집으면 90도 회전이 됨.
원리만 알면 구현은 쉬운편이므로 빠르게 해결.
'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m_len = len(matrix)
        # Transpose
        for i in range(m_len):
            for j in range(i + 1, m_len):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp

        # Reverse
        for i in range(m_len):
            for j in range(m_len // 2):
                end = m_len - 1 - j
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i][end]
                matrix[i][end] = tmp