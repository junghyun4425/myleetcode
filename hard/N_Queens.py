# Problem Link: https://leetcode.com/problems/n-queens/

'''
문제 요약: 체스칸 n 을 받아서 퀸이 서로 공격받지 않는 공간에 둘수 있는 모든 경우의 수를 반환하는 문제. (n은 사이즈, 퀸의 갯수)
ask: n = 4
answer: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]] (2가지 경우가 있으므로)

해석:
예전에 풀었던 백트랙킹 문제 스도쿠와 유사함. 재귀함수로 가능한 경우의 수를 모두 찾아냄.
한가지 실수했던 부분은 가로세로를 검사할때 가로는 안해도 되고 대각선도 아래쪽은 검사하지 않아도 되는데 굳이 넣었었음.
그 이유는 가로엔 무조건 퀸이 하나만 들어가게 로직을 짰고, 위에서부터 아래로 퀸을 추가하기 떄문에 아래쪽 대각선은 넣을 필요가 없음.
그런 사소한 부분만 제외하면 무난하게 풀었던 문제.
'''

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        chess = [['.'] * n for _ in range(n)]

        def is_valid(r, c):
            # Checking Straight ways
            for i in range(n):
                if not i == r and chess[i][c] == 'Q':
                    return False

            # Checking Diagonal ways
            for i in range(1, n):
                if (r - i) >= 0 and (c - i) >= 0 and chess[r - i][c - i] == 'Q':
                    return False
                if (r - i) >= 0 and (c + i) < n and chess[r - i][c + i] == 'Q':
                    return False
            return True

        def backtrack(row_n):
            if row_n == n:
                ans.append(["".join(chess[i]) for i in range(n)])
                return True
            for i in range(n):
                chess[row_n][i] = 'Q'
                if is_valid(row_n, i):
                    backtrack(row_n + 1)
                chess[row_n][i] = '.'

        backtrack(0)
        return ans