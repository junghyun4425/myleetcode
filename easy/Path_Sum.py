# Problem Link: https://leetcode.com/problems/path-sum/

'''
문제 요약: 트리의 노드에서부터 리프까지 합이 targetSum 과 일치하는지 확인하는 문제.
ask: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
answer: True (5->4->11->2)

해석:
노드가 리프노드인지 아닌지 조건문 없이 그저 노드를 따라 합한 값과 targetSum을 비교하면 문제가 하나 생김.
targetSum = 0 인 경우, res 이 0 에서부터 시작하기 때문에 False임에도 True를 반환.
따라서 targetSum과 res를 비교하는 때는 리프노드에 도착했을때만 비교를 해야함.
이 조건 외에는 간단했던 문제.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def sumNodes(root, res):
            if not root:
                return False
            if not root.left and not root.right:
                return res+root.val == targetSum
            return sumNodes(root.left, res+root.val) or sumNodes(root.right, res+root.val)
        return sumNodes(root, 0)