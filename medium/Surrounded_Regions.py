# Problem Link: https://leetcode.com/problems/surrounded-regions/

'''
문제 요약: 2D 배열에 O가 X에 둘러쌓였다면 X로 바꾸는 문제. (단, 모서리에 위치한 O는 둘러쌓인게 아님)
ask:
X X X X
X O O X
X X O X
X O X X
answer:
X X X X
X X X X
X X X X
X O X X

해석:
이 문제에서 핵심 포인트는 모서리. 모서리에 'O'가 존재하냐 안하냐에 따라서 닫히고 안닫히고가 결정됨.
따라서 모서리에 있는 'O'를 스택에 담아두고, DFS 방식으로 'O'와 연결된 모든 'O'를 탐색해서 임시 문자 '-'로 바꿔줌.
'-'문자는 'O'였고 바뀌어선 안된다는 것을 의미하며, 남은 둘러쌓인 'O'들은 'X'로 교환해주면 됨.
'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return []
        w, h = len(board[0]), len(board)
        di = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        stack = []

        for i in range(h):
            for j in range(w):
                if i == 0 or i == h - 1 or j == 0 or j == w - 1 and board[i][j] == 'O':
                    stack.append((i, j))

        while stack:
            i, j = stack.pop()
            if i < 0 or j < 0 or i >= h or j >= w or board[i][j] != 'O':
                continue
            board[i][j] = '-'
            for d in di:
                stack.append((i + d[0], j + d[1]))

        for i in range(h):
            for j in range(w):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'