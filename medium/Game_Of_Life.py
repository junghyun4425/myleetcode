# Problem Link: https://leetcode.com/problems/game-of-life/

'''
문제 요약: 살아있는 cell은 1 죽은 cell은 0 으로 표기할떄, 아래 규칙을 만족하는 결과로 배열을 바꾸는 문제.
규칙1 - 주변 cell(8방향) 중에 1인 cell의 개수가 2보다 작거나 3보다 크면 본인은 죽음.
규칙2 - 주변 cell중에서 1인 cell의 개수가 3개면 본인이 죽은cell인 경우 1로 바뀜.
규칙3 - 현재 살아있던 죽었던 주변셀의 개수에 죽을수도, 그대로 있을수도, 살수도 있음.

ask: board = [
[0,1,0],
[0,0,1],
[1,1,1],
[0,0,0]
]
answer: [
[0,0,0],
[1,0,1],
[0,1,1],
[0,1,0]
]

해석:
석사과정에서 이미 다 이해를 한 룰이라 문제를 딱히 읽지 않아도 되었던 문제. 단, 조건은 확인함.
조건중에 메모리사용제약이 존재. 여기서 어려운 부분은 cell을 바꿔줘야 함. (cell의 상태가 바뀐걸 다른 cell의 네이버로써 적용시키면 안되기 때문)
그래서 특수한 룰을 적용시킴.
cell이 살아있다가 죽었을경우 -1 로 바꾸고, 죽었다가 살아난경우를 2 로 바꿈.
이렇게되면 이후의 cell에서 네이버의 살아있는 cell개수를 파악할때 지장을 주지 않음.
고로 O(1)의 공간복잡도로 해결 가능.
'''

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        h, w = len(board), len(board[0])
        neighbors = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
        for i in range(h):
            for j in range(w):
                live_cnt = 0
                for n in neighbors:
                    r = i+n[0]
                    c = j+n[1]
                    if 0 <= r < h and 0 <= c < w and abs(board[r][c]) == 1:
                        live_cnt += 1
                if board[i][j] == 1 and (live_cnt < 2 or live_cnt > 3):
                    board[i][j] = -1
                if board[i][j] == 0 and live_cnt == 3:
                    board[i][j] = 2
        for i in range(h):
            for j in range(w):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0