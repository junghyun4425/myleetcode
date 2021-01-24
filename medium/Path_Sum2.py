# Problem Link: https://leetcode.com/problems/path-sum-ii/

'''
문제 요약: 트리의 노드에서부터 리프까지 합이 targetSum 과 일치하는 모든 경로를 출력하는 문제.
ask: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
answer: [[5,4,11,2],[5,8,4,5]]

해석:
이전에 풀었던 Path_Sum 처럼 경로가 있는지 확인하는 문제에 경로를 찍어내는 문제로 바뀜.
따라서 노드의 값들을 기록하는 vals 리스트를 하나 추가해서 기록하고, 리프노드이며 res == targetSum 이 일치할때 ans에 기록함.
왼쪽과 오른쪽 노드를 각각 다 탐색하면 모든 경로들이 출력됨.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        ans = []
        def recordPath(root, vals, res):
            if not root:
                return
            if not root.left and not root.right:
                if res+root.val == targetSum:
                    ans.append(vals+[root.val])
            recordPath(root.left, vals+[root.val], res+root.val)
            recordPath(root.right, vals+[root.val], res+root.val)
        recordPath(root, [], 0)
        return ans