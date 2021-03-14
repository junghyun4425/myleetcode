# Problem Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

'''
문제 요약: Binary Tree에서 p와 q노드의 가장 가까운 공통 부모노드를 찾는 문제.
ask: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
answer: 3

해석:
BST의 공통부모노드를 찾는 문제는 굉장히 간단했다면 바이너리트리는 좀더 많은 고민을 필요로 함.
DFS방식으로 찾으면 해결 가능하고 여기에 추가적으로 몇가지 flag를 넣어서 최소로 만족하는 노드를 찾아야 함.
서브트리의 left와 right 혹은 현재 node 세가지 중에서 p와 q 가 존재한다면 현재 노드가 정답이 됨.
이를 위해 먼저 left와 right방향으로 DFS 탐색.
그리고 밑에서부터 차근차근 노드가 p와 q인지 확인해야하는데, 주의할점은 현재 노드도 확인해줘야한다는 점.
왼쪽, 오른쪽 현재노드 세군데 중에서 두군데가 True를 만족하면 현재 노드가 가장 가까운 공통분모.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = []
        def recursion(root):
            if not root:
                return False
            left = recursion(root.left)
            right = recursion(root.right)
            cur = root == p or root == q
            if left + right + cur > 1:
                ans.append(root)
            return left or right or cur
        recursion(root)
        return ans[0]

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