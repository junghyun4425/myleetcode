# Problem Link: https://leetcode.com/problems/sum-of-left-leaves/

'''
문제 요약: 이진트리에서 왼쪽 leaf node만 모두 더하는 문제.
ask: root = [3,9,20,null,null,15,7]
answer: 24

해석:
root는 더하면 안되기 때문에 이부분을 주의해야 함.
그 외에는 재귀함수를 통해 왼쪽인지 아닌지만 판별해주는 인자를 하나 추가해주면 쉽게 파악이 가능.
따라서 왼쪽인 부분만 모두 더해서 최종적으로 return 해주면 해결되는 문제.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def recursion(node, isLeft):
            if not node:
                return 0
            if not node.left and not node.right and isLeft:
                return node.val
            return recursion(node.left, True) + recursion(node.right, False)
        return recursion(root, False)