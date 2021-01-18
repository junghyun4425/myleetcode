# Problem Link: https://leetcode.com/problems/binary-tree-inorder-traversal/

'''
문제 요약: 들어오는 트리를 좌,부모,우 노드 순서로 깊이우선탐색 방식을 통한 서칭 결과를 반환하는 문제.
ask: [1,null,2,3]
answer: [1,3,2]

해석:
제일 보편적인 방식의 재귀함수를 통해 먼저 해결. 순서대로 좌측을 최대깊이로 들어가고, 돌아오면서 우측으로 한칸 후 좌측으로 최대깊이 만큼 탐색하는 것을 반복.
좌측, 가운데, 우측 순서로 프린트 되어야 하기 때문에 좌측 재귀함수가 끝나는 시점에 ans.append() 를 통해 순서대로 값을 저장.

다른 방법으로는 스택을 활용할 수 있음.
트리의 노드를 스택에 저장해서 재귀함수와 마찬가지로 백트래킹이 가능. 속도 면에서는 두 방식이 동일한 수준이므로 연습삼아 한번 더 풀어본 정도.
'''

# Using Stack
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ans.append(root.val)
            root = root.right
        return ans

# Using Recursion
'''
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        def recursion(tree):
            if tree.left:
                recursion(tree.left)
            ans.append(tree.val)
            if tree.right:
                recursion(tree.right)
        if not root:
            return ans
        recursion(root)
        return ans
'''