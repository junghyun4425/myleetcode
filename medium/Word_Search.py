# Problem Link: https://leetcode.com/problems/word-search/

'''
문제 요약: m x n 사이즈 문자 리스에서 word와 같은 문자를 인접한칸에 한해서 만들수 있는지 여부를 반환하는 문제.
ask: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
answer: True

해석:
백트래킹 방식으로 모든 m x n 문자에 대해서 시작지점으로 놓고 DFS와 같이 문자를 탐색.
맵을 탐색하는 경우와 유사하기 때문에 4방향(우, 아래, 좌, 위) 모두 검사.
고려해야 할 조건이 많긴하지 (new_c와 new_r의 범위값, 경로상에 들렸는지 체크, 문자가 같은지 체크) 만이걸 제외하면 간단하게 해결되는 문제.
여기서 경로는 리스트가 아니라 set으로행 구현 좀더 빠르게 수가능.해
l이 word의 길이와 같아지면 참을 반환. (char가 같은지는 함수 호출전에 이미 확인)
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        h, w = len(board), len(board[0])
        w_len = len(word)
        di = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def backtrack(path, r, c, l):
            if l == w_len:
                print(path)
                return True
            for d in di:
                new_r, new_c = r + d[0], c + d[1]
                if (new_r, new_c) not in path and 0 <= new_r < h and 0 <= new_c < w and board[new_r][new_c] == word[l]:
                    path.add((r, c))
                    if backtrack(path, new_r, new_c, l + 1):
                        return True
                    path.discard((r, c))
            return False

        for i in range(h):
            for j in range(w):
                if board[i][j] == word[0] and backtrack({(i, j)}, i, j, 1):
                    return True
        return False