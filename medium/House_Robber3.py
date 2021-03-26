# Problem Link: https://leetcode.com/problems/house-robber-iii/

'''
문제 요약: 연속된 집을 도둑질할때는 경찰이 오게됨. 연속되지 않은 집을 도둑질 했을때 최대로 훔칠수 있는 금액을 반환하는 문제.
ask: root = [3,2,3,null,3,null,1]
answer: 7 (Binary Tree기 때문에 3 + 3 + 1 이 최대가 됨)

해석:
기존의 House Robber 문제에서 입력의 형태가 트리고 바뀌게 됨.
이는 recursion을 활용해 아래에서부터 이전에 도둑질 했을때, 도둑질을 하지 않았을때 두가지 경우로 나눠서 탐색해야 함.
왼쪽과 오른쪽을 나눠서 탐색하면 왼쪽에 훔쳤을때와 안훔쳤을때, 오른쪽에 훔쳤을때와 안훔쳤을때 총 4가지로 나뉘게 됨.
이는 쓸데없이 재귀를 많이 호출하는 경우이므로 이를 줄이고자 입력을 하나의 노드로 탐색함.
단, 하나만 받기 때문에 반환할때 값을 훔친경우와 안훔친경우 두가지를 한번에 반환.
현재 노드 기준으로 훔칠때와 안 훔칠때 두가지를 계산해서 반환하면 끝.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return (0, 0)
            left = dfs(root.left)
            right = dfs(root.right)
            rob = root.val + left[1] + right[1]
            not_rob = max(left) + max(right)
            return (rob, not_rob)
        return max(dfs(root))