# Problem Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

'''
문제 요약: 정렬된 리스트가 들어오면 BST로 바꿔서 반환하는 문
ask: [-10,-3,0,5,9]
answer: [0,-3,9,-10,null,5]

해석:
BST의 성질은 가운데 값이 루트이고, 왼쪽은 작은값들 오른쪽은 큰값들을 자식으로 가짐.
정렬된 배열의 값들이 들어오기 때문에 따로 정렬할 필요 없이 (l + r) // 2 의 결과가 subTree의 root가 됨.
l 부터  m-1 까지가 left subTree, m+1 부터 r 까지가 right subTree로 구성하면 해결.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def makeBST(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            return TreeNode(nums[m], makeBST(l, m-1), makeBST(m+1, r))
        return makeBST(0, len(nums)-1)