# Problem Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

'''
문제 요약: 완벽한 바이너리 트리가 들어오면, 각 노드의 next를 같은 레벨의 오른쪽에 있는 노드를 가리키게 바꾸는 문제. (단, 공간복잡도 O(1)의 제한)
ask: root = [1,2,3,4,5,6,7]
answer: [1,#,2,3,#,4,5,6,7,#]

해석:
처음보는 문제를 이해하는데 시간이 조금 걸렸지만 생각보다 쉬운 문제.
문제를 좀더 쉽게 설명하자면, 각 트리의 노드에는 next라는 변수가 존재하며, 이는 같은레벨의 다음 노드를 가리키게 바꿔주면 됨.
이를 위해 queue 두개를 활용해서 레벨단위로 노드를 체크하며, 다음레벨의 노드들을 queue2에 저장시킴.
queue에서 뽑아낸 노드의 다음번째 순서는 queue[0] 이므로 이를 가리키게하면 끝. 대신, queue가 존재하지 않으면 None을 가리키게 하면 됨.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = [root]
        while queue:
            queue2 = []
            while queue:
                node = queue.pop(0)
                if node:
                    node.next = queue[0] if queue else None
                    queue2.extend([node.left, node.right])
            queue = queue2
        return root