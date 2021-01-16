# Problem Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

'''
문제 요약: 트리의 최대 깊이를 구하는 문제.
ask: 3 <- 2 <- 1 -> 5
answer: 3

해석:
바텀업 방식으로 끝에 노드가 없는경우 까지 내려가서 하나씩 깊이를 더해가는 방법으로 구현.
재귀를 통해 왼쪽과 오른쪽의 깊이중 더 깊은곳의 값에다 하나씩 더해가면서 최대 깊이를 측정.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def recursive(tree, d=0):
            if not tree:
                return 0
            return 1 + max(recursive(tree.left, d+1), recursive(tree.right, d+1))
        return recursive(root)