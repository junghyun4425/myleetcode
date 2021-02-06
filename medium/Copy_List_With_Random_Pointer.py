# Problem Link: https://leetcode.com/problems/copy-list-with-random-pointer/

'''
문제 요약: 랜덤링크라는 상태가 추가된 링크드 리스트를 deep copy하는 문제.
ask: [[7,null],[13,0],[11,4],[10,2],[1,0]]
answer: [[7,null],[13,0],[11,4],[10,2],[1,0]] (val값은 중복가능, 앞에값이 next를, 뒤에값이 random을 가리킴)

해석:
그래프 deep copy 문제를 풀어보았기 때문에 hash map을 쓰면 간단하게 해결할 수 있는 문제라는 걸 알고있었음.
hm 에 각 노드들을 넣음과 동시에, next, random 노드들도 key로써 활용되고 value에는 새로운 deep copy할 노드를 넣어놓음.
그리고 순차적으로 새로운 하나의 노드에 val, next, random을 담고 현재노드에 연결시켜주면 끝.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        cur = head
        hm = {None: None}
        while cur:
            if cur not in hm:
                hm[cur] = Node(cur.val)
            if cur.next not in hm:
                hm[cur.next] = Node(cur.next.val)
            if cur.random not in hm:
                hm[cur.random] = Node(cur.random.val)
            copy = hm[cur]
            copy.next = hm[cur.next]
            copy.random = hm[cur.random]

            cur = cur.next
        return hm[head]