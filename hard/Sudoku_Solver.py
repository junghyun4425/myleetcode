# Problem Link: https://leetcode.com/problems/sudoku-solver/

'''
문제 요약: 주어진 스도쿠판을 정답으로 채우는 문제. 단, 답이 한가지만 있는 경우의 문제만 예시로 주어짐.
ask: [['1', '5', .... ], [...], ... , ['3', '.', '.' ...]]
answer: [['1', '5', .... ], [...], ... , ['3', '7', '9' ...]]

해석:
처음에는 평소에 스도쿠를 푸는방법으로 시도하려했지만 구현으로는 어려움이 많다는것을 깨달음. (소거법)
따라서 알고리즘이 복잡하지않은, 숫자들을 대입하면서 진행하고 막히면 백트랙킹 방법으로 다시 돌아오는 방법으로 결정.
스도쿠에서 새로넣은 값이 규칙에 맞는지 확인하는 check_nums 함수와, 재귀함수 형식으로 오답이 나왔을시 백트랙킹이 가능하게 만든 함수로 구성.
i와 j가 8이 넘어갔을시에는 적절히 대처하며 끝까지 간 경우 True를 반환하여 모든 재귀함수를 마무리. (실패가 없다고 가정하기 때문에 가능)
속도 자체는 느리게 나왔기에 만약 다음에 다시 도전한다면 메모리를 좀더 쓰더라도 해시맵을 활용해 빠르게 값을 찾는 방법으로 시도할 것.
'''

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def check_nums(r, c, n):
            # Check Row
            for j in range(9):
                if board[r][j] == str(n):
                    return False
            # Check Col
            for i in range(9):
                if board[i][c] == str(n):
                    return False
            # Check Box
            box_r = (r // 3) * 3
            box_c = (c // 3) * 3
            for i in range(box_r, box_r + 3):
                for j in range(box_c, box_c + 3):
                    if board[i][j] == str(n):
                        return False
            return True

        def backtracking(i, j):
            # Find next empty space
            while i < 9 and (j > 8 or board[i][j] != '.'):
                j += 1
                if j > 8:
                    j = 0
                    i += 1
            # Finish if i is gt 8
            if i > 8:
                return True

            for n in range(1, 10):
                if check_nums(i, j, n):
                    board[i][j] = str(n)
                    if backtracking(i, j + 1): return True
                    board[i][j] = '.'

        backtracking(0, 0)