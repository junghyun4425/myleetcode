# Problem Link: https://leetcode.com/problems/sum-root-to-leaf-numbers/

'''
문제 요약: 트리의 root부터 leaf까지 조합한 숫자들을 모두 합한 결과를 반환하는 문제.
ask: [1,2,3]
answer: 25 (12 + 13)

해석:
DFS 혹은 BFS로 간단히 해결할 수 있는 문제.
Base case로, None인곳은 0을 반환하고 left right 노드가 없는 리프노드에서는 값을 계산해서 반환.
아래에서 위로 올라가면서 left와 right의 결과를 합치며 root까지 계산해 나가면 끝.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root, val):
            if not root:
                return 0
            if not root.left and not root.right:
                return val*10+root.val
            return dfs(root.left, val*10+root.val) + dfs(root.right, val*10+root.val)
        return dfs(root, 0)