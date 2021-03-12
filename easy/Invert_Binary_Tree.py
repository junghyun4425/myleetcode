# Problem Link: https://leetcode.com/problems/invert-binary-tree/

'''
문제 요약: 트리를 좌우 invert 시키는 문제.
ask: [4,2,7,1,3,6,9]
answer: [4,7,2,9,6,3,1]

해석:
어렵게 생각해서 큐2개를 가지고 전체 순회하면서 순서를 레벨별로 다 바꾸려고 시도함.
생각보다 복잡해지고 많은 조건문이 필요해 단순화시킬 필요가 있었음.
생각해보니 그냥 맨 마지막에서부터 하나씩 바꾸면 되는 문제였음.
그럼 자동으로 위로오면서 다 뒤집혀 질것이고 원리만 알면 굉장히 쉬워지는 문제.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def recursion(root):
            if not root:
                return None
            right = recursion(root.right)
            left = recursion(root.left)
            root.left = right
            root.right = left
            return root
        return recursion(root)