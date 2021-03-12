# Problem Link: https://leetcode.com/problems/implement-trie-prefix-tree/

'''
문제 요약: Trie (Prefix Tree)를 구현하는 문제.
ask:
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
answer:
[null, null, true, false, true, null, true]

해석:
자료구조를 공부하면서 언제 Trie를 구현해보려고 했었는제 문제에서 나와주니 굉장히 반가웠음.
Node가 따로 없었어서 노드 클래스를 직접 구현. 처음에는 child를 array로 구현했었지만 실용성, 메모리 문제 때문에 hashmap으로 바꿈.
그외엔 다소 특별한게 없지만 간략하게 소개하면,
search: 특정 word가 들어가있는지 확인하기위해 트리를 root부터 타고 내려감. 여기서 도중에 hashmap에 없거나 마지막에 isEnd가 False면 없다는 의미.
insert: hashmap에 노드를 추가시켜주면서 내려감. 마지막에는 isEnd = True 바꿔줘야 실제 단어가 있는지 확인이 가능.
sratWith: Prefix를 찾는 문제로, search와는 다르게 isEnd가 True든 아니든 노드에 존재하기만 하면 True를 반환함.
이런식으로 Trie를 직접 구현해봄.
'''

class Node:
    def __init__(self):
        self.isEnd = False
        self.child = {}

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for c in word:
            if not c in node.child:
                node.child[c] = Node()
            node = node.child[c]
        node.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for c in word:
            if not c in node.child:
                return False
            node = node.child[c]
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for c in prefix:
            if not c in node.child:
                return False
            node = node.child[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)