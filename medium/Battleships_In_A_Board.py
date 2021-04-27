# Problem Link: https://leetcode.com/problems/battleships-in-a-board/

'''
문제 요약: 전투함이 'X'이고 비어있는 공간이 '.'일때, 모여있는 전투함 군단은 몇개인지 확인하는 문제. (좌우상하에 연속적으로 X가 붙어있어야 군단)
ask: board = [
["X",".",".","X"],
[".",".",".","X"],
[".",".",".","X"]
]
answer: 2

해석:
First Try
Follow up으로 추가 메모리를 사용하지 않고 해결하는 도전 조건이 있음.
이를 만족하기 위해 기존의 배열에 검사했던 부분을 'X' 대신 'O' 로 바꿔서 표현하기로 결정.
모든 좌표를 DFS탐색으로 군단을 찾으며, 찾은 군단은 모두 'O'로 바꿔서 다음에 또 카운팅하는 일이 없도록 함.
이러면 공간복잡도를 O(1)로 해결이 가능.

Second Try
문제에서 군단은 오로지 직선으로만 표현이 됨. 따라서 가로, 세로 중 하나라는 점을 이용해 훨씬 같단하게 해결이 가능.
직선으로 표현되기 떄문에 현재 좌표에서 'X'인 경우 우측과 아래쪽이 '.' 이거나 최대길이일때 군단을 하나 더해주면 됨.
이게 가능한 이유는 ㄱ자나 ㄴ자 모양인 군단의 경우가 없기 때문. 첫번째 시도가 범용성이 넓다면 두번째 시도는 문제 제약을 파악해 효율적인 구현을 시도함.
'''

# Second Try
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        h, w = len(board), len(board[0])
        ans = 0
        for i in range(h):
            for j in range(w):
                if board[i][j] == 'X':
                    if i == h-1 or board[i+1][j] == '.':
                        if j == w-1 or board[i][j+1] == '.':
                            ans += 1
        return ans

# First Try: Using DFS // O(1) space complexity
'''
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        h, w = len(board), len(board[0])
        di =[(1,0), (0,1), (-1,0), (0,-1)]
        ans = 0
        def dfs(i, j):
            if board[i][j] == 'X':
                board[i][j] = 'O'
            else:
                return
            for d in di:
                new_i, new_j = d[0]+i, d[1]+j
                if 0 <= new_i < h and 0 <= new_j < w and board[new_i][new_j] == 'X':
                    dfs(new_i, new_j)
        for i in range(h):
            for j in range(w):
                if board[i][j] == 'X':
                    dfs(i, j)
                    ans += 1
        return ans
'''