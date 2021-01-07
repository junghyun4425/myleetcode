# Problem Link: https://leetcode.com/problems/set-matrix-zeroes/

'''
문제 요약: 2차원 배열에서 0인 위치의 가로, 세로 모두 0으로 바꾸는 문제. (단, 메모리 복잡도를 O(1)로 풀기)
ask: [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
answer: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

해석:
메모리를 O(mn)와 O(m+n)의 방법은 알아냈지만, O(1)의 경우는 근접했다고 생각.
O(mn)은 0의 위치에 대한 가로 세로 인덱스를 저장하면 되며,
O(m+n)은 0의 위치에 대한 세로 인덱스만 저장. (가로는 탐색도중 0을 마주치면 다음칸으로 넘어갈때 가로를 모두 0으로 바꿔버리면 됨)
O(1)은 아무래도 들렸던 곳만 0으로 바꿔줘야 가능한 일. (좌 -> 우 / 위 -> 아래 로 움직이면 현재 인덱스에 좌, 위쪽은 0으로 바꿔도 무방하다는 점 때문)
몇번 시도해봤지만, 마무리가 안되어서 다른 색다른 방법이 있는지 알아봤으나, 적용하던 접근법이 맞음.
단지 index 0 인 부분을 기준으로 잡고 index 1 이후의 0위치를 index 0인 부분에 기록하는 방식.
for문을 여러번 돌려야 하는 단점이 있지만 메모리를 사용하지 않기 때문에 감수해야 할 부분.
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        h = len(matrix)
        w = len(matrix[0])
        first_c = False

        for i in range(h):
            if matrix[i][0] == 0:
                first_c = True
            for j in range(1, w):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, h):
            for j in range(1, w):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(w):
                matrix[0][j] = 0
        if first_c:
            for i in range(h):
                matrix[i][0] = 0