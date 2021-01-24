# Problem Link: https://leetcode.com/problems/minimum-depth-of-binary-tree/

'''
문제 요약: 트리의 최소 레벨을 출력하는 문제.
ask: [3,9,20,null,null,15,7]
answer: 2

해석:
재귀함수로 너무 빨리 풀어서 BFS 방법으로도 두가지 방법으로 문제를 풀어봄.
재귀함수일때 주의해야 할게 하나 있다면, 한쪽만 None인 경우엔 depth를 계산하면 안되는 점.
left와 right 둘중 하나라도 값이 0이라면 max(left, right)로 return하면 해결됨. (둘다 0이면 어차피 0으로 반환되기에 문제되지 않음)

BFS는 기존의 트리를 서치하는 방법(큐 두개로 수행)에서 도중에 left와 right 둘다 None을 가지면 바로 depth를 반환하면 해결.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        queue = [root]
        depth = 1

        while queue:
            queue2 = []
            while queue:
                node = queue.pop(0)
                if node:
                    if not node.left and not node.right:
                        return depth
                    queue2.extend([node.left, node.right])
            queue = queue2
            depth += 1
        return depth

# Recursion
'''
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def depth(root):
            if not root:
                return 0
            left, right = depth(root.left), depth(root.right)
            if min(left, right) == 0:
                return 1 + max(left, right)
            return 1 + min(left, right)
        return depth(root)
'''