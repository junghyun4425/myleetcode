# Problem Link: https://leetcode.com/problems/n-ary-tree-level-order-traversal/

'''
문제 요약: Tree가 주어지면, 레벨단위로 배열에 저장해서 반환하는 문제.
ask: root = [1,null,3,2,4,null,5,6]
answer: [[1],[3,2,4],[5,6]]

해석:
트리의 레벨단위 탐색을 할수 있는지 묻는 문제.
큐를 활용하면 BFS의 탐색방법으로 노드들을 방문함.
따라서 BFS탐색으로 레벨 단위로 값들을 저장해 반환하여 해결함.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node:
                    continue
                level.append(node.val)
                queue.extend(node.children)
            if level:
                ans.append(level)
        return ans