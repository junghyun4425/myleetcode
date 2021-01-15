# Problem Link: https://leetcode.com/problems/same-tree/

'''
문제 요약: 두개의 트리가 같은 값과 구조를 가지는지 확인하는 문제.
ask: p = 1<-2->3 q = 1<-2->3
answer: True

해석:
모든 트리노드들을 p와 q가 함께 탐색해야 하기 때문에 재귀함수로 탐색을 결정.
몇가지 조건이 필요한데, val 가 같은지 판단하는 것과 left 나 right가 None인지 아닌지에 대한 유무도 판단해야 함.
val는 노드가 존재하지 않는 None이라면 오류를 내기 때문에 먼저 left or right가 없는가에 대해 먼저 조건문을 걸어야 함.
left에 대한 재귀, right에 대한 재귀 모두 만족하면 최종적으로 True을 반환.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def recursive(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return recursive(p.left, q.left) and recursive(p.right, q.right)
        return recursive(p, q)