# Problem Link: https://leetcode.com/problems/binary-tree-paths/

'''
문제 요약: Binary Tree의 leaf노드 경로를 모두 출력하는 문제.
ask: [1,2,3,null,5]
answer: ["1->2->5","1->3"]

해석:
DFS로 끝까지 탐색해가면서 노드의 자식이 없는경우 ans에 path를 붙여주면서 모든 경로를 찾음.
마지막엔 path를 하나의 string으로 변환시켜 정답이 요구하는 형태로 만들어줌.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []
        def dfs(path, root):
            if not root.left and not root.right:
                ans.append(path+[str(root.val)])
            if root.left:
                dfs(path+[str(root.val)], root.left)
            if root.right:
                dfs(path+[str(root.val)], root.right)
        dfs([], root)
        return ['->'.join(nodes) for nodes in ans]