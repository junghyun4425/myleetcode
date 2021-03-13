# Problem Link: https://leetcode.com/problems/word-search-ii/

'''
문제 요약: m x n 사이즈 문자 리스트에서 words와 같은 문자를 인접한칸에 한해서 만들수 있는지 여부를 반환하는 문제.
ask:
board = [
["o","a","a","n"],
["e","t","a","e"],
["i","h","k","r"],
["i","f","l","v"]],
words = ["oath","pea","eat","rain"]
answer: ["eat","oath"]

해석:
Word_Search 문제에서 풀었던 방식을 그대로 활용하면 O(n^3) 으로 시간초과가 날것이 분명하기 때문에 다른방법을 생각함.
자료구조에서 Trie를 쓰면 메모리 면에서는 비효율적이지만 성능상 이점이 있기 떄문에 시도함.
방법 자체는 Word_Search 와 비슷한 DFS구조로 구현했지만 words를 미리 Trie자료구조에 모두 담고 시작함.
Trie의 isEnd는 True/False를 담는게 아니라 word 그 자체를 담고 있음. (그래야 찾았을때 word를 save할수 있음)
ans 를 set() 으로 선택한 이유는, 중복을 제거하기 위함. 같은 word가 다른데도 나타날 수 있기 때문.
성능 자체는 그렇게 뛰어나진 않지만 통과 가능함. 다음 리뷰때는 최적화도 한번 생각해 보는걸로.
'''

class TrieNode:
    def __init__(self):
        self.child = {}
        self.isEnd = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        ans = set()
        h, w = len(board), len(board[0])
        di = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def makeTrie(word):
            node = root
            for c in word:
                if c not in node.child:
                    node.child[c] = TrieNode()
                node = node.child[c]
            node.isEnd = word

        for word in words:
            makeTrie(word)

        def dfs(root, i, j):
            if board[i][j] not in root.child:
                return
            node = root.child[board[i][j]]
            if node.isEnd:
                ans.add(node.isEnd)
            tmp = board[i][j]
            board[i][j] = '*'
            for d in di:
                new_i, new_j = i + d[0], j + d[1]
                if 0 <= new_i < h and 0 <= new_j < w:
                    dfs(node, i + d[0], j + d[1])
            board[i][j] = tmp

        for i in range(h):
            for j in range(w):
                dfs(root, i, j)
        return list(ans)