# Problem Link: https://leetcode.com/problems/symmetric-tree/

'''
문제 요약: 트리가 입력으로 주어지면 대칭을 형성하고 있는가에 대한 여부를 반환하는 문제.
ask: 1 <- 2 -> 1
answer: True

해석:
트리를 대칭인가를 검사하기 위해선 루트에 대해 왼쪽과 오른쪽으로 먼저 재귀함수를 통해 검사한 뒤, 돌아오면서 반대인 오른쪽과 왼쪽을 검사.
즉, 바깥라인부터 먼저 쭉 내려가면서 검사하고 다음에 안쪽 노드들을 검사하는 방식으로 구현.
노드가 둘다 존재하지 않으면 대칭에 문제가 없지만, 둘중 하나만 존재하지 않으면 비대칭.
이전 트리 구조가 같은지 묻는 문제와 유사한 문제.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def recursive(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return t1.val == t2.val and recursive(t1.right, t2.left) and recursive(t1.left, t2.right)
        return recursive(root.right, root.left)