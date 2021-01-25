# Problem Link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

'''
문제 요약: 트리가 들어오면, 트리의 preorder순서로 linked_list와 같은 형태로 바꾸는 문제. (단, 추가메모리는 O(1)의 공간복잡도)
ask: [1,2,5,3,4,null,6]
answer: [1,null,2,null,3,null,4,null,5,null,6]

해석:
pre_order 순서이기 때문에 루트 -> 왼 -> 오 순으로 연결되어야 함. bottom-up 방식으로, 가장 왼쪽 밑에 존재하는 서브트리부터 탐색.
left로 내려가면서 l_node와 r_node를 기록.
만약 l_node가 존재하지 않는다면 그냥 넘겨도 괜찮음. (오른쪽은 이미 순서에 맞게 존재하므로)
단, l_node가 존재하면 r_node 사이에 끼워줘야 하므로 약간의 수정이 필요함.
여기서 주의해야 할 점은, l_node는 이미 left노드가 없거나 혹은 right에 붙은 상태이기 때문에 while문으로 가장 오른쪽까지 내려간 다음 r_node를 붙여줘야 함.
재귀함수의 로직만 짠다면 간단하게 해결되는 문제.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def recursion(root):
            if not root:
                return None
            l_node = recursion(root.left)
            r_node = recursion(root.right)
            root.left = None
            if l_node:
                root.right = l_node
                while l_node.right:
                    l_node = l_node.right
                l_node.right = r_node
            return root
        recursion(root)