# Problem Link: https://leetcode.com/problems/search-a-2d-matrix-ii/

'''
문제 요약: 각 row 그리고 col 끼리 오름차순으로 정렬된 2D 배열에서 target값이 존재하는지 확인하는 문제.
ask:
matrix = [
[1,4,7,11,15],
[2,5,8,12,19],
[3,6,9,16,22],
[10,13,14,17,24],
[18,21,23,26,30]
], target = 5
answer: True

해석:
First Try: DFS
문제를 보자마자 그냥 길찾기 문제인가 싶어서 바로 DFS를 빠르게 구현해봄. 하지만 예상밖의 시간초과가 발생.
아마 쓸데없는곳까지 모두 탐색하다보니 결국 최악의경우(matrix의 가장 끝자리보다 target값이 클때) O(m*n).
너무 생각없이 돌진한 느낌. 따라서 좀더 생각해봄

Second Try: Remove row or col
Binary Search 방식에서 생각난 아이디어. 위쪽 row 한줄과 왼쪽 col 마지막줄은 한줄로 쭉 이을수 있고 이는 정렬된 결과와 같음.
그렇게 형성된 한줄의 가운데값은 위의 예제에서 15가 됨.
여기서 한줄씩 소거해 나갈 수 있음.
만약 target이 15보다 크면 이전값은 쓸모없으니 row를 한줄 제거함.
target이 15보다 작다면 큰값들은 쓸모없으니 col을 한줄 빼버림.
이렇게 제거하다보면 최악의 경우에도 m+n 으로 굉장히 효율적.
'''

# Second Try: Remove col or row
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h, w = len(matrix), len(matrix[0])
        r, c = 0, w-1
        while r < h and c >= 0:
            if matrix[r][c] == target:
                return True
            if matrix[r][c] > target:
                c -= 1
            else:
                r += 1
        return False

# First Try: DFS (Time Limit Exceeded)
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h, w = len(matrix), len(matrix[0])
        def dfs(i, j):
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                down = dfs(i+1,j) if i+1 < h else False
                right = dfs(i,j+1) if j+1 < w else False
                return any([down, right])
            else:
                return False
        return dfs(0,0)
'''