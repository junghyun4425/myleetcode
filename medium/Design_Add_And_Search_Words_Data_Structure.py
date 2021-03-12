# Problem Link: https://leetcode.com/problems/design-add-and-search-words-data-structure/

'''
문제 요약: WordDictionary를 구현하는 문제. 문자를 입력해서 추가하고, 검색하는 기능을 구현. ('.'은 wildcard)
ask:
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
answer:
[null,null,null,null,false,true,true,true]

해석:
Trie를 활용하면 간편하게 구현할 수 있는문제. 따라서 TrieNode를 따로 클래스로 만들어 놓음.
insert는 기존의 Trie 자료구조 사용하던것 처럼 구현하면 해결됨.
하지만 search는 조금 복잡한데, 이유는 wildcard를 구현해야 하기 때문. 이는 모든 노드를 검사해야 하는데, index값을 받아와 DFS방식으로 해결하기로 결정.
wildcard를 타고 들어간 노드들중 어느 하나라도 True가 나온다면 그것은 search가 참인것을 의미하기 때문에 any()함수를 활용.
그 외에는 마찬가지로 node를 한단계씩 타고 들어가면서 검사하면 해결.
개인적으로 Trie 자료구조를 활용한 알고리즘이 재밌는편인것 같음.
'''

class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.child = {}

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.child:
                node.child[c] = TrieNode()
            node = node.child[c]
        node.isEnd = True

    def search(self, word: str) -> bool:
        w_len = len(word)
        def dfs(node, i):
            if i >= w_len:
                return node.isEnd
            if word[i] == '.':
                return any([dfs(c, i+1) for c in node.child.values()])
            if word[i] not in node.child:
                return False
            node = node.child[word[i]]
            return dfs(node, i+1)
        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)