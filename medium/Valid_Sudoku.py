# Problem Link: https://leetcode.com/problems/4sum/

'''
문제 요약: 스도쿠 판이 주어졌을 때, 정상인지 아닌지 판별하는 문제.
ask: [['8', '7', '.', '.',...], ..., [...]]
answer: True

해석:
두가지 방법중에 하나를 선택. 첫째는 메모리를 아끼고 시간을 더 걸리게 해결하는 방법. 두번째는 메모리를 많이 쓰고 시간을 절약하는 방법.
여기선 메모리를 많이 쓰고 하나의 이중루프 안에서 모든 문제를 해결하는 방법으로 해결.
해시맵 배열을 만들어 row, col, box 모두의 값들에 대한 해시맵을 각각 배정.
i, j 와 box의 번호간 상관관계를 찾느라 시간이 조금 걸렸지만 문제없이 성공.
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_len = 9
        row_m = [{} for _ in range(board_len)]
        col_m = [{} for _ in range(board_len)]
        box_m = [{} for _ in range(board_len)]
        for i in range(board_len):
            for j in range(board_len):
                if board[i][j] != '.':
                    row_m[i][board[i][j]] = row_m[i].get(board[i][j], 0) + 1
                    col_m[j][board[i][j]] = col_m[j].get(board[i][j], 0) + 1
                    n_box = (i // 3) + (j // 3) * 3
                    box_m[n_box][board[i][j]] = box_m[n_box].get(board[i][j], 0) + 1

                if board[i][j] != '.' and (
                        row_m[i][board[i][j]] > 1 or col_m[j][board[i][j]] > 1 or box_m[n_box][board[i][j]] > 1):
                    return False
        return True