# Problem Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

'''
문제 요약: BST의 p와 q노드의 가장 가까운 공통 부모노드를 찾는 문제.
ask: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
answer: 6

해석:
굉장히 어려운듯 보이지만 생각보다 간단하게 구현이 가능한 문제.
이 문제를 풀기위해선 BST의 성질을 파악해야 함.
루트노드의 값보다 작으면 왼쪽, 크면 오른쪽에 노드들이 존재한다는 것.
그렇다면 p와 q가 루트노드의 왼쪽에 있다면 왼쪽 노드 어딘가에 공통부모가 존재한다는 뜻. 반대는 오른쪽 어딘가에 존재.
하지만 p와 q가 왼쪽 오른쪽 각각에 위치하고있다면 가장 가까운 공통부모는 현재의 노드가 됨.
이 원리만 알면 굉장히 쉽게 문제가 해결.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recursion(root):
            if root.val < p.val and root.val < q.val:
                return recursion(root.right)
            elif root.val > p.val and root.val > q.val:
                return recursion(root.left)
            else:
                return root
        return recursion(root)