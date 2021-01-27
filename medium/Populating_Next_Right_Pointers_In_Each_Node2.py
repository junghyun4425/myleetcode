# Problem Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

'''
문제 요약: 바이너리 트리가 들어오면, 각 노드의 next를 같은 레벨의 오른쪽에 있는 노드를 가리키게 바꾸는 문제. (단, 공간복잡도 O(1)의 제한)
ask: root = [1,2,3,4,5,null,7]
answer: [1,#,2,3,#,4,5,7,#]

해석:
Populating_Next_Right_Pointers_In_Each_Node 문제가 완벽한 바이너리 트리였다면, 이번엔 완벽하지 않은 바이너리 트리.
이번 문제에선 node.left 혹은 node.right 가 None인 경우를 queue에 넣으면 안됨. 이유는 다음 노드가 있음에도 None을 가리킬수 있기 때문.
따라서 이전과 유사하게 큐 2개로 레벨단위 탐색을 하고, 다음노드를 가리키게 할때 queue[0] 을 지목하되, None값이 들어가지 않는다는 제약을 넣어서 해결.
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
                    if node.left:
                        queue2.append(node.left)
                    if node.right:
                        queue2.append(node.right)
            queue = queue2
        return root