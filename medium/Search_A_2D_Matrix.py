# Problem Link: https://leetcode.com/problems/search-a-2d-matrix/

'''
문제 요약: 정렬된 2차원 배열에서 target이 존재하는지 맞추는 문제.
ask: [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
answer: False

해석:
서칭 하면 빠른속도의 바이너리 서치를 떠올림. 2차원 배열이라 해도 결국 1차원으로 표현할 수 있기때문에 바이너리 서치가 가능.
길이가 mn 이라면, 가로 n을 나눈 몫이 세로위치, 나머지가 가로위치 이기 때문에 이를 활용해 문제를 해결.
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h = len(matrix)
        w = len(matrix[0])
        l, r = 0, h * w - 1
        while l <= r:
            m = (l + r) // 2
            v = matrix[m // w][m % w]
            if v == target:
                return True
            elif v > target:
                r = m - 1
            else:
                l = m + 1

        return False