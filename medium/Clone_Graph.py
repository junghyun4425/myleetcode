# Problem Link: https://leetcode.com/problems/clone-graph/

'''
문제 요약: 그래프를 똑같이 복사해서 반환하는 문제.
ask: [[2,4],[1,3],[2,4],[1,3]]
answer: [[2,4],[1,3],[2,4],[1,3]]

해석:
DFS 방식으로 visited 를 체크해 가면서 재귀함수를 수행하며 해결.
처음엔 visited에 node.val와 같은 숫자로 구분하여 for문 안에서 방문한 노드는 새로 생성하는 방식으로 할 수 있지만 코드가 길어짐.
간결하게 하기위해 메모리를 조금 더 쓰고 node 자체를 저장함. 이러면 방문했던 노드에 대해서 따로 만들지 않고 반환만 해주면 됨.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}
        def recursion(node):
            if not node:
                return None
            if node in visited:
                return visited[node]
            clone = Node(node.val)
            visited[node] = clone
            for n in node.neighbors:
                clone.neighbors.append(recursion(n))
            return clone
        return recursion(node)